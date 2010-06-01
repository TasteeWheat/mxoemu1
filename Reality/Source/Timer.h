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

#ifndef MXOSIM_TIMER_H
#define MXOSIM_TIMER_H

#include <time.h>
#include <stdlib.h>

/**
 * This is a very simple timer that can be used to schedule different
 * events to happen over certain periods of time. The timer period is
 * limited to about 60000 units, no matter what units - the timer
 * does not make any assumptions about that.
 */
class Timer
{
	uint16 Interval;
	uint16 Current;

public:
	/**
	 * Initialize the timer so that it ticks with specified period.
	 * If interval is 0, timer is disabled.
	 */
    Timer ()
	{ Current = 0; }

	/// Check if timer is enabled
	bool Enabled () const
	{ return Interval != 0; }

	/// Disable timer: there's no way to enable it other than using SetInterval()
	void Disable ()
	{ Interval = 0; }

	/**
	 * Change timer interval
	 */
	void SetInterval (uint16 interval)
	{ Interval = interval; Current = 0; }

	/**
	 * Tell the timer that a certain interval of time has passed.
	 * @arg delta
	 *   Delta time that have passed since last call to this function.
	 * @return
	 *   Number of timer pulses that have passed.
	 */
	uint Tick (uint delta)
	{
		Current += delta;
		if (!Interval || Current < Interval)
			return 0;
		div_t d = div (Current, Interval);
		Current = d.rem;
		return d.quot;
	}

	/**
	 * Reset the timer so that next event will happen
	 * after Interval ticks.
	 */
	void Reset ()
	{ Current = 0; }
};

inline uint32 getTime()
{
    return (uint32)time(NULL);
}

#ifdef WIN32
__forceinline uint32 getMSTime() { return GetTickCount(); }
#else
inline uint32 getMSTime()
{
	struct timeval tv;
	gettimeofday(&tv, NULL);
	return (tv.tv_sec * 1000) + (tv.tv_usec / 1000);
}
#endif

#endif
