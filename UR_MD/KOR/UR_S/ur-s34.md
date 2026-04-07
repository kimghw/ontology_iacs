# S34 Functional Requirements on Load Cases for Strength Assessment of Container Ships by Finite Element Analysis

**S34**
(May 2015)

## S34.1 Application

This UR applies to container ships and ships dedicated primarily to carry their cargo in containers.

## S34.2 Principles

The requirements in this UR are functional requirements on load cases to be considered on finite element analysis for the structural strength assessment (yielding and buckling).

The procedure for yielding and buckling assessment are to be in accordance with the Rules of the Classification Society. All in-plane stress components (i.e. bi-axial and shear stresses) induced by hull girder loads and local loads as specified in this UR are to be considered.

All aspects and principles not mentioned explicitly in this UR are to be applied according to the procedures of the Classification Society.

## S34.3 Definitions

### S34.3.1 Global Analysis

A Global Analysis is a finite element analysis, using a full ship model, for assessing the structural strength of global hull girder structure, cross deck structures and hatch corner radii.

### S34.3.2 Cargo Hold Analysis

A Cargo Hold Analysis is a finite element analysis for assessing the structural strength of the cargo hold primary structural members (PSM) in the midship region.

### S34.3.3 Primary Structural Members (PSM)

Primary structural members are members of girder or stringer type which provide the overall structural integrity of the hull envelope and cargo hold boundaries, such as:

(i) double bottom structure (bottom plate, inner bottom plate, girders, floors)
(ii) double side structure (shell plating, inner hull, stringers and web frames)
(iii) bulkhead structure
(iv) deck and cross deck structure

---

**Note:**

1. This UR is to be uniformly implemented by IACS Societies for ships contracted for construction on or after 1 July 2016.
2. The "contracted for construction" date means the date on which the contract to build the vessel is signed between the prospective owner and the shipbuilder. For further details regarding the date of "contract for construction", refer to IACS Procedural Requirement (PR) No. 29.

---

## S34.4 Analysis

### S34.4.1 Global Analysis

A Global Analysis is to be carried out for ships of length 290 m or above. Hull girder loads (including torsional effects) are to be considered in accordance with the procedures of the Classification Society. The following methods may be used for Global Analysis:

**Method 1:** Analysis where hull girder loads only (vertical bending moment, horizontal bending moment and torsional moment) are directly applied to the full ship finite element model

**Method 2:** Analysis where direct loads transferred from direct load analysis are applied to the full ship finite element model

### S34.4.2 Cargo Hold Analysis

Cargo Hold Analysis is to be carried out for ships of length 150 m or above. Local loads such as sea pressure and container loads as well as hull girder loads are to be considered in accordance with the procedures of the Classification Society.

## S34.5 Load principles

### S34.5.1 Wave environment

The ship is to be considered sailing in the North Atlantic wave environment for yielding and buckling assessments. The corresponding vertical wave bending moments are to be in line with UR S11A and the other hull girder loads are to be taken in accordance with the Rules of the Classification Society. The corresponding local loads are to be taken in accordance with the Rules of the Classification Society.

### S34.5.2 Ship operating conditions

Seagoing conditions are to be considered. Harbour conditions and special conditions such as flooded conditions, tank testing conditions may be considered in accordance with the Rules of the Classification Society.

## S34.6 Load components

### S34.6.1 Global Analysis

The load components to be considered in Global Analysis are shown in Table 1.

**Table 1: Load components to be considered in Global Analysis**

| | Static load | Dynamic load |
| :--- | :--- | :--- |
| **Method 1** | ✓ Still water vertical bending moment<br>✓ Still water torsional moment | ✓ Wave-induced vertical bending moment<br>✓ Wave-induced horizontal bending moment<br>✓ Wave-induced torsional moment |
| **Method 2** | ✓ Static sea pressure<br>✓ Static container loads<br>✓ Static loads for ballast and fuel oil<br>✓ Self-weight of hull structure | ✓ Wave-induced sea pressure<br>✓ Dynamic loads for hull structure, containers, ballast and fuel oil |

### S34.6.2 Cargo Hold Analysis

The load components to be considered in Cargo Hold Analysis are defined in Table 2.

**Table 2: Load components to be considered in Cargo Hold Analysis**

| | Static load | Dynamic load |
| :--- | :--- | :--- |
| **Hull girder loads** | ✓ Still water vertical bending moment | ✓ Wave-induced vertical bending moment |
| **Local loads** | ✓ Static sea pressure<br>✓ Static container loads<br>✓ Static loads for ballast and fuel oil$^{(1)}$<br>✓ Self-weight of hull structure | ✓ Wave-induced sea pressure<br>✓ Dynamic loads for hull structure, containers, ballast and fuel oil$^{(1)}$ |

(1) For the minimum set of loading conditions specified in Table 3, all ballast and fuel oil tanks in way of the cargo hold model are to be empty. If additional loading conditions other than those given in Table 3 are considered, ballast and fuel oil loads may be taken into consideration at the discretion of the Classification Society.

## S34.7 Loading conditions

### S34.7.1 Global Analysis

Loading conditions to be considered for the Global Analysis are to be in accordance with the Loading Manual and with the Rules of the Classification Society.

### S34.7.2 Cargo Hold Analysis

The minimum set of loading conditions is specified in Table 3. In addition, loading conditions from the Loading Manual are to be considered in the Cargo Hold Analysis where deemed necessary.

**Table 3: Minimum set of loading conditions for Cargo Hold Analysis**

| Loading condition | Draught | Container weight | Ballast and fuel oil tanks | Still water hull girder moment |
| :--- | :--- | :--- | :--- | :--- |
| Full load condition | Scantling draught | Heavy cargo weight$^{(1)}$ (40' containers) | Empty | Permissible hogging |
| Full load condition | Scantling draught | Light cargo weight$^{(2)}$ (40' containers) | Empty | Permissible hogging |
| Full load condition | Reduced draught$^{(3)}$ | Heavy cargo weight$^{(1)}$ (20' containers) | Empty | Permissible sagging (minimum hogging) |
| One bay empty condition$^{(4)}$ | Scantling draught | Heavy cargo weight$^{(1)}$ (40' containers) | Empty | Permissible hogging |

(1) Heavy cargo weight of a container unit is to be calculated as the permissible stacking weight divided by the maximum number of tiers planned.

(2) Light cargo weight corresponds to the expected cargo weight when light cargo is loaded in the considered holds.
*   Light cargo weight of a container unit in hold is not to be taken more than 55% of its related heavy cargo weight (see (1) above).
*   Light cargo weight of a container unit on deck is not to be taken more than 90% of its related heavy cargo weight (see (1) above) or 17 metric tons, whichever is the lesser.

(3) Reduced draught corresponds to the expected draught amidships when heavy cargo is loaded in the considered holds while lighter cargo is loaded in other holds. Reduced draught is not to be taken more than 90% of scantling draught.

(4) For one bay empty condition, if the cargo hold consists of two or more bays, then each bay is to be considered entirely empty in hold and on deck (other bays full) in turn as separate load cases.

## S34.8 Wave conditions

### S34.8.1 Global Analysis

Wave conditions presumed to lead to the most severe load combinations due to vertical bending moment, horizontal bending moment and torsional moment are to be considered.

### S34.8.2 Cargo Hold Analysis

The following wave conditions are to be considered:

(i) Head sea condition yielding the maximum hogging and sagging vertical bending moments.
(ii) Beam sea condition yielding the maximum roll motion. This condition may be disregarded for some loading conditions defined in Table 3 where deemed not necessary.
