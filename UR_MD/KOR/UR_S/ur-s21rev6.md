# S21 Evaluation of Scantlings of Hatch Covers and Hatch Coamings and Closing Arrangements of Cargo Holds of Ships

**(1997) (Rev.1 2002) (Rev.2 Nov 2002) (Rev.3 April 2003) (Rev.4 July 2004) (Corr.1 Oct 2004) (Rev.5 May 2010) (Rev.6 Jan 2023 Complete Revision)**

---

## TABLE OF CONTENTS

### 1 APPLICATION AND DEFINITIONS (Page 4)
1.1 Application (Page 4)
1.2 Definitions (Page 4)
1.2.1 Hatch cover types (Page 4)
1.2.2 Positions (Page 5)
1.3 Material (Page 5)
1.4 General requirements (Page 5)
1.5 Net scantling approach (Page 5)

### 2 HATCH COVER AND COAMING LOAD MODEL (Page 6)
2.1 Vertical weather design load (Page 6)
2.2 Horizontal weather design load (Page 8)
2.2.1 General horizontal weather design load (Page 8)
2.2.2 Horizontal weather design load applicable to coamings of Type-2 ships (Page 10)
2.3 Cargo loads (Page 11)
2.3.1 Distributed loads (Page 11)
2.3.2 Point loads (Page 11)
2.4 Container loads (Page 11)
2.4.1 General (Page 11)
2.4.2 Corner loads for ship in upright condition (Page 11)
2.4.3 Corner loads for ship in heel condition (Page 12)
2.4.4 Load cases with partial loading (Page 13)
2.4.5 Mixed stowage of 20' and 40' containers on hatch cover (Page 14)
2.5 Loads due to elastic deformations of the ship's hull (Page 14)

### 3 HATCH COVER STRENGTH CRITERIA (Page 15)
3.1 Permissible stresses and deflections (Page 15)
3.1.1 Yield strength (Page 15)
3.1.2 Deflection (Page 16)
3.2 Local net plate thickness (Page 16)
...

---

### Notes:
1. The "contracted for construction" date means the date on which the contract to build the vessel is signed between the prospective owner and the shipbuilder. For further details regarding the date of "contract for construction", refer to IACS Procedural Requirement (PR) No. 29.
2. Rev. 3 of this UR applies to ships contracted for construction on or after 1 January 2004.
3. Till Rev. 5 of this UR, it only applies to Type-2 ships as defined in 1.1.
4. Rev.6 of this UR applies to both Type-1 and Type-2 ships as defined in 1.1 which are contracted for construction on or after 1 July 2024. UR S21A originally applicable to Type-1 ships is superseded by this UR since 1 July 2024.

---

## 1 Application and definitions

### 1.1 Application
These requirements apply to all ships except CSR bulk carriers, and are for all cargo hatch covers and coamings on exposed decks.

As specified in this UR, parts of the requirements are for some specific ship types as categorized below:
*   **Type-1 ships**, including all ships except bulk carriers, self-unloading bulk carriers, ore carriers and combination carriers, as defined in UR Z11.
*   **Type-2 ships**, including all bulk carriers, self-unloading bulk carriers, ore carriers and combination carriers, as defined in UR Z11.

The strength requirements are applicable to hatch covers and hatch coamings of stiffened plate construction and its closing arrangements.

This UR is applicable to hatch covers and coamings made of steel. In case of alternative materials and innovative designs the approval is subject to the individual class society.

This UR does not apply to portable covers secured weathertight by tarpaulins and battening devices, or pontoon covers, as defined in ICLL Regulation 15.

Hatch covers and hatch coamings of fishing vessels are to comply with the requirements of the individual class society.

These requirements are in addition to the requirements of the ICLL.

### 1.2 Definitions
**ICLL**: Where ICLL is referred to in the text, this is to be taken as the International Convention on Load Lines, 1966 as amended by the 1988 protocol, as amended in 2003.

#### 1.2.1 Hatch cover types
*   **Single skin cover**: A hatch cover made of steel or equivalent material that is designed to comply with ICLL Regulation 16. The cover has continuous top and side plating, but is open underneath with the stiffening structure exposed. The cover is weathertight and fitted with gaskets and clamping devices unless such fittings are specifically excluded.
*   **Double skin cover**: A hatch cover as above but with continuous bottom plating such that all the stiffening structure and internals are protected from the environment.
*   **Pontoon type cover**: A special type of portable cover, secured weathertight by tarpaulins and battening devices. Such covers are to be designed in accordance with ICLL Regulation 15 and are not covered by this UR.

**Clarification note**: Modern hatch cover designs of lift-away-covers (also called lift-on/lift-off, or just simply LoLo covers) are in many cases called pontoon covers. This definition does not fit to the definition above. Modern lift-away hatch cover designs should belong to one of the two categories - single skin covers or double skin cover.

#### 1.2.2 Positions
The hatchways are classified according to their position as follows:
*   **Position 1**: Upon exposed freeboard and raised quarterdecks, and upon exposed superstructure decks situated forward of a point located a quarter of ship's length from forward perpendicular.
*   **Position 2**: Upon exposed superstructure decks situated abaft a quarter of the ship's length from the forward perpendicular and located at least one standard height of the superstructure above the freeboard deck.
    *   Upon exposed superstructure decks situated forward of a point located a quarter of the ship's length from the forward perpendicular and located at least two standard height of the superstructure above the freeboard deck.

### 1.3 Material
Hatch covers and coamings are to be made of material in accordance with the definitions of UR S6. Material class I is to be applied for top plate, bottom plate and primary supporting members.

### 1.4 General requirements
Primary supporting members and stiffeners of hatch covers are to be continuous over the breadth and length of hatch covers, as far as practical. When this is impractical, sniped end connections are not to be used and appropriate arrangements are to be adopted to provide sufficient load carrying capacity.

Generally, the spacing of primary supporting members parallel to the direction of stiffeners is not to exceed 1/3 of the span of primary supporting members. If sufficient strength based on FE analysis can be verified, this requirement may be waived.

Stiffeners of hatch coamings are to be continuous over the breadth and length of hatch coamings, as far as practical.

### 1.5 Net scantling approach
Unless otherwise quoted, the thicknesses $t$ of the following sections are net thicknesses. The net thicknesses are the member thicknesses necessary to obtain the minimum net scantlings required by 3 and 5.

The required gross thicknesses are obtained by adding corrosion additions, $t_c$, given in Tab.8 in 7.1.

Strength calculations using FEM are to be performed with net scantlings.

---

## 2 Hatch cover and coaming load model
Structural assessment of hatch covers and hatch coamings is to be carried out using the design loads, defined in this chapter.

### Definitions
*   $L$ = length of ship, in m, as defined in UR S2
*   $L_{LL}$ = freeboard length of ship, in m, as defined in ICLL Regulation 3
*   $x$ = longitudinal coordinate of midpoint of assessed structural member measured from aft end of length $L$ or $L_{LL}$, as applicable
*   $D_{min}$ = the least moulded depth, in m, as defined in ICLL Regulation 3
*   $h_N$ = standard superstructure height in m
    *   $h_N = 1.05 + 0.01 L_{LL}, 1.8 \le h_N \le 2.3$

### 2.1 Vertical weather design load
The pressure $P_{HC}$, in kN/m², on the hatch cover panels is given by ICLL. This may be taken from Tab.1. The vertical weather design load needs not to be combined with cargo loads according to 2.3 and 2.4.

In Fig.1 the positions 1 and 2 are illustrated for an example ship.

Where an increased freeboard is assigned, the design load for hatch covers according to Tab.1 on the actual freeboard deck may be as required for a superstructure deck, provided the summer freeboard is such that the resulting draught will not be greater than that corresponding to the minimum freeboard calculated from an assumed freeboard deck situated at a distance at least equal to the standard superstructure height $h_N$ below the actual freeboard deck, see Fig.2.

For hatch covers of cargo holds designed for carriage of ballast or liquid cargo, the internal lateral pressures are also to be considered according to the Rules of individual societies.

---

### Tab.1 Design load $P_{HC}$ of weather deck hatches

| Position | $\frac{x}{L_{LL}} \le 0.75$ | $0.75 < \frac{x}{L_{LL}} \le 1.0$ |
| :--- | :--- | :--- |
| **1** | **for $24\text{ m} \le L_{LL} \le 100\text{ m}$** | |
| | $\frac{9.81}{76} (1.5 L_{LL} + 116)$ | **on freeboard deck**<br>$\frac{9.81}{76} \left[ (4.28 L_{LL} + 28) \frac{x}{L_{LL}} - 1.71 L_{LL} + 95 \right]$<br>**upon exposed superstructure decks located at least one superstructure standard height above the freeboard deck**<br>$\frac{9.81}{76} (1.5 L_{LL} + 116)$ |
| | **for $L_{LL} > 100\text{ m}$** | |
| | $9.81 \times 3.5$ | **on freeboard deck for type B ships according to ICLL**<br>$9.81 \left[ (0.0296 \cdot L_1 + 3.04) \cdot \frac{x}{L_{LL}} - 0.0222 \cdot L_1 + 1.22 \right]$<br>**on freeboard deck for ships with less freeboard than type B according to ICLL**<br>$9.81 \left[ (0.1452 L_1 - 8.52) \frac{x}{L_{LL}} - 0.1089 L_1 + 9.89 \right]$<br>$L_1 = L_{LL}$ but not more than 340 m<br>**upon exposed superstructure decks located at least one superstructure standard height above the freeboard deck**<br>$9.81 \times 3.5$ |
| **2** | **for $24\text{ m} \le L_{LL} \le 100\text{ m}$** | |
| | $\frac{9.81}{76} (1.1 L_{LL} + 87.6)$ | |
| | **for $L_{LL} > 100\text{ m}$** | |
| | $9.81 \times 2.6$ | |
| | **upon exposed superstructure decks located at least one superstructure standard height above the lowest Position 2 deck** | |
| | $9.81 \times 2.1$ | |

---

### 2.2 Horizontal weather design load

#### 2.2.1 General horizontal weather design load
The horizontal weather design load $P_A$, in kN/m², for determining the scantlings of outer edge girders (skirt plates) of weather deck hatch covers and of hatch coamings is:

$$P_A = f_n f_c (f_b c_L C_w - z)$$

$$C_w = \frac{L}{25} + 4.1 \quad \text{for } L < 90\text{ m}$$
$$C_w = 10.75 - \left( \frac{300 - L}{100} \right)^{1.5} \quad \text{for } 90\text{ m} \le L < 300\text{ m}$$
$$C_w = 10.75 \quad \text{for } 300\text{ m} \le L < 350\text{ m}$$
$$C_w = 10.75 - \left( \frac{L - 350}{150} \right)^{1.5} \quad \text{for } 350\text{ m} \le L \le 500\text{ m}$$

$$c_L = \sqrt{\frac{L}{90}} \quad \text{for } L < 90\text{ m}$$
$$c_L = 1 \quad \text{for } L \ge 90\text{ m}$$

$f_n = 20 + \frac{L_1}{12}$ for unprotected front coamings and hatch cover skirt plates.
$f_n = 10 + \frac{L_1}{12}$ for unprotected front coamings and hatch cover skirt plates, where the distance from the actual freeboard deck to the summer load line exceeds the minimum non-corrected tabular freeboard according to ICLL by at least one standard superstructure height $h_N$.
$f_n = 5 + \frac{L_1}{15}$ for side and protected front coamings and hatch cover skirt plates.
$f_n = 7 + \frac{L_1}{100} - 8 \frac{x'}{L}$ for aft ends of coamings and aft hatch cover skirt plates abaft amidships.
$f_n = 5 + \frac{L_1}{100} - 4 \frac{x'}{L}$ for aft ends of coamings and aft hatch cover skirt plates forward of amidships.

$L_1 = L$, need not be taken greater than 300 m.

$$f_b = 1.0 + \left( \frac{\frac{x'}{L} - 0.45}{C_B + 0.2} \right)^2 \quad \text{for } \frac{x'}{L} < 0.45$$
$$f_b = 1.0 + 1.5 \left( \frac{\frac{x'}{L} - 0.45}{C_B + 0.2} \right)^2 \quad \text{for } \frac{x'}{L} \ge 0.45$$

$0.6 \le C_B \le 0.8$, when determining scantlings of aft ends of coamings and aft hatch cover skirt plates forward of amidships, $C_B$ need not be taken less than 0.8.

$x'$ = distance in m between the transverse coaming or hatch cover skirt plate considered and aft end of the length $L$. When determining side coamings or side hatch cover skirt plates, the side is to be subdivided into parts of approximately equal length, not exceeding $0.15L$ each, and $x'$ is to be taken as the distance between aft end of the length $L$ and the centre of each part considered.

$z$ = vertical distance in m from the summer load line to the midpoint of stiffener span, or to the middle of the plate field.

$$f_c = 0.3 + 0.7 \frac{b'}{B'}$$
$b'$ = breadth of coaming in m at the position considered.
$B'$ = actual maximum breadth of ship in m on the exposed weather deck at the position considered.
$b'/B'$ is not to be taken less than 0.25.

The design load $P_A$ is not to be taken less than the minimum values $P_{A-min}$ given in Tab.2.

---

### Tab.2 Minimum design load $P_{A-min}$

| $L$ | $P_{A-min}$ in kN/m² for unprotected fronts | $P_{A-min}$ in kN/m² elsewhere |
| :--- | :---: | :---: |
| $\le 50$ | 30 | 15 |
| $> 50$ | $25 + \frac{L}{10}$ | $12.5 + \frac{L}{20}$ |
| $< 250$ | | |
| $\ge 250$ | 50 | 25 |

---

#### 2.2.2 Horizontal weather design load applicable to coamings of Type-2 ships
The pressure $P_{Coam}$, in kN/m², on the No. 1 forward transverse hatch coaming is given by:
$P_{Coam} = 220$, when a forecastle is fitted in accordance with UR S28
$P_{Coam} = 290$ in the other cases

The pressure $P_{Coam}$, in kN/m², on the other coamings is given by:
$P_{Coam} = 220$

**Note**: The horizontal weather design loads $P_A$ and $P_{Coam}$ need not be included in the direct strength calculation of the hatch cover, unless it is utilized for the design of substructures of horizontal support according to 6.2.3.

---

### 2.3 Cargo loads

#### 2.3.1 Distributed loads
The load on hatch covers due to distributed cargo loads $P_L$, in kN/m², resulting from heave and pitch (i.e. ship in upright condition) is to be determined according to the following formula:
$$P_L = P_{Cargo}(1 + a_v)$$
where:
$P_{Cargo} = \text{uniform cargo load in kN/m}^2$
$a_v = \text{vertical acceleration addition as follows:}$
$$a_v = F \cdot m$$
$$F = 0.11 \frac{v_0}{\sqrt{L}}$$
$$m = m_0 - 5(m_0 - 1) \frac{x}{L} \quad \text{for } 0 \le \frac{x}{L} \le 0.2$$
$$m = 1.0 \quad \text{for } 0.2 < \frac{x}{L} \le 0.7$$
$$m = 1 + \frac{m_0 + 1}{0.3} \left[ \frac{x}{L} - 0.7 \right] \quad \text{for } 0.7 < \frac{x}{L} \le 1.0$$
$m_0 = 1.5 + F$
$v_0 = \text{maximum speed at summer load line draught, } v_0 \text{ is not to be taken less than } \sqrt{L} \text{ in knots}$

#### 2.3.2 Point loads
The load $P$, in kN, due to a concentrated force $P_S$, in kN, except for container load, resulting from heave and pitch (i.e. ship in upright condition) is to be determined as follows:
$$P = P_S(1 + a_v)$$

---

### 2.4 Container loads

#### 2.4.1 General
The loads defined in 2.4.2 to 2.4.4 are to be applied where containers are stowed on the hatch cover.

#### 2.4.2 Corner loads for ship in upright condition
The load $P$ in kN, applied at each corner of a container stack, and resulting from heave and pitch (i.e. ship in upright condition) is to be determined as follows:
$$P = 9.81 \frac{M}{4} (1 + a_v)$$
where:
$a_v = \text{acceleration addition according to 2.3.1.}$
$M = \text{maximum designed mass of container stack in t.}$

---

#### 2.4.3 Corner loads for ship in heel condition
The loads, in kN, applied at each corner of a container stack, and resulting from heave, pitch, and the ship's rolling motion (i.e. ship in heel condition) are to be determined as follows:
$$A_z = 9.81 \frac{M}{2} (1 + a_v) \left( 0.45 - 0.42 \frac{h_m}{b} \right)$$
$$B_z = 9.81 \frac{M}{2} (1 + a_v) \left( 0.45 + 0.42 \frac{h_m}{b} \right)$$
$$B_y = 2.4 M$$
where:
$a_v = \text{acceleration addition according to 2.3.1.}$
$M = \text{maximum designed mass of container stack in t } = \sum W_i$
$h_m = \text{designed height of centre of gravity of stack above hatch cover top in m,}$
may be calculated as weighted mean value of the stack, where the centre of gravity of each tier is assumed to be located at the centre of each container,
$$h_m = \frac{\sum (z_i \cdot W_i)}{M}$$
$z_i = \text{distance from hatch cover top to the centre of } i\text{-th container in m.}$
$W_i = \text{weight of } i\text{-th container in t}$
$b = \text{distance between midpoints of foot points in m.}$
$A_z, B_z = \text{support forces in } z\text{-direction at the forward and aft stack corners.}$
$B_y = \text{support force in } y\text{-direction at the forward and aft stack corners.}$

Values of $A_z$ and $B_z$ applied for the assessment of hatch cover strength are to be shown in the drawings of the hatch covers.

**Note**: It is recommended that container loads as calculated above are considered as limit for foot point loads of container stacks in the calculations of cargo securing (container lashing).

---

### 2.4.4 Load cases with partial loading

The load cases defined in 2.4.2 and 2.4.3 are also to be considered for partial non homogeneous loading which may occur in practice, e.g. where specified container stack places are empty. For each hatch cover, the heel directions, as shown in Tab. 3, are to be considered.

The load case *partial loading of container hatch covers* can be evaluated using a simplified approach, where the hatch cover is loaded without the outermost stacks that are located completely on the hatch cover. If there are additional stacks that are supported partially by the hatch cover and partially by container stanchions then the loads from these stacks are also to be neglected, refer to Tab. 3. Partial loading of container hatch covers.

In addition, the case where only the stack places supported partially by the hatch cover and partially by container stanchions are left empty is to be assessed in order to consider the maximum loads in the vertical hatch cover supports.

It may be necessary to also consider partial load cases where more or different container stack places are left empty. Therefore, a classification society may require that additional partial load cases be considered.

![Fig.3: Forces due to container loads](image_description)
**Fig.3 Forces due to container loads**

---

### Tab.3 Partial loading of container hatch covers

| Heel direction | Left to Right | Right to Left |
| :--- | :---: | :---: |
| **Hatch covers supported by the longitudinal hatch coaming with all container stacks located completely on the hatch cover** | [Diagram showing inner stacks loaded, outermost empty] | [Diagram showing inner stacks loaded, outermost empty] |
| **Hatch covers supported by the longitudinal hatch coaming with the outermost container stack supported partially by the hatch cover and partially by container stanchions** | [Diagram showing partial stacks empty] | [Diagram showing partial stacks empty] |
| **Hatch covers not supported by the longitudinal hatch coaming (center hatch covers)** | [Diagram showing outer stacks empty] | [Diagram showing outer stacks empty] |

### 2.4.5 Mixed stowage of 20' and 40' containers on hatch cover

In the case of mixed stowage (20'+40' container combined stack), the foot point forces at the fore and aft end of the hatch cover are not to be higher than resulting from the design stack weight for 40' containers, and the foot point forces at the middle of the cover are not to be higher than resulting from the design stack weight for 20' containers.

### 2.5 Loads due to elastic deformations of the ship's hull

Hatch covers, which in addition to the loads according to 2.1 to 2.4 are loaded in the ship's transverse direction by forces due to elastic deformations of the ship's hull, are to be designed such that the sum of stresses does not exceed the permissible values given in 3.1.1.

---

## 3 Hatch cover strength criteria

### 3.1 Permissible stresses and deflections

#### 3.1.1 Yield strength

All hatch cover structural members are to comply with the following formulae:

$\sigma_{vm} \le \sigma_a$ for shell elements in general.

$\sigma_{axial} \le \sigma_a$ for rod or beam elements in general.

where:
*   $\sigma_a$ : Allowable stress as defined in Tab. 4.
*   $R_{eH}$ : Specified minimum yield stress, in N/mm², of the material.
*   $\sigma_{vm}$ : Von Mises stress, in N/mm², to be taken as follows:
    $\sigma_{vm} = \sqrt{\sigma_x^2 - \sigma_x \sigma_y + \sigma_y^2 + 3 \tau_{xy}^2}$
*   $\sigma_x$ : Normal stress, in N/mm², in $x$-direction.
*   $\sigma_y$ : Normal stress, in N/mm², in $y$-direction.
*   $\tau_{xy}$ : Shear stress, in N/mm², in the $x-y$ plane.
*   $\sigma_{axial}$ : Axial stress in rod or beam elements, in N/mm².

Indices $x$ and $y$ are coordinates of a two-dimensional Cartesian system in the plane of the considered structural element.

In case of finite element (FE) calculations using shell (or plate) elements, the stresses are to be read from the centre of the individual element. It is to be observed that, in particular, at flanges of unsymmetrical girders, the evaluation of stress from element centre may lead to non-conservative results. Thus, a sufficiently fine mesh is to be applied in these cases or, the stress at the element edges shall not exceed the allowable stress. Where shell elements are used, the stresses are to be evaluated at the mid plane of the element.

For steels with a minimum yield stress of more than 355 N/mm², the value of $R_{eH}$ to be applied throughout this requirement is subject to the individual classification society but is not to be more than the minimum yield stress of the material.

Stress concentrations are to be assessed to the satisfaction of the individual classification society.

### Tab. 4 Allowable stresses

| Members of | Subject to | $\sigma_a$, in N/mm² |
| :--- | :--- | :--- |
| **Hatch cover structure** | External pressure, as defined in 2.1 | $0.80 R_{eH}$ |
| | Other loads, as defined in 2.2 to 2.5 | $0.90 R_{eH}$ for static+dynamic load case<br>$0.72 R_{eH}$ for static load case |

---

#### 3.1.2 Deflection

The vertical deflection of primary supporting members due to the vertical weather design load according to 2.1 is to be not more than $0.0056 l_g$, where $l_g$ is the greatest span of primary supporting members.

*Note:*
*Where hatch covers are arranged for carrying containers and mixed stowage is allowed, i.e., a 40'-container stowed on top of two 20'-containers, particular attention should be paid to the deflections of hatch covers. Further the possible contact of deflected hatch covers within hold cargo has to be observed.*

### 3.2 Local net plate thickness

The local net plate thickness $t$, in mm, of the hatch cover top plating is not to be less than:

$t = 0.0158 F_p s \sqrt{\frac{P}{0.95 R_{eH}}}$

and to be not less than 1% of the spacing of the stiffener or 6 mm if that be greater.

*   $F_p$ = factor for combined membrane and bending response
    *   $= 1.5$ in general
    *   $= 1.9 \frac{\sigma}{\sigma_a}$, for $\frac{\sigma}{\sigma_a} \ge 0.8$ for the attached plate flange of primary supporting members
*   where:
    *   $s$ = stiffener spacing in mm
    *   $P$ = pressure $P_{HC}$ and $P_L$, in kN/m², as defined in 2.
    *   $\sigma$ = maximum normal stress, in N/mm², of hatch cover top plating, determined according to Fig. 4
    *   $\sigma_a$ = as defined in Tab. 4

For flange plates under compression sufficient buckling strength according to 3.6 is to be demonstrated.

---

![Fig.4: Determination of normal stress of the hatch cover plating](image_description)
**Fig.4 Determination of normal stress of the hatch cover plating**
$\sigma = \max(\sigma_x, \sigma_y)$

#### 3.2.1 Local net plate thickness of hatch covers for wheel loading

The local net plate thickness of hatch covers for wheel loading have to be derived from the individual classification society's Rules.

#### 3.2.2 Lower plating of double skin hatch covers and box girders

The thickness to fulfill the strength requirements is to be obtained from the calculation according to 3.5 under consideration of permissible stresses according to 3.1.1. When the lower plating is taken into account as a strength member of the hatch cover, the net thickness, in mm, of lower plating is to be taken not less than 5 mm. When project cargo is intended to be carried on a hatch cover, the net thickness must not be less than:

$t = 6.5s \times 10^{-3}$ mm

where:
*   $s$ = stiffener spacing in mm

*Note:*
*Project cargo means especially large or bulky cargo lashed to the hatch cover. Examples are parts of cranes or wind power stations, turbines, etc. Cargoes that can be considered as uniformly distributed over the hatch cover, e.g., timber, pipes or steel coils need not to be considered as project cargo.*

When the lower plating is not considered as a strength member of the hatch cover, the thickness of the lower plating should be determined according to the individual class society's rules.

### 3.3 Net scantling of stiffeners

The net section modulus $Z$ and net shear area $A_{shr}$ of uniformly loaded hatch cover stiffeners constraint at both ends must not be less than:

$Z = \frac{P s l^2}{f_{bc} \sigma_a}$, in cm³

$A_{shr} = \frac{8.7 P s l}{\sigma_a} 10^{-3}$, in cm²

where:
*   $l$ = stiffener span, in m, to be taken as the spacing, in m, of primary supporting members or the distance between a primary supporting member and the edge support, as applicable. When brackets are fitted at both ends of all stiffener spans, the secondary stiffener span may be reduced by an amount equal to 2/3 of the minimum brackets arm length, but not greater than 10% of the unsupported span, for each bracket.
*   $s$ = stiffener spacing in mm
*   $P$ = pressure $P_{HC}$ and $P_L$, in kN/m², as defined in 2.
*   $f_{bc}$ = boundary coefficient of stiffener, taken equal to:
    *   $f_{bc} = 8$, in the case of stiffener simply supported at both ends or simply supported at one end and clamped at the other end
    *   $f_{bc} = 12$, in the case of stiffener clamped at both ends.
*   $\sigma_a$ = allowable stress as defined in Tab. 4

For stiffeners of lower plating of double skin hatch covers, requirements mentioned above are not applied if there are no lateral loads. For double skin hatch covers of holds designed for ballast or liquid cargo, the stiffeners on lower plating are to be strengthened according to individual class society rules.

The net thickness, in mm, of the stiffener (except U-type/trapeze stiffeners) web is to be taken not less than 4 mm.

The net section modulus of the stiffeners is to be determined based on an attached plate width assumed equal to the stiffener spacing.

Stiffeners parallel to primary supporting must be continuous at crossing primary supporting member and may be regarded for calculating the cross-sectional properties of primary supporting members. It is to be verified that the combined stress of those stiffeners induced by the bending of primary supporting members and lateral pressures does not exceed the permissible stresses according to 3.1.1. The requirements of this paragraph are not applied to stiffeners of lower plating of double skin hatch covers if the lower plating is not considered as strength member.

For hatch cover stiffeners under compression sufficient safety against lateral and torsional buckling according to 3.6.3 is to be verified.

For hatch covers subject to wheel loading or point loads stiffener scantlings are to be determined under consideration of the permissible stresses according to 3.1.1 or are to be determined according to the individual class society's rules.

---

### 3.4 Net scantling of primary supporting members

#### 3.4.1 Primary supporting members

Scantlings of primary supporting members are obtained from calculations according to 3.5 under consideration of permissible stresses according to 3.1.1.

For all components of primary supporting members sufficient safety against buckling must be verified according to 3.6.

The net thickness, in mm, of webs of primary supporting members shall not be less than:

$t = 6.5s \times 10^{-3}$ in mm
$t_{min} = 5$ mm

where:
*   $s$ = stiffener spacing in mm

#### 3.4.2 Edge girders (Skirt plates)

Scantlings of edge girders are obtained from the calculations according to 3.5 under consideration of permissible stresses according to 3.1.1.

The net thickness, in mm, of the outer edge girders exposed to wash of sea shall not be less than the largest of the following values:

$t = 0.0158s \sqrt{\frac{P_A}{0.95 R_{eH}}}$
$t = 8.5s \times 10^{-3}$ in mm
$t_{min} = 5$ mm

where:
*   $P_A$ = horizontal pressure as defined in 2.2.1
*   $s$ = stiffener spacing in mm

For the required moment of inertia of edge girders, refer to 6.1.4.

### 3.5 Strength calculations

The stresses in hatch covers are to be determined by FE analysis.

The stress calculation model in this section is to be used for both yielding and buckling strength assessments in accordance with 3.1 and 3.6, respectively.

The net scantlings as defined in 1.5 are to be used.

---

#### 3.5.1 General requirements for FEM calculations

For the strength assessments of hatch covers by means of FE analysis, the hatch cover geometry shall be idealized as realistically as possible. In no case shall element width be larger than stiffener spacing. In way of force transfer points and cutouts the mesh is to be refined where applicable. The ratio of element length to width shall not exceed 3.

The element size along the height of webs of primary supporting member is not to exceed one-third of the web height. Stiffeners, which support plates subjected to lateral pressure loads, are to be included in the FE model idealization. Stiffeners may be modelled by using beam elements, or shell/plate elements. Buckling stiffeners may be disregarded for the stress calculation.

Hatch covers fitted with U-type stiffeners as shown in Fig. 5 are to be assessed by means of FE analysis. The geometry of the U-type stiffeners is to be accurately modelled using shell/plate elements. Nodal points are to be properly placed on the intersections between the webs of a U-type stiffener and the hatch cover plate, and between the webs and flange of the U-type stiffener.

![Fig.5: Example of hatch cover fitted with U-type stiffeners](image_description)
**Fig.5: Example of hatch cover fitted with U-type stiffeners**

Wherever applicable the following boundary conditions are to be applied to the FE model:
*   Boundary nodes in way of a bearing pad on the hatch coamings are to be fixed against displacement in the direction perpendicular to the pad.
*   Lifting stoppers are to be fixed against displacements in the direction determined by the stoppers.
*   For a folding type hatch cover, the FE nodes connected through a hinge are to have the same translational displacement in the direction perpendicular to the hatch cover top plating.

### 3.6 Buckling strength of hatch cover structures

#### 3.6.1 General

Buckling strength of all hatch cover structures is to be checked. Buckling assessments are to be performed in compliance with the requirements in UR S35 for the conditions specified in 3.6.2 and 3.6.3.

The net scantlings as defined in 1.5 are to be used for buckling check.

---

#### 3.6.2 Slenderness requirements

The slenderness requirements are to be in accordance with those specified in UR S35/Sec 2. The slenderness requirements need not be applied to the lower boundary of double skin hatch covers unless the cargo hold is designed for carriage of ballast or liquid cargo.

The breadth of the primary supporting member flange is to be not less than 40% of their depth for laterally unsupported spans greater than 3.0 m. Tripping brackets attached to the flange may be considered as a lateral support for primary supporting members.

#### 3.6.3 Buckling requirements

**3.6.3.1 Application**

These requirements apply to the buckling assessment of hatch cover structures subjected to compressive and shear stresses and lateral pressures. The buckling assessment is to be performed for the following structural elements:
*   Stiffened and unstiffened panels, including curved panels and panels stiffened with U-type stiffeners.
*   Web panels of primary supporting members in way of openings.

The buckling strength assessment of coaming parts is to be done according to the individual Society's rules.

For rule application, the panel types and assessment methods, the applied lateral pressure and stresses, safety factors and buckling check criteria are defined in 3.6.3.2, 3.6.3.3, 3.6.3.4 and 3.6.3.5, respectively. The procedure and detailed requirements for buckling assessment are given in UR S35/Sec4, including idealization of irregular plate panels, definition of reference stresses and buckling criteria.

Unless otherwise specified, the symbols used in 3.6.3 are defined in UR S35.

**3.6.3.2 Panel types and assessment methods**

The plate panel of a hatch cover structure is to be modelled as stiffened panel (SP) or unstiffened panel (UP) as defined in UR S35/Sec 4, [2]. Assessment Method A (-A) and Method B (-B) as defined in UR S35/Sec 1, [3] are to be used in accordance with Tab. 5, Fig. 6 and Fig. 7. For a web panel with opening, the procedure for opening should be used for its buckling assessment.

For a hatch cover fitted with U-type stiffeners, the additional buckling assessment requirements specific for panels with U-type stiffeners in UR S35/Sec 5, [2.5] are also to be followed.

---

### Tab.5 Structural members and assessment methods

| Structural elements | Assessment method | Normal panel definition |
| :--- | :---: | :--- |
| **Hatch cover top/bottom plating structures, see Fig. 6** | | |
| Hatch cover top/bottom plating | SP-A | Length: between transverse girders<br>Width: between longitudinal girders |
| Irregularly stiffened panels | UP-B | Plate between local stiffeners/PSM |
| **Hatch cover web panels of primary supporting members, see Fig. 7** | | |
| Web of transverse/longitudinal girder (single skin type) | UP-B | Plate between local stiffeners/face plate/PSM |
| Web of transverse/longitudinal girder (double skin type) | SP-B | Length: between PSM<br>Width: full web depth |
| Web panel with opening | Procedure for opening | Plate between local stiffeners/face plate/PSM |
| Irregularly stiffened panels | UP-B | Plate between local stiffeners/face plate/PSM |

*Note 1: SP and UP stand for stiffened and unstiffened panel respectively.*
*Note 2: A and B stand for Method A and Method B respectively.*
*Note 3: In case that the buckling carlings/brackets are irregularly arranged in the web of transverse/longitudinal girder, UP-B method may be used.*

![Fig.6: Hatch cover top/bottom plating structures](image_description)
**Fig.6 Hatch cover top/bottom plating structures**

---

![Fig.7: Hatch cover webs of primary supporting members](image_description)
**Fig.7 Hatch cover webs of primary supporting members**

**3.6.3.3 Applied lateral pressure and stresses**

The buckling assessment of hatch covers is based on the lateral pressure as defined in S2.1 and 2.2, and stresses obtained from FE analysis, refer to 3.5.

**3.6.3.4 Safety factors**

For all hatch cover structural members, safety factor $S=1.0$ is to be applied to both of the plating and stiffener buckling capacity formulas as defined in UR S35/Sec5/2.2 and UR S35/Sec5/2.3, respectively.

**3.6.3.5 Buckling acceptance criteria**

A structural member is considered to have an acceptable buckling strength if it satisfies the following criterion:

$\eta_{act} \le \eta_{all}$

where:
*   $\eta_{act}$ : Buckling utilisation factor based on the applied stress, as defined in UR S35 /Sec1 [3.2.2] and UR S35/Sec4, and calculated per UR S35/Sec5.
*   $\eta_{all}$ : Allowable buckling utilisation factor, taken as given in Tab. 6.

### Tab.6 Allowable buckling utilisation factors

| Structural component | Subject to | $\eta_{all}$, Allowable buckling utilisation factor |
| :--- | :--- | :---: |
| **Plates and stiffeners Web of PSM** | External pressure, as defined in 2.1 | 0.80 |
| | Other loads, as defined in 2.2 to 2.5 | 0.90 for static+dynamic load case<br>0.72 for static load case |

---

## 4 Details of hatch covers

### 4.1 Container foundations on hatch covers

Container foundations are to be designed to the satisfaction of the individual class society. The substructures of container foundations are to be designed for cargo and container loads according to 2, applying the permissible stresses according to 3.1.1.

### 4.2 Weather tightness

Further to the following requirements IACS Rec. 14 is applicable to hatch covers.

#### 4.2.1 Packing material (General)

The packing material is to be suitable for all expected service conditions of the ship and is to be compatible with the cargoes to be transported. The packing material is to be selected with regard to dimensions and elasticity in such a way that expected deformations can be carried. Forces are to be carried by the steel structure only.

The packings are to be compressed so as to give the necessary tightness effect for all expected operating conditions. Special consideration shall be given to the packing arrangement in ships with large relative movements between hatch covers and coamings or between hatch cover sections. The specification or grade of the packing material is to be indicated on the drawings.

#### 4.2.2 Dispensation of weather tight gaskets

For hatch covers of cargo holds solely for the transport of containers, upon request by the owners and subject to compliance with the following conditions the fitting of weather tight gaskets according to 4.2.1 may be dispensed with:

*   The hatchway coamings shall be not less than 600 mm in height.
*   The exposed deck on which the hatch covers are located is situated above a depth $H(x)$. $H(x)$ is to be shown to comply with the following criteria:
    $H(x) \ge T_{fb} + f_b + h$ in m
    *   $T_{fb}$ = draught, in m, corresponding to the assigned summer load line
    *   $f_b$ = minimum required freeboard, in m, determined in accordance with ICLL Reg. 28 as modified by further regulations as applicable
    *   $h = 4.6$ m for $\frac{x}{L_{LL}} \le 0.75$
    *   $h = 6.9$ m for $\frac{x}{L_{LL}} > 0.75$
*   Labyrinths, gutter bars or equivalents are to be fitted proximate to the edges of each panel in way of the coamings. The clear profile of these openings is to be kept as small as possible.
*   Where a hatch is covered by several hatch cover panels the clear opening of the gap in between the panels shall not be wider than 50mm.

---

## 5 HATCH COAMING STRENGTH AND LOCAL DETAILS

### 5.1 Local net plate thickness of coamings

The net thickness of weather deck hatch coamings shall not be less than the larger of the following values:

(1) For Type-1 ships:
$$t = 0.0142s \sqrt{\frac{P_A}{0.95R_{eH}}} \text{ in mm}$$
$$t_{min} = 6 + \frac{L_1}{100} \text{ mm}$$

(2) For Type-2 ships:
$$t = 0.016s \sqrt{\frac{P_{coam}}{0.95R_{eH}}} \text{ in mm}$$
$$t_{min} = 9.5 \text{ mm}$$

where:
$P_A$ = pressure, in kN/m², as defined in S21.2.2.1
$P_{coam}$ = pressure, in kN/m², as defined in S21.2.2.2
$s$ = stiffener spacing in mm
$L_1$ = $L$, need not be taken greater than 300 m

In addition, for both Type-1 and Type-2 ships, longitudinal strength aspects are to be observed.

### 5.2 Net scantling of stiffeners of coamings

The stiffeners must be continuous at the coaming stays. For stiffeners with both ends constraint the elastic net section modulus $Z$ in cm³ and net shear area $A_{shr}$ in cm², calculated on the basis of net thickness, must not be less than:

(1) For Type-1 ships:
$$Z = \frac{P_A s l^2}{f_{bc} R_{eH}}$$
$$A_{shr} = \frac{P_A s l}{R_{eH}} 10^{-2}$$

where:
$f_{bc}$ = 12 in general
= 8 for the end spans of stiffeners sniped at the coaming corners
$l$ = stiffener span, in m, to be taken as the spacing of coaming stays
$s$ = stiffener spacing in mm

Note that for sniped stiffeners of coaming at hatch corners shear area at the fixed support has to be increased by 35%. The gross thickness of the coaming plate at the sniped stiffener end shall not be less than:
$$t_{gr} = 19.6 \sqrt{\frac{P_A s (l - 0.0005s)}{1000 R_{eH}}} \text{ in mm}$$

(2) For Type-2 ships:
$$Z = 1.21 \frac{P_{coam} s l^2}{f_{bc} c_p R_{eH}}$$

where:
$f_{bc}$ = 16 in general
= 12 for the end spans of stiffeners sniped at the coaming corners
$l$ = span, in m, of stiffeners
$s$ = spacing, in mm, of stiffeners
$P_A$ = pressure in kN/m² as defined in 2.2.1
$P_{coam}$ = pressure in kN/m² as defined in 2.2.2
$c_p$ = ratio of the plastic section modulus to the elastic section modulus of the stiffeners with an attached plate breadth, in mm, equal to 40 $t$, where $t$ is the plate net thickness
= 1.16 in the absence of more precise evaluation

In addition, for both Type-1 and Type-2 ships, horizontal stiffeners on hatch coamings, which are part of the longitudinal hull structure, are to be designed according to the individual classification society's rules.

### 5.3 Coaming stays

Coaming stays are to be designed for the loads transmitted through them and permissible stresses according to 3.1.1.

#### 5.3.1 Coaming stay section modulus and web thickness

At the connection with deck, the net section modulus $Z$, in cm³, and the net thickness $t_w$, in mm, of the coaming stays designed as beams with flange (examples 1 and 2 are shown in Fig. 8) are to be taken not less than:
$$Z = \frac{P s_c H_C^2}{1.9 R_{eH}} \text{ in cm³}$$
$$t_w = \frac{2 P s_c H_C}{h R_{eH}} \text{ in mm}$$

where:
$H_C$ = stay height, in m
$s_c$ = stay spacing, in mm
$h$ = stay depth, in mm, at the connection with the deck
$P$ = pressure on coaming, in kN/m², taken as $P_A$ defined in 2.2.1 in general and as $P_{coam}$ defined in 2.2.2 for Type-2 ships.

For other designs of coaming stays, such as those shown in Fig. 8, examples 3 and 4, the stresses are to be determined through FEM. The calculated stresses are to comply with the permissible stresses according to 3.1.1.

Coaming stays are to be supported by appropriate substructures. For calculating the section modulus of coaming stays, their face plate area is to be taken into account only when it is welded with full penetration welds to the deck plating and adequate underdeck structure is fitted to support the stresses transmitted by it.

Webs are to be connected to the deck by fillet welds on both sides with a throat thickness of $a = 0.44 t_w$.

For Type-2 ships, toes of stay webs are to be connected to the deck plating with full or partial penetration double bevel welds extending over a distance not less than 15% of the stay width. For other ship types the size of welding for toes of webs at the lower end of coaming stays should be according to the individual class society's Rules.

![Fig. 8: Examples of coaming stays](image_description)
*Fig. 8 Examples of coaming stays*

#### 5.3.2 Coaming stays under friction load

For coaming stays, which transfer friction forces at hatch cover supports, fatigue strength is to be considered according to individual class society's rules, refer to 6.2.2.

### 5.4 Further requirements for hatch coamings

#### 5.4.1 Longitudinal strength

Hatch coamings which are part of the longitudinal hull structure are to be designed according to the requirements for longitudinal strength of the individual classification society.

For structural members welded to coamings and for cutouts in the top of coamings sufficient fatigue strength is to be verified.

Longitudinal hatch coamings with a length exceeding 0.1L m are to be provided with tapered brackets or equivalent transitions and a corresponding substructure at both ends. At the end of the brackets they are to be connected to the deck by full penetration welds of minimum 300 mm in length.

#### 5.4.2 Local details

If the design of local details is not regulated in 5, local details are to comply with the individual classification society's requirement for the purpose of transferring the loads on the hatch covers to the hatch coamings and, through them, to the deck structures below. Hatch coamings and supporting structures are to be adequately stiffened to accommodate the loading from hatch covers, in longitudinal, transverse and vertical directions.

Structures under deck are to be checked against the load transmitted by the stays.

Unless otherwise stated, weld connections and materials are to be dimensioned and selected in accordance with the individual classification society's requirements.

#### 5.4.3 Stays

On ships carrying cargo on deck, such as timber, coal or coke, the stays are to be spaced not more than 1,5 m apart.

#### 5.4.4 Extend of coaming plates

Coaming plates are to extend to the lower edge of the deck beams or hatch side girders are to be fitted that extend to the lower edge of the deck beams. Extended coaming plates and hatch side girders are to be flanged or fitted with face bars or half-round bars. Fig. 9 gives an example.

![Fig. 9: Example for a hatch side girder](image_description)
*Fig. 9 Example for a hatch side girder*

#### 5.4.5 Drainage arrangement at the coaming

If drain channels are provided inside the line of gasket by means of a gutter bar or vertical extension of the hatch side and end coaming, drain openings are to be provided at appropriate positions of the drain channels.

Drain openings in hatch coamings are to be arranged with sufficient distance to areas of stress concentration (e.g. hatch corners, transitions to crane posts).

Drain openings are to be arranged at the ends of drain channels and are to be provided with non-return valves to prevent ingress of water from outside. It is unacceptable to connect fire hoses to the drain openings for this purpose.

If a continuous outer steel contact between cover and ship structure is arranged, drainage from the space between the steel contact and the gasket is also to be provided for.

---

## 6 CLOSING ARRANGEMENTS

### 6.1 Securing devices

#### 6.1.1 General

Securing devices between cover and coaming and at cross-joints are to be installed to provide weathertightness. Sufficient packing line pressure is to be maintained.

Securing devices must be appropriate to bridge displacements between cover and coaming due to hull deformations.

Securing devices are to be of reliable construction and effectively attached to the hatchway coamings, decks or covers. Individual securing devices on each cover are to have approximately the same stiffness characteristics.

Sufficient number of securing devices is to be provided at each side of the hatch cover considering the requirements of 3.4.2. This applies also to hatch covers consisting of several parts.

The materials of stoppers, securing devices and their weldings are to be to the satisfaction the individual class society. Specifications of the materials are to be shown in the drawings of the hatch covers.

#### 6.1.2 Rod cleats

Where rod cleats are fitted, resilient washers or cushions are to be incorporated.

#### 6.1.3 Hydraulic cleats

Where hydraulic cleating is adopted, a positive means is to be provided so that it remains mechanically locked in the closed position in the event of failure of the hydraulic system.

#### 6.1.4 Cross-sectional area of the securing devices

The gross cross-sectional area in cm² of the securing devices is not to be less than:
$$A = 0.28 q S_{SD} k_l$$

Correspondingly, the stiffness of edge girders is to be sufficient to maintain adequate sealing pressure between securing devices. The moment of inertia, in cm⁴, of edge girders is not to be less than:
$$I = 6 q S_{SD}^4$$

where:
$q$ = packing line pressure in N/mm, minimum 5 N/mm.
$S_{SD}$ = spacing between securing devices in m, not to be taken less than 2 m.
$k_l = \left(\frac{235}{R_{eH}}\right)^e$

$R_{eH}$ is the minimum yield strength of the material in N/mm², but is not to be taken greater than $0.7R_m$, where $R_m$ is the tensile strength of the material in N/mm².

$e$ = 0.75 for $R_{eH} > 235 \text{ N/mm²}$
= 1.00 for $R_{eH} \leq 235 \text{ N/mm²}$

Rods or bolts are to have a gross diameter not less than 19 mm for hatchways exceeding 5 m² in area.

Securing devices of special design in which significant bending or shear stresses occur may be designed as anti-lifting devices according to 6.1.5. The packing line pressure $q$ is to be specified, and as load, $q$ multiplied by the spacing between securing devices $S_{SD}$ is to be applied.

#### 6.1.5 Anti lifting devices

The securing devices of hatch covers, on which cargo is to be lashed, are to be designed for the lifting forces resulting from loads according to 2.4, refer Fig. 10. Unsymmetrical loadings, which may occur in practice, are to be considered. Under these loadings the equivalent stress in the securing devices is not to exceed:
$$\sigma_{vm} = \frac{150}{k_l} \text{ in N/mm²}$$

Note:
The partial load cases given in Tab. 3 may not cover all unsymmetrical loadings, critical for hatch cover lifting.

Chapter 5.6 of IACS Rec. 14 should be referred to for the omission of anti-lifting devices.

![Fig. 10: Lifting forces at a hatch cover](image_description)
*Fig. 10 Lifting forces at a hatch cover*

### 6.2 Hatch cover supports, stoppers and supporting structures

#### 6.2.1 Horizontal mass forces

For the design of hatch cover supports the horizontal mass forces $F_h = m \cdot a$ are to be calculated with the following accelerations:
$a_X = 0.2g$ in longitudinal direction
$a_Y = 0.5g$ in transverse direction
$m$ = Sum of mass of cargo lashed on the hatch cover and mass of hatch cover.

The accelerations in longitudinal direction and in transverse direction do not need to be considered as acting simultaneously.

#### 6.2.2 Hatch cover supports

For the transmission of the support forces resulting from the load cases specified in 2 and of the horizontal mass forces specified in 6.2.1, supports are to be provided which are to be designed such that the nominal surface pressures in general do not exceed the following values:
$$P_{nmax} = d P_n \text{ in N/mm²}$$
$$d = 3.75 - 0.015L$$
$d_{max} = 3.0$
$d_{min} = 1.0$ in general
= 2.0 for partial loading conditions, see 2.4.1
$P_n$ = permissible nominal surface pressure, see Tab. 7

For metallic supporting surfaces not subjected to relative displacements the nominal surface pressure applies:
$P_{nmax} = 3 p_n \text{ in N/mm²}$

Note:
When the maker of vertical hatch cover support material can provide proof that the material is sufficient for the increased surface pressure, not only statically but under dynamic conditions including relative motion for adequate number of cycles, permissible nominal surface pressure may be relaxed at the discretion of the individual classification society. However, realistic long-term distribution of spectra for vertical loads and relative horizontal motion should be assumed and agreed with the individual classification society.

Drawings of the supports must be submitted. In the drawings of supports the permitted maximum pressure given by the material manufacturer must be specified.

**Tab. 7 Permissible nominal surface pressure $P_n$**

| Support material | $P_n$ [N/mm²] when loaded by Vertical force | $P_n$ [N/mm²] when loaded by Horizontal force (on stoppers) |
| :--- | :---: | :---: |
| Hull structural steel | 25 | 40 |
| Hardened steel | 35 | 50 |
| Lower friction materials | 50 | – |

Where large relative displacements of the supporting surfaces are to be expected, the use of material having low wear and frictional properties is recommended.

The substructures of the supports must be of such a design, that a uniform pressure distribution is achieved.

Irrespective of the arrangement of stoppers, the supports must be able to transmit the following force $P_h$ in the longitudinal and transverse direction:
$$P_h = \mu \cdot P_v$$

where:
$P_v$ = vertical supporting force
$\mu$ = frictional coefficient
= 0.5 in general

For non-metallic, low-friction support materials on steel, the friction coefficient may be reduced but not to be less than 0.35 and to the satisfaction of the individual class society.

Supports as well as the adjacent structures and substructures are to be designed such that the permissible stresses according to 3.1.1 are not exceeded.

For substructures and adjacent structures of supports subjected to horizontal forces $P_h$, fatigue strength is to be considered according to the individual classification society's rules.

#### 6.2.3 Hatch cover stoppers

Hatch covers shall be sufficiently secured against horizontal shifting. Stoppers are to be provided for hatch covers on which cargo is carried.

The greater of the loads resulting from 2.2 and 6.2.1 is to be applied for the dimensioning of the stoppers and their substructures.

The permissible stress in stoppers and their substructures, in the cover, and of the coamings is to be determined according to 3.1.1. In addition, the provisions in 6.2.2 are to be observed.

Specifically for Type-2 ships, the following additional requirements are to be complied with:

Hatch covers are to be effectively secured, by means of stoppers, against the transverse forces arising from a pressure of 175 kN/m².

With the exclusion of No. 1 hatch cover, hatch covers are to be effectively secured, by means of stoppers, against the longitudinal forces acting on the forward end arising from a pressure of 175 kN/m².

No. 1 hatch cover is to be effectively secured, by means of stoppers, against the longitudinal forces acting on the forward end arising from a pressure of 230 kN/m².

This pressure may be reduced to 175 kN/m² when a forecastle is fitted in accordance with UR S28.

The equivalent stress:
i. in stoppers and their supporting structures, and
ii. calculated in the throat of the stopper welds is not to exceed the allowable value of $0.8R_{eH}$.

---

## 7 CORROSION ADDITION AND STEEL RENEWAL

### 7.1 Corrosion addition for hatch covers and hatch coamings

The scantling requirements of the above sections imply the following general corrosion additions $t_c$:

**Tab. 8 Corrosion additions $t_c$ for hatch covers and hatch coamings**

| Application | Structure | $t_c$ [mm] |
| :--- | :--- | :---: |
| Weather deck cargo hatches of container ships, car carriers, paper carriers, passenger vessels | Hatch covers | 1.0 |
| | Hatch coamings | according to individual class society's rules |
| Weather deck cargo hatches of Type-2 ships | Hatch covers in general | 2.0 |
| | Top and bottom plating of double skin hatch covers | 2.0 |
| | Internal structure of double skin hatch covers | 1.5 |
| | Hatch coamings and coaming stays | 1.5 |
| Weather deck cargo hatches of all other ship types covered by this UR | Hatch covers in general | 2.0 |
| | Weather exposed plating and bottom plating of double skin hatch covers | 1.5 |
| | Internal structure of double skin hatch covers and closed box girders | 1.0 |
| | Hatch coamings not part of the longitudinal hull structure | 1.5 |
| | Hatch coamings part of the longitudinal hull structure | according to individual class society's rules |
| | Coaming stays and stiffeners | 1.5 |

### 7.2 Steel renewal

Steel renewal is required where the gauged thickness is less than $t_{net} + 0.5 \text{ mm}$ for
- single skin hatch covers,
- the plating of double skin hatch covers, and
- coaming structures the corrosion additions $t_c$ of which are provided in Tab. 8.

Where the gauged thickness is within the range $t_{net} + 0.5 \text{ mm}$ and $t_{net} + 1.0 \text{ mm}$, coating (applied in accordance with the coating manufacturer's requirements) or annual gauging may be adopted as an alternative to steel renewal. Coating is to be maintained in GOOD condition, as defined in UR Z10.2.1.2.

For the internal structure of double skin hatch covers, thickness gauging is required when hatch cover top or bottom plating renewal is to be carried out or when this is deemed necessary, at the discretion of the individual class society's surveyor, on the basis of the plating corrosion or deformation condition. In these cases, steel renewal for the internal structures is required where the gauged thickness is less than $t_{net}$.

For corrosion addition $t_c = 1.0 \text{ mm}$ the thickness for steel renewal is $t_{net}$ and the thickness for coating or annual gauging is when gauged thickness is between $t_{net}$ and $t_{net} + 0.5 \text{ mm}$.

For coaming structures, the corrosion additions $t_c$ of which are not provided in Tab. 8, steel renewal and coating or annual gauging are to be in accordance with the individual classification society's requirements.
