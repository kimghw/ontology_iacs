
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

