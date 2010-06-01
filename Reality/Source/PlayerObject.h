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

#ifndef MXOEMU_PLAYEROBJECT_H
#define MXOEMU_PLAYEROBJECT_H

#include "LocationVector.h"
#include "MessageTypes.h"

class PlayerObject
{
public:
	class CharacterNotFound {};

	PlayerObject(class GameClient &parent,uint64 charUID);
	~PlayerObject();

	void InitializeWorld();
	void SpawnSelf();
	void PopulateWorld();

	void initGoId(uint32 theGoId);
	void HandleStateUpdate(ByteBuffer &srcData);
	void HandleCommand(ByteBuffer &srcCmd);

	string getHandle() const {return m_handle;}
	string getFirstName() const {return m_firstName;}
	string getLastName() const {return m_lastName;}
	string getBackground() const {return m_background;}
	bool setBackground(string newBackground);

	uint64 getExperience() const {return m_exp;}
	uint64 getInformation() const {return m_cash;}
	LocationVector getPosition() const {return m_pos;}
	void setPosition(const LocationVector& newPos) {m_pos = newPos;}
	uint8 getRsiData(byte* outputBuf,uint32 maxBufLen) const ;
	uint16 getCurrentHealth() const {return m_healthC;}
	uint16 getMaximumHealth() const {return m_healthM;}
	uint16 getCharacterUID() const {return m_characterUID;}
	uint16 getCurrentIS() const {return m_innerStrC;}
	uint16 getMaximumIS() const {return m_innerStrM;}
	uint32 getProfession() const {return m_prof;}
	uint8 getLevel() const {return m_lvl;}
	uint8 getAlignment() const {return m_alignment;}
	bool getPvpFlag() const {return m_pvpflag;}

	uint8 getCurrentAnimation() const {return m_currAnimation;}
	uint8 getCurrentMood() const {return m_currMood;}

	void checkAndStore();
	void saveDataToDB();

	class GameClient& getClient() { return m_parent; }

	vector<msgBaseClassPtr> getCurrentStatePackets();
private:
	class GameClient &m_parent;
	
	//Player info
	uint64 m_characterUID;
	string m_handle;
	string m_firstName;
	string m_lastName;
	string m_background;

	
	uint32 m_goId;
	uint64 m_exp,m_cash;
	uint8 m_district;
	LocationVector m_pos,m_savedPos;
	shared_ptr<class RsiData> m_rsi;
	uint16 m_healthC,m_healthM,m_innerStrC,m_innerStrM;
	uint32 m_prof;
	uint8 m_lvl,m_alignment;
	bool m_pvpflag;
	uint32 testCount;

	bool m_spawnedInWorld;
	uint32 m_lastStore;

	uint32 m_lastTestedCommand;

	uint8 m_currAnimation;
	uint8 m_currMood;

	uint8 m_emoteCounter;

	bool m_isAdmin;
	void ParseAdminCommand(string theCmd);
	void ParsePlayerCommand(string theCmd);
	void GoAhead(double distanceToGo);
	void GoDownTown();
	void Update();
};

#endif