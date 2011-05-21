# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from CIM14.CDPSM.GIS_Connectivity.IEC61970.Wires.ACLineSegment import ACLineSegment

class DistributionLineSegment(ACLineSegment):
    """Extends ACLineSegment with references to a library of standard types from which electrical parameters can be calculated, as follows:
    """

    def __init__(self, ConductorInfo=None, SequenceImpedance=None, PhaseImpedance=None, *args, **kw_args):
        """Initialises a new 'DistributionLineSegment' instance.

        @param ConductorInfo: Conductor data of this conductor segment.
        @param SequenceImpedance: Sequence impedance of this conductor segment; used for balanced model.
        @param PhaseImpedance: Phase impedance of this conductor segment; used for unbalanced model.
        """
        self._ConductorInfo = None
        self.ConductorInfo = ConductorInfo

        self._SequenceImpedance = None
        self.SequenceImpedance = SequenceImpedance

        self._PhaseImpedance = None
        self.PhaseImpedance = PhaseImpedance

        super(DistributionLineSegment, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["ConductorInfo", "SequenceImpedance", "PhaseImpedance"]
    _many_refs = []

    def getConductorInfo(self):
        """Conductor data of this conductor segment.
        """
        return self._ConductorInfo

    def setConductorInfo(self, value):
        if self._ConductorInfo is not None:
            filtered = [x for x in self.ConductorInfo.ConductorSegments if x != self]
            self._ConductorInfo._ConductorSegments = filtered

        self._ConductorInfo = value
        if self._ConductorInfo is not None:
            if self not in self._ConductorInfo._ConductorSegments:
                self._ConductorInfo._ConductorSegments.append(self)

    ConductorInfo = property(getConductorInfo, setConductorInfo)

    def getSequenceImpedance(self):
        """Sequence impedance of this conductor segment; used for balanced model.
        """
        return self._SequenceImpedance

    def setSequenceImpedance(self, value):
        if self._SequenceImpedance is not None:
            filtered = [x for x in self.SequenceImpedance.ConductorSegments if x != self]
            self._SequenceImpedance._ConductorSegments = filtered

        self._SequenceImpedance = value
        if self._SequenceImpedance is not None:
            if self not in self._SequenceImpedance._ConductorSegments:
                self._SequenceImpedance._ConductorSegments.append(self)

    SequenceImpedance = property(getSequenceImpedance, setSequenceImpedance)

    def getPhaseImpedance(self):
        """Phase impedance of this conductor segment; used for unbalanced model.
        """
        return self._PhaseImpedance

    def setPhaseImpedance(self, value):
        if self._PhaseImpedance is not None:
            filtered = [x for x in self.PhaseImpedance.ConductorSegments if x != self]
            self._PhaseImpedance._ConductorSegments = filtered

        self._PhaseImpedance = value
        if self._PhaseImpedance is not None:
            if self not in self._PhaseImpedance._ConductorSegments:
                self._PhaseImpedance._ConductorSegments.append(self)

    PhaseImpedance = property(getPhaseImpedance, setPhaseImpedance)
