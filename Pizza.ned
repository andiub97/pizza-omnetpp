//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU Lesser General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
// 
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU Lesser General Public License for more details.
// 
// You should have received a copy of the GNU Lesser General Public License
// along with this program.  If not, see http://www.gnu.org/licenses/.
// 

package org.omnetpp.queueing;

network Pizza
{
    @display("bgb=486,223");
    submodules:
        U1: Source {
            @display("p=58,59");
            jobType = 1;
            jobPriority = 1;
        }
        U2: Source {
            @display("p=58,137");
            jobType = 2;
            jobPriority = 0;
        }
        sink: Sink {
            @display("p=407,98");
        }
        PS: Server {
            @display("p=219,98");
        }
        EntryQueue: PassiveQueue {
            @display("p=134,98");
        }
        CS: Queue {
            @display("p=314,98");
            capacity = 0;
        }
    connections:
        U1.out --> EntryQueue.in++;
        U2.out --> EntryQueue.in++;
        EntryQueue.out++ --> PS.in++;
        PS.out --> CS.in++;
        CS.out --> sink.in++;
}
