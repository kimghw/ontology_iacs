# FILE: UR_E/UR-E27-Rev.1-Sep-2023-CLN.md
================================================================================

# E27 Cyber resilience of on-board systems and equipment

**(Apr 2022 Withdrawn)**
**(Rev.1 Sep 2023)**

## 1. General

### 1.1 Introduction

Technological evolution of vessels, ports, container terminals, etc. and increased reliance upon Operational Technology (OT) and Information Technology (IT) has created an increased possibility of cyber-attacks to affect business, personnel data, human safety, the safety of the ship, and also possibly threaten the marine environment. Safeguarding shipping from current and emerging threats must involve a range of controls that are continually evolving which would require incorporating security features in the equipment and systems at design and manufacturing stage. It is therefore necessary to establish a common set of minimum requirements to deliver systems and equipment that can be described as cyber resilient.

This document specifies unified requirements for cyber resilience of on-board systems and equipment.

### 1.2 Limitations

This UR does not cover environmental performance for the system hardware and the functionality of the software. In addition to this UR, following URs shall be applied:

- UR E10 for environmental performance for the system hardware
- UR E22 for safety of equipment for the functionality of the software

**Note:**

1. The Unified Requirement published in April 2022 was withdrawn before coming into force on 1 January 2024
2. Rev.1 to this UR is to be uniformly implemented by IACS Societies on ships contracted for construction on or after 1 July 2024 and may be used for other ships as non-mandatory guidance.
3. The "contracted for construction" date means the date on which the contract to build the vessel is signed between the prospective owner and the shipbuilder. For further details regarding the date of "contract for construction", refer to IACS Procedural Requirement (PR) No. 29.

---

### 1.3 Scope of applicability

The requirements specified in this UR are applicable to computer based systems specified in UR E26 for the following types of vessels:

**Mandatory requirements for**

a) Passenger ships (including passenger high-speed craft) engaged in international voyages
b) Cargo ships of 500 GT and upwards engaged in international voyages
c) High speed craft of 500 GT and upwards engaged in international voyage
d) Mobile offshore drilling units of 500 GT and upwards
e) Self-propelled mobile offshore units engaged in construction

**Non-mandatory guidance to**

a) Ships of war and troopships
b) Cargo ships less than 500 gross tonnage
c) Vessels not propelled by mechanical means
d) Wooden ships of primitive build
e) Passenger yachts (passengers not more than 12).
f) Pleasure yachts not engaged in trade
g) Fishing vessels
h) Site specific offshore installations (i.e. FPSOs, FSUs, etc)

For navigation and radiocommunication systems, the application of IEC 61162-460 or other equivalent standards in lieu of the required security capabilities in UR E27 section 4 may be accepted by the Society, on the condition that requirements in IACS UR E26 are complied with.

#### 1.3.1 Information and Communication Technology (ICT)

Attention is made to additional IACS documents on Computer Based Systems and Cyber Resilience as follows:

IACS UR E22 "Computer based systems" includes requirements for design, construction, commissioning and maintenance of computer-based systems where they depend on software for the proper achievement of their functions.

IACS UR E26 "Cyber resilience of Ships" includes requirements for cyber resilience of ships, with the purpose of providing technical means to stakeholders which would lead to cyber resilient ships.

IACS Recommendation 166 on Cyber Resilience: non-mandatory recommended technical requirements that stakeholders may reference and apply to assist with the delivery of cyber resilient ships.

---

### 1.4 Definitions & Abbreviations

**Attack surface:** The set of all possible points where an unauthorized user can access a system, cause an effect on or extract data from.

**Authentication:** Provision of assurance that a claimed characteristic of an identity is correct.

**Compensating countermeasure:** An alternate solution to a countermeasure employed in lieu of or in addition to inherent security capabilities to satisfy one or more security requirements.

**Computer Based System (CBS):** A programmable electronic device, or interoperable set of programmable electronic devices, organized to achieve one or more specified purposes such as collection, processing, maintenance, use, sharing, dissemination, or disposition of information.

**Computer Network:** A connection between two or more computers for the purpose of communicating data electronically by means of agreed communication protocols.

**Control:** Means of managing risk, including policies, procedures, guidelines, practices or organizational structures, which can be administrative, technical, management, or legal in nature.

**Cyber incident:** An event resulting from any offensive cyber manoeuvre, either intentional or unintentional, that targets or affects one or more CBS onboard.

**Cyber resilience:** The capability to reduce the occurrence and mitigating the effects of incidents arising from the disruption or impairment of operational technology (OT) used for the safe operation of a ship.

**Defence in depth:** Information Security strategy integrating people, technology, and operations capabilities to establish variable barriers across multiple layers and missions of the organization.

**Essential Systems:** Computer Based System contributing to the provision of services essential for propulsion and steering, and safety of the ship.

**Firewall:** A logical or physical barrier that monitors and controls incoming and outgoing network traffic controlled via predefined rules.

**Firmware:** Software embedded in electronic devices that provide control, monitoring and data manipulation of engineered products and systems.

**Hardening:** Hardening is the practice of reducing a system's vulnerability by reducing its attack surface.

**Information Technology (IT):** Devices, software and associated networking focusing on the use of data as information, as opposed to Operational Technology (OT).

**Integrated system:** A system combining a number of interacting sub-systems and/or equipment organized to achieve one or more specified purposes.

**Network switch (Switch):** A device that connects devices together on a computer network, by using packet switching to receive, process and forward data to the destination device.

**Offensive cyber manoeuvre:** Actions that result in denial, degradation, disruption, destruction, or manipulation of OT or IT systems.

**Operational technology (OT):** Devices, sensors, software and associated networking that monitor and control onboard systems.

**OT system:** Computer based systems, which provide control, alarm, monitoring, safety or internal communication functions.

**Patches:** Software designed to update installed software or supporting data to address security vulnerabilities and other bugs or improve operating systems or applications.

**Protocols:** A common set of rules and signals that computers on the network use to communicate.

**Recovery:** Develop and implement the appropriate activities to maintain plans for resilience and to restore any capabilities or services that were impaired due to a cyber security event.

**Supplier:** A manufacturer or provider of hardware and/or software products, system components or equipment.

**System:** Combination of interacting programmable devices and/or sub-systems organized to achieve one or more specified purposes.

**System Categories (I, II, III):** System categories based on their effects on system functionality, which are defined in IACS UR E22.

**System Integrator:** The specific person or organization responsible for the integration of systems and products provided by suppliers into the system invoked by the requirements in the ship specifications.

**Untrusted network:** Any network outside the scope of applicability of this UR.

---

## 2. Security Philosophy

### 2.1 Systems and Equipment

2.1.1 A System can consist of group of hardware and software enabling safe, secure and reliable operation of a process.

2.1.2 Equipment may be one of the following:
- Network devices (i.e. routers, managed switches)
- Security devices (i.e. firewall, Intrusion Detection System)
- Computers (i.e. workstation, servers)
- Automation devices (i.e. Programmable Logic Controllers)
- Virtual machine cloud-hosted

### 2.2 Cyber Resilience

The cyber resilience requirements in section 4 will be applicable for all systems in scope of UR E26 as applicable. Additional requirements related to interface with untrusted networks will only apply for systems where such connectivity is designed.

### 2.3 Essential Systems Availability

2.3.1 Security measures for Essential system shall not adversely affect the systems availability.

2.3.2 Implementation of security measures shall not cause loss of safety functions, loss of control functions, loss of monitoring functions or loss of other functions which could result in health, safety and environmental consequences.

2.3.3 The system shall be adequately designed to allow the ship to continue its mission critical operations in a manner that ensures the confidentiality, integrity, and availability of the data necessary for safety of the vessel, its systems, personnel and cargo.

### 2.4 Compensating Countermeasures

2.4.1 Compensating countermeasure may be employed in lieu of or in addition to inherent security capabilities to satisfy one or more security requirements.

---

## 3. Documentation

### 3.1 CBS Documentation

The following documents shall be submitted to Classification society for review and approval in accordance with the requirements in this UR.

#### 3.1.1 CBS asset inventory

The CBS asset inventory shall include:
- List of hardware components (name, brand/manufacturer, model/type, description, physical interfaces, system software, version/patch level, supported protocols)
- List of software components (hardware location, brand/manufacturer, model/type, description, version)

#### 3.1.2 Topology diagrams

Physical topology diagram shall illustrate the physical architecture. Logical topology diagram shall illustrate the data flow between components.

#### 3.1.3 Description of security capabilities

This document shall describe how the CBS meets the required security capabilities in section 4.1.

#### 3.1.4 Test procedure of security capabilities

This document shall describe how to demonstrate by testing that the system complies with requirements in section 4.1 and 4.2.

#### 3.1.5 Security configuration guidelines

This document shall describe recommended configuration settings of the security capabilities and specify default values.

#### 3.1.6 Secure development lifecycle documents

This documentation shall describe the supplier's processes and controls in accordance with requirements for secure development lifecycle in section 5.

#### 3.1.7 Plans for maintenance and verification of the CBS

This document shall include procedures for security-related maintenance and testing of the system.

#### 3.1.8 Information supporting the owner's incident response and recovery plan

This document shall include procedures or instructions for local independent control, network isolation, forensics, deterministic output, backup, restore, and controlled shutdown/reset/roll-back/restart.

#### 3.1.9 Management of change plan

#### 3.1.10 Test reports

CBSs with Type approval certificate covering the security capabilities may be exempted from survey by the Society.

---

## 4. System Requirements

### 4.1 Required security capabilities

**Table 1**

| Item No | Objective | Requirements |
| :--- | :--- | :--- |
| 1 | Human user identification and authentication | The CBS shall identify and authenticate all human users (IEC 62443-3-3/SR 1.1) |
| 2 | Account management | Support management of all accounts (IEC 62443-3-3/SR 1.3) |
| 3 | Identifier management | Support management of identifiers by user, group and role (IEC 62443-3-3/SR 1.4) |
| 4 | Authenticator management | Initialize, change defaults, change/refresh, protect authenticators (IEC 62443-3-3/SR 1.5) |
| 5 | Wireless access management | Identify and authenticate all wireless users (IEC 62443-3-3/SR 1.6) |
| 6 | Strength of password-based authentication | Enforce configurable password strength (IEC 62443-3-3/SR 1.7) |
| 7 | Authenticator feedback | Obscure feedback during authentication (IEC 62443-3-3/SR 1.10) |
| 8 | Authorization enforcement | Assign authorizations per segregation of duties and least privilege (IEC 62443-3-3/SR 2.1) |
| 9 | Wireless use control | Authorize, monitor and enforce wireless usage restrictions (IEC 62443-3-3/SR 2.2) |
| 10 | Use control for portable and mobile devices | Limit and restrict portable/mobile device use (IEC 62443-3-3/SR 2.3) |
| 11 | Mobile code | Control use of mobile code (IEC 62443-3-3/SR 2.4) |
| 12 | Session lock | Prevent access after configurable inactivity time (IEC 62443-3-3/SR 2.5) |
| 13 | Auditable events | Generate audit records for security events (IEC 62443-3-3/SR 2.8) |
| 14 | Audit storage capacity | Allocate audit record storage capacity (IEC 62443-3-3/SR 2.9) |
| 15 | Response to audit processing failures | Prevent loss of essential services on audit failure (IEC 62443-3-3/SR 2.10) |
| 16 | Timestamps | Timestamp audit records (IEC 62443-3-3/SR 2.11) |
| 17 | Communication integrity | Protect integrity of transmitted information (IEC 62443-3-3/SR 3.1) |
| 18 | Malicious code protection | Prevent, detect and mitigate malicious code (IEC 62443-3-3/SR 3.2) |
| 19 | Security functionality verification | Support verification of security functions (IEC 62443-3-3/SR 3.3) |
| 20 | Deterministic output | Set outputs to predetermined state if normal operation cannot be maintained (IEC 62443-3-3/SR 3.6) |
| 21 | Information confidentiality | Protect confidentiality of information at rest or in transit (IEC 62443-3-3/SR 4.1) |
| 22 | Use of cryptography | Use commonly accepted cryptographic algorithms (IEC 62443-3-3/SR 4.3) |
| 23 | Audit log accessibility | Provide read-only access to audit logs (IEC 62443-3-3/SR 6.1) |
| 24 | Denial of service protection | Maintain essential functions during DoS events (IEC 62443-3-3/SR 7.1) |
| 25 | Resource management | Limit resource use by security functions (IEC 62443-3-3/SR 7.2) |
| 26 | System backup | Support backups without affecting normal operations (IEC 62443-3-3/SR 7.3) |
| 27 | System recovery and reconstitution | Recover to known secure state after disruption (IEC 62443-3-3/SR 7.4) |
| 28 | Alternative power source | Switch power sources without affecting security state (IEC 62443-3-3/SR 7.5) |
| 29 | Network and security configuration settings | Configure according to recommended settings (IEC 62443-3-3/SR 7.6) |
| 30 | Least Functionality | Limit software, services, ports, protocols to strict needs (IEC 62443-3-3/SR 7.7) |

---

### 4.2 Additional security capabilities

For CBSs with network communication to untrusted networks:

**Table 2**

| Item No | Objective | Requirements |
| :--- | :--- | :--- |
| 31 | Multifactor authentication for human users | Required when accessing from untrusted network (IEC 62443-3-3/SR 1.1, RE 2) |
| 32 | Software process and device identification and authentication | Identify and authenticate software processes and devices (IEC 62443-3-3/SR 1.2) |
| 33 | Unsuccessful login attempts | Enforce limit of consecutive invalid login attempts (IEC 62443-3-3/SR 1.11) |
| 34 | System use notification | Display notification message before authenticating (IEC 62443-3-3/SR 1.12) |
| 35 | Access via Untrusted Networks | Monitor and control access from untrusted networks (IEC 62443-3-3/SR 1.13) |
| 36 | Explicit access request approval | Deny access unless explicitly approved on board (IEC 62443-3-3/SR 1.13, RE1) |
| 37 | Remote session termination | Terminate remote sessions automatically or manually (IEC 62443-3-3/SR 2.6) |
| 38 | Cryptographic integrity protection | Employ cryptographic mechanisms for untrusted networks (IEC 62443-3-3/SR 3.1, RE1) |
| 39 | Input validation | Validate syntax, length and content of input from untrusted networks (IEC 62443-3-3/SR 3.5) |
| 40 | Session integrity | Protect session integrity, reject invalid session IDs (IEC 62443-3-3/SR 3.8) |
| 41 | Invalidation of session IDs after session termination | Invalidate session IDs upon logout (IEC 62443-3-3/SR 3.8, RE1) |

---

## 5. Secure Development Lifecycle Requirements

A Secure Development Lifecycle (SDLC) broadly addressing security aspects in following stages shall be followed:

- Requirement analysis phase
- Design phase
- Implementation phase
- Verification phase
- Release phase
- Maintenance Phase
- End of life phase

5.1 (IEC 62443-4-1/SM-8) Procedural and technical controls for private keys used for code signing.

5.2 (IEC 62443-4-1/SUM-2) Documentation about product security updates made available to users.

5.3 (IEC 62443-4-1/SUM-3) Documentation about dependent component or operating system security updates.

5.4 (IEC 62443-4-1/SUM-4) Security updates made available with verification of authenticity.

5.5 (IEC 62443-4-1/SG-1) Product documentation describing security defence in depth strategy.

5.6 (IEC 62443-4-1/SG-2) Documentation of defence in depth measures expected from external environment.

5.7 (IEC 62443-4-1/SG-3) Guidelines for hardening the product during installation and maintenance.

---

## 6. Demonstration of compliance

### 6.1 Introduction

Suppliers shall in cooperation with the System integrator determine if UR E27 is mandatory for the CBS.

![Figure 1: Flowchart to determine if UR E27 is mandatory for CBS](e27_mandatory_flowchart)

![Figure 2: Classification process flowchart for UR E27 compliance](e27_classification_process)

### 6.2 Plan approval

Plan approval is assessment of documents of a CBS intended for a specific vessel.

### 6.3 Survey and factory acceptance test

Survey and FAT is a vessel-specific verification activity required for CBSs without valid Type approval certificate.

#### 6.3.1 General survey items
#### 6.3.2 Test of security capabilities
#### 6.3.3 Correct configuration of security capabilities
#### 6.3.4 Secure development lifecycle

---

## Appendix I

**Requirements:**
I. IACS UR E10: Test Specification for Type Approval
II. IACS UR E22: Computer based systems
III. IACS UR E26: Cyber Resilience of Ships

**Credits:**
I. IACS Rec 166 (Corr.1 2020): Recommendation on Cyber Resilience
II. IEC 62443-3-3 (2013): Industrial communication networks – Network and system security
III. IEC 62443-4-1 (2018): Security for industrial automation and control systems

---

## Appendix II

| Document | Requirements | Class |
| :--- | :--- | :--- |
| CBS asset inventory (E27 sec.3.1.1) | To be incorporated in Vessel asset inventory (E26 sec.4.1.1) | Approve |
| Topology diagrams (E27 sec.3.1.2) | Enabling System integrator to design security zones and conduits (E26 sec.4.2.1) | Approve |
| Description of security capabilities (E27 sec.3.1.3) | Required security capabilities (E27 sec.4.1) | Approve |
| Test procedure for security capabilities (E27 sec.3.1.4) | Required security capabilities (E27 sec.4.1) | Approve |
| Security configuration guidelines (E27 sec.3.1.5) | Network and security configuration settings (E27 sec.4.1 item 29) | Info |
| Secure development lifecycle (E27 sec.3.1.6) | SDLC requirements (E27 sec.5) | Approve |
| Plans for maintenance and verification (E27 sec.3.1.7) | Security functionality verification (E27 sec.4.1 item 19) | Info |
| Information supporting incident response and recovery plans (E27 sec.3.1.8) | Multiple items from E27 sec.4.1 | Info |
| Management of change plan (E27 sec.3.1.9) | Management of change process (E22) | Info |
| Test reports (E27 sec.3.1.10) | Configuration and hardening (E27 sec.3.1.5 and sec.5.7) | Info |

Note 1: Required for CBS without type approved security capabilities
Note 2: Required for CBS with type approved security capabilities

**End of Document**

================================================================================
# FILE: UR_E/UR-E7-Rev.5-Feb-2021CLN.md
================================================================================

# E7 Cables

**E7**
(1975)
(Rev.1 1990)
(Rev.2 June 2000)
(Rev.3 May 2006)
(Rev.4 Apr 2016)
(Rev.5 Feb 2021)

1. Cables are to be of a type approved by the Classification Society.

2. Cables manufactured in accordance with the relevant recommendations of IEC 60092-350:2020, 60092-352:2005, 60092-353:2016, 60092-354:2020, 60092-360:2014, 60092-370:2019 and 60092-376:2017 will be accepted by the Classification Society provided that they are tested to its satisfaction.

3. Cables manufactured and tested to standards other than those specified in 2 will be accepted provided they are in accordance with an acceptable and relevant international or national standard and are of an equivalent or higher safety level than those listed in paragraph 2. However, cables such as flexible cable, fibre-optic cable, etc. used for special purposes may be accepted provided they are manufactured and tested in accordance with the relevant standards accepted by the Classification Society.

***

**Note:**

1. Rev.4 of this UR is to be uniformly implemented by IACS Societies from 1 July 2017.

2. Rev.5 of this UR is to be uniformly implemented by IACS Societies for cables:
    i) when an application for certification of cables is dated on or after 1 July 2022; or
    ii) which are installed in new ships contracted for construction on or after 1 July 2022.

3. The "contracted for construction" date means the date on which the contract to build the vessel is signed between the prospective owner and shipbuilder. For further details regarding the date of "contract for construction", refer to IACS Procedural Requirement (PR) No. 29.

4. The "date of application for certification of cables" is the date of whatever document the Classification Society requires/accepts as an application or request for certification of cables.

**End of Document**

================================================================================
# FILE: UR_E/ur-e1.md
================================================================================

# E1–E3

---

### **E1** (1975) Governing characteristics of generator prime movers

**see revised M 3.2**

---

### **E2** Deleted (December 1996)

---

### **E3** Deleted (December 1996)

---

IACS Req. 1996

================================================================================
# FILE: UR_E/ur-e12rev2.md
================================================================================

# E12 Electrical Equipment allowed in paint stores and in the enclosed spaces leading to paint stores

**E12**
(1994)
(Corr.1 1997)
(Rev.1 May 2001)
(Rev.2 Dec 2020)

## 1. General

Electrical equipment is to be installed in paint stores and in ventilation ducts serving such spaces only when it is essential for operational services.

Certified safe type equipment of the following type is acceptable;

a. intrinsically safe Exi
b. flameproof Exd
c. pressurised Exp
d. increased safety Exe
e. special protection Exs

Cables (through-runs or terminating cables) of armoured type or installed in metallic conduits are to be used.

## 2. Minimum Requirements

The minimum requirements for the certified safe type equipment are as follows:

- explosion group II B
- temperature class T3

**Footnote:**
The paint stores and inlet and exhaust ventilation ducts under Clause 1 are classified as Zone-1 and areas on open deck under Clause 4 as Zone 2, as defined in IEC 60092-502:1999.

A watertight door may be considered as being gastight.

---

**Note:**

1. Rev.2 of this Unified Requirement is to be uniformly implemented by IACS Societies on ships contracted for construction on and after 1 January 2022.
2. The "contracted for construction" date means the date on which the contract to build the vessel is signed between the prospective owner and the shipbuilder. For further details regarding the date of "contract for construction", refer to IACS Procedural Requirement (PR) No. 29.

---

## 3. Special requirements

3.1 Switches, protective devices, motor control gear of electrical equipment installed in a paint store are to interrupt all poles or phases and preferably are to be located in non-hazardous space.

3.2 In the areas on open deck within 1m of inlet and exhaust ventilation openings or within 3 m of exhaust mechanical ventilation outlets, the following electrical equipment may be installed:

- electrical equipment with the type of protection as permitted in paint stores;
- equipment of protection class Exn;
- appliances which do not generate arcs in service and whose surface does not reach unacceptably high temperature;
- appliances with simplified pressurised enclosures or vapour-proof enclosures (minimum class of protection IP55) whose surface does not reach unacceptably high temperature;
- or
- cables as specified in clause 1.

3.3 The enclosed spaces giving access to the paint store may be considered as nonhazardous, provided that:

- the door to the paint store is a gastight door with self-closing devices without holding back arrangements,
- the paint store is provided with an acceptable, independent, natural ventilation system ventilated from a safe area, and
- warning notices are fitted adjacent to the paint store entrance stating that the store contains flammable liquids.

End of Document

================================================================================
# FILE: UR_E/ur-e13rev3corr1.md
================================================================================

# E13 Test requirements for Rotating Machines

**E13**
(1996)
(Rev.1 May 2001)
(Corr.1 May 2004)
(Rev.2 Aug 2015)
(Corr.1 June 2018)
(Rev.3 Dec 2020)
(Corr.1 May 2022)

## 1. General

All machines are to be tested by the manufacturer.

Manufacturer's test records are to be provided for machines for essential services, for other machines they are to be available upon request.

All tests are to be carried out according to IEC 60092-301:1980/AMD2:1995.

All machines of 100kW and over, intended for essential services, are to be surveyed by the Society during test and, if appropriate, during manufacturing.

**Note:** An alternative survey scheme may be agreed by the Society with the manufacturer whereby attendance of the Surveyor will not be required as required above.

***

**Note:**

1. Rev.2 of this UR is to be uniformly implemented by IACS Societies for rotating machines:
   i) when an application for certification of a rotating machine is dated on or after 1 January 2017; or
   ii) which are installed in new ships for which the date of contract for construction is on or after 1 January 2017.

2. Rev.3 of this UR is to be uniformly implemented by IACS Societies for rotating machines:
   i) when an application for certification of a rotating machine is dated on or after 1 January 2022; or
   ii) which are installed in new ships for which the date of contract for construction is on or after 1 January 2022.

3. The "contracted for construction" date means the date on which the contract to build the vessel is signed between the prospective owner and the shipbuilder. For further details regarding the date of "contract for construction", refer to IACS Procedural Requirement (PR) No. 29.

## 2. Shaft Material

Shaft material for electric propulsion motors and for main engine driven generators where the shaft is part of the propulsion shafting is to be certified by the Society.

Shaft material for other machines is to be in accordance with recognised international or national standard.

## 3. Tests

Type tests are to be carried out on a prototype machine or on the first of a batch of machines, and routine tests carried out on subsequent machines in accordance with Table 1.

**Note:** Test requirements may differ for shaft generators, special purpose machines and machines of novel construction.

### Table 1

| No. | Tests | A.C. Generators Type test | A.C. Generators Routine test | Motors Type test | Motors Routine test |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 1. | Examination of the technical documentation and visual inspection | X | X | X | X |
| 2. | Insulation resistance measurement | X | X | X | X |
| 3. | Winding resistance measurement | X | X | X | X |
| 4. | Verification of the voltage regulation system | X | X^3 | | |
| 5. | Rated load test and temperature rise measurements | X | | X | |
| 6. | Overload/overcurrent test | X | X^4 | X | X^4 |
| 7. | Verification of steady short circuit conditions^5 | X | | | |
| 8. | Overspeed test | X | X | X^6 | X^6 |
| 9. | Dielectric strength test | X | X | X | X |
| 10. | No-load test | X | X | X | X |
| 11. | Verification of degree of protection | X | | X | |
| 12. | Verification of bearings | X | X | X | X |

^1 Type tests on prototype machine or tests on at least the first batch of machines.
^2 The report of machines routine tested is to contain the manufacturer's serial number of the machine which has been type tested and the test result.
^3 Only functional test of voltage regulator system.
^4 Only applicable for machine of essential services rated above 100kW.
^5 Verification of steady short circuit condition applies to synchronous generators only.
^6 Not applicable for squirrel cage motors.

## 4. Description of the test

### 4.1 Examination of the technical documentation, as appropriate and visual inspection

#### 4.1.1 Examination of the technical documentation
Technical documentation of machines rated at 100kW and over is to be available for examination by the Surveyor.

#### 4.1.2 Visual inspection
A visual examination is to be made of the machine to ensure, as far as is practicable, that it complies with technical documentation.

### 4.2 Insulation resistance measurement

Immediately after the high voltage tests the insulation resistances are to be measured using a direct current insulation tester between:

a) all current carrying parts connected together and earth,
b) all current carrying parts of different polarity or phase, where both ends of each polarity or phase are individually accessible.

#### Table 2

| Related Voltage Un (V) | Minimum Test Voltage (V) | Test Minimum Insulation Resistance (MΩ) |
| :--- | :---: | :---: |
| Un ≤ 250 | 2 x Un | 1 |
| 250 < Un ≤ 1000 | 500 | 1 |
| 1000 < Un ≤ 7200 | 1000 | (Un / 1000) + 1 |
| 7200 < Un ≤ 15000 | 5000 | (Un / 1000) + 1 |

### 4.3 Winding resistance measurement

The resistances of the machine windings are to be measured and recorded using an appropriate bridge method or voltage and current method.

### 4.4 Verification of the voltage regulation system

The alternating current generator, together with its voltage regulation system shall, at all loads from no-load running to full load, be able to keep rated voltage at the rated power factor under steady conditions within ± 2.5%. These limits may be increased to ± 3.5% for emergency sets.

When the generator is driven at rated speed, giving its rated voltage, and is subjected to a sudden change of symmetrical load within the limits of specified current and power factor, the voltage is not to fall below 85% nor exceed 120% of the rated voltage.

The voltage of the generator is then to be restored to within plus or minus 3% of the rated voltage for the main generator sets in not more than 1.5 s. For emergency sets, these values may be increased to plus or minus 4% in not more than 5 s, respectively.

In the absence of precise information concerning the maximum values of the sudden loads, the following conditions may be assumed: 60% of the rated current with a power factor of between 0.4 lagging and zero to be suddenly switched on with the generator running at no load, and then switched off after steady - state conditions have been reached.

### 4.5 Rated load test and temperature rise measurements

The temperature rises are to be measured at the rated output, voltage, frequency and the duty for which the machine is rated and marked in accordance with the testing methods specified in IEC 60034-1:2017, or by means of a combination of other tests.

The limits of temperature rise are those specified in the relevant table of IEC 60034-1:2017 adjusted as necessary for the ambient reference temperatures specified in UR M40.

### 4.6 Overload/overcurrent tests

Overload test is to be carried out as a type test for generators as a proof of overload capability of generators and excitation system, for motors as a proof of momentary excess torque as required in IEC 60034-1:2017. The overload test can be replaced at routine test by the overcurrent test. The over current test shall be the proof of current capability of windings, wires, connections etc. of each machine. The overcurrent test can be done at reduced speed (motors) or at short circuit (generators).

### 4.7 Verification of steady short-circuit conditions

It is to be verified that under steady-state short-circuit conditions, the generator with its voltage regulating system is capable of maintaining, without sustaining any damage, a current of at least three times the rated current for a duration of at least 2 s or, where precise data is available, for a duration of any time delay which will be fitted in the tripping device for discrimination purposes.

The generator manufacturer shall provide documentation showing the transient behaviour of the short circuit current upon a sudden short-circuit occurring when excited, and running at nominal speed. The decrement curve need not be based on physical testing. The manufacturer's simulation model for the generator and the voltage regulator may be used where this has been validated through the previous type test on the same model.

### 4.8 Overspeed test

Machines are to withstand the overspeed test as specified in to IEC 60034-1:2017. This test is not applicable for squirrel cage motors.

### 4.9 Dielectric strength test

Machines are to withstand a dielectric test as specified in IEC 60034-1:2017.

For high voltage machine an impulse test is to be carried out on the coils according to UR E11.

### 4.10 No load test

Machines are to be operated at no load and rated speed whilst being supplied at rated voltage and frequency as a motor or if a generator it is to be driven by a suitable means and excited to give rated terminal voltage.

During the running test, the vibration of the machine and operation of the bearing lubrication system, if appropriate, are to be checked.

### 4.11 Verification of degree of protection

As specified in IEC 60034-5:2000+AMD1:2006.

### 4.12 Verification of bearings

Upon completion of the above tests, machines which have sleeve bearings are to be opened upon request for examination by the Classification Society Surveyor, to establish that the shaft is correctly seated in the bearing shells.

**End of Document**

================================================================================
# FILE: UR_E/ur-e15rev4.md
================================================================================

# E15 Electrical Services Required to be Operable Under Fire Conditions and Fire Resistant Cables

**E15**
(Nov 1999)
(Rev.1 May 2004)
(Rev.2 Feb 2006)
(Rev.3 Dec 2014)
(Rev.4 Dec 2020)

1. Electrical services required to be operable under fire conditions are as follows:

    - Control and power systems to power-operated fire doors and status indication for all fire doors
    - Control and power systems to power-operated watertight doors and their status indication
    - Emergency fire pump
    - Emergency lighting
    - Fire and general alarms
    - Fire detection systems
    - Fire-extinguishing systems and fire-extinguishing media release alarms
    - Low location lighting
    - Public address systems
    - Remote emergency stop/shutdown arrangements for systems which may support the propagation of fire and/or explosion

2. Where cables for services specified in 1 including their power supplies pass through high fire risk areas, and in addition for passenger ships, main vertical fire zones, other than those which they serve, they are to be so arranged that a fire in any of these areas or zones does not affect the operation of the service in any other area or zone. This may be achieved by either of the following measures:

    a) Cables being of a fire resistant type complying with IEC 60331-1:2018 for cables of greater than 20 mm overall diameter, otherwise IEC 60331-21:1999+AMD1:2009 or IEC 60331-2:2018 for cables with an overall diameter not exceeding 20 mm, are installed and run continuous to keep the fire integrity within the high fire risk area, see Figure 1.

    b) At least two-loops/radial distributions run as widely apart as is practicable and so arranged that in the event of damage by fire at least one of the loops/radial distributions remains operational.

    c) Systems that are self monitoring, fail safe or duplicated with cable runs as widely separated as is practicable may be exempted.

3. The electrical cables to the emergency fire pump are not to pass through the machinery spaces containing the main fire pumps and their source(s) of power and prime mover(s). They are to be of a fire resistant type, in accordance with 2 (a), where they pass through other high fire risk areas.

### Notes:

1. Rev.3 of this UR is to be uniformly implemented by IACS Societies from 1 January 2016.
2. Rev.4 of this Unified Requirement is to be uniformly implemented by IACS Societies on ships contracted for construction on and after 1 January 2022.
3. The "contracted for construction" date means the date on which the contract to build the vessel is signed between the prospective owner and the shipbuilder. For further details regarding the date of "contract for construction", refer to IACS Procedural Requirement (PR) No. 29.

a) For the purpose of E15 application, the definition for "high fire risk areas" is the following:

   (i) Machinery spaces as defined by Regulation 3.30 of SOLAS Chapter II-2, as amended by IMO resolutions up to MSC.421(98), except spaces having little or no fire risk as defined by paragraphs (10) of Regulation 9.2.2.3.2.2 of SOLAS Chapter II-2.

   (ii) Spaces containing fuel treatment equipment and other highly flammable substances

   (iii) Galley and Pantries containing cooking appliances

   (iv) Laundry containing drying equipment

   (v) Spaces as defined by paragraphs (8), (12), and (14) of Regulation 9.2.2.3.2.2 of SOLAS Chapter II-2 for ships carrying more than 36 passengers

b) Fire resistant type cables should be easily distinguishable.

c) For special cables, requirements in the following standards may be used:
   - IEC 60331-23:1999: Procedures and requirements – Electric data cables
   - IEC 60331-25:1999: Procedures and requirements – Optical fibre cables

***

![Figure 1: Schematic diagram illustrating the routing of fire resistant and flame retardant cables through high fire risk and other areas. The diagram shows an Emergency Generator (EG) connected to an Emergency Switchboard (ESB). From the ESB, cables run through an "Other area" and a "High fire risk area" to reach electrical consumers. Solid lines represent Fire resistant cables, dashed lines represent Flame retardant cables.](e15_cable_routing_diagram)

**End of Document**

================================================================================
# FILE: UR_E/ur-e16.md
================================================================================

# E16 Cable trays/protective casings made of plastics materials

(June 2002)

### 1. General requirement

Cable trays/protective casings made of plastics materials are to be type tested.

> **Note:** "Plastics" means both thermoplastic and thermosetting plastic materials with or without reinforcement, such as PVC and fibre reinforced plastics - FRP.
> "Protective casing" means a closed cover in the form of a pipe or other closed ducts of non-circular shape.

### 2. Installation Requirements

**2.1.** Cable trays/protective casings made of plastics materials are to be supplemented by metallic fixing and straps such that in the event of a fire they, and the cables affixed, are prevented from falling and causing an injury to personnel and/or an obstruction to any escape route.

> **Note:** When plastics cable trays/protective casings are used on open deck, they are additionally to be protected against UV light.

**2.2.** The load on the cable trays/protective casings is to be within the Safe Working Load (SWL). The support spacing is not to be greater than the Manufacturer's recommendation nor in excess of spacing at the SWL test. In general the spacing is not to exceed 2 meters.

> **Note:** The selection and spacing of cable tray/protective casing supports are to take into account:
> - cable trays/protective casings' dimensions;
> - mechanical and physical properties of their material;
> - mass of cable trays/protective casings;
> - loads due weight of cables, external forces, thrust forces and vibrations;
> - maximum accelerations to which the system may be subjected;
> - combination of loads.

**2.3.** The sum of the cables' total cross-sectional area, based on the cables' external diameter, is not to exceed 40% of the protective casing's internal cross-sectional area. This does not apply to a single cable in a protective casing.

***

**Note:**
1) Cable trays/protective casings made of plastic materials are to be type tested in accordance with the Type Approval Procedure applied by the Society. For guidance on testing, refer to REC 73.

End of Document

================================================================================
# FILE: UR_E/ur-e19rev1.md
================================================================================

# E19 Ambient Temperatures for Electrical Equipment installed in environmentally controlled spaces

**(July 2003)**
**(Rev.1 Sept. 2005)**

1. Where electrical equipment is installed within environmentally controlled spaces the ambient temperature for which the equipment is to be suitable may be reduced from 45°C and maintained at a value not less than 35°C provided:
    * the equipment is not for use for emergency services.
    * temperature control is achieved by at least two cooling units so arranged that in the event of loss of one cooling unit, for any reason, the remaining unit(s) is capable of satisfactorily maintaining the design temperature.
    * the equipment is able to be initially set to work safely within a 45°C ambient temperature until such a time that the lesser ambient temperature may be achieved; the cooling equipment is to be rated for a 45°C ambient temperature.
    * audible and visual alarms are provided, at a continually manned control station, to indicate any malfunction of the cooling units.

2. In accepting a lesser ambient temperature than 45°C, it is to be ensured that electrical cables for their entire length are adequately rated for the maximum ambient temperature to which they are exposed along their length.

3. The equipment used for cooling and maintaining the lesser ambient temperature is to be classified as a secondary essential service, in accordance with UI SC 134 and to be subject to survey in accordance with the requirements of the relevant Society.

**End of Document**

================================================================================
# FILE: UR_E/ur-e20rev1.md
================================================================================

# E20 Installation of electrical and electronic equipment in engine rooms protected by fixed water-based local application fire-fighting systems (FWBLAFFS)

(May 2004)
(Rev.1 June 2009)

**Definitions:**

**Protected space:**
- Is a machinery space where a FWBLAFFS is installed.

**Protected areas:**
- Areas within a protected space which is required to be protected by FWBLAFFS.

**Adjacent areas:**
- Areas, other than protected areas, exposed to direct spray.
- Areas, other than those defined above, where water may extend.

See also Fig. 1

Electrical and electronic equipment enclosures located within areas protected by FWBLAFFS and those within adjacent areas exposed to direct spray are to have a degree of protection not less than IP44, except where evidence of suitability is submitted to and approved by the Society.

The electrical and electronic equipment within adjacent areas not exposed to direct spray may have a lower degree of protection provided evidence of suitability for use in these areas is submitted taking into account the design and equipment layout, e.g. position of inlet ventilation openings, cooling airflow for the equipment is to be assured.

***

**Note**

1. Additional precautions may be required to be taken in respect of:
    a. tracking as the result of water entering the equipment
    b. potential damage as the result of residual salts from sea water systems
    c. high voltage installations
    d. personnel protection against electric shock

***

# E20 (cont)

**Fig. 1**

![Figure 1: Schematic diagram showing the classification of areas around machinery. A central unit labeled 'D/Eng' is surrounded by a 'Protected Area'. This is enclosed by a dotted line indicating the 'Adjacent Area of direct spray'. A further outer boundary defines the 'Adjacent Area where water may extend'. A small component labeled 'G' is shown adjacent to the 'D/Eng' unit within the spray zones.](e20_area_classification_diagram)

**End of Document**

================================================================================
# FILE: UR_E/ur-e23del-1.md
================================================================================

# E23 Selection of low voltage circuit breakers on the basis of their short circuit capacity and co-ordination in service

**(Feb 2007)**

Deleted Mar 2011

***

**End of Document**

================================================================================
# FILE: UR_E/ur-e24rev1.md
================================================================================

# E24 Harmonic Distortion for Ship Electrical Distribution System including Harmonic Filters

**(June 2016)**
**(Rev.1 Dec 2018)**

## 1. Scope

The requirements of this UR apply to ships where harmonic filters are installed on main busbars of electrical distribution system, other than those installed for single application frequency drives such as pump motors.

## 2. General

The total harmonic distortion (THD) of electrical distribution systems is not to exceed 8%.

This limit may be exceeded where all installed equipment and systems have been designed for a higher specified limit and this relaxation on limits is documented (harmonic distortion calculation report) and made available on board as a reference for the surveyor at each periodical survey.

## 3. Monitoring of harmonic distortion levels for a ship including harmonic filters

3.1 The ships are to be fitted with facilities to continuously monitor the levels of harmonic distortion experienced on the main busbar as well as alerting the crew should the level of harmonic distortion exceed the acceptable limits. Where the engine room is provided with automation systems, this reading should be logged electronically, otherwise it is to be recorded in the engine log book for future inspection by the surveyor.

3.2 As a minimum, harmonic distortion levels of main busbar on board such existing ships are to be measured annually under seagoing conditions as close to the periodical machinery survey as possible so as to give a clear representation of the condition of the entire plant to the surveyor. Harmonic distortion readings are to be carried out when the greatest amount of distortion is indicated by the measuring equipment. An entry showing which equipment was running and/or filters in service is to be recorded in the log so this can be replicated for the next periodical survey. Harmonic distortion levels are also to be measured following any modification to the ship's electrical distribution system or associated consumers by suitably trained ship's personnel or from a qualified outside source.

Records of all the above measurements are to be made available to the surveyor at each periodical survey.

## 4. Mitigation of the effects of harmonic filter failure on a ship's operation

Where the electrical distribution system on board a ship includes harmonic filters the system integrator of the distribution system is to show, by calculation, the effect of a failure of a harmonic filter on the level of harmonic distortion experienced.

The system integrator of the distribution system is to provide the ship owner with guidance documenting permitted modes of operation of the electrical distribution system while maintaining harmonic distortion levels within acceptable limits during normal operation as well as following the failure of any combination of harmonic filters.

The calculation results and validity of the guidance provided are to be verified by the surveyor during sea trials.

## 5. Protection arrangements for harmonic filters

Arrangements are to be provided to alert the crew in the event of activation of the protection of a harmonic filter circuit.

A harmonic filter should be arranged as a three phase unit with individual protection of each phase. The activation of the protection arrangement in a single phase shall result in automatic disconnection of the complete filter. Additionally, there shall be installed a current unbalance detection system independent of the overcurrent protection alerting the crew in case of current unbalance.

Consideration is to be given to additional protection for the individual capacitor element as e.g. relief valve or overpressure disconnector in order to protect against damage from rupturing. This consideration should take into account the type of capacitors used.

***

**Note:**

1. This UR, except for Section 3.2, is to be uniformly implemented by IACS Societies:
   i. for ships contracted for construction on or after 1 July 2017 or
   ii. for ships where an application for a periodical or occasional machinery survey after the retrofit of harmonic filters is dated on or after 1 July 2017.

2. Section 3.2 is to be uniformly implemented by IACS Societies for ships contracted for construction before 1 July 2017, at any scheduled Machinery periodical survey having a due date on or after 1 July 2017.

3. The "contracted for construction" date means the date on which the contract to build the vessel is signed between the prospective owner and the shipbuilder. For further details regarding the date of "contract for construction", refer to IACS Procedural Requirement (PR) No.29.

4. UR E24 Rev.1, except for Section 3.2, is to be uniformly implemented by IACS Societies:
   i. for ships contracted for construction on or after 1 January 2020 or
   ii. for ships where an application for a periodical or occasional machinery survey after the retrofit of harmonic filters is dated on or after 1 January 2020.

**End of Document**

================================================================================
# FILE: UR_E/ur-e2del.md
================================================================================

# E2 Deleted (December 1996)

IACS Req. 1996

================================================================================
# FILE: UR_E/ur-e3del.md
================================================================================

# E3 Deleted (December 1996)

IACS Req. 1996

================================================================================
# FILE: UR_E/ur-e4del.md
================================================================================

# E4 Earthing of non-current-carrying parts

(1978)

Deleted in June 2000.

***

IACS Req. 2000

================================================================================
# FILE: UR_E/ur-e5rev1.md
================================================================================

# E5 Voltage and frequency variations

**E5**
(1979)
(Rev.1 Sept. 2005)

1. All electrical appliances supplied from the main or emergency systems are to be so designed and manufactured that they are capable of operating satisfactorily under the normally occurring variations in voltage and frequency.

2. Unless otherwise stated in the national or international standards, all equipment should operate satisfactorily with the variations from its rated value shown in the Tables 1 to 3 on the following conditions.

    (a) For alternative current components, voltage and frequency variations shown in the Table 1 are to be assumed.

    (b) For direct current components supplied by d.c. generators or converted by rectifiers, voltage variations shown in the Table 2 are to be assumed.

    (c) For direct current components supplied by electrical batteries, voltage variations shown in the Table 3 are to be assumed.

3. Any special system, e.g. electronic circuits, whose function cannot operate satisfactorily within the limits shown in the Table should not be supplied directly from the system but by alternative means, e.g. through stabilized supply.

### Table 1: Voltage and frequency variations for a.c. distribution systems

| Quantity in Operation | Variations: Permanent | Variations: Transient |
| :--- | :--- | :--- |
| Frequency | ±5% | ±10% (5 sec) |
| Voltage | +6%, -10% | ±20% (1.5 sec) |

### Table 2: Voltage variations for d.c distribution systems

| Parameters | Variations |
| :--- | :--- |
| Voltage tolerance (continuous) | ±10% |
| Voltage cyclic variation deviation | 5% |
| Voltage ripple (a.c. r.m.s. over steady d.c. voltage) | 10% |

### Table 3: Voltage variations for battery systems

| Systems | Variations |
| :--- | :--- |
| Components connected to the battery during charging (see Note) | +30%, -25% |
| Components not connected to the battery during charging | +20%, -25% |

**Note:** Different voltage variations as determined by the charging/discharging characteristics, including ripple voltage from the charging device, may be considered.

**End of Document**

================================================================================
# FILE: UR_E/ur-e6del.md
================================================================================

# E6 Deleted

**End of Document**

================================================================================
# FILE: UR_E/ur-e9rev1.md
================================================================================

# E9 Earthing and bonding of cargo tanks/ process plant/piping systems for the control of static electricity

(1988)
(Rev.1 Oct 2012)

**E9.1** The hazard of an incentive discharge due to the build-up of static electricity resulting from the flow of liquids/gases/vapours can be avoided if the resistance between the cargo tanks/process plant/piping systems and the hull of the ship is not greater than $10^6$ ohm.

**E9.2** This value of resistance will be readily achieved without the use of bonding straps where cargo tanks/process plant/piping systems are directly or via their supports, either welded or bolted to the hull of the ship.

**E9.3** Bonding straps are required for cargo tanks/process plant/piping systems which are not permanently connected to the hull of the ship, e.g.

a) independent cargo tanks;

b) cargo tanks/piping systems which are electrically separated from the hull of the ship;

c) pipe connections arranged for the removal of spool pieces.

d) wafer-style valves with non-conductive (e.g PTFE) gaskets or seals.

**E9.4** Where bonding straps are required, they should be:

a) clearly visible so that any shortcomings can be clearly detected;

b) designed and sited so that they are protected against mechanical damage and that they are not affected by high resistivity contamination e.g. corrosive products or paint;

c) easy to install and replace.

**E9.5** Checks should be made on the resistance to the hull of the ship during construction of the ship and at subsequent major surveys, supplemented by visual inspection during annual surveys.

---

**Note:**

1. Revision 1 of this UR is to be implemented for ships contracted for construction on or after 1 January 2014.

2. The "contracted for construction" date means the date on which the contract to build the vessel is signed between the prospective owner and the shipbuilder. For further details regarding the date of "contract for construction", refer to IACS Procedural Requirement (PR) No. 29.

**End of Document**

================================================================================
# FILE: UR_F/UR-F15-Rev.7-Sep-2023CLN.md
================================================================================

# F15 Reinforced thickness of ballast and cargo oil piping

**F15**
(1982)
(Rev.4 1989)
(Rev.5 1996)
(Rev.6 Feb 2021)
(Corr.1 Feb 2022)
(Rev.7 Sep 2023)

**F15.1** Ballast piping passing through cargo tanks and cargo oil pipes passing through segregated ballast tanks, as permitted by Regulation 19.3.6 of MARPOL Annex I, are to comply with the following requirements.

**F15.1.1** The pipes are to be of heavy gauge steel of minimum wall thickness according to the table hereunder with welded or heavy flanged joints the number of which is to be kept to a minimum.

Expansion bends only are permitted in these lines within cargo tanks for serving the ballast tanks and within the ballast tanks for serving the cargo tanks.

| Nominal diameter (mm) | Minimum wall thickness (mm) |
| :--- | :--- |
| 50 | 6.3 |
| 100 | 8.6 |
| 125 | 9.5 |
| 150 | 11.0 |
| 200 and above | 12.5 |

**Note:** Heavy flanges joints means welded flange joints rated at least PN10 or one pressure rating higher than required design pressure, whichever is greater. Expansion bends means expansion loops such as an omega bend ('Ω') in piping system to counteract excessive stresses or displacement caused by thermal expansion or hull deformation which could be fabricated from straight lengths of pipe.

**F15.2** The thicknesses shown in the above table refer to carbon steel.

**F15.3** Connection between cargo piping and ballast piping referred to above is not permitted except for emergency discharge as specified in the Unified Interpretation to Regulation 1.18 of MARPOL Annex I.

Nevertheless, provision may be made for emergency discharge of the segregated ballast by means of a connection to a cargo pump through a portable spool piece. In this case non-return valves should be fitted on the segregated ballast connections to prevent the passage of oil to the ballast tanks. The portable spool piece should be mounted in a conspicuous position in the pump room and a permanent notice restricting its use should be prominently displayed adjacent to it.

Shut-off valves shall be provided to shut off the cargo and ballast lines before the spool piece is removed.

**F15.4** The ballast pump is to be located in the cargo pump room, or a similar space within the cargo area not containing any source of ignition.

***

**Note:**

1. Rev.7 of this Unified Requirement is to be uniformly implemented by IACS Societies on ships contracted for construction on or after 1 January 2025.
2. The "contracted for construction" date means the date on which the contract to build the vessel is signed between the prospective owner and the shipbuilder. For further details regarding the date of "contract for construction", refer to IACS Procedural Requirement (PR) No. 29.

**End of Document**

================================================================================
# FILE: UR_F/UR-F42-Del-Nov-2023.md
================================================================================

# F42 Fire testing of flexible pipes

**F42**
(1995)
(Del Nov 2023)

Deleted in November 2023, as these interpretations are considered by IACS UR P2.

***

**End of Document**

================================================================================
# FILE: UR_F/UR-F43Del.md
================================================================================

# F43 Installation requirements for analysing units for continuous monitoring of flammable vapours

**F43**
(1997)
(Rev.1 July 1999)
(Rev.2 June 2002)
(Del Jan 2025)

Deleted in January 2025.

All the requirements have been included into FSS CODE CHAPTER 16 FIXED HYDROCARBON GAS DETECTION SYSTEMS, as amended by resolution MSC.292(87), and relating SOLAS provisions.

***

**End of Document**

================================================================================
# FILE: UR_F/UR-F44-Rev.3-Corr.1-Mar-2025-CLN.md
================================================================================

# F44 Fore peak ballast tanks and space arrangements on oil & chemical tankers

**F44**
(June 2000)
(Rev.1 Aug 2008)
(Rev.2 Oct 2010)
(Rev.3 Sep 2024)
(Corr.1 Mar 2025)

## Definitions

The following definitions apply in this UR.

**Hazardous area** means an area in which an explosive gas atmosphere is present, or may be expected to be present, in quantities such as to require special precautions for the construction, installation and use of equipment.

**Non-hazardous area** means an area that is not a hazardous area.

**Cargo area of tankers** are defined in:

- for tankers to which regulation 1.6.1 of SOLAS Chapter II-2 as amended by IMO resolutions up to MSC.421(98) applies, regulation 3.6 of SOLAS Chapter II-2:
- for chemical tankers, Paragraph 1.3.6 of the IBC Code as amended by IMO resolutions up to MSC.460(101):

---

## 1 Fore peak ballast tanks and space arrangements on tankers for oil and/or chemicals

1.1 The fore peak tank can be ballasted with the system serving other ballast tanks within the cargo area, provided:

a) The vent pipe openings are located on open deck at a distance from sources of ignition as required by IEC 60092-502:1999 Electrical installations in ships – Tankers – Special features; This requirement does not apply to sounding arrangements.

b) Access to the fore peak tank is direct from open deck. Alternatively, indirect access from the open deck to the forepeak tank may be from a pump-room, deep cofferdam, pipe tunnel, cargo hold, double hull space, bosun's store or similar compartment not intended for the carriage of oil or hazardous cargoes, conforming to the requirements of SOLAS II-1/3-6.3.1. Electrical equipment in such indirect access shall be of the certified safe type suitable for use in the hazardous area it opens into or shall be isolated before entry.

c) Continuous ventilation is maintained while accessing the forepeak tank

d) The sounding arrangement to the fore peak tank is direct from open deck.

e) The forepeak tank is gas freed direct from open deck, or through a dedicated trunk to open deck. Before the manhole and the entrance of the dedicated trunk are opened, the trunk and the forepeak tank shall be confirmed as made gas free. Means are to be provided to free the space of gas without opening manholes or the entrance to a dedicated trunk. Manholes on the open deck and away from sources of ignition at the top of the dedicated trunk which are used to gas-free the space are allowed to be opened.

f) The fore peak ballast tank is considered as a hazardous zone 2 if segregated from cargo area with a cofferdam, or as a hazardous zone 1 if located adjacent to a cargo tank. For tankers where a bow thruster space is provided, the piping passing through the non-hazardous bow thruster room shall be fully welded and it is required to have the collision bulkhead valve located within the forepeak tank.

g) Means are to be provided on the open deck by a suitable portable instrument, to allow detection of toxic and flammable vapours within the FPT (based on the cargoes carried in current voyage, and since last de-ballasting of FPT was carried out), in order to ensure the FPT is fully gas freed. In the case that sounding arrangements can be used as the means for the portable instrument additional means for the purpose is not required.

---

**Note:**

1. Rev.2 of this UR is to be uniformly implemented by IACS Societies on ships contracted for construction on or after 1 January 2012.
2. Rev.3 of this Unified Requirement is to be uniformly implemented by IACS Societies on ships contracted for construction on or after 1 January 2026.
3. The "contracted for construction" date means the date on which the contract to build the vessel is signed between the prospective owner and the shipbuilder. For further details regarding the date of "contract for construction", refer to IACS Procedural Requirement (PR) No. 29.

---

## 2 Additional requirements for forward spaces not being defined as a ballast tank

2.1 Any spaces, voids and/or indirect accesses from the open deck or intermediate space being located adjacent to cargo tanks, and/or are defined as hazardous area zone 1 or 2, shall follow the same requirements to openings and access as reflected for fore peak ballast tanks in section 1.

2.2 In case any spaces or voids are defined as non-hazardous spaces and have access to other non-hazardous spaces (such as bosun store), the following applies:

a) For any non-hazardous space with access to a hazardous space (example: fore peak ballast tank), the non-hazardous space must have access directly to open deck and shall be gas freed directly from open deck, and not through the non-hazardous space (example: bosun store).

b) Access from bosun store to a non-hazardous space (example: void) having access to hazardous space (example: fore peak ballast tank) may be accepted through a gas tight bolted manhole, with signboard stating that the non-hazardous space cannot be entered until the space is confirmed gas free.

![Figure: Sample 1 - Tanker bow arrangement with Cargo Tank, Cofferdam, Void Space, and FPT (Zone 2)](f44_sample1)

![Figure: Sample 2 - Tanker bow arrangement with Cargo Tank, Cofferdam, and FPT (Zone 2)](f44_sample2)

![Figure: Sample 3 - Oil tanker arrangement with Cargo Tank, Cofferdam, Void Space, and FPT](f44_sample3)

![Figure: Sample 4 - Oil tanker arrangement with Cargo Tank and FPT with Void Space](f44_sample4)

![Figure: Sample 5 - Tanker bow arrangement similar to Sample 1](f44_sample5)

![Figure: Sample 6 - Tanker bow arrangement similar to Sample 2](f44_sample6)

**<Operational requirements>**
1. Continuous ventilation is maintained while accessing the FPT as per 1.1(c).
2. To detect toxic and flammable vapours within the FPT in order to ensure the FPT is fully gas freed as per 1.1(g).
3. Where toxic-vapour-detection equipment is not available for some cargoes which require such detection, the FPT may be ventilated by dilution method at a minimum rate of 6 air changes/hr for a minimum of 24 hrs.

**End of Document**

================================================================================
# FILE: UR_F/ur-f10del-1.md
================================================================================

# F10 Deleted

IACS Req. 2013

================================================================================
# FILE: UR_F/ur-f11del-1.md
================================================================================

# F11 Deleted

IACS Req. 2013

================================================================================
# FILE: UR_F/ur-f12del-1.md
================================================================================

# F12 Deleted

IACS Req. 2013

================================================================================
# FILE: UR_F/ur-f13rev1-1.md
================================================================================

# F13 Gland seals in pump room bulkheads

**F13**
(1972)
(Rev. 1 1977)

Where drive shafts pass through pump room bulkhead or deck plating, gastight glands are to be fitted. The glands are to be efficiently lubricated from outside the pumproom. The seal parts of the glands are to be of material that will not initiate sparks. The glands are to be constructed and fitted in accordance with the relative rules for fittings attached to watertight bulkheads, and if a bellows piece is incorporated in the design, it should be pressure tested before fitting.

***

IACS Req. 1989

================================================================================
# FILE: UR_F/ur-f14del-1.md
================================================================================

# F14 Deleted

- the requirements are now addressed by IMO Res. A.446 (XI)

***

IACS Req. 1989/Rev 1996

================================================================================
# FILE: UR_F/ur-f16rev1-1.md
================================================================================

# F16 Bow and stern loading and unloading arrangements on oil tankers

(1972)
(Rev.1 June 2000)

Where a cargo hose connection is arranged outside the cargo tank area, the pipe leading to such connections is to be provided with means of segregation such as a spectacle flange, removable spool piece or equivalent* located within the cargo area. The space within 3 m of the manifold is to be considered as a dangerous area with regard to electrical or incendive equipment.

---
* See MSC/Circ. 474.

***

IACS Req. 1972/Rev.1 2000

================================================================================
# FILE: UR_F/ur-f17del-1.md
================================================================================

# F17 Deleted

- this is of a general nature concerning operational matters and should not be categorised as UR.

IACS Req. 1986/Rev 1996

================================================================================
# FILE: UR_F/ur-f18del-1.md
================================================================================

# F18 Deleted (1997)

IACS Req. 1997

================================================================================
# FILE: UR_F/ur-f19del-1.md
================================================================================

# F19 Deleted

IACS Req. 1997

================================================================================
# FILE: UR_F/ur-f1rev1.md
================================================================================

# F1 Cathodic protection on oil tankers

(1971)
(Rev.1 June 2002)

F1.1 Impressed current systems are not permitted in oil cargo tanks.

F1.2 Magnesium or magnesium alloy anodes are not permitted in oil cargo tanks and tanks adjacent to cargo tanks.

F1.3 Aluminium anodes are only permitted in cargo tanks and tanks adjacent to cargo tanks in locations where the potential energy does not exceed 28 kg m (200 ft lb). The height of the anode is to be measured from the bottom of the tank to the centre of the anode, and its weight is to be taken as the weight of the anode as fitted, including the fitting devices and inserts. However, where aluminium anodes are located on horizontal surfaces such as bulkhead girders and stringers not less than 1 m wide and fitted with an upstanding flange or face flat projecting not less than 75 mm above the horizontal surface, the height of the anode may be measured from this surface. Aluminium anodes are not to be located under tank hatches or Butterworth openings (in order to avoid any metal parts falling on the fitted anodes), unless protected by adjacent structure.

F1.4 There is no restriction on the positioning of zinc anodes.

F1.5 The anodes should have steel cores and these should be sufficiently rigid to avoid resonance in the anode support and be designed so that they retain the anode even when it is wasted.

F1.6 The steel inserts are to be attached to the structure by means of a continuous weld of adequate section. Alternatively they may be attached to separate supports by bolting, provided a minimum of two bolts with locknuts are used. However, approved mechanical means of clamping will be accepted.

F1.7 The supports at each end of an anode should not be attached to separate items which are likely to move independently.

F1.8 When anode inserts or supports are welded to the structure, they should be arranged so that the welds are clear of stress raisers.

**End of Document**

================================================================================
# FILE: UR_F/ur-f20rev7-1.md
================================================================================

# F20 Inert Gas Systems

**F20**
(1974)
(Rev.1 1983)
(Rev.2 1987)
(Rev.3 May 1998)
(Corr. Sept 2001)
(Rev.4 May 2004)
(Rev.5 Nov 2005)
(Rev.6 May 2012)
(Rev.7 May 2015)

## F20.1 General Requirements

F20.1.1 All types of inert gas systems are to comply with the following:

.1 Plans in diagrammatic form are to be submitted for appraisal and should include the following:
- details and arrangement of the inert gas generating plant including all control and monitoring devices;
- arrangement of the piping system for distribution of the inert gas.

.2 An automatic control capable of producing suitable inert gas under all service conditions is to be fitted.

.3 Subsequent surveys are to be carried out at the intervals required by the Classification Society Rules.

## F20.2 Requirements for All Systems on Tankers, including Chemical Tankers, to which SOLAS regulation II-2/4.5.5.1 applies

F20.2.1 An inert gas system complying with the applicable requirements of Ch. 15 of the FSS Code, as amended by MSC.367 (93), is to be fitted on tankers to which SOLAS regulation II-2/4.5.5.1 applies. In applying the applicable requirements of Ch. 15 of the FSS Code, any use of the word "Administration" therein is to be considered as meaning the relevant Classification Society. The inert gas system is to be operated in accordance with SOLAS regulation II-2/16.3.3, as amended by MSC.365(93). In applying SOLAS regulation II-2/16.3.3.2, paragraph 2.2.1.2.4 of Ch. 15 of the FSS Code is to be complied with.

---

**NOTES:**

1. Rev.6 is to be applied by IACS Societies on ships contracted for construction on or after 1 July 2013.
2. Rev.7 is to be applied by IACS Societies on ships constructed on or after 1 January 2016.
3. The "contracted for construction" date means the date on which the contract to build the vessel is signed between the prospective owner and the shipbuilder. For further details regarding the date of "contract for construction", refer to IACS Procedural Requirement (PR) No. 29.

---

## F20.3 Additional Requirements for Nitrogen Generator Systems on Tankers, including Chemical Tankers, to which SOLAS regulation II-2/4.5.5.1 applies

F20.3.1 The following requirements apply where a nitrogen generator system is fitted on board as required by SOLAS regulation II-2/4.5.5.1. For the purpose, the inert gas is to be produced by separating air into its component gases by passing compressed air through a bundle of hollow fibres, semi-permeable membranes or adsorber materials.

F20.3.2 In addition to the applicable requirements of Ch. 15 of the FSS Code, as amended by MSC.367(93), the nitrogen generator system is to comply with SOLAS regulations II-2/4.5.3.4.2, 4.5.6.3 and 11.6.3.4.

F20.3.3 A nitrogen generator is to consist of a feed air treatment system and any number of membrane or adsorber modules in parallel necessary to meet paragraph 2.2.1.2.4 of Ch.15 of the FSS Code, as amended by MSC.367(93).

F20.3.4 The nitrogen generator is to be capable of delivering high purity nitrogen in accordance with paragraph 2.2.1.2.5 of Ch.15 of the FSS Code, as amended by MSC.367(93). In addition to paragraph 2.2.2.4 of Ch.15 of the FSS Code, as amended by MSC.367(93), the system is to be fitted with automatic means to discharge "off-spec" gas to the atmosphere during start-up and abnormal operation.

F20.3.5 The system is to be provided with one or more compressors to generate enough positive pressure to be capable of delivering the total volume of gas required by 2.2.1.2 of the FSS Code, as amended by MSC.367(93). Where two compressors are provided, the total required capacity of the system is preferably to be divided equally between the two compressors, and in no case is one compressor to have a capacity less than 1/3 of the total capacity required.

F20.3.6 The feed air treatment system fitted to remove free water, particles and traces of oil from the compressed air as required by 2.4.1.2 of Ch.15 of the FSS Code, as amended by MSC.367(93), is also to preserve the specification temperature.

F20.3.7 The oxygen-enriched air from the nitrogen generator and the nitrogen-product enriched gas from the protective devices of the nitrogen receiver are to be discharged to a safe location on the open deck.

F20.3.8 In order to permit maintenance, means of isolation are to be fitted between the generator and the receiver.

---

**Safe location definitions:**

1. oxygen-enriched air from the nitrogen generator - safe locations on the open deck are:
   - outside of hazardous area;
   - not within 3m of areas traversed by personnel; and
   - not within 6m of air intakes for machinery (engines and boilers) and all ventilation inlets.

2. nitrogen-product enriched gas from the protective devices of the nitrogen receiver - safe locations on the open deck are:
   - not within 3m of areas traversed by personnel; and
   - not within 6m of air intakes for machinery (engines and boilers) and all ventilation inlets/outlets.

---

## F20.4 Nitrogen /Inert Gas Systems Fitted for Purposes other than Inerting Required by SOLAS Reg. II-2/4.5.5.1 and 4.5.5.2

F20.4.1 This section applies to systems fitted on oil tankers, gas tankers or chemical tankers to which SOLAS regulations II-2/4.5.5.1 and 4.5.5.2 do not apply.

F20.4.2 Paragraphs 2.2.2.2, 2.2.2.4, 2.2.4.2, 2.2.4.3, 2.2.4.5.1.1, 2.2.4.5.1.2, 2.2.4.5.4, 2.4.1.1, 2.4.1.2, 2.4.1.3, 2.4.1.4, 2.4.2.1 and 2.4.2.2 of Ch.15 of the FSS Code, as amended by MSC.367(93), as applicable apply to the systems.

F20.4.3 The requirements of section F20.3 apply except paragraphs F20.3.1, F20.3.2, F20.3.3 and F20.3.5.

F20.4.4 Materials used in inert gas systems are to be suitable for their intended purpose in accordance with the Rules of the Classification Society.

F20.4.5 All the equipment is to be installed on board and tested under working conditions to the satisfaction of the Surveyor.

F20.4.6 The two non-return devices as required by paragraph 2.2.3.1.1 of Ch.15 of the FSS Code, as amended by MSC.367(93) are to be fitted in the inert gas main. The non-return devices are to comply with 2.2.3.1.2 and 2.2.3.1.3 of Ch.15 of the FSS Code, as amended by MSC.367(93); however, where the connections to the cargo tanks, to the hold spaces or to cargo piping are not permanent, the non-return devices required by paragraph 2.2.3.1.1 of Ch.15 of the FSS Code, as amended by MSC.367(93) may be substituted by two non-return valves.

**End of Document**

================================================================================
# FILE: UR_F/ur-f21-1.md
================================================================================

# F21 Pump room ventilation

(1974)

With the following arrangement of exhaust trunking there should be 20 air changes per hour on the total volume of the pump room:

(i) In the pump room bilges just above the transverse floor plates on bottom longitudinals, so that air can flow over the top from adjacent spaces.

(ii) An emergency intake located about 2 m above the pump room lower grating. This emergency intake would be used when the lower intakes are sealed off due to flooding in the bilges. The emergency intake should have a damper fitted which is capable of being opened or closed from the exposed main deck and lower grating level.

(iii) The foregoing exhaust system is in association with open grating floor plates to allow the free flow of air.

(iv) Arrangements involving a specific ratio of areas of upper emergency and lower main ventilator openings, which can be shown to result in at least the required 20 air changes per hour through the lower inlets, can be adopted without the use of dampers. When the lower access inlets are closed then at least 15 air changes per hour should be obtained through the upper inlets.

---

# F22 Direct loading pipes to oil tanker cargo tanks

(1974)

In order to avoid the generation of static electricity when cargo is loaded direct into tanks, the loading pipes are to be led as low as practicable in the tank.

IACS Req. 1987

================================================================================
# FILE: UR_F/ur-f22-1.md
================================================================================

# F21 Pump room ventilation

(1974)

With the following arrangement of exhaust trunking there should be 20 air changes per hour on the total volume of the pump room:

(i) In the pump room bilges just above the transverse floor plates on bottom longitudinals, so that air can flow over the top from adjacent spaces.
(ii) An emergency intake located about 2 m above the pump room lower grating. This emergency intake would be used when the lower intakes are sealed off due to flooding in the bilges. The emergency intake should have a damper fitted which is capable of being opened or closed from the exposed main deck and lower grating level.
(iii) The foregoing exhaust system is in association with open grating floor plates to allow the free flow of air.
(iv) Arrangements involving a specific ratio of areas of upper emergency and lower main ventilator openings, which can be shown to result in at least the required 20 air changes per hour through the lower inlets, can be adopted without the use of dampers. When the lower access inlets are closed then at least 15 air changes per hour should be obtained through the upper inlets.

***

# F22 Direct loading pipes to oil tanker cargo tanks

(1974)

In order to avoid the generation of static electricity when cargo is loaded direct into tanks, the loading pipes are to be led as low as practicable in the tank.

***

IACS Req. 1987

================================================================================
# FILE: UR_F/ur-f23del-1.md
================================================================================

# F23 Deleted

- the requirements are overtaken by the development of MARPOL Convention.

---
IACS Req. 1986/Rev 1996

================================================================================
# FILE: UR_F/ur-f24rev2-1.md
================================================================================

# F24 Temperature of Steam and Heating Media within the Cargo Area

(1971)
(Rev. 1 1975)
(Rev. 2 May 1998)

On oil tankers, the steam and heating media temperature within the cargo area is not to exceed 220°C.

On gas carriers and chemical tankers, the maximum temperature is to be adjusted to take into account the temperature class of the cargoes.

**End of Document**

================================================================================
# FILE: UR_F/ur-f25del-1.md
================================================================================

# F25 Deleted

IACS Req. 1971, Rev. 2 1998

================================================================================
# FILE: UR_F/ur-f26rev3-1.md
================================================================================

# F26 Safety aspects of double bottoms and duct keels under cargo oil tanks

**F26**
(1977)
(Rev 1 1996)
(Rev.2 June 2000)
(Rev.3 May 2004)

Pipe ducts in the double bottom shall comply with the following requirements:

(i) They should not communicate with the engine room.
(ii) Provision shall be made for at least two exits to the open deck arranged at a maximum distance from each other. One of these exits fitted with a watertight closure may lead to the cargo pumproom.
(iii) In the duct, provision shall be made for adequate mechanical ventilation.

**Note:** For ships to which the convention applies, refer to SOLAS 1974 (as amended), Reg II-2/4.5.2.4

***

Revision Note: Rev.3 only updates references

**End of Document**

================================================================================
# FILE: UR_F/ur-f27-1.md
================================================================================

# F27 Cargo openings in the bottoms of topside tanks of ships carrying alternatively oil and grain

(1978)

*Ships carrying alternatively oil having a flash point not exceeding 60°C (closed cup test) or other cargoes.*

When ships are designed to transport alternatively oil or dry cargoes, openings which may be used for cargo operations are not permitted in bulkheads and decks separating oil cargo spaces from other spaces not designed and equipped for the carriage of oil cargoes unless alternative approved means are provided to ensure equivalent integrity.

**End of Document**

================================================================================
# FILE: UR_F/ur-f28del-1.md
================================================================================

# F28 Deleted

IACS Req. 1986

================================================================================
# FILE: UR_F/ur-f29rev6-1.md
================================================================================

# F29 Non-sparking fans

**F29**
(1973)
(Rev. 1 1978)
(Rev. 2 1979)
(Rev. 3 1980)
(Rev. 4 1983)
(Rev. 5 1994)
(Rev. 6 June 2005)

### F29.1 Introduction

A fan is considered as non-sparking if in either normal or abnormal conditions it is unlikely to produce sparks.

### F29.2 Design criteria

**F29.2.1** The air gap between the impeller and the casing shall be not less than 0,1 of the shaft diameter in way of the impeller bearing but not less than 2 mm. It need not be more than 13 mm.

**F29.2.2** Protection screens of not more than 13 mm square mesh are to be fitted in the inlet and outlet ventilation openings on the open deck to prevent the entrance of objects into the fan housing.

### F29.3 Materials

**F29.3.1** The impeller and the housing in way of the impeller are to be made of alloys which are recognised as being spark proof by appropriate test.

**F29.3.2** Electrostatic charges both in the rotating body and the casing are to be prevented by the use of antistatic materials. Furthermore, the installation on board of the ventilation units is to be such as to ensure the safe bonding to the hull of the units themselves.

**F29.3.3** Tests may not be required for fans having the following combinations:

(i) impellers and/or housings of nonmetallic material, due regard being paid to the elimination of static electricity,
(ii) impellers and housings of non-ferrous materials,
(iii) Impellers of aluminium alloys or magnesium alloys and a ferrous (including austenitic stainless steel) housing on which a ring of suitable thickness of non-ferrous materials is fitted in way of the impeller,
(iv) any combination of ferrous (including austenitic stainless steel) impellers and housings with not less than 13 mm tip design clearance.

**F29.3.4** The following impellers and housings are considered as sparking and are not permitted:

(i) impellers of an aluminium alloy or magnesium alloy and a ferrous housing, regardless of tip clearance,
(ii) housing made of an aluminium alloy or a magnesium alloy and a ferrous impeller, regardless of tip clearance,
(iii) any combination of ferrous impeller and housing with less than 13 mm design tip clearance.

**F29.3.5** Type tests on the finished product are to be carried out in accordance with the requirements of the Classification Society or an equivalent national or international standard.

**End of Document**

================================================================================
# FILE: UR_F/ur-f2rev2.md
================================================================================

# F2 Aluminium coatings on board oil tankers and chemical tankers

(1971)
(Rev.1 May 1998)
(Corr.1 Mar 1999)
(Rev.2 Nov 2012)

The use of aluminium coatings containing greater than 10 percent aluminium by weight in the dry film is prohibited in cargo tanks, cargo tank deck area, pump rooms, cofferdams or any other area where cargo vapour may accumulate.

Aluminised pipes may be permitted in ballast tanks, in inerted cargo tanks and, provided the pipes are protected from accidental impact, in hazardous areas on open deck.

***

**Note:**

1. Revision 2 of this UR is to be applied by IACS Societies from 1 January 2014 to new tankers and new applications of coating and piping on existing tankers.

**End of Document**

================================================================================
# FILE: UR_F/ur-f3-1.md
================================================================================

# F3 Tank cleaning openings

(1971)

Ullage plugs, sighting ports and tank cleaning openings are not to be arranged in enclosed spaces.

**End of Document**

================================================================================
# FILE: UR_F/ur-f30del-1.md
================================================================================

# F30 Emergency fire pumps in cargo ships

(1974)
(Rev. 1 1976)
(Rev. 2 1978)
(Rev. 3 1980)
(Rev. 4 1984)
(Rev. 5 1995)
(Rev. 6 1997)
(Rev. 7 Feb 2002)

Deleted in February 2002.

**End of Document**

================================================================================
# FILE: UR_F/ur-f31del-1.md
================================================================================

# F31 Fire prevention for unattended machinery spaces

(1976)

The whole UR F31 was deleted as the requirements are now covered by F35.

**End of Document**

================================================================================
# FILE: UR_F/ur-f32-1.md
================================================================================

# F32 Fire detecting system for unattended machinery spaces

**F32 (1976)**

**F32.1** An automatic fire detection system is to be fitted in the machinery spaces.

**F32.2** The system is to be designed with self-monitoring properties. Power or system failures are to initiate an audible alarm distinguishable from the fire alarm.

**F32.3** The fire detection indicating panel is to be located on the navigating bridge, fire control station, or other accessible place where a fire in the machinery space will not render it inoperative.

**F32.4** The fire detection indicating panel is to indicate the place of the detected fire in accordance with the arranged fire zones by means of a visual signal. Audible signals clearly distinguishable in character from any other audible signals shall be audible throughout the navigating bridge and the accommodation area of the personnel responsible for the operation of the machinery space.

**F32.5** Fire detectors are to be of types, and so located, that they will rapidly detect the onset of fire in conditions normally present in the machinery space. Consideration is to be given to avoiding false alarms. The type and location of detectors are to be approved by the Classification Society and a combination of detector types is recommended in order to enable the system to react to more than one type of fire symptom.

**F32.6** Fire detector zones are to be arranged in a manner that will enable the operating staff to locate the seat of the fire. The arrangement and the number of loops and the location of detector heads is to be approved in each case. Air currents created by the machinery are not to render the detection system ineffective.

**F32.7** When fire detectors are provided with the means to adjust their sensitivity, necessary arrangements are to be ensured to fix and identify the set point.

**F32.8** When it is intended that a particular loop or detector is to be temporarily switched off, this state is to be clearly indicated. Reactivation of the loop or detector is to be performed automatically after a preset time.

**F32.9** The fire detection indicating panel is to be provided with facilities for functional testing.

**F32.10** The fire detecting system shall be fed automatically from the emergency source of power by a separate feeder if the main source of power fails.

**F32.11** Facilities are to be provided in the fire detecting system to release manually the fire alarm from the following places:

- Passageways having entrances to engine and boiler rooms,
- navigating bridge,
- control station in engine room.

**F32.12** The testing of the fire detecting system on board is to be carried out to the satisfaction of the individual Classification Society.

#### NOTE
Requirements on indication of the operation of each individual detecting head are left to the discretion of each Classification Society.

**End of Document**

================================================================================
# FILE: UR_F/ur-f33-1.md
================================================================================

# F33 Prohibition of carriage in fore peak tanks of oil or other liquid substances which are flammable

**(1981)**

In ships of 400 tons gross tonnage and above, compartments forward of the collision bulkhead shall not be arranged for the carriage of oil or other liquid substances which are flammable.

**End of Document**

================================================================================
# FILE: UR_F/ur-f34del-1.md
================================================================================

# F34 Low-pressure carbon dioxide smothering systems

**F34**
(1982)
(Rev.1 1989)

Deleted with effect from 1 July 2010 following entry into force of IMO Res. MSC.206(81).

**End of Document**

================================================================================
# FILE: UR_F/ur-f35rev8-1.md
================================================================================

# F35 Fire Protection of Machinery Spaces

(1986)
(Rev. 1 1989)
(Rev. 2 1992)
(Rev. 3 1995)
(Rev. 4 1996)
(Rev. 5 1997)
(Rev. 6 June 1999)
(Rev. 7 July 2003)
(Rev. 8 June 2005)

In the implementation of the SOLAS Chapter II-2, the following requirements are to be met:

### 1. Reg.II-2/4.2.2.4

Air pipes from oil fuel tanks should be led to a safe position on the open deck.

Air pipes from lubricating oil storage tanks may terminate in the machinery space, provided that the open ends are so situated that issuing oil cannot come into contact with electrical equipment or heated surfaces.

Any overflow pipe should have a sectional area of at least 1,25 times that of the filling pipe and should be led to an overflow tank of adequate capacity or to a storage tank having space reserved for overflow purposes.

An alarm device should be provided to give warning when the oil reaches a predetermined level in the tank, or alternatively, a sight glass should be provided in the overflow pipe to indicate when any tank is overflowing. Such sight glasses should be placed on vertical pipes only and in readily visible positions.

### 2. Reg.II-2/4.2.2.3.5.1

Short sounding pipes may be used for tanks other than double bottom tanks without the additional closed level gauge provided an overflow system is fitted.

### 3. Reg.II-2/4.2.2.3

Level switches may be used below the tank top provided they are contained in a steel enclosure or other enclosures not capable of being destroyed by fire.

### 4. Reg.II-2/5.2.2.3

Controls required by this regulation should also be provided from the compartment itself.

### 5. Reg.II-2/4.2.2.5.1

Hose clamps and similar types of attachments for flexible pipes should not be permitted.

### 6. Reg.II-2/4.2.2 and 4.2.5.2

Oil fuel in storage tanks should not to be heated to temperatures within 10°C below the flash point of the fuel oil, except that where oil fuel in service tanks, settling tanks and any other tanks in supply system is heated the following arrangements should be provided:

- the length of the vent pipes from such tanks and/or a cooling device is sufficient for cooling the vapours to below 60°C, or the outlet of the vent pipes is located 3m away from a source of ignition;
- the vent pipes are fitted with flame screens;
- there are no openings from the vapour space of the fuel tanks into machinery spaces (bolted manholes are acceptable);
- enclosed spaces are not located directly over such fuel tanks, except for vented cofferdams;
- electrical equipment is not fitted in the vapour space of the tanks, unless it is certified to be intrinsically safe.

**End of Document**

================================================================================
# FILE: UR_F/ur-f36del-1.md
================================================================================

# F36 Deleted

IACS Req. 1996

================================================================================
# FILE: UR_F/ur-f37del-1.md
================================================================================

# F37 Deleted

UR F37 has been recategorised to be Recom 53.1 and deleted (May, 1998).

IACS Req. 1989, Rev. 1998

================================================================================
# FILE: UR_F/ur-f38del-1.md
================================================================================

# F38 Deleted

F38 has been re-categorised to be Recom. 53.2 and deleted (May 1998).

IACS Req. 1989, Rev. 1998

================================================================================
# FILE: UR_F/ur-f39del-1.md
================================================================================

# F39 Measures to prevent explosions in cargo pump rooms on oil tankers

**F39**
(1993)
(Rev. 1 1994)
(Rev 2 1997)
(Rev. 2/ Corr. 1 1998)
(Rev.3 July 1999)
(Rev.4 May 2001)

F 39 was deleted on 1 July 2002.

**End of Document**

================================================================================
# FILE: UR_F/ur-f40del-1.md
================================================================================

# F40 Deleted 1997

**End of Document**

================================================================================
# FILE: UR_F/ur-f41-1.md
================================================================================

# F41 Sea intakes for fire pump on ships with ICE Class

(1993)

1. On ships with ICE Class at least one of the fire pumps is to be connected to a sea chest which is provided with de-icing arrangements.

**End of Document**

================================================================================
# FILE: UR_F/ur-f45new-1.md
================================================================================

# F45 Installation of BWMS on-board ships

**(June 2021)**

## 1 General

### 1.1 Application

1.1.1 This Unified Requirement details fire safety measures, in addition to that required by SOLAS II-2, related to the installation of Ballast Water Management Systems onboard any ship.

This UR is to be read in conjunction with IACS UR M74 rev.2 - Ballast Water Management Systems.

1.1.2 The requirements of this UR apply for BWMS technologies as listed in Table 1. BWMS with alternative technologies are to be specially considered by the Classification Society.

### 1.2 Definitions

#### 1.2.1 Airlock
An airlock is a space enclosed by gastight steel bulkheads with two gastight doors spaced not more than 2.5 m apart. The doors shall be self-closing without any holding back arrangements. Air locks shall have mechanical ventilation and shall not be used for other purposes.

#### 1.2.2 Ballast Water Management System (BWMS)
Ballast Water Management System means any system defined in paragraph 2.1 of UR M74, Rev.2.

---

**Note:**
1. This UR is to be uniformly implemented by IACS Societies for BWMS:
   i) For existing ships, where the application for approval for the installation plans of BWMS is dated on or after 1 July 2022; or
   ii) For new ships contracted for construction on or after 1 July 2022.
2. The "contracted for construction" date means the date on which the contract to build the vessel is signed between the prospective owner and the shipbuilder.

---

### Table 1 - Categorization of BWMS technologies

| Cat. | Technology | Examples of dangerous gas |
| :--- | :--- | :--- |
| 1 | In-line UV or UV + AOT or UV + TiO2 or UV + Plasma | Case by case |
| 2 | In-line Flocculation | - |
| 3a | In-line membrane separation and de-oxygenation (injection of N2) | O2 N2 |
| 3b | In-line de-oxygenation (injection of Inert Gas) | CO2 CO |
| 3c | In-tank de-oxygenation with Inert Gas Generator | In-tank technology |
| 4 | In-line full flow electrolysis | H2 Cl2 |
| 5 | In-line side stream electrolysis | H2 Cl2 |
| 6 | In-line (stored) chemical injection | Case by case |
| 7a | In-line side-stream ozone injection (no separation tank) | O2 O3 N2 |
| 7b | In-line side-stream ozone injection (with separation tank) | - |
| 8 | In-tank pasteurization and de-oxygenation with N2 generator | In-tank technology |

#### 1.2.3 Ballast Water Management Room (BWMR)
A Ballast Water Management Room is any space containing equipment belonging to the Ballast Water Management System.

#### 1.2.4 BWMS storing, introducing or generating chemicals
In general, BWMS storing, introducing or generating chemicals refer to:
- In-line flocculation (cat.2)
- Chemical injection (cat.6)
- BWM technologies using neutralizers injection (cat.4, 5, 6 and 7)

### Table 2: Requirements that may be reduced for BWMS depending on the chemicals

| Requirement | Conditions to be met before reducing the requirement |
| :--- | :--- |
| 2.3.4 | The stored chemicals are neither toxic nor flammable |
| 3.1.1 | The BWMS does not use any flammable or toxic chemical substances |
| 3.3.1 | No dangerous gas will be generated by the BWMS |
| 6.1.1 | No toxic chemical is stored and no toxic gas will be generated by the BWMS |
| 7.1.1, 7.1.3, 7.1.6 | No toxic chemical is used or will be generated by the BWMS |

## 2 Fire categorization

### 2.1 General
BWMR shall be classified as follows for the purpose of applying the requirements of SOLAS Chapter II-2:
- BWMR containing oil-fired inert gas generators (cat.3b and 3c) shall be treated as machinery spaces of category A
- Other BWMR shall be considered as other machinery spaces

### 2.2 BWMS located in the cargo area of tankers
Where a BWMS is located in the cargo area of a tanker, the BWMR shall be categorized as a cargo pump-room.

### 2.3 Storage of chemicals

2.3.1 Spaces where the storage of liquid or solid chemicals for BWMS is intended shall be categorized as store-rooms for the purpose of applying SOLAS Chapter II-2.

2.3.2 Where the storage of chemicals is foreseen in the same room as the ballast water management machinery, this room shall be considered both as a store-room and as a machinery space.

2.3.3 When the chemical substances are stored inside integral tanks, the ship's shell plating shall not form any boundary of the tank.

2.3.4 Tanks containing chemicals shall be segregated from accommodation, service spaces, control stations, machinery spaces not related to the BWMS and from drinking water and stores for human consumption by means of a cofferdam, void space, cargo pump-room, empty tank, oil fuel storage tank, BWMR or other similar space.

## 3 BWMR location and boundaries

### 3.1 BWMS using chemical substances
3.1.1 For BWMS storing, introducing or generating chemicals, the BWMR and chemical substance storage rooms are not to be located in the accommodation area. Any ventilation exhaust or other openings from these rooms shall be located not less than 3m from entrances, air inlets and openings to accommodation spaces.

### 3.2 Ozone-based BWMS
3.2.1 Ozone-based BWMS (cat.7a and 7b) shall be located in dedicated compartment, separated from any other space by gastight boundaries. Access to the BWMR from any other enclosed space shall be through airlock only, except if the only access is from the open deck.

3.2.2 A sign shall be affixed on the door providing personnel with a warning that ozone may be present.

### 3.3 General
3.3.1 BWMR containing equipment for BWMS of the following types shall be equipped with tested gastight and self-closing doors:
- BWMS storing, introducing or generating chemical substances
- De-oxygenation based on inert gas generator
- Electrolysis
- Ozone injection

## 4 Fire fighting

### 4.1 Fixed fire-extinguishing system
4.1.1 Where fitted, fixed fire extinguishing systems shall comply with the relevant provisions of the Fire Safety Systems Code.

4.1.2 BWMR containing equipment related to ozone-based BWMS shall be provided with a fixed fire extinguishing system suitable for category A machinery spaces.

4.1.3 Where a fixed fire-extinguishing system is provided in the BWMR, it should be compatible with the BWMS and the chemical products.

4.1.4 For all kinds of BWMS, in case a foam fire extinguishing system is installed in the BWMR, its efficiency shall not be impaired by chemicals used by the BWMS.

4.1.5 Where a fixed fire-extinguishing system is installed, automatic shutdown of the BWMS upon release shall be arranged.

4.1.6 Where BWMS includes air or O2 storage in a room covered by fixed gas fire-extinguishing system, storage shall be taken into account for gas capacity calculation.

### 4.2 Portable fire-fighting equipment
4.2.1 At least one portable fire extinguisher suitable for electrical fires shall be provided in BWMR containing UV-type BWMS.

## 5 Fire prevention

### 5.1 Equipment protection
5.1.1 Overcurrent or overvoltage protection is to be installed to protect UV type BWMS.

5.1.2 Electrolysis reactors are to be provided with at least two independent means of monitoring operation.

### 5.2 Fire detection
5.2.1 A fixed fire detection and fire alarm system shall be installed in spaces containing an inert gas generator or an ozone generator.

5.2.2 A section of fire detectors covering a control station, service space or accommodation space is not to include a BWMR containing ozone-based BWMS equipment.

## 6 Ventilation

### 6.1 Ventilation arrangement
6.1.1 The ventilation systems for BWMR containing the following BWMS types shall be independent:
- BWMS storing, introducing or generating chemical substances
- De-oxygenation (cat.3 and cat.8)
- Electrolysis
- Ozone injection

6.1.2 Ventilation exhaust for BWMR with nitrogen generator shall be in the lower part of the room.

6.1.3 Ventilation exhaust for BWMR with electrolysis systems shall efficiently evacuate dangerous gases.

6.1.4 Ventilation ducts serving BWMR for ozone-based BWMS shall be steel with minimum thickness requirements.

6.1.5 Ventilation for BWMR with ozone-based BWMS shall be interlocked with BWMS.

### 6.2 Ventilation rate
6.2.1 An adequate power ventilation system shall be provided in enclosed BWMR.

6.2.2 The ventilation capacity shall be at least 30 air changes per hour where explosive or toxic gases may be generated.

6.2.3 Reduced ventilation rates:
- Flocculation-type BWMS: 6 air changes/hour
- De-oxygenation (cat.3 and cat.8): 6 air changes/hour
- Full flow electrolysis: 6 air changes/hour
- Side-stream electrolysis: 20 air changes/hour
- Ozone injection: 20 air changes/hour
- Chemical injection: 6 air changes/hour

## 7 Personal equipment

7.1.1 Suitable protection equipment shall be available onboard for crew members servicing BWMS storing, introducing or generating chemicals.

7.1.2 Work clothes and protective equipment shall be kept in easily accessible places.

7.1.3 Decontamination showers and an eyewash shall be available near the BWMS and chemical store rooms.

7.1.4 An emergency escape breathing apparatus (EEBD) is to be provided in the BWMR. Not required for cat.1 BWMS.

7.1.5 A personal ozone detector shall be provided for each person servicing ozone-based BWMS.

7.1.6 A two-way portable radiotelephone apparatus dedicated for BWMS service shall be provided. Not required for cat.1 BWMS.

**End of Document**

================================================================================
# FILE: UR_F/ur-f46new-1.md
================================================================================

# F46 Low pressure CO₂ piping system

**F46**
(Aug 2021)

**(FSS Code Ch.5.2.2)**

Where a low-pressure CO₂ system is fitted, the piping system is to be designed in such a way that the CO₂ pressure at the nozzles should not be less than 1 N/mm².

***

**Note:**

1. This Unified Requirement is to be uniformly implemented by IACS Societies on ships constructed on or after 1 July 2022.

**End of Document**

================================================================================
# FILE: UR_F/ur-f4del-1.md
================================================================================

# F4 Deleted

---

# F5 Pump room alarms

**(1971) (Rev. 1 1973)**

Where audible alarms are fitted to warn of the release of fire extinguishing medium into pump rooms, they may be of the pneumatic type or electric type.

### (a) Pneumatically operated alarms
In cases where the periodic testing of such alarms is required, CO₂ operated alarms should not be used owing to the possibility of the generation of static electricity in the CO₂ cloud. Air operated alarms may be used provided the air supply is clean and dry.

### (b) Electrically operated alarms
When electrically operated alarms are used, the arrangements are to be such that the electric actuating mechanism is located outside the pump room except where the alarms are certified intrinsically safe.

It was further agreed that the use of CO₂ operated alarms should be discouraged.

**End of Document**

================================================================================
# FILE: UR_F/ur-f5rev1-1.md
================================================================================

# F5 Pump room alarms

(1971)
(Rev. 1 1973)

Where audible alarms are fitted to warn of the release of fire extinguishing medium into pump rooms, they may be of the pneumatic type or electric type.

**(a) Pneumatically operated alarms**

In cases where the periodic testing of such alarms is required, CO2 operated alarms should not be used owing to the possibility of the generation of static electricity in the CO2 cloud. Air operated alarms may be used provided the air supply is clean and dry.

**(b) Electrically operated alarms**

When electrically operated alarms are used, the arrangements are to be such that the electric actuating mechanism is located outside the pump room except where the alarms are certified intrinsically safe.

It was further agreed that the use of CO2 operated alarms should be discouraged.

**End of Document**

================================================================================
# FILE: UR_F/ur-f6rev1-1.md
================================================================================

# F6 Standardization of flash points

**F6**
(1971)
(Rev 1 1996)

In context of these Unified Requirements, oil tankers shall be considered as vessels capable of carrying oil having a flash point not exceeding 60°C (closed cup test).

**End of Document**

================================================================================
# FILE: UR_F/ur-f7corr1-1.md
================================================================================

# F7 Portable instruments for measuring oxygen and flammable vapour concentrations

**F7**
(1971)
(Rev.1 1989)
(Rev.2 May 1999)
(Rev.3 June 2020)
(Corr.1 Nov 2020)

Every oil tanker is to be provided with at least two portable gas detectors capable of measuring flammable vapour concentrations in air (%LEL) and at least two portable O2 analysers. Alternatively, at least two gas detectors, each capable of measuring both oxygen and flammable vapour concentrations in air (%LEL), are to be provided.

In addition, for tankers fitted with inert gas systems, at least two portable gas detectors are to be capable of measuring concentrations of flammable vapours in inerted atmosphere (% gas by volume).

***

**Note:**

1. Rev.3 of this UR is to be uniformly implemented by IACS Societies on ships contracted for construction on or after 1 July 2021.

**End of Document**

================================================================================
# FILE: UR_F/ur-f8rev1-1.md
================================================================================

# F8 Pressurisation of cargo tanks

**F8**
(1971)
(Rev.1 1989)

PV valves to oil tanks should not be set at pressures in excess of 0,21 bar unless the tank scantlings have been specially considered.

**End of Document**

================================================================================
# FILE: UR_F/ur-f9del-1.md
================================================================================

# F9 Lighting and sighting ports in pump room/engine room bulkheads

**(1971)**

Deleted Dec 2013.

(According to Members' experience, the use of lighting and sighting ports is now obsolete.)

**End of Document**

================================================================================
# FILE: UR_G/UR-G1-Rev.3-Corr.3-Sep-2023-CLN.md
================================================================================

# G1 Vessels with cargo containment system for liquefied gas

**G1**
(1974)
(Rev.1 1979)
(Rev.2 1997)
(Corr.1 Sept 2003)
(Rev.3 June 2016)
(Corr.1 May 2018)
(Corr.2 Oct 2021)
(Corr.3 Sep 2023)

---

### G1.1 General

**G1.1.1** The present text gives the general principles which are applied by Classification Societies for approval and survey of the relevant items of vessels with cargo containment system for liquefied gas for classification purposes.

**G1.1.2** Where appropriate, this Requirement refers to the basic tank types which are defined under G1.2.

**G1.1.3** This UR does not apply to vessels which must comply with the requirements of IMO Resolution MSC.370(93) Amendments to the International Code for the Construction and Equipment of Ships Carrying Liquefied Gases in Bulk (IGC Code).

---

### G1.2 Definitions

#### G1.2.1 Integral tanks
Integral tanks form a structural part of the ship's hull. The design vapour pressure P₀ is not normally to exceed 0,025 N/mm² (0.25 bar). If hull scantlings are increased accordingly, P₀ may be increased but less than 0,07 N/mm² (0.7 bar).

#### G1.2.2 Membrane tanks
Membrane tanks are non-self-supporting tanks consisting of a thin layer (membrane) supported through insulation by the adjacent hull structure. Design vapour pressure P₀ not normally to exceed 0,025 N/mm² (0.25 bar).

#### G1.2.3 Semi-membrane tanks
Semi-membrane tanks are non-self-supporting tanks in the loaded condition. Design vapour pressure P₀ not normally to exceed 0,025 N/mm² (0.25 bar).

#### G1.2.4 Independent tanks
Independent tanks are self-supporting; they do not form part of the ship hull.

Three categories:
(i) **Independent tanks type A** - designed using classical structural analysis procedures. P₀ < 0,07 N/mm².
(ii) **Independent tanks type B** - designed using model tests, refined analytical tools. P₀ < 0,07 N/mm².
(iii) **Independent tanks type C** (pressure tanks) - design vapour pressure P₀ not less than:

$$P_0 = 0,2 + 0,1AC\rho_0^{3/2} \quad (\text{N/mm}^2)$$

where:
- A = 0,0185(σₘ/ΔσA)²
- σₘ = design primary membrane stress (N/mm²)
- ΔσA = allowable dynamic membrane stress = 55 N/mm² for steels, 25 N/mm² for aluminium alloy (5083-0)
- C = characteristic tank dimension = greatest of h; 0,75b or 0,45l
- ρ₀ = relative density of cargo at design temperature

#### G1.2.5 Design vapour pressure
The maximum gauge pressure at the top of the tank used in design.

#### G1.2.6 Design temperature
The minimum temperature at which cargo may be loaded and/or transported.

---

### G1.3 Design loads

#### G1.3.1 General
Tanks with supports and fixtures are to be designed for combinations of: internal pressure, external pressure, dynamic loads, thermal loads, sloshing loads, ship deflection loads, tank/cargo weight, insulation weight, loads from towers and attachments.

#### G1.3.2 Internal pressure
$$h_{eq} = P_0 + (h_{gd})_{\max}$$

$$h_{gd} = a_\beta \times Z_\beta \frac{\rho}{1,02 \times 10^5} \quad (\text{N/mm}^2)$$

#### G1.3.3 External pressure
Based on difference between minimum internal pressure and maximum external pressure.

#### G1.3.4 Dynamic loads due to ships motions
Long term distribution of ship motions including surge, sway, heave, roll, pitch and yaw corresponding to 10⁸ wave encounters. Probability level of 10⁻⁸ for design against plastic deformation and buckling.

#### G1.3.5 Sloshing loads
When partial filling is contemplated, risk of significant sloshing loads is to be considered.

#### G1.3.6 Thermal loads
Transient thermal loads during cooling down for cargoes below -55°C. Stationary thermal loads where significant thermal stress may arise.

---

### G1.4 Structural analysis

**G1.4.1** Integral tanks - per Classification Society rules.
**G1.4.2** Membrane tanks - effects of all static and dynamic loads for plastic deformation and fatigue. Model testing normally required.
**G1.4.3** Semi-membrane tanks - per membrane or independent tank requirements as appropriate.
**G1.4.4** Independent tanks type A - per Classification Society rules for deep tanks.
**G1.4.5** Independent tanks type B - statistical wave load analysis, FEM, fracture mechanics. Cumulative fatigue: Σ(nᵢ/Nᵢ) + 10³/Nⱼ ≤ Cw (Cw ≤ 0.5).
**G1.4.6** Independent tanks type C - per G2.

---

### G1.5 Allowable stress – corrosion allowance

#### G1.5.1 Allowable stresses
(a) Integral tanks: per hull structure rules.
(c) Independent tanks type A: bending stresses ≤ lower of 0,75σF or 0,38σB.
(d) Independent tanks type B (bodies of revolution): σₘ ≤ f, σL ≤ 1,5f, σb ≤ 1,5F, etc.

Equivalent stress (von Mises):
$$\sigma_c = \sqrt{\sigma_x^2 + \sigma_y^2 - \sigma_x\sigma_y + 3\tau_{xy}^2}$$

#### G1.5.2 Corrosion allowance
No corrosion allowance generally required unless no environmental control or corrosive cargo.

---

### G1.6 Supports

**G1.6.1** Cargo tanks supported to prevent bodily movement while allowing contraction/expansion.
**G1.6.2** Design for static inclination of 30°.
**G1.6.4** Collision force: one-half weight forward, one-quarter weight aft.
**G1.6.7** Anti-flotation chocks for independent tanks.

---

### G1.7 Secondary barrier

| Cargo temp tᵦ at atm. pressure | tᵦ < –55°C | –55°C ≤ tᵦ < –10°C | tᵦ ≥ –10°C |
| :--- | :--- | :--- | :--- |
| Membrane | Complete secondary barrier | Hull may act as secondary barrier | No secondary barrier required |
| Independent Type A | Complete secondary barrier | Hull may act as secondary barrier | No secondary barrier required |
| Independent Type B | Partial secondary barrier | Hull may act as secondary barrier | No secondary barrier required |
| Independent Type C | No secondary barrier required | No secondary barrier required | No secondary barrier required |

---

### G1.8 Insulation

**G1.8.1** Suitable insulation when cargo below –10°C, ambient 5°C air, 0°C sea water.
**G1.8.4** Approved means of heating may be used for transverse hull structural material.

---

### G1.9 Materials

**G1.9.1-G1.9.9** Shell/deck plating per Classification Society rules unless temperature below –5°C due to cargo. Hull material forming secondary barrier per IGC Code Ch.6 Table 6.2 and UR W1. Insulation materials to be tested for compatibility, shrinkage, ageing, thermal conductivity, fire resistance, etc.

---

### G1.10 Construction and testing

**G1.10.1** All welded joints of independent tank shells: butt-weld full-penetration type.
**G1.10.5** Integral tanks: hydrostatic or hydropneumatic test.
**G1.10.7** Independent tanks: hydrostatic or hydropneumatic test. Type B max stress ≤ 90% yield strength.
**G1.10.10** At least one Type B tank to be instrumented.
**G1.10.13** Hull inspection for cold spots after first loaded voyage.

---

### APPENDIX 1 - Guidance formulae for acceleration components

For ships with L > 50 m, probability level 10⁻⁸ in North Atlantic:

**Vertical acceleration:**
$$a_z = \pm a_0 \sqrt{1 + \left( 5,3 - \frac{45}{L} \right)^2 \left( \frac{x}{L} + 0,05 \right)^2 \left( \frac{0,6}{C_B} \right)^{3/2}}$$

**Transverse acceleration:**
$$a_y = \pm a_0 \sqrt{0,6 + 2,5 \left( \frac{x}{L} - 0,05 \right)^2 + K \left( 1 + 0,6 K \frac{z}{B} \right)^2}$$

**Longitudinal acceleration:**
$$a_x = \pm a_0 \sqrt{0,06 + A^2 - 0,25 A}$$

where:
$$a_0 = 0,2 \frac{V}{\sqrt{L}} + \frac{34 - 600/L}{L}$$

**End of Document**

================================================================================
# FILE: UR_G/UR-G3-Rev.8-Oct-2023-CLN.md
================================================================================

# G3 Liquefied gas cargo and process piping

**G3**
(1974)
(Rev.1 1979)
(Rev.2 1997)
(Rev.3 Dec 2008 withdrawn)
(Rev.4 Mar 2011)
(Rev.5 Jan 2013)
(Rev.6 Jan 2016)
(Rev.7 Dec 2019)
(Rev.8 Oct 2023)

---

## G3.1 General

**G3.1.1** The present texts give general principles for approval and survey of the relevant items of liquefied gas tankers for classification purposes.

**G3.1.3** IGC Code means the International Code for the Construction and Equipment of Ships Carrying Liquefied Gases in Bulk (as amended by IMO Resolutions MSC.370(93), MSC.411(97) and MSC.441(99)).

---

## G3.2 Scope

Requirements apply to liquefied gas cargo and process piping including cargo gas piping and exhaust lines of safety valves.

---

## G3.3 Scantlings for internal pressure

### G3.3.2 Design pressure
The greatest of the following conditions is to be used based on cargoes carried, in accordance with IGC Code sections 4.13.2.2 and 5.4.

### G3.3.3 Allowable stress
For pipes, allowable stress K is the lower of values defined in 5.11.3.1 of IGC Code.

### G3.3.4 Minimum wall thickness

$$t = \frac{t_0 + b + c}{1 - \frac{a}{100}}$$

where:
- t₀ = PD/(2Ke + P) (theoretical thickness)
- P = design pressure (MPa)
- D = outside diameter (mm)
- K = allowable stress (N/mm²)
- e = efficiency factor (1 for seamless/approved welded pipes)
- b = allowance for bending = (1/2.5)(D/r)t₀
- c = corrosion allowance (mm)
- a = negative manufacturing tolerance (%)

### G3.3.5 Flanges, valves, fittings
Per recognized standards taking into account design pressure per IGC Code 5.4.

---

## G3.4 Stress analysis

**G3.4.1** Complete stress analysis when design temperature ≤ -110°C, considering weight, internal pressure, thermal contraction and hull deflection.

---

## G3.5 Materials

**G3.5.1** Per IGC Code 5.12.1, 5.12.2 and W1 considering minimum design temperature.

---

## G3.6 Tests of piping components and pumps prior to installation on board

### G3.6.1 Valves

**G3.6.1.1 Prototype Testing:** Each type below -55°C per IGC Code 5.13.1.1.1-5.13.1.1.3. Emergency shutdown valves with materials <925°C melting point require fire test.

**G3.6.1.2 Unit Production Testing:** Hydrostatic test at 1.5× design pressure. Seat/stem leakage at 1.1× design pressure. Cryogenic testing for 10% minimum of valves below -55°C.

### G3.6.2 Bellows
Prototype tests per IGC Code 5.13.1.2.1-5.13.1.2.4.

### G3.6.3 Cargo Pumps and Gas/Reliquefication/Refrigeration Compressors

Equipment to be suitable for marine environment considering UR E10 and UR M46.

**G3.6.3.1 Cargo Pumps:**
(a) Material testing per IGC Code 6.2.2 for boundary components below -55°C.
(b) Prototype testing: hydrostatic 1.5× design pressure, capacity test.
(c) Unit production testing: hydrostatic 1.5× design pressure, capacity test.

**G3.6.3.2 Gas Cargo and Reliquefication/Refrigeration Compressors:**
(a) Material testing per IGC Code 6.2.2 for boundary components below -55°C.
(b) Prototype testing: hydrostatic test, mechanical running test, performance test.
(c) Unit production testing: hydrostatic test at 1.5× design pressure.
(d) Installation: leak test of complete assembly.

---

## G3.7 Piping fabrication and joining details

### G3.7.2 Direct connection
Per IGC Code 5.8.2.1-5.8.2.3.

### G3.7.3 Flange connections
Welding neck, slip-on or socket welding type.

### G3.7.6 Welding, post-weld heat treatments and NDT
(a) Per IGC Code 5.9 and Classification Society requirements.
(b) PWHT for all butt welds of carbon/carbon-manganese/low alloy steels. May be waived for wall thickness <10mm.
(c) 100% radiographic/ultrasonic for piping below -10°C with ID >75mm or wall >10mm. 10% minimum for others.

---

## G3.8 Tests onboard

### G3.8.2 Pressure tests
Per IGC Code 5.13.2.2 (strength), 5.13.2.3 (leak), 5.13.2.4 (double wall gas-fuel).

### G3.8.3 Functional tests
All piping systems tested under normal operating conditions at first loading.

---

## G3.9 Cargo piping insulation system

Per IGC Code 5.12.3.1 and 5.12.3.2.

### Guidance Standards
- ISO 7919-3:2009, ISO 10816-3:2009, ISO 10816-7:2009, ISO 10816-8:2014, ISO 20816-1:2016, ISO 20816-8:2018

**End of Document**

================================================================================
