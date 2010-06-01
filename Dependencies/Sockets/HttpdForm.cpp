/** \file HttpdForm.cpp - read stdin, parse cgi input
 **
 **	Written: 1999-Feb-10 grymse@alhem.net
 **/

/*
Copyright (C) 1999-2008  Anders Hedstrom

This library is made available under the terms of the GNU GPL.

If you would like to use this library in a closed-source application,
a separate license agreement is available. For information about 
the closed-source license agreement for the C++ sockets library,
please visit http://www.alhem.net/Sockets/license.html and/or
email license@alhem.net.

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
*/
#ifdef _MSC_VER
#pragma warning(disable:4786)
#endif
#include "socket_include.h"
#include "Parse.h"
#include "IFile.h"
#include "HttpdForm.h"
#include "IFileUpload.h"
#include "IStream.h"
#include "Debug.h"

#ifdef SOCKETS_NAMESPACE
namespace SOCKETS_NAMESPACE {
#endif

#define TMPSIZE 32000
#ifdef _DEBUG
#define DEB(x) x
#else
#define DEB(x)
#endif


HttpdForm::HttpdForm(IFile *infil, const std::string& content_type, size_t content_length) : raw(false)
, m_file_upload(NULL)
, m_upload_stream(NULL)
{
DEB(	Debug deb("HttpdForm");)
	CGI *cgi = NULL;
	size_t extra = 2;
	int cl = (int)content_length;

	m_current = m_cgi.end();
DEB(	deb << "Content-Type: " << content_type << Debug::endl();)

	if (content_type.size() >= 19 && content_type.substr(0, 19) == "multipart/form-data")
	{
		Parse pa(content_type,";=");
		char *tempcmp = NULL;
		size_t tc = 0;
		size_t l = 0;
		std::string str = pa.getword();
		m_strBoundary = "";
		while (!str.empty())
		{
			if (!strcmp(str.c_str(),"boundary"))
			{
				m_strBoundary = pa.getword();
				l = m_strBoundary.size();
				tempcmp = new char[l + extra];
			}
			//
			str = pa.getword();
		}
		if (!m_strBoundary.empty())
		{
DEB(			Debug deb("HttpdForm; parsing, boundary = " + m_strBoundary);)
			std::string content_type;
			std::string current_name;
			std::string current_filename;
			char *slask = new char[TMPSIZE];
			infil -> fgets(slask, TMPSIZE);
			cl -= strlen(slask);
			while (cl >= 0 && !infil -> eof())
			{
				while (strlen(slask) && (slask[strlen(slask) - 1] == 13 || slask[strlen(slask) - 1] == 10))
				{
					slask[strlen(slask) - 1] = 0;
				}
				content_type = "";
				current_name = "";
				current_filename = "";
				if ((strstr(slask,m_strBoundary.c_str()) || strstr(m_strBoundary.c_str(),slask)) && strcmp(slask, m_strBoundary.c_str()))
				{
					m_strBoundary = slask;
					l = m_strBoundary.size();
					delete[] tempcmp;
					tempcmp = new char[l + extra];
				}
				if (!strcmp(slask, m_strBoundary.c_str()))
				{
					// Get headers until empty line
					infil -> fgets(slask, TMPSIZE);
					cl -= strlen(slask);
					while (strlen(slask) && (slask[strlen(slask) - 1] == 13 || slask[strlen(slask) - 1] == 10))
					{
						slask[strlen(slask) - 1] = 0;
					}
DEB(					deb << "Parsing header, line = " << slask << Debug::endl();)
					while (cl >= 0 && !infil -> eof() && *slask)
					{
						Parse pa(slask,":");
						std::string h = pa.getword();
						std::string h2 = pa.getrest();
DEB(						deb << "KEY:" << h << "  REST:" << h2 << Debug::endl();)
						if (!strcasecmp(h.c_str(),"Content-type"))
						{
							Parse pa(h2, ";");
							content_type = pa.getword();
DEB(							deb << "Found Content-Type: " << content_type << Debug::endl();)
						}
						else
						if (!strcasecmp(h.c_str(),"Content-Disposition"))
						{
							Parse pa(h2, ";");
							h = pa.getword();
							if (!strcmp(h.c_str(),"form-data"))
							{
DEB(								deb << "Found Content-Disposition: form-data, parsing" << Debug::endl();)
								pa.EnableQuote(true);
								h = pa.getword();
								while (!h.empty())
								{
									Parse pa2(h,"=");
									std::string name = pa2.getword();
									h = pa2.getrest();
									if (!strcmp(name.c_str(),"name"))
									{
										if (!h.empty() && h[0] == '"')
										{
											current_name = h.substr(1, h.size() - 2);
										}
										else
										{
											current_name = h;
										}
DEB(										deb << "  Found name = " << current_name << Debug::endl();)
									}
									else
									if (!strcmp(name.c_str(),"filename"))
									{
										if (!h.empty() && h[0] == '"')
										{
											current_filename = h.substr(1, h.size() - 2);
										}
										else
										{
											current_filename = h;
										}
										size_t x = 0;
										for (size_t i = 0; i < current_filename.size(); i++)
										{
											if (current_filename[i] == '/' || current_filename[i] == '\\')
												x = i + 1;
										}
										if (x)
										{
											current_filename = current_filename.substr(x);
										}
DEB(										deb << "  Found filename = " << current_filename << Debug::endl();)
									}
									h = pa.getword();
								}
							}
						}
						// get next header value
						infil -> fgets(slask, TMPSIZE);
						cl -= strlen(slask);
						while (strlen(slask) && (slask[strlen(slask) - 1] == 13 || slask[strlen(slask) - 1] == 10))
						{
							slask[strlen(slask) - 1] = 0;
						}
					}
					// Read content, save...?
					if (current_filename.empty()) // not a file
					{
						std::string val;
						infil -> fgets(slask, TMPSIZE);
						cl -= strlen(slask);
						while (cl >= 0 && !infil -> eof() && strncmp(slask,m_strBoundary.c_str(),m_strBoundary.size() ))
						{
							val += slask;
							infil -> fgets(slask, TMPSIZE);
							cl -= strlen(slask);
						}
						// remove trailing cr/linefeed
						while (!val.empty() && (val[val.size() - 1] == 13 || val[val.size() - 1] == 10))
						{
							val = val.substr(0,val.size() - 1);
						}
						cgi = new CGI(current_name, val);
						m_cgi.push_back(cgi);
DEB(						deb << current_name << ": " << val << Debug::endl();)
						if (!cl)
						{
							break;
						}
					}
					else // current_filename.size() > 0
					{
						// read until m_strBoundary...
						FILE *fil = NULL;
						int out = 0;
						char c;
						char fn[2000]; // where post'd file will be saved
#ifdef _WIN32
						{
							char tmp_path[2000];
							::GetTempPathA(2000, tmp_path);
							if (tmp_path[strlen(tmp_path) - 1] != '\\')
							{
								strcat(tmp_path, "\\");
							}
							sprintf(fn,"%s%s",tmp_path,current_filename.c_str());
						}
#else
						sprintf(fn,"/tmp/%s",current_filename.c_str());
#endif
						if (m_file_upload && !m_upload_stream)
							m_upload_stream = &m_file_upload -> IFileUploadBegin(current_name, current_filename, content_type);
						else
							fil = fopen(fn, "wb");
						if (fil || m_upload_stream)
						{
							infil -> fread(&c,1,1);
							cl -= 1;
							while (cl >= 0 && !infil -> eof())
							{
								if (out)
								{
									if (m_upload_stream)
										m_upload_stream -> IStreamWrite(&tempcmp[tc], 1);
									else
										fwrite(&tempcmp[tc],1,1,fil);
								}
								tempcmp[tc] = c;
								tc++;
								if (tc >= l + extra)
								{
									tc = 0;
									out = 1;
								}
								if (tc)
								{
									if (!strncmp(tempcmp + tc + extra, m_strBoundary.c_str(), l - tc) &&
											!strncmp(tempcmp, m_strBoundary.c_str() + l - tc, tc))
									{
										break;
									}
								}
								else
								{
									if (!strncmp(tempcmp + extra, m_strBoundary.c_str(), l))
									{
										break;
									}
								}
								infil -> fread(&c,1,1);
								cl -= 1;
							}
							if (m_file_upload && m_upload_stream)
							{
								m_file_upload -> IFileUploadEnd();
								m_upload_stream = NULL;
							}
							else
							if (fil)
							{
								fclose(fil);
							}

							cgi = new CGI(current_name,fn,fn);
							m_cgi.push_back(cgi);
						
							strcpy(slask, m_strBoundary.c_str());
							size_t l = strlen(slask);
							infil -> fgets(slask + l, TMPSIZE); // next line
							cl -= strlen(slask + l);
						}
						else
						{
							// couldn't open file
							break;
						}
						if (!cl)
						{
							break;
						}
					}
				}
				else
				{
					// Probably '<m_strBoundary>--'
					break;
				}
			} // while (!infil -> eof())
			delete[] slask;
		} // if (m_strBoundary)
		if (tempcmp)
		{
			delete[] tempcmp;
		}
	} // end of multipart
	else
	if (strstr(content_type.c_str(), "x-www-form-urlencoded"))
	{
		bool got_name = false; // tnx to FatherNitwit
		int cl = (int)content_length;
		char c,chigh,clow;
		std::string slask;
		m_current = m_cgi.end();
		std::string name;

		infil -> fread(&c,1,1);
		cl--;
		while (cl >= 0 && !infil -> eof())
		{
			switch (c) // built-in url decoder
			{
				case '=': /* end of name */
					name = slask;
					slask.resize(0);
					got_name = true;
					break;
				case '&': /* end of value */
					if (got_name)
					{
						cgi = new CGI(name,slask);
						got_name = false;
					}
					else
					{
						cgi = new CGI(slask, "");
					}
					slask.resize(0);
					m_cgi.push_back(cgi);
					break;
				case '+': /* space */
					slask += " ";
					break;
				case '%': /* hex value */
					infil -> fread(&chigh,1,1);
					cl--;
					chigh -= 48 + (chigh > '9' ? 7 : 0) + (chigh >= 'a' ? 32 : 0);
					infil -> fread(&clow,1,1);
					cl--;
					clow -= 48 + (clow > '9' ? 7 : 0) + (clow >= 'a' ? 32 : 0);
					slask += (char)(chigh * 16 + clow);
					break;
				default: /* just another char */
					slask += c;
					break;
			}
			//
			if (cl > 0)
			{
				infil -> fread(&c,1,1);
			}
			cl--;
		}
		if (got_name)
		{
			cgi = new CGI(name,slask);
		}
		else
		{
			cgi = new CGI(slask, "");
		}
		m_cgi.push_back(cgi);
	}
}


// HttpdForm(buffer,l) -- request_method GET

HttpdForm::HttpdForm(const std::string& buffer,size_t l) : raw(false)
, m_file_upload(NULL)
, m_upload_stream(NULL)
{
	CGI *cgi = NULL;
	std::string slask;
	std::string name;
	char c,chigh,clow;
	size_t ptr = 0;
	bool got_name = false;

	m_current = m_cgi.end();

	ptr = 0;
	while (ptr < l)
	{
		c = buffer[ptr++];
		switch (c)
		{
			case '=': /* end of name */
				name = slask;
				slask.resize(0);
				got_name = true;
				break;
			case '&': /* end of value */
				if (got_name)
				{
					cgi = new CGI(name,slask);
					got_name = false;
				}
				else
				{
					cgi = new CGI(slask, "");
				}
				slask.resize(0);
				m_cgi.push_back(cgi);
				break;
			case '+': /* space */
				slask += " ";
				break;
			case '%': /* hex value */
				chigh = buffer[ptr++];
				chigh -= 48 + (chigh > '9' ? 7 : 0) + (chigh >= 'a' ? 32 : 0);
				clow = buffer[ptr++];
				clow -= 48 + (clow > '9' ? 7 : 0) + (clow >= 'a' ? 32 : 0);
				slask += (char)(chigh * 16 + clow);
				break;
			default: /* just another char */
				slask += c;
				break;
		}
	}
	if (got_name)
	{
		cgi = new CGI(name,slask);
	}
	else
	{
		cgi = new CGI(slask, "");
	}
	m_cgi.push_back(cgi);
}


HttpdForm::~HttpdForm()
{
	CGI *cgi = NULL; //,*tmp;

	for (cgi_v::iterator it = m_cgi.begin(); it != m_cgi.end(); it++)
	{
		cgi = *it;
		delete cgi;
	}
}


void HttpdForm::EnableRaw(bool b)
{
	raw = b;
}


void HttpdForm::strcpyval(std::string& v,const char *value) const
{
	v = "";
	for (size_t i = 0; i < strlen(value); i++)
	{
		if (value[i] == '<')
		{
			v += "&lt;";
		}
		else
		if (value[i] == '>')
		{
			v += "&gt;";
		}
		else
		if (value[i] == '&')
		{
			v += "&amp;";
		}
		else
		{
			v += value[i];
		}
	}
}


bool HttpdForm::getfirst(std::string& n) const
{
	m_current = m_cgi.begin();
	return getnext(n);
}


bool HttpdForm::getnext(std::string& n) const
{
	if (m_current != m_cgi.end() )
	{
		CGI *current = *m_current;
		n = current -> name;
		m_current++;
		return true;
	}
	else
	{
		n = "";
	}
	return false;
}


bool HttpdForm::getfirst(std::string& n,std::string& v) const
{
	m_current = m_cgi.begin();
	return getnext(n,v);
}


bool HttpdForm::getnext(std::string& n,std::string& v) const
{
	if (m_current != m_cgi.end() )
	{
		CGI *current = *m_current;
		n = current -> name;
		if (raw)
		{
			v = current -> value;
		}
		else
		{
			strcpyval(v,current -> value.c_str());
		}
		m_current++;
		return true;
	}
	else
	{
		n = "";
	}
	return false;
}


int HttpdForm::getvalue(const std::string& n,std::string& v) const
{
	CGI *cgi = NULL;
	int r = 0;

	for (cgi_v::const_iterator it = m_cgi.begin(); it != m_cgi.end(); it++)
	{
		cgi = *it;
		if (cgi -> name == n)
			break;
		cgi = NULL;
	}
	if (cgi)
	{
		if (raw)
		{
			v = cgi -> value;
		}
		else
		{
			strcpyval(v,cgi -> value.c_str());
		}
		r++;
	}
	else
	{
		v = "";
	}

	return r;
}


std::string HttpdForm::getvalue(const std::string& n) const
{
	for (cgi_v::const_iterator it = m_cgi.begin(); it != m_cgi.end(); it++)
	{
		CGI *cgi = *it;
		if (cgi -> name == n)
		{
			return cgi -> value;
		}
	}
	return "";
}


size_t HttpdForm::getlength(const std::string& n) const
{
	CGI *cgi = NULL;
	size_t l;

	for (cgi_v::const_iterator it = m_cgi.begin(); it != m_cgi.end(); it++)
	{
		cgi = *it;
		if (cgi -> name == n)
			break;
		cgi = NULL;
	}
	l = cgi ? cgi -> value.size() : 0;
	if (cgi && !raw)
	{
		for (size_t i = 0; i < cgi -> value.size(); i++)
		{
			switch (cgi -> value[i])
			{
			case '<': // &lt;
			case '>': // &gt;
				l += 4;
				break;
			case '&': // &amp;
				l += 5;
				break;
			}
		}
	}
	return l;
}


HttpdForm::cgi_v& HttpdForm::getbase()
{
	return m_cgi;
}


const std::string& HttpdForm::GetBoundary() const
{
	return m_strBoundary;
}


void HttpdForm::SetFileUpload(IFileUpload& cb)
{
	m_file_upload = &cb;
}


#ifdef SOCKETS_NAMESPACE
}
#endif


