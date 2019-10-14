//
// This file is part of an OMNeT++/OMNEST simulation example.
//
// Copyright (C) 2006-2015 OpenSim Ltd.
//
// This file is distributed WITHOUT ANY WARRANTY. See the file
// `license' for details on this and other legal matters.
//

package org.omnetpp.queueing;

//
// Queue server. It serves multiple input queues (PassiveQueue), using a preset
// algorithm. Inputs must be connected to Passive Queues (PassiveQueue)
//
simple Server
{
    parameters:
        @group(Queueing);
        @display("i=block/server");
        @signal[busy](type="bool");
        @statistic[busy](title="server busy state";record=vector?,timeavg;interpolationmode=sample-hold);

        string fetchingAlgorithm @enum("priority","random","roundRobin","longestQueue") = default("priority");
             // how the next job will be choosen from the attached queues
        volatile double serviceTimeDirectU1 @unit(s); // service time of a PS job directly managed
        volatile double serviceTimeDirectU2 @unit(s);
        volatile double serviceTimeForInventoryU1 @unit(s); //service time of a PS job gotten from inventory
        volatile double serviceTimeForInventoryU2 @unit(s); //service time of a PS job gotten from inventory
        volatile double probabilityProducing;
        volatile int maxInventoriedPS; //maximum number of inventoried PS stored
    gates:
        input in[];
        output out;
}


