// *************************************************************************************************
// --------------------------------------
// Copyright (C) 2006-2010 Rajko Stojadinovic
//
//
// This program is free software; you can redistribute it and/or
// modify it under the terms of the GNU Lesser General Public
// License as published by the Free Software Foundation; either
// version 2.1 of the License, or (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
// Lesser General Public License for more details.
//
// You should have received a copy of the GNU Lesser General Public
// License along with this library; if not, write to the Free Software
// Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
//
// *************************************************************************************************

#ifndef MXOSIM_AUTHSOCKET_H
#define MXOSIM_AUTHSOCKET_H

#include "TCPVarLenSocket.h"
#include "Common.h"
#include "Crypto.h"
#include "SymmetricCrypto.h"

class AuthSocket : public TCPVarLenSocket
{
public:
	AuthSocket(ISocketHandler& );
	~AuthSocket();
private:
	void HandleGetPublicKeyRequest(ByteBuffer &packet);
	void HandleAuthRequest(ByteBuffer &packet);
	void HandleAuthChallengeResponse(ByteBuffer &packet);


	void ProcessData(const byte *buf,size_t len);
	bool VerifyPassword( const string& plaintextPass, const string& passwordSalt, const string& passwordHash );
	uint32 packetNum;
	string username;

	typedef CryptoPP::CBC_Mode<CryptoPP::Twofish>::Decryption Decryptor;
	TwofishCryptEngine m_tfEngine;

	uint32 matrixVersion;
	byte challenge[16];
	byte finalChallenge[16];

	uint32 m_userId;
	string m_username;
	string m_passwordSalt;
	string m_passwordHash;
	uint16 m_publicExponent;
	string m_publicModulus;
	string m_privateExponent;
	uint32 m_timeCreated;
};


#endif
