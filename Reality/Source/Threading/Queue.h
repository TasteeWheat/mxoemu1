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

#ifndef MXOSIM_QUEUE_H
#define MXOSIM_QUEUE_H

#include "Condition.h"
#include "NativeMutex.h"

template<class T> 
class FQueue 
{
public:
	inline FQueue() : cond(&lock) {first=last=NULL;size=0;}
	volatile unsigned int size;

	uint32 get_size()
	{
		uint32 ret;
		cond.BeginSynchronized();
		ret = size;
		cond.EndSynchronized();
		return ret;
	}

	void push(T item)
	{
		h*p=new h;
		p->value=item;
		p->pNext=NULL;

		//lock.Acquire();
		cond.BeginSynchronized();
		if(last)//have some items
		{
			last->pNext=p;
			last=p;
			size++;
		}
		else//first item
		{
			last=first=p;
			size=1;
			cond.Signal();
		}
		//lock.Release();
		cond.EndSynchronized();
	}

	T pop_nowait()
	{
		//lock.Acquire();
		cond.BeginSynchronized();
		if(size==0)
		{
			cond.EndSynchronized();
			return NULL;
		}

		h*tmp=first;
		if(tmp == NULL)
		{
			cond.EndSynchronized();
			return NULL;
		}

		if(--size)//more than 1 item
		{
			first=(h*)first->pNext;
		}
		else//last item
		{
			first=last=NULL;
		}
		//lock.Release();
		cond.EndSynchronized();

		T returnVal = tmp->value;
		delete tmp;

		return returnVal;
	}

	T pop()
	{
		//lock.Acquire();
		cond.BeginSynchronized();
		if(size==0)
			cond.Wait();

		h*tmp=first;
		if(tmp == NULL)
		{
			cond.EndSynchronized();
			return NULL;
		}

		if(--size)//more than 1 item
		{
			first=(h*)first->pNext;
		}
		else//last item
		{
			first=last=NULL;
		}
		//lock.Release();
		cond.EndSynchronized();

		T returnVal = tmp->value;
		delete tmp;

		return returnVal;
	}	

	inline Condition& GetCond() { return cond; }

private:
	struct h
	{
		T value;
		void *pNext;
	};

	h*first;
	h*last;

	NativeMutex lock;
	Condition cond;

};

#endif 


