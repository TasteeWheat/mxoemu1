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

#include "ObjectMgr.h"
#include "PlayerObject.h"
#include "GameClient.h"

uint32 ObjectMgr::constructPlayer( GameClient* requester, uint64 charUID )
{
	if (requester == NULL)
		throw ClientNotAvailable();

	PlayerObject *newPlayerObj = NULL;
	try
	{
		newPlayerObj = new PlayerObject(*requester,charUID);
	}
	catch (PlayerObject::CharacterNotFound)
	{
		throw ObjectNotAvailable();
	}

	uint32 theNewObjectId = getNewObjectId();
	newPlayerObj->initGoId(theNewObjectId);
	m_objects[theNewObjectId]=objectPtr(newPlayerObj);
	return theNewObjectId;
}

void ObjectMgr::destroyObject( uint32 goId )
{
	//erase from valid objects
	objectsMap::iterator it=m_objects.find(goId);
	if (it!=m_objects.end())
	{
		it->second.reset();
	}
	if (it!=m_objects.end())
	{
		m_objects.erase(it);
	}

	//erase from object view maps (of all clients) and release object view
	for (clientToViewMap::iterator it1=m_views.begin();it1!=m_views.end();++it1)
	{
		for (viewIdsMap::iterator it2=it1->second.begin();it2!=it1->second.end();)
		{
			uint32 theGoId = it2->second;
			if (theGoId == goId)
				it1->second.erase(it2++);
			else
				++it2;
		}
	}
}

class PlayerObject* ObjectMgr::getGOPtr( uint32 goId )
{
	objectsMap::iterator it=m_objects.find(goId);
	if (it!=m_objects.end())
		return it->second.get();

	throw ObjectNotAvailable();
}

uint32 ObjectMgr::getGOId( class PlayerObject* forWhichObj )
{
	if (forWhichObj==NULL)
		throw ObjectNotAvailable();

	for (objectsMap::iterator it=m_objects.begin();it!=m_objects.end();++it)
	{
		if (it->second.get() == forWhichObj)
			return it->first;
	}

	throw ObjectNotAvailable();
}

uint16 ObjectMgr::getViewForGO( GameClient* requester, uint32 goId )
{
	if (requester==NULL)
		throw ClientNotAvailable();

	if (m_objects.find(goId)==m_objects.end())
		throw ObjectNotAvailable();

/*	viewIdsMap &viewsOfClient = m_views[requester];
	for (viewIdsMap::const_iterator it=viewsOfClient.begin();it!=viewsOfClient.end();++it)
	{
		if (it->second == goId)
			return it->first;
	}

	//otherwise allocate new viewID, put that in the views list with the goId, and return it
	uint16 newViewId = allocateViewId(requester);
	m_views[requester][newViewId] = goId;
	return newViewId;*/

	return uint16(goId);
}

void ObjectMgr::releaseRelevantSet( GameClient *requester )
{
	clientToViewMap::iterator it=m_views.find(requester);
	if (it!=m_views.end())
		m_views.erase(it);
}

uint16 ObjectMgr::allocateViewId( GameClient* requester)
{
	if (requester == NULL)
		throw ClientNotAvailable();

	//get the views map for current client
	const viewIdsMap &viewsOfClient = m_views[requester];
	//go through all possible viewIds, when we find one thats not in the list, return it
	for (uint16 i=3;i<0xFFFF;i++) //we start from 2 because 1 is the object manager id, it spawns and deletes objects  // we start from 3, cuz 2 doesnt work
	{
		if (viewsOfClient.find(i)==viewsOfClient.end())
			return i;
	}
	throw NoMoreFreeViews();
}

#include "GameServer.h"

void ObjectMgr::RandomObject( uint32 randomObjectId, GameClient* requester, double X, double Y, double Z, double ROT)
{
	//uint32 randObjId = rand() % 0xFFFFFFFF;

	string msg1 = (format("{c:0FFFF0}Object :%1%{/c}") % (int)randomObjectId).str();
	sGame.AnnounceCommand(NULL,make_shared<SystemChatMsg>(msg1));

	
	uint16 randViewId = rand() % 0xFFFF;

	std::string s;
	std::stringstream out;
	out << "Do Object With ViewId: ";
	out << int(randViewId);
	s = out.str();

	sGame.AnnounceCommand(NULL,make_shared<SystemChatMsg>(s));
	sGame.AnnounceStateUpdate(NULL,make_shared<DoorAnimationMsg>(randomObjectId, randViewId, X, Y, Z, ROT, 1));	
}


void ObjectMgr::OpenDoor( uint32 doorId, GameClient* requester)
{
	//Does this work?
	int doorOpenCount = 0;
	for (map<uint16,uint32>::iterator it=m_openDoors.begin();it!=m_openDoors.end();++it)
	{
		doorOpenCount++;
		if (it->second == doorId)
		{
			//Didnt work first time, lets change door type
			string sqlUpdateDoorType = (format("Update Doors Set DoorType = 0, `DoorId` = '%1%' Limit 1") % (int)doorId).str();
			if (sDatabase.Execute(sqlUpdateDoorType))
			{
				string msg1 = (format("{c:0FFFF0}Door:%1% Set to Indoors since u tried to open it but I think it is open, try again.{/c}") % (int)doorId).str();
				
				//Close Doors not working
				//sGame.AnnounceStateUpdate(NULL,make_shared<CloseDoorMsg>(it->first));	

				sGame.AnnounceCommand(NULL,make_shared<SystemChatMsg>(msg1));
			}
			m_openDoors.erase(it);
			return;
		}
		
	}

	string msg2 = (format("{c:0FFFF0}Door:%1%{/c}") % (int)doorId).str();
	sGame.AnnounceCommand(NULL,make_shared<SystemChatMsg>(msg2));

	if (doorOpenCount > 30) //if 10+ doors, then we want to close one
	{
		for (map<uint16,uint32>::iterator it=m_openDoors.begin();it!=m_openDoors.end();++it)
		{
			//Close Doors not working
			//sGame.AnnounceStateUpdate(NULL,make_shared<CloseDoorMsg>(it->first));						
			m_openDoors.erase(it);						
			break; //exit loop we just wanted the first one
		}
		
		
	}

	uint16 viewId = allocateViewId(requester);
	viewIdsMap &viewsOfClient = m_views[requester];
	viewsOfClient[viewId]=doorId;
	m_openDoors[viewId]=doorId;
	

	std::string s;
	std::stringstream out;
	out << "Door Opened With ViewId: ";
	out << int(viewId);
	s = out.str();

	sGame.AnnounceCommand(NULL,make_shared<SystemChatMsg>(s));

	//sGame.AnnounceStateUpdate(NULL,make_shared<DeleteDoorMsg>(doorId));	
	string sqlDoor = (format("Select X,Y,Z,ROT,DoorType from Doors Where `DoorId` = '%1%' Limit 1") % (int)doorId).str();

	scoped_ptr<QueryResult> resultDoor(sDatabase.Query(sqlDoor));
	if (resultDoor != NULL)
	{
		Field *field = resultDoor->Fetch();
		double X = field[0].GetDouble();
		double Y = field[1].GetDouble();
		double Z = field[2].GetDouble();
		double O = field[3].GetDouble();
		int doorType = field[4].GetUInt16();
		//int doorType = 1;

		sGame.AnnounceStateUpdate(NULL,make_shared<DoorAnimationMsg>(doorId, viewId, X, Y, Z, O, doorType));
	}

}

vector<msgBaseClassPtr> ObjectMgr::GetAllOpenDoors( GameClient* requester )
{
	vector<msgBaseClassPtr> tempVec;

	//Does this work?

	//Set cleitn views to current views.. (so we know which doors are open)
	viewIdsMap &viewsOfClient = m_views[requester];

	for (map<uint16,uint32>::iterator it=m_openDoors.begin();it!=m_openDoors.end();++it)
	{
		viewsOfClient[it->first] = it->second;

		string sqlDoor = (format("Select X,Y,Z,ROT,DoorType from Doors Where `DoorId` = '%1%' Limit 1") % (int)it->second).str();
		scoped_ptr<QueryResult> resultDoor(sDatabase.Query(sqlDoor));
		if (resultDoor != NULL)
		{
			Field *field = resultDoor->Fetch();
			double X = field[0].GetDouble();
			double Y = field[1].GetDouble();
			double Z = field[2].GetDouble();
			double O = field[3].GetDouble();
			int doorType = field[4].GetUInt16();
			//int doorType = 1;
			
			tempVec.push_back(make_shared<DoorAnimationMsg>(it->second,it->first, X, Y, Z, O, doorType));
		}
	}
	return tempVec;
}