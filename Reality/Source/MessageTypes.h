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

#ifndef MXOSIM_MESSAGETYPES_H
#define MXOSIM_MESSAGETYPES_H

#include "Common.h"
#include "ByteBuffer.h"
#include "Util.h"
#include "Crypto.h"

#include "Log.h"
#include "Config.h"
#include "Database/DatabaseEnv.h"

#ifndef M_PI
#define M_PI 3.14159265358979323846264338327
#endif

class MsgBaseClass
{
public:
	class PacketNoLongerValid {};

	MsgBaseClass() {m_buf.clear();}
	virtual ~MsgBaseClass() {}
	virtual const ByteBuffer& toBuf() = 0;
protected:
	ByteBuffer m_buf;
};

typedef shared_ptr<MsgBaseClass> msgBaseClassPtr;

class ObjectUpdateMsg : public MsgBaseClass
{
public:
	ObjectUpdateMsg(uint32 objectId);
	~ObjectUpdateMsg();
	virtual void setReceiver(class GameClient *toWho);
protected:
	uint32 m_objectId;
	class GameClient *m_toWho;
};



class DeletePlayerMsg : public ObjectUpdateMsg
{
public:
	DeletePlayerMsg(uint32 objectId);
	~DeletePlayerMsg();
	const ByteBuffer& toBuf();
	void setReceiver(class GameClient *toWho);
};


class CloseDoorMsg : public ObjectUpdateMsg
{
public:
	CloseDoorMsg(uint32 objectId );
	~CloseDoorMsg();
	const ByteBuffer& toBuf();
	void setReceiver(class GameClient *toWho);
};

class SitDownMsg : public ObjectUpdateMsg
{
public:
	SitDownMsg(uint32 objectId);
	~SitDownMsg();
	const ByteBuffer& toBuf();
	void setReceiver(class GameClient *toWho);
};


class PlayerSpawnMsg : public ObjectUpdateMsg
{
public:
	PlayerSpawnMsg(uint32 objectId);
	~PlayerSpawnMsg();
	const ByteBuffer& toBuf();
};

class EmoteMsg : public ObjectUpdateMsg
{
public:
	EmoteMsg(uint32 objectId, uint32 emoteId, uint8 emoteCount);
	~EmoteMsg();
	const ByteBuffer& toBuf();
private:
	uint8 m_emoteCount;
	static map<uint32,uint8> m_emotesMap;
	uint8 m_emoteAnimation;
};

class AnimationStateMsg : public ObjectUpdateMsg
{
public:
	AnimationStateMsg(uint32 objectId);
	~AnimationStateMsg();
	const ByteBuffer& toBuf();
};

class PositionStateMsg : public ObjectUpdateMsg
{
public:
	PositionStateMsg(uint32 objectId);
	~PositionStateMsg();
	const ByteBuffer& toBuf();
};

class StateUpdateMsg : public ObjectUpdateMsg
{
public:
	StateUpdateMsg(uint32 objectId, ByteBuffer stateData);
	~StateUpdateMsg();
	const ByteBuffer& toBuf();
private:
	ByteBuffer restOfData;
};

class StaticMsg : public MsgBaseClass
{
public:
	StaticMsg() {}
	StaticMsg(const ByteBuffer &inputBuf) {m_buf = inputBuf;}
	~StaticMsg() {}
	const ByteBuffer& toBuf() {return m_buf;}
};

class EmptyMsg : public StaticMsg
{
public:
	EmptyMsg() {m_buf.clear();}
	~EmptyMsg() {}
};

class DoorAnimationMsg : public StaticMsg
{
public:

	DoorAnimationMsg(uint32 doorId, uint16 viewId, double X, double Y, double Z, double ROT, int doorType)
	{
				

		Y += 50;

		double distanceToGo = 6; //This will be 1/2 of 1 unit
		double sAngle = sin(ROT);
		double xInc = distanceToGo * sAngle; 
		double zInc = sqrt(distanceToGo * distanceToGo - xInc * xInc);
		xInc *= 10;
		zInc *= 10;
		X -= xInc;
		if (abs(ROT) > M_PI/2)
		{
			Z += zInc;
		}
		else
		{
			Z -= zInc;
		}

		byte rotation = 0xbf;
		//Rotation
		if (abs(ROT) > 2.3) // facing North
		{
			rotation = 0x03; //0xbf;
		}
		else if (abs(ROT) < .78) // facing South
		{
			rotation = 0x03;  //gave up and am having u facing south hve doors open same as u facing north..
		}
		else if (ROT < 0) // facing west
		{
			rotation = 0x3f;
		}
		else 
		{
			rotation = 0xbf;  //facing east
		}

		
/*

03 01 00 08 da 19 19 00 50 30 ef cd ab 03 84 00 00 00 00 f2 04 35 bf 00 00 00 00 f3 04 35 3f 
41 00 00 00 00 00 c1 06 41 00 00 00 00 00 b8 8a c0 00 00 00 00 80 da e8 40 34 08 00 00 03 00 00 
00 00 

*/
		//Get door type
	
		//int doorType = 1;

		if (doorType == 0) // inside (white hallsays slums)
		{

			byte insideDoor[65] =
			{
				0x03, 0x01, 0x00, 0x08, 0xda, 0x19, 
				
				0xAA, 0xAA, 0xAA, 0xAA, 

				0xef, 
				
				0xcd, 0xab, 0x03, 0x84, 0x00, 0x00, 0x00, 0x00, 
				0xf2, 0x04,	
				//rotatation?
				0x35, 0xbf, 
			    
				0x00, 0x00, 0x00, 0x00, 
				//??        ??    
				0xf3, 0x04, 0x35, 
				//width 
				  0x3f, 
				//?? (not 41 breaks door openin)
				0x41, 
				0x00, 0x00, 0x00, 0x00,0xBB, 0xBB, 0xBB, 0xBB,  //X
				0x00, 0x00, 0x00, 0x00,0xCC, 0xCC, 0xCC, 0xCC,  //Y
				0x00, 0x00, 0x00, 0x00,0xDD, 0xDD, 0xDD, 0xDD,  //Z

				0x34, 0x08, 0x00, 0x00, 
				0xBB, 0xBB, 0x00, 0x00, 0x00, 
			};
			//03 03 00 01 80 02 38 08 00 00 00 00 

			//uint2 clientDoorId = rand() % 255;
			//insideDoor[22] = rand() % 128 + 63;

			memcpy(&insideDoor[6],&doorId,sizeof(doorId));   //uint32
			memcpy(&insideDoor[60],&viewId,sizeof(viewId));   //uint16


			ByteBuffer bufferBytesCoords;
			bufferBytesCoords << double(X) << double(Y) << double(Z);
			
			byte byteCoords[24] = {
				0x00, 0x00, 0x00, 0x00,0x00, 0xc1, 0x06, 0x41,  //X
				0x00, 0x00, 0x00, 0x00,0x00, 0xb8, 0x8a, 0xc0,  //Y
				0x00, 0x00, 0x00, 0x00,0x80, 0xda, 0xe8, 0x40,  //Z			
			};
			//Put new coords in
			bufferBytesCoords.read(byteCoords, bufferBytesCoords.size());

			
			
			memcpy(&insideDoor[32],&byteCoords,sizeof(byteCoords));   //uint16

			//Rotation
			insideDoor[22] = rotation;



			m_buf.clear();
			m_buf.append(insideDoor,sizeof(insideDoor));
		}
		else if (doorType == 1) //outside
		{

			byte OutsideDoor[65] =
			{
				0x03, 0x01, 0x00, 0x08, 0x33, 0x1b, 
				0xAA, 0xAA, 0xAA, 0xAA,  
				0xbc, 0xcd, 0xab, 0x03, 0x84, 0x00, 0x00, 0x00, 0x00, 0xf3, 0x04, 0x35, 0xbf, 0x00, 0x00, 
				0x00, 0x00, 0xf3, 0x04, 0x35, 0x3f, 0x41, 0x00, 0x00, 0x00, 0x00, 0x20, 0xf4, 0xea, 0x40, 
				0x00, 0x00, 0x00, 0x00, 0x00, 0x20, 0x62, 0x40, 0x00, 0x00, 0x00, 0x00, 0x00, 0x7e, 0xcd, 
				0x40, 0x34, 0x08, 0x00, 0x00, 0xBB, 0xBB, 0x00, 0x00, 0x00, 
			};

			

			memcpy(&OutsideDoor[6],&doorId,sizeof(doorId));   //uint32
			memcpy(&OutsideDoor[60],&viewId,sizeof(viewId));   //uint16


			ByteBuffer bufferBytesCoords;
			bufferBytesCoords << double(X) << double(Y) << double(Z);
			
			byte byteCoords[24] = {
				0x00, 0x00, 0x00, 0x00,0x00, 0xc1, 0x06, 0x41,  //X
				0x00, 0x00, 0x00, 0x00,0x00, 0xb8, 0x8a, 0xc0,  //Y
				0x00, 0x00, 0x00, 0x00,0x80, 0xda, 0xe8, 0x40,  //Z			
			};
			//Put new coords in
			bufferBytesCoords.read(byteCoords, bufferBytesCoords.size());

			
			
			memcpy(&OutsideDoor[32],&byteCoords,sizeof(byteCoords));   //uint16

			//Rotation
			OutsideDoor[22] = rotation;


			
			//ROT


			m_buf.clear();
			m_buf.append(OutsideDoor,sizeof(OutsideDoor));
		}
		//memcpy(&doorX[6],&doorId,sizeof(doorId));   //uint32
		//memcpy(&doorX[55],&viewId,sizeof(viewId));   //uint16
		//m_buf.append(doorX,sizeof(insideDoor));



			/*uint32 theDoorId = doorId;
			memcpy(&rawData[6],&theDoorId,sizeof(theDoorId));
			uint16 theViewId = viewId;
			memcpy(&rawData[0x2C],&theViewId,sizeof(theViewId));
			m_buf.clear();
			m_buf.append(rawData,sizeof(rawData));*/

		
	}
	~DoorAnimationMsg() {}
};

class WhereAmIResponse : public StaticMsg
{
public:
	WhereAmIResponse(const class LocationVector &currPos);
	~WhereAmIResponse();
};

class WhisperMsg : public StaticMsg
{
public:
	WhisperMsg(string sender, string message)
	{
		m_buf << uint16(swap16(0x2E11));
		m_buf << uint8(0);
		m_buf << uint32(0);

		uint32 putSenderStrLenPosHere = m_buf.wpos();
		m_buf << uint32(0); //will overwrite this later
		uint32 putMessageStrLenPosHere = m_buf.wpos();
		m_buf << uint32(0); //will overwrite this later

		//0x15 bytes of 0s
		for (int i=0;i<0x15;i++)
			m_buf << uint8(0);

		uint32 senderStrLenPos = m_buf.wpos();

		sender = "SOE+MXO+Recursion+" + sender;
		uint16 senderStrLen = sender.length()+1;
		m_buf << uint16(senderStrLen);
		m_buf.append(sender.c_str(),senderStrLen);
		
		uint32 messageStrLenPos = m_buf.wpos();
		uint16 messageStrLen = message.length()+1;
		m_buf << uint16(messageStrLen);
		m_buf.append(message.c_str(),messageStrLen);

		//go back and put positions there
		m_buf.wpos(putSenderStrLenPosHere);
		m_buf << uint32(senderStrLenPos);
		m_buf.wpos(putMessageStrLenPosHere);
		m_buf << uint32(messageStrLenPos);
	}
	~WhisperMsg()
	{

	}
};

class SystemMsg : public StaticMsg
{
public:
	SystemMsg(uint16 opcode,string message)
	{
		m_buf.clear();

		m_buf << uint16(swap16(opcode));
		m_buf << uint8(0);
		m_buf << uint32(0);

		m_buf << uint32(0); //no sender
		uint32 putMessageStrLenPosHere = m_buf.wpos();
		m_buf << uint32(0); //we will overwrite this later

		//0x15 bytes of 0s
		for (int i=0;i<0x15;i++)
			m_buf << uint8(0);

		uint32 messageStrLenPos = m_buf.wpos();
		uint16 messageStrLen = message.length()+1;
		m_buf << uint16(messageStrLen);
		m_buf.append(message.c_str(),messageStrLen);

		//go back and put position there
		m_buf.wpos(putMessageStrLenPosHere);
		m_buf << uint32(messageStrLenPos);
	}
	~SystemMsg() {}
};

class BroadcastMsg : public SystemMsg
{
public:
	BroadcastMsg(string message) : SystemMsg(0x2EC7,message) {}
	~BroadcastMsg() {}
};

class ModalMsg : public SystemMsg
{
public:
	ModalMsg(string message) : SystemMsg(0x2ED7,message) {}
	~ModalMsg() {}
};

class SystemChatMsg : public SystemMsg
{
public:
	SystemChatMsg(string message) : SystemMsg(0x2E07,message) {}
	~SystemChatMsg() {}
};

class PlayerChatMsg : public StaticMsg
{
public:
	PlayerChatMsg(string charHandle,string theChatMsg) 
	{
		m_buf.clear();
		
		m_buf << swap16(0x2E10);
		m_buf << uint8(0); //could be 1 as well ?
		m_buf << uint32(swap32(0x12610200)); //some id, different, ill just use something
		size_t injectHandleLenPosHere = m_buf.wpos();
		uint32 handleLenPos=0;
		m_buf << handleLenPos; //will come back here and overwrite later
		size_t injectMessageLenPosHere = m_buf.wpos();
		uint32 messageLenPos=0;
		m_buf << messageLenPos;
		m_buf.wpos(m_buf.wpos()+0x15);
		handleLenPos=m_buf.wpos();
		uint16 handleLen=charHandle.length()+1;
		m_buf << handleLen;
		m_buf.append(charHandle.c_str(),handleLen);
		messageLenPos = m_buf.wpos();
		uint16 messageLen=theChatMsg.length()+1;
		m_buf << messageLen;
		m_buf.append(theChatMsg.c_str(),messageLen);

		//overwrite the pos we didnt before
		m_buf.wpos(injectHandleLenPosHere);
		m_buf << handleLenPos;
		m_buf.wpos(injectMessageLenPosHere);
		m_buf << messageLenPos;
	}
	~PlayerChatMsg() {}
};

class BackgroundResponseMsg : public StaticMsg
{
public:
	BackgroundResponseMsg(string playerBackground)
	{
		m_buf.clear();

		m_buf << uint16(swap16(0x8195));
		uint32 insertBackgroundStrLenPosHere = m_buf.wpos();
		m_buf << uint16(0); //placeholder
		m_buf << uint8(0);
		uint16 backgroundStrLenPos = m_buf.wpos();
		uint16 backgroundStrLen = playerBackground.length()+1;
		m_buf << uint16(backgroundStrLen);
		m_buf.append(playerBackground.c_str(),backgroundStrLen);

		//go back and put position there
		m_buf.wpos(insertBackgroundStrLenPosHere);
		m_buf << uint16(backgroundStrLenPos);
	}
	~BackgroundResponseMsg() {}
};

class PlayerDetailsMsg : public StaticMsg
{
public:
	PlayerDetailsMsg(class PlayerObject *thePlayer);
	~PlayerDetailsMsg();
};

class PlayerBackgroundMsg : public StaticMsg
{
public:
	PlayerBackgroundMsg(string playerBackground)
	{
		m_buf.clear();

		m_buf << uint16(swap16(0x8198));
		uint32 insertBackgroundStrLenPosHere = m_buf.wpos();
		m_buf << uint16(0); //placeholder
		m_buf << uint8(1);
		uint16 backgroundStrLenPos = m_buf.wpos();
		uint16 backgroundStrLen = playerBackground.length()+1;
		m_buf << uint16(backgroundStrLen);
		m_buf.append(playerBackground.c_str(),backgroundStrLen);

		//go back and put position there
		m_buf.wpos(insertBackgroundStrLenPosHere);
		m_buf << uint16(backgroundStrLenPos);
	}
	~PlayerBackgroundMsg() {}
};

class HexGenericMsg : public StaticMsg
{
public:
	HexGenericMsg(string hexadecimalData)
	{
		m_buf.clear();
		string output;
		CryptoPP::HexDecoder decoder;
		decoder.Attach( new CryptoPP::StringSink( output ) );
		decoder.Put( (const byte*)hexadecimalData.c_str(), hexadecimalData.length() );
		decoder.MessageEnd();		
		m_buf.append(output);
	}
	~HexGenericMsg() {}
};

class LoadWorldCmd : public StaticMsg
{
public:
	typedef enum
	{
		TUTORIAL = 0x00,
		SLUMS = 0x01,
		DOWNTOWN = 0x02,
		INTERNATIONAL = 0x03,
		ARCHIVE01 = 0X04,
		ARCHIVE02 = 0X05,
		ASHENCOURT = 0X06,
		DATAMINE = 0X07,
		SAKURA = 0X08,
		SATI = 0X09,
		WIDOWSMOOR = 0X0A,
		YUKI = 0X0B,
		LARGE01 = 0X0C,
		LARGE02 = 0X0D,
		MEDIUM01 = 0X0E,
		MEDIUM02 = 0X0F,
		MEDIUM03 = 0X10,
		SMALL03 = 0X11,
		CAVES = 0X12,
	} mxoLocation;

	LoadWorldCmd(mxoLocation theLoc,string theSky)
	{
		m_buf.clear();
		locs[TUTORIAL] = "resource/worlds/final_world/tutorial_v2/tutorial_v2.metr";
		locs[SLUMS] = "resource/worlds/final_world/slums_barrens_full.metr";
		locs[DOWNTOWN] = "resource/worlds/final_world/downtown/dt_world.metr";
		locs[INTERNATIONAL] = "resource/worlds/final_world/international/it.metr";
		
		locs[ARCHIVE01] = "resource/worlds/final_world/constructs/archive/archive01/archive01.metr";
		locs[ARCHIVE02] = "resource/worlds/final_world/constructs/archive/archive02/archive02.metr";
		locs[ASHENCOURT] = "resource/worlds/final_world/constructs/archive/archive_ashencourte/archive_ashencourte.metr";
		locs[DATAMINE] = "resource/worlds/final_world/constructs/archive/archive_datamine/datamine.metr";
		locs[SAKURA] = "resource/worlds/final_world/constructs/archive/archive_sakura/archive_sakura.metr";
		locs[SATI] = "resource/worlds/final_world/constructs/archive/archive_sati/sati.metr";
		locs[WIDOWSMOOR] = "resource/worlds/final_world/constructs/archive/archive_widowsmoor/archive_widowsmoor.metr";
		locs[YUKI] = "resource/worlds/final_world/constructs/archive/archive_yuki/archive_yuki.metr";
		locs[LARGE01] = "resource/worlds/final_world/constructs/large/large01/large01.metr";
		locs[LARGE02] = "resource/worlds/final_world/constructs/large/large02/large02.metr";
		locs[MEDIUM01] = "resource/worlds/final_world/constructs/medium/medium01/medium01.metr";
		locs[MEDIUM02] = "resource/worlds/final_world/constructs/medium/medium02/medium02.metr";
		locs[MEDIUM03] = "resource/worlds/final_world/constructs/medium/medium03/medium03.metr";
		locs[SMALL03] = "resource/worlds/final_world/constructs/small/small03/small03.metr";
		locs[CAVES] = "resource/worlds/final_world/zion_caves.metr";


		m_buf << uint16(swap16(0x060E))
			  << uint8(0)
			  << uint32(theLoc)
			  //<< uint32(swap32(0x4B61BD47)) //dunno lol
			  << uint32(swap32(0xd868c847))
			  << uint8(1);
		uint16 bytesSoFar = (uint16)m_buf.wpos();
		string metrFile = locs[theLoc];
		uint16 metrFileLen = (uint16)metrFile.length()+1;
		m_buf << uint16(bytesSoFar+sizeof(uint16)+sizeof(uint16)+metrFileLen) //offset to sky length byte
			  << uint16(metrFileLen); //length of string (including null term)
		m_buf.append(metrFile.c_str(),metrFileLen); //string itself (including null term)
		uint16 skyLen = (uint16)theSky.length()+1;
		m_buf << uint16(skyLen);
		m_buf.append(theSky.c_str(),skyLen);
	}
	~LoadWorldCmd() {}
private:
	map<mxoLocation,string> locs;
};

class SetExperienceCmd : public StaticMsg
{
public:
	SetExperienceCmd(uint64 theExp)
	{
		m_buf.clear();
		m_buf << uint16(swap16(0x80e5))
			<< uint64(theExp);
	}
	~SetExperienceCmd() {}
};

class SetInformationCmd : public StaticMsg
{
public:
	SetInformationCmd(uint64 theCash)
	{
		m_buf.clear();
		m_buf << uint16(swap16(0x80e4))
			<< uint64(theCash);
	}
	~SetInformationCmd() {}
};

class EventURLCmd : public StaticMsg
{
public:
	EventURLCmd(string eventURL)
	{
		m_buf.clear();
		//81 a5 00 00 07 00 05
		m_buf << uint16(swap16(0x81a5)) // can also be 81a9
			  << uint16(0)
			  << uint16(7)
			  << uint8(5);
		uint16 eventURLSize = (uint16)eventURL.length()+1;
		m_buf << uint16(eventURLSize);
		m_buf.append(eventURL.c_str(),eventURLSize);
	}
	~EventURLCmd() {}
};

struct MsgBlock 
{
	uint16 sequenceId;
	list<ByteBuffer> subPackets;

	bool FromBuffer(ByteBuffer &source)
	{
		{
			uint16 theId;
			if (source.remaining() < sizeof(theId))
				return false;

			source >> theId;
			sequenceId = swap16(theId);
		}
		uint8 numSubPackets;
		if (source.remaining() < sizeof(numSubPackets))
			return false;

		source >> numSubPackets;
		subPackets.clear();
		for (uint8 i=0;i<numSubPackets;i++)
		{
			uint8 firstTwoBytes[2];
			if (source.remaining() < sizeof(uint8))
				return false;
			source >> firstTwoBytes[0];

			int sizeOfPacketSize = 1;
			if (firstTwoBytes[0] > 0x7F)
			{
				sizeOfPacketSize = 2;
				firstTwoBytes[0] -= 0x80;

				if (source.remaining() < sizeof(uint8))
					return false;

				source >> firstTwoBytes[1];
			}
			uint16 subPacketSize = 0;
			if (sizeOfPacketSize == 1)
			{
				subPacketSize = firstTwoBytes[0];
			}
			else if (sizeOfPacketSize == 2)
			{
				memcpy(&subPacketSize,firstTwoBytes,sizeof(subPacketSize));
				subPacketSize = swap16(subPacketSize);
			}

			if (subPacketSize<1)
				return false;

			vector<byte> dataBuf(subPacketSize);
			if (source.remaining() < dataBuf.size())
				return false;

			source.read(&dataBuf[0],dataBuf.size());
			subPackets.push_back(ByteBuffer(&dataBuf[0],dataBuf.size()));
		}
		return true;
	}
	bool FromBuffer(const byte* buf,size_t size)
	{
		ByteBuffer derp;
		derp.append(buf,size);
		derp.wpos(0);
		derp.rpos(0);
		return FromBuffer(derp) && (derp.remaining() == 0);
	}
	void ToBuffer(ByteBuffer &destination)
	{
		destination << uint16(swap16(sequenceId));

		uint8 numSubPackets = subPackets.size();
		destination << uint8(numSubPackets);
		for (list<ByteBuffer>::iterator it=subPackets.begin();it!=subPackets.end();++it)
		{
			uint16 packetSize = it->size();
			if (packetSize > 0x7f)
			{
				packetSize = htons(packetSize | 0x8000);
				destination << uint16(packetSize);
			}
			else
			{
				destination << uint8(packetSize);
			}
			destination.append(it->contents(),it->size());
		}
	}
	uint32 GetTotalSize()
	{
		uint32 startSize = sizeof(uint16)+sizeof(uint8);
		for (list<ByteBuffer>::iterator it=subPackets.begin();it!=subPackets.end();++it)
		{
			startSize += it->size();
		}		
		return startSize;
	}
};

class OrderedPacket : public StaticMsg
{
public:
	OrderedPacket() {m_buf.clear();}
	OrderedPacket(ByteBuffer &source)
	{
		m_buf.clear();
		FromBuffer(source);
	}
	OrderedPacket(const byte* buf,size_t size)
	{
		m_buf.clear();
		FromBuffer(buf,size);
	}
	OrderedPacket(MsgBlock justOneBlock)
	{
		m_buf.clear();
		msgBlocks.push_back(justOneBlock);
	}
	bool FromBuffer(ByteBuffer &source)
	{
		uint8 zeroFourId=0;
		if (source.remaining() < sizeof(zeroFourId))
			return false;

		source >> zeroFourId;

		if (zeroFourId != 0x04)
			return false;

		uint8 numOrderPackets=0;
		if (source.remaining() < sizeof(numOrderPackets))
			return false;

		source >> numOrderPackets;

		if (numOrderPackets < 1)
			return false;

		msgBlocks.clear();
		for (uint8 i=0;i<numOrderPackets;i++)
		{
			MsgBlock thePacket;
			if (thePacket.FromBuffer(source) == false)
				return false;

			msgBlocks.push_back(thePacket);
		}
		return true;
	}
	bool FromBuffer(const byte* buf,size_t size)
	{
		ByteBuffer derp;
		derp.append(buf,size);
		derp.wpos(0);
		derp.rpos(0);
		return FromBuffer(derp) && (derp.remaining()==0);
	}
private:
	void ToBuffer(ByteBuffer &destination)
	{
		destination << uint8(0x04);
		destination << uint8(msgBlocks.size());

		for (list<MsgBlock>::iterator it=msgBlocks.begin();it!=msgBlocks.end();++it)
		{
			it->ToBuffer(destination);
		}
	}
public:
	const ByteBuffer& toBuf()
	{
		m_buf.clear();
		ToBuffer(m_buf);
		return m_buf;
	}
	uint32 GetTotalSize()
	{
		uint32 startSize = sizeof(uint8)*2;
		for (list<MsgBlock>::iterator it=msgBlocks.begin();it!=msgBlocks.end();++it)
		{
			startSize += it->GetTotalSize();
		}		
		return startSize;
	}
	list<MsgBlock> msgBlocks;
};


#endif