
# E10 Test Specification for Type Approval

**E10**
(1991)
(Rev.1 1993)
(Rev.2 1997)
(Rev. 2.1 July 1999)
(Rev.3 May 2001)
(Corr.1 July 2003)
(Rev.4 May 2004)
(Rev.5 Dec 2006)
(Rev.6 Oct 2014)
(Rev.7 Oct 2018)
(Rev.8 Feb 2021)
(Corr.1 Jan 2022)
(Rev.9 Aug 2023)
(Rev.10 Aug 2024)

## E10.1 General

This Test Specification is applicable, but not confined, to electrical, electronic and programmable equipment intended for control, monitoring, alarm and protection systems for use in ships.

## E10.2 Testing

These tests are to demonstrate the ability of the equipment to function as intended under the specified testing conditions.

The extent of the testing (i.e. the selection and sequence of carrying out tests and number of pieces to be tested) is to be determined upon examination and evaluation of the equipment or component subject to testing giving due regard to its intended usage.

Equipment is to be tested in its normal position if otherwise not specified in the test specification.

**Note:**

1. Rev.5 of this UR is to be uniformly implemented by IACS Societies from 1 January 2008.
2. Rev.6 of this UR is to be uniformly implemented by IACS Societies from 1 January 2016.
3. Rev.7 of this UR is to be uniformly implemented by IACS Societies for equipment for which the date of application for type approval certification is dated on or after 1 January 2020.
4. Equipment intended to be installed on ships contracted for construction on or after 1 January 2022 is to comply with Rev.7 of this UR.
5. The "contracted for construction" date means the date on which the contract to build the vessel is signed between the prospective owner and the shipbuilder. For further details regarding the date of "contract for construction", refer to IACS Procedural Requirement (PR) No. 29.
6. The "date of application for type approval" is the date of documents accepted by the Classification Society as request for type approval certification of a new equipment type or of an equipment type that has undergone substantive modifications in respect of the one previously type approved, or for renewal of an expired type approval certificate.
7. Rev.8 of this UR is to be uniformly implemented by IACS Societies for equipment for which the date of application for type approval certification is dated on or after 1 July 2022.
8. Rev.9 of this UR is to be uniformly implemented by IACS Societies for equipment for which the date of application for type approval certification is dated on or after 1 July 2024.
9. Rev.10 of this UR is to be uniformly implemented by IACS Societies for equipment for which the date of application for type approval certification is dated on or after 1 January 2026.

---

Relevant tests are as listed in the Table.

**Note:**

a) * These test requirements are harmonised with IEC 60092-504:2016 "Electrical Installations in Ships – Part 504: Special features – Control and Instrumentation" and IEC 60533:2015 "Electrical and electronic installations in ships – electromagnetic compatibility". Electrical and electronic equipment on board ships, required neither by classification rules nor by International Conventions, liable to cause electromagnetic disturbance shall be of type which fulfil the test requirements of test specification items 19 and 20.

b) As used in this document, and in contrast to a complete performance test, a functional test is a simplified test sufficient to verify that the equipment under test (EUT) has not suffered any deterioration caused by the individual environmental tests.

### Type testing condition for equipment covered by E10.1

| NO. | TEST | PROCEDURE ACC. TO:* | TEST PARAMETERS | OTHER INFORMATION |
| :--- | :--- | :--- | :--- | :--- |
| | | * indicates the testing procedure which is normally to be applied. However, equivalent testing procedure may be accepted by the individual Society provided that the Unified Requirements stated in the other columns are fulfilled. Later versions (including revisions) of the international standards specified in this UR are acceptable for use, provided the Society determines them to be equivalent to the technical specifications of this UR. | | |
| 1. | Visual inspection | - | - | - conformance to drawings, design data |
| 2. | Performance test | Manufacturer performance test programme based upon specification and relevant Rule requirements. When the EUT is required to comply with an international performance standard, e.g. protection relays, verification of requirements in the standard are to be part of the performance testing required in this initial test and subsequent performance tests after environmental testing where required in the UR. | - standard atmosphere conditions<br>- temperature: 25°C ± 10°C<br>- relative humidity: 60% ± 30%<br>- air pressure: 96 Kpa ± 10KPa | - confirmation that operation is in accordance with the requirements specified for particular system or equipment;<br>- checking of self-monitoring features;<br>- checking of specified protection against an access to the memory;<br>- checking against effect of unerroneous use of control elements in the case of computer systems. |
| 3. | External power supply failure | - | - 3 interruptions during 5 minutes;<br>- switching-off time 30 s each case | - The time of 5 minutes may be exceeded if the equipment under test needs a longer time for start-up, e.g. booting sequence<br>- For equipment which requires booting, one additional power supply interruption during booting to be performed<br>Verification of:<br>- equipment behaviour upon loss and restoration of supply;<br>- possible corruption of programme or data held in programmable electronic systems, where applicable. |
| 4. | Power supply variations<br>a) electric<br>b) pneumatic and hydraulic | - | **AC SUPPLY**<br>Combination 1: Voltage +6%, Frequency +5%<br>Combination 2: Voltage +6%, Frequency -5%<br>Combination 3: Voltage -10%, Frequency -5%<br>Combination 4: Voltage -10%, Frequency +5%<br>Combination 5: Voltage transient +20% (1.5s), Frequency transient +10% (5s)<br>Combination 6: Voltage transient -20% (1.5s), Frequency transient -10% (5s)<br><br>**DC SUPPLY**<br>Voltage tolerance continuous: ±10%<br>Voltage cyclic variation: 5%<br>Voltage ripple: 10%<br><br>**Electric battery supply:**<br>- +30% to –25% for equipment connected to charging battery or as determined by the charging/discharging characteristics, including ripple voltage from the charging device;<br>- +20% to –25% for equipment not connected to the battery during charging.<br><br>Pressure: ±20%<br>Duration: 15 minutes | Verification of:<br>- equipment behaviour upon loss and restoration of supply;<br>- possible corruption of programme or data held in programmable electronic systems, where applicable. |
| 5. | Dry heat (see note 1) | IEC 60068-2-2:2007 Test Bb for non-heat dissipating equipment / Test Be for heat dissipating equipment | Temperature: 55°C ± 2°C or 70°C ± 2°C<br>Duration: 16 hours | - equipment operating during conditioning and testing;<br>- functional test (b) during the last hour at the test temperature. |
| 6. | Damp heat | IEC 60068-2-30:2005 test Db | Temperature: 55°C<br>Humidity: 95%<br>Duration: 2 cycles 2 x (12 + 12 hours) | - measurement of insulation resistance before test;<br>- the test shall start with 25°C ± 3°C and at least 95% humidity;<br>- equipment operating during the complete first cycle and switched off during second cycle except for functional test;<br>- recovery at standard atmosphere conditions;<br>- insulation resistance measurements and performance test. |
| 7. | Vibration | IEC 60068-2-6:2007 Test Fc | 2 Hz to 13.2 Hz – amplitude ±1mm<br>13.2 Hz to 100 Hz – acceleration ± 0.7 g.<br>For severe vibration conditions:<br>2.0 Hz to 25 Hz – amplitude ±1.6 mm<br>25.0 Hz to 100 Hz – acceleration ± 4.0 g. | - duration at each resonance frequency at which Q ≥ 2 is recorded - 90 minutes;<br>- during the vibration test, functional tests are to be carried out;<br>- tests to be carried out in three mutually perpendicular planes;<br>- it is recommended as guidance that Q does not exceed 5. |
| 8. | Inclination | IEC 60092-504:2016 | Static 22.5°<br>Dynamic 22.5° | a) inclined to the vertical at an angle of at least 22.5° in four directions;<br>Dynamic: rolled to an angle of 22.5° each side with a period of 10 seconds, not less than 15 minutes per direction. |
| 9. | Insulation resistance | - | Un ≤ 65V: Test 2xUn min 24V, Min 10/1.0 MΩ<br>Un > 65V: Test 500V, Min 100/10 MΩ | - insulation resistance test before and after: damp heat, cold, salt mist, high voltage test;<br>- between all phases and earth. |
| 10. | High voltage | - | Up to 65V: 2xUn + 500V<br>66-250V: 1500V<br>251-500V: 2000V<br>501-690V: 2500V | - period of application: 1 minute |
| 11. | Cold | IEC 60068-2-1:2007 | Temperature: +5°C ± 3°C or –25°C ± 3°C<br>Duration: 2 hours | - functional test during the last hour at the test temperature |
| 12. | Salt mist | IEC 60068-2-52:2017 Test Kb | Four spraying periods with a storage of 7 days after each. | - functional test on the 7th day of each storage period |
| 13. | Electrostatic discharge | IEC 61000-4-2:2008 | Contact discharge: 6kV<br>Air discharge: 2kV, 4kV, 8kV<br>No. of pulses: 10 per polarity<br>Test level 3. | - Performance Criterion B |
| 14. | Electromagnetic field | IEC 61000-4-3:2020 or IEC 61000-4-3:2006+AMD1:2007+AMD2:2010 | Frequency range: 80 MHz to 6 GHz<br>Modulation: 80% AM at 1000Hz<br>Field strength: 10V/m<br>Test level 3. | - Performance criterion A |
| 15. | Conducted low Frequency | - | **AC:** Frequency range: rated frequency to 200th harmonic<br>**DC:** Frequency range: 50 Hz - 10 kHz | - performance criterion A |
| 16. | Conducted Radio Frequency | IEC 61000-4-6:2023 | Frequency range: 150 kHz - 80 MHz<br>Amplitude: 3 V rms<br>Modulation: 80% AM at 1000 Hz<br>Test level 2. | - performance criterion A |
| 17. | Electrical Fast Transients / Burst | IEC 61000-4-4:2012 | Amplitude (peak): 2kV power supply; 1kV I/O ports<br>Test level 3. | - performance criterion B |
| 18. | Surge | IEC 61000-4-5:2014+AMD1:2017 | Amplitude (peak): 1kV line/earth; 0.5kV line/line<br>Test level 2. | - performance criterion B |
| 19. | Radiated Emission | CISPR 16-2-3:2016+AMD1:2019+AMD2:2023<br>IEC 60945:2002 for 156-165 MHz | Bridge/deck zone and general power distribution zone limits specified per frequency range. | - distance 3 m between equipment and antenna |
| 20. | Conducted Emission | CISPR 16-2-1:2014+AMD1:2017 | Bridge/deck zone and general power distribution zone limits specified per frequency range. | |
| 21. | Flame retardant | IEC 60092-101:2018 or IEC 60695-11-5:2016 | Flame application: 5 times 15 s each or 1 time 30s. | - burnt/damaged part not more than 60 mm long;<br>- extinguish within 30 s |

---

**Notes:**

1. Dry heat at 70 °C is to be carried out to automation, control and instrumentation equipment subject to high degree of heat, for example mounted in consoles, housings, etc. together with other heat dissipating power equipment.
2. For equipment installed in non-weather protected locations or cold locations test is to be carried out at –25°C.
3. Salt mist test is to be carried out for equipment installed in weather exposed areas.
4. Performance Criterion B: (For transient phenomena): The EUT shall continue to operate as intended after the tests. No degradation of performance or loss of function is allowed. During the test, degradation or loss of function which is self recoverable is allowed but no change of actual operating state or stored data is allowed.
5. Performance Criterion A: (For continuous phenomena): The Equipment Under Test shall continue to operate as intended during and after the test. No degradation of performance or loss of function is allowed.
6. For equipment installed on the bridge and deck zone, the test levels shall be increased to 10V rms for spot frequencies in accordance with IEC 60945:2002 at 2, 3, 4, 6.2, 8.2, 12.6, 16.5, 18.8, 22, 25 MHz.

![Figure 1: Test set-up for Conducted Low Frequency Test showing a generator connected to the EUT with a voltmeter and optional decoupling capacitor, powered by an AC or DC supply.](test_setup_conducted_low_frequency)

**End of Document**

