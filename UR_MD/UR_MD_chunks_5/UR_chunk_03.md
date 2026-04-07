In no case is the allowable hold loading, considering flooding, to be greater than the design hold loading in the intact condition.

This UR does not apply to CSR Bulk Carriers.

### S20.2 - Loading model

#### S20.2.1 - General

The loads to be considered as acting on the double bottom are those given by the external sea pressures and the combination of the cargo loads with those induced by the flooding of the hold which the double bottom belongs to.

The most severe combinations of cargo induced loads and flooding loads are to be used, depending on the loading conditions included in the loading manual:
- homogeneous loading conditions;
- non homogeneous loading conditions;
- packed cargo conditions (such as steel mill products).

For each loading condition, the maximum bulk cargo density to be carried is to be considered in calculating the allowable hold loading limit.

**Note:**
1. The "contracted for construction" date means the date on which the contract to build the vessel is signed between the prospective owner and the shipbuilder. For further details regarding the date of "contract for construction", refer to IACS Procedural Requirement (PR) No. 29.
2. Revision 4 or subsequent revisions or corrigenda as applicable of this UR is to be applied by IACS Societies to ships contracted for construction on or after 1 July 2006.

---

#### S20.2.2 - Inner bottom flooding head

The flooding head $h_f$ (see Figure 1) is the distance, in m, measured vertically with the ship in the upright position, from the inner bottom to a level located at a distance $d_f$, in m, from the baseline equal to:

a) in general:
- D for the foremost hold
- 0.9D for the other holds

b) for ships less than 50,000 tonnes deadweight with Type B freeboard:
- 0.95D for the foremost hold
- 0.85D for the other holds

D being the distance, in m, from the baseline to the freeboard deck at side amidship (see Figure 1).

### S20.3 - Shear capacity of the double bottom

The shear capacity C of the double bottom is defined as the sum of the shear strength at each end of:

- all floors adjacent to both hoppers, less one half of the strength of the two floors adjacent to each stool, or transverse bulkhead if no stool is fitted (see Figure 2).
- all double bottom girders adjacent to both stools, or transverse bulkheads if no stool is fitted.

Where in the end holds, girders or floors run out and are not directly attached to the boundary stool or hopper girder, their strength is to be evaluated for the one end only.

Note that the floors and girders to be considered are those inside the hold boundaries formed by the hoppers and stools (or transverse bulkheads if no stool is fitted). The hopper side girders and the floors directly below the connection of the bulkhead stools (or transverse bulkheads if no stool is fitted) to the inner bottom are not to be included.

When the geometry and/or the structural arrangement of the double bottom are such to make the above assumptions inadequate, to the Society's discretion, the shear capacity C of double bottom is to be calculated according to the Society's criteria.

In calculating the shear strength, the net thickness of floors and girders is to be used. The net thickness $t_{net}$, in mm, is given by:

$$t_{net} = t - 2.5$$

where:
t = thickness, in mm, of floors and girders.

---

#### S20.3.1 - Floor shear strength

The floor shear strength in way of the floor panel adjacent to hoppers $S_{f1}$, in kN, and the floor shear strength in way of the openings in the outmost bay (i.e. that bay which is closer to hopper) $S_{f2}$, in kN, are given by the following expressions:

$$S_{f1} = 10^{-3} A_f \frac{\tau_a}{\eta_1}$$
$$S_{f2} = 10^{-3} A_{f,h} \frac{\tau_a}{\eta_2}$$

where:
$A_f$ = sectional area, in mm², of the floor panel adjacent to hoppers
$A_{f,h}$ = net sectional area, in mm², of the floor panels in way of the openings in the outmost bay (i.e. that bay which is closer to hopper)
$\tau_a$ = allowable shear stress, in N/mm², to be taken equal to the lesser of

$$\tau_a = \frac{162 \sigma_F^{0.6}}{(s/t_{net})^{0.8}} \quad \text{and} \quad \frac{\sigma_F}{\sqrt{3}}$$

For floors adjacent to the stools or transverse bulkheads, as identified in S20.3 $\tau_a$ may be taken $\sigma_F / \sqrt{3}$

$\sigma_F$ = minimum upper yield stress, in N/mm², of the material
$s$ = spacing of stiffening members, in mm, of panel under consideration
$\eta_1 = 1.10$
$\eta_2 = 1.20$

$\eta_2$ may be reduced, to the Society's discretion, down to 1.10 where appropriate reinforcements are fitted to the Society's satisfaction

#### S20.3.2 - Girder shear strength

The girder shear strength in way of the girder panel adjacent to stools (or transverse bulkheads, if no stool is fitted) $S_{g1}$, in kN, and the girder shear strength in way of the largest opening in the outmost bay (i.e. that bay which is closer to stool, or transverse bulkhead, if no stool is fitted) $S_{g2}$, in kN, are given by the following expressions:

$$S_{g1} = 10^{-3} A_g \frac{\tau_a}{\eta_1}$$
$$S_{g2} = 10^{-3} A_{g,h} \frac{\tau_a}{\eta_2}$$

where:
$A_g$ = minimum sectional area, in mm², of the girder panel adjacent to stools (or transverse bulkheads, if no stool is fitted)
$A_{g,h}$ = net sectional area, in mm², of the girder panel in way of the largest opening in the outmost bay (i.e. that bay which is closer to stool, or transverse bulkhead, if no stool is fitted)
$\tau_a$ = allowable shear stress, in N/mm², as given in S20.3.1
$\eta_1 = 1.10$
$\eta_2 = 1.15$

$\eta_2$ may be reduced, to the Society's discretion, down to 1.10 where appropriate reinforcements are fitted to the Society's satisfaction

---

### S20.4 - Allowable hold loading

The allowable hold loading W, in tonnes, is given by:

$$W = \rho_c V \frac{1}{F}$$

where:
F = 1.1 in general
    1.05 for steel mill products
$\rho_c$ = cargo density, in t/m³; for bulk cargoes see S20.2.1; for steel products, $\rho_c$ is to be taken as the density of steel
V = volume, in m³, occupied by cargo at a level $h_1$

$$h_1 = \frac{X}{\rho_c g}$$

X = for bulk cargoes the lesser of $X_1$ and $X_2$ given by:

$$X_1 = \frac{Z + \rho g(E - h_f)}{1 + \frac{\rho}{\rho_c} (perm - 1)}$$

$$X_2 = Z + \rho g(E - h_f perm)$$

X = for steel products, X may be taken as $X_1$, using $perm = 0$
$\rho$ = sea water density, in t/m³
$g = 9.81 \text{ m/s}^2$, gravity acceleration
E = ship immersion in m for flooded hold condition = $d_f - 0.1D$
$d_f, D$ = as given in S20.2.2
$h_f$ = flooding head, in m, as defined in S20.2.2
perm = cargo permeability, (i.e. the ratio between the voids within the cargo mass and the volume occupied by the cargo); it needs not be taken greater than 0.3.
Z = the lesser of $Z_1$ and $Z_2$ given by:

$$Z_1 = \frac{C_h}{A_{DB,h}}$$
$$Z_2 = \frac{C_e}{A_{DB,e}}$$

$C_h$ = shear capacity of the double bottom, in kN, as defined in S20.3, considering, for each floor, the lesser of the shear strengths $S_{f1}$ and $S_{f2}$ (see S20.3.1) and, for each girder, the lesser of the shear strengths $S_{g1}$ and $S_{g2}$ (see S20.3.2)
$C_e$ = shear capacity of the double bottom, in kN, as defined in S20.3, considering, for each floor, the shear strength $S_{f1}$ (see S20.3.1) and, for each girder, the lesser of the shear strengths $S_{g1}$ and $S_{g2}$ (see S20.3.2)

$$A_{DB,h} = \sum_{i=1}^{i=n} S_i B_{DB,i}$$
$$A_{DB,e} = \sum_{i=1}^{i=n} S_i (B_{DB} - s_1)$$

n = number of floors between stools (or transverse bulkheads, if no stool is fitted)
$S_i$ = space of ith-floor, in m
$B_{DB,i} = B_{DB} - s_1$ for floors whose shear strength is given by $S_{f1}$ (see S20.3.1)
$B_{DB,i} = B_{DB,h}$ for floors whose shear strength is given by $S_{f2}$ (see S20.3.1)
$B_{DB}$ = breadth of double bottom, in m, between hoppers (see Figure 3)
$B_{DB,h}$ = distance, in m, between the two considered opening (see Figure 3)
$s_1$ = spacing, in m, of double bottom longitudinals adjacent to hoppers

---

![Figure 1: Cross-section of a ship's hold showing flooding and loading parameters.](A cross-section diagram of a ship's hold illustrating the dimensions D (baseline to freeboard deck), df (baseline to flooding level), hf (inner bottom to flooding level), h1 (inner bottom to cargo level), d1 (baseline to cargo level), and V (volume of cargo).)

![Figure 2: Structural details of the double bottom and hold boundaries.](A multi-part diagram showing: 1) A profile view of a hold boundary with a lower stool and a transverse bulkhead. 2) A plan view of the double bottom structure highlighting floors adjacent to the stool and transverse bulkhead, as well as the grid of floors and longitudinal girders.)

![Figure 3: Dimensions of the double bottom between hoppers and openings.](A cross-section diagram of the double bottom showing openings in the floors. It labels B_DB as the total breadth between hoppers and B_DB,h as the distance between the outermost openings.)

**End of Document**

================================================================================
# FILE: UR_S/ur-s21adel.md
================================================================================

# S21A

**Requirements concerning**
# STRENGTH OF SHIPS

## Evaluation of Scantlings of Hatch Covers and Hatch Coamings and Closing Arrangements of Cargo Holds of Ships

Deleted on 1 July 2024 as UR S21A was superseded by UR S21 Rev.6

**S21A**
(May 2011)
(Corr.1 Oct 2011)
(Rev.1 May 2015)
(Corr.1 Feb 2018)
(Corr.2 Mar 2019)
(Deleted Jan 2023)

***

Page 1 of 1 IACS Req. 2011/Del 2023

================================================================================
# FILE: UR_S/ur-s21rev6.md
================================================================================

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


================================================================================
# FILE: UR_S/ur-s22rev3.md
================================================================================

**S22**
(1997)
(Rev. 1 1997)
(Rev. 2 Sept. 2000)
(Rev. 3 July 2004)

# S22 Evaluation of Allowable Hold Loading of Cargo Hold No. 1 with Cargo Hold No. 1 Flooded, for Existing Bulk Carriers

## S22.1 - Application and definitions

These requirements apply to all bulk carriers of 150 m in length and above, in the foremost hold, intending to carry solid bulk cargoes having a density of 1,78 t/m$^3$, or above, with single deck, topside tanks and hopper tanks, where:

(i) the foremost hold is bounded by the side shell only for ships which were contracted for construction prior to 1 July 1998, and have not been constructed in compliance with IACS Unified Requirement S20,

(ii) the foremost hold is double side skin construction less than 760 mm breadth measured perpendicular to the side shell in ships, the keels of which were laid, or which were at a similar stage of construction, before 1 July 1999 and have not been constructed in compliance with IACS Unified Requirement S20 (Rev. 2, Sept. 2000).

Early completion of a special survey coming due after 1 July 1998 to postpone compliance is not allowed.

The loading in cargo hold No. 1 is not to exceed the allowable hold loading in the flooded condition, calculated as per S22.4, using the loads given in S22.2 and the shear capacity of the double bottom given in S22.3.

In no case, the allowable hold loading in flooding condition is to be taken greater than the design hold loading in intact condition.

## S22.2 - Load model

### S22.2.1 - General

The loads to be considered as acting on the double bottom of hold No. 1 are those given by the external sea pressures and the combination of the cargo loads with those induced by the flooding of hold No. 1.

The most severe combinations of cargo induced loads and flooding loads are to be used, depending on the loading conditions included in the loading manual:
- homogeneous loading conditions;
- non homogeneous loading conditions;
- packed cargo conditions (such as steel mill products).

For each loading condition, the maximum bulk cargo density to be carried is to be considered in calculating the allowable hold limit.

### S22.2.2 - Inner bottom flooding head

The flooding head $h_f$ (see Figure 1) is the distance, in m, measured vertically with the ship in the upright position, from the inner bottom to a level located at a distance $d_f$, in m, from the baseline equal to:
- $D$ in general
- $0,95 \cdot D$ for ships less than 50,000 tonnes deadweight with Type B freeboard.

$D$ being the distance, in m, from the baseline to the freeboard deck at side amidship (see Figure 1).

**Note:**
1. Changes introduced in Rev.2 are to be uniformly implemented by IACS Members and Associates from 1 July 2001.
2. The "contracted for construction" date means the date on which the contract to build the vessel is signed between the prospective owner and the shipbuilder. For further details regarding the date of "contract for construction", refer to IACS Procedural Requirement (PR) No. 29.

## S22.3 - Shear capacity of the double bottom of hold No. 1

The shear capacity $C$ of the double bottom of hold No. 1 is defined as the sum of the shear strength at each end of:
- all floors adjacent to both hoppers, less one half of the strength of the two floors adjacent to each stool, or transverse bulkhead if no stool is fitted (see Figure 2),
- all double bottom girders adjacent to both stools, or transverse bulkheads if no stool is fitted.

The strength of girders or floors which run out and are not directly attached to the boundary stool or hopper girder is to be evaluated for the one end only.

Note that the floors and girders to be considered are those inside the hold boundaries formed by the hoppers and stools (or transverse bulkheads if no stool is fitted). The hopper side girders and the floors directly below the connection of the bulkhead stools (or transverse bulkheads if no stool is fitted) to the inner bottom are not to be included.

When the geometry and/or the structural arrangement of the double bottom are such to make the above assumptions inadequate, to the Society's discretion, the shear capacity $C$ of the double bottom is to be calculated according to the Society's criteria.

In calculating the shear strength, the net thicknesses of floors and girders are to be used. The net thickness $t_{net}$, in mm, is given by:

$$t_{net} = t - t_c$$

where:
- $t$ = as built thickness, in mm, of floors and girders
- $t_c$ = corrosion diminution, equal to 2 mm, in general; a lower value of $t_c$ may be adopted, provided that measures are taken, to the Society's satisfaction, to justify the assumption made.

### S22.3.1 - Floor shear strength

The floor shear strength in way of the floor panel adjacent to hoppers $S_{f1}$, in kN, and the floor shear strength in way of the openings in the "outermost" bay (i.e. that bay which is closest to hopper) $S_{f2}$, in kN, are given by the following expressions:

$$S_{f1} = 10^{-3} \cdot A_f \cdot \frac{\tau_a}{\eta_1}$$

$$S_{f2} = 10^{-3} \cdot A_{f,h} \cdot \frac{\tau_a}{\eta_2}$$

where:
- $A_f$ = sectional area, in mm$^2$, of the floor panel adjacent to hoppers
- $A_{f,h}$ = net sectional area, in mm$^2$, of the floor panels in way of the openings in the "outermost" bay
- $\tau_a$ = allowable shear stress, in N/mm$^2$, to be taken equal to : $\sigma_F / \sqrt{3}$
- $\sigma_F$ = minimum upper yield stress, in N/mm$^2$, of the material
- $\eta_1 = 1,10$
- $\eta_2 = 1,20$. $\eta_2$ may be reduced, at the Society's discretion, down to 1,10 where appropriate reinforcements are fitted to the Society's satisfaction.

### S22.3.2 - Girder shear strength

The girder shear strength in way of the girder panel adjacent to stools (or transverse bulkheads, if no stool is fitted) $S_{g1}$, in kN, and the girder shear strength in way of the largest opening in the "outermost" bay (i.e. that bay which is closest to stool, or transverse bulkhead, if no stool is fitted) $S_{g2}$, in kN, are given by the following expressions:

$$S_{g1} = 10^{-3} \cdot A_g \cdot \frac{\tau_a}{\eta_1}$$

$$S_{g2} = 10^{-3} \cdot A_{g,h} \cdot \frac{\tau_a}{\eta_2}$$

where:
- $A_g$ = minimum sectional area, in mm$^2$, of the girder panel adjacent to stools (or transverse bulkheads, if no stool is fitted)
- $A_{g,h}$ = net sectional area, in mm$^2$, of the girder panel in way of the largest opening in the "outermost" bay
- $\tau_a$ = allowable shear stress, in N/mm$^2$, as given in S22.3.1
- $\eta_1 = 1,10$
- $\eta_2 = 1,15$. $\eta_2$ may be reduced, at the Society's discretion, down to 1,10 where appropriate reinforcements are fitted to the Society's satisfaction.

## S22.4 - Allowable hold loading

The allowable hold loading $W$, in t, is given by:

$$W = \rho_c \cdot V \cdot \frac{1}{F}$$

where:
- $F$ = 1,05 in general; 1,00 for steel mill products
- $\rho_c$ = cargo density, in t/m$^3$; for bulk cargoes see S22.2.1; for steel products, $\rho_c$ is to be taken as the density of steel
- $V$ = volume, in m$^3$, occupied by cargo at a level $h_1$

$$h_1 = \frac{X}{\rho_c \cdot g}$$

- $X$ = for bulk cargoes, the lesser of $X_1$ and $X_2$ given by:

$$X_1 = \frac{Z + \rho \cdot g \cdot (E - h_f)}{1 + \frac{\rho}{\rho_c} (perm - 1)}$$

$$X_2 = Z + \rho \cdot g \cdot (E - h_f \cdot perm)$$

- $X$ = for steel products, $X$ may be taken as $X_1$, using $perm = 0$
- $\rho$ = sea water density, in t/m$^3$
- $g = 9,81$ m/s$^2$, gravity acceleration
- $E = d_f - 0,1 \cdot D$
- $d_f, D$ = as given in S22.2.2
- $h_f$ = flooding head, in m, as defined in S22.2.2
- $perm$ = permeability of cargo, to be taken as 0,3 for ore (corresponding bulk cargo density for iron ore may generally be taken as 3,0 t/m$^3$).
- $Z$ = the lesser of $Z_1$ and $Z_2$ given by:

$$Z_1 = \frac{C_h}{A_{DB,h}}$$

$$Z_2 = \frac{C_e}{A_{DB,e}}$$

- $C_h$ = shear capacity of the double bottom, in kN, as defined in S22.3, considering, for each floor, the lesser of the shear strengths $S_{f1}$ and $S_{f2}$ (see S22.3.1) and, for each girder, the lesser of the shear strengths $S_{g1}$ and $S_{g2}$ (see S22.3.2)
- $C_e$ = shear capacity of the double bottom, in kN, as defined in S22.3, considering, for each floor, the shear strength $S_{f1}$ (see S22.3.1) and, for each girder, the lesser of the shear strengths $S_{g1}$ and $S_{g2}$ (see S22.3.2)

$$A_{DB,h} = \sum_{i=1}^{i=n} S_i \cdot B_{DB,i}$$

$$A_{DB,e} = \sum_{i=1}^{i=n} S_i \cdot (B_{DB} - s)$$

- $n$ = number of floors between stools (or transverse bulkheads, if no stool is fitted)
- $S_i$ = space of $i$-th floor, in m
- $B_{DB,i} = B_{DB} - s$ for floors whose shear strength is given by $S_{f1}$ (see S22.3.1)
- $B_{DB,i} = B_{DB,h}$ for floors whose shear strength is given by $S_{f2}$ (see S22.3.1)
- $B_{DB}$ = breadth of double bottom, in m, between hoppers (see Figure 3)
- $B_{DB,h}$ = distance, in m, between the two considered opening (see Figure 3)
- $s$ = spacing, in m, of double bottom longitudinals adjacent to hoppers

---

![Figure 1: Cross-section of cargo hold No. 1 showing flooding head (hf), cargo height (h1), cargo volume (V), and baseline reference distances (D, df).](Cross-section of cargo hold No. 1 showing flooding head (hf), cargo height (h1), cargo volume (V), and baseline reference distances (D, df).)

![Figure 2: Plan view of the double bottom structure of hold No. 1, indicating lower stool, transverse bulkhead, floors, and girders.](Plan view of the double bottom structure of hold No. 1, indicating lower stool, transverse bulkhead, floors, and girders.)

![Figure 3: Transverse section of the double bottom indicating distances B_DB and B_DB,h.](Transverse section of the double bottom indicating distances B_DB and B_DB,h.)

================================================================================
# FILE: UR_S/ur-s23rev4.md
================================================================================

# S23 Implementation of IACS Unified Requirements S19 and S22 for Existing Single Side Skin Bulk Carriers

**S23**
(1997)
(Rev. 1 1997)
(Rev. 2 April 1998)
(Rev. 2.1 November 1998)
(Rev. 3 Mar. 2002)
(Rev. 3.1 Dec. 2002)
(Rev. 4 Aug 2007)

## S23.1 Application and Implementation Timetable*

a. Unified Requirements S19 and S22 are to be applied in conjunction with the damage stability requirements set forth in S23.2. Compliance is required:

i. for ships which were 20 years of age or more on 1 July 1998, by the due date of the first intermediate, or the due date of the first special survey to be held after 1 July 1998, whichever comes first;

ii. for ships which were 15 years of age or more but less than 20 years of age on 1 July 1998, by the due date of the first special survey to be held after 1 July 1998, but not later than 1 July 2002;

iii. for ships which were 10 years of age or more but less than 15 years of age on 1 July 1998, by the due date of the first intermediate, or the due date of the first special survey to be held after the date on which the ship reaches 15 years of age but not later than the date on which the ship reaches 17 years of age;

iv. for ships which were 5 years of age or more but less than 10 years of age on 1 July 1998, by the due date, after 1 July 2003, of the first intermediate or the first special survey after the date on which the ship reaches 10 years of age, whichever occurs first;

v. for ships which were less than 5 years of age on 1 July 1998, by the date on which the ship reaches 10 years of age.

b. Completion prior to 1 July 2003 of an intermediate or special survey with a due date after 1 July 2003 cannot be used to postpone compliance. However, completion prior to 1 July 2003 of an intermediate survey the window for which straddles 1 July 2003 can be accepted.

## S23.2 Damage Stability

a. Bulk carriers which are subject to compliance with Unified Requirements S19 and S22 shall, when loaded to the summer loadline, be able to withstand flooding of the foremost cargo hold in all loading conditions and remain afloat in a satisfactory condition of equilibrium, as specified in SOLAS regulation XII/4.3 to 4.7.

b. A ship having been built with an insufficient number of transverse watertight bulkheads to satisfy this requirement may be exempted from the application of Unified Requirements S19, S22 and this requirement provided the ship fulfills the requirement in SOLAS regulation XII/9.

---
\* See Annex for details.

IACS Req. 1997/Rev.4 2007 S23-1

---

# Annex

**S23 cont'd**

### 1. Surveys to be held
The term "survey to be held" is interpreted to mean that the survey is "being held" until it is "completed".

### 2. Due dates and completion allowance
2.1 intermediate survey:
2.1.1 Intermediate survey carried out either at the second or third annual survey: 3 months after the due date (i.e. 2nd or 3rd anniversary) can be used to carry out and complete the survey;
2.1.2 Intermediate survey carried out between the second and third annual survey: 3 months after the due date of the 3rd Annual Survey can be used to carry out and complete the survey;
2.2 special survey: 3 months extension after the due date may be allowed subject to the terms/conditions of PR4;
2.3 ships controlled by "1 July 2002": same as for special survey;
2.4 ships controlled by "age 15 years" or "age 17 years": same as for special survey.

### 3. Intermediate Survey Interpretations/Applications
3.1 If the 2nd anniversary is prior to or on 1 July 1998 and the intermediate survey is completed prior to or on 1 July 1998, the ship need not comply until the next special survey.
3.2 If the 2nd anniversary is prior to or on 1 July 1998 and the intermediate survey is completed within the window of the 2nd annual survey but after 1 July 1998, the ship need not comply until the next special survey.
3.3 If the 2nd anniversary is prior to or on 1 July 1998 and the intermediate survey is completed outside the window of the 2nd annual survey and after 1 July 1998, it is taken that the intermediate survey is held after 1 July 1998 and between the second and third annual surveys. Therefore, the ship shall comply no later than 3 months after the 3rd anniversary.
3.4 If the 2nd anniversary is after 1 July 1998 and the intermediate survey is completed within the window of the 2nd annual survey but prior to or on 1 July 1998, the ship need not comply until the next special survey.
3.5 If the 3rd anniversary is prior to or on 1 July 1998 and the intermediate survey is completed prior to or on 1 July 1998, the ship need not comply until the next special survey.
3.6 If the 3rd anniversary is prior to or on 1 July 1998 and the intermediate survey is completed within the window of the 3rd annual survey but after 1 July 1998, the ship need not comply until the next special survey.
3.7 If the 3rd anniversary is after 1 July 1998 and the intermediate survey is completed within the window prior to or on 1 July 1998, the ship need not comply until the next special survey.

### 4. Special Survey Interpretations/Applications
4.1 If the due date of a special survey is after 1 July 1998 and the special survey is completed within the 3 month window prior to the due date and prior to or on 1 July 1998, the ship need not comply until the next relevant survey (i.e. special survey for ships under 20 years of age on 1 July 1998, intermediate survey for ships 20 years of age or more on 1 July 1998).

### 5. Early Completion of an Intermediate Survey (coming due after 1 July 1998 to postpone compliance is not allowed):
5.1 Early completion of an intermediate survey means completion of the survey prior to the opening of the window (i.e. completion more than 3 months prior to the 2nd anniversary since the last special survey).
5.2 The intermediate survey may be completed early and credited from the completion date but in such a case the ship will still be required to comply not later than 3 months after the 3rd anniversary.

### 6. Early Completion of a Special Survey (coming due after 1 July 1998 to postpone compliance is not allowed):
6.1 Early completion of a special survey means completion of the survey more than 3 months prior to the due date of the special survey.
6.2 The special survey may be completed early and credited from the completion date, but in such a case the ship will still be required to comply by the due date of the special survey.

IACS Req. 1997/Rev.4 2007 S23-2

================================================================================
# FILE: UR_S/ur-s24del.md
================================================================================

# S24

**S24**
(September 1998)
(Deleted Jan 2004)

## Detection of Water Ingress into Cargo Holds of Bulk Carriers

URS24 superceded by UI SC 179 and SC 180

Deleted on 1 January 2004

***

S24-1
IACS Req. 1998

================================================================================
# FILE: UR_S/ur-s25del.md
================================================================================

# S25 Harmonised Notations and Corresponding Design Loading Conditions for Bulk Carriers

**S25**
(June 2002)
(Rev.1 Feb 2003)
(Corr.1 May 2004)
(Rev.2 July 2004)

Deleted May 2010.

***

**End of Document**

**Page 1 of 1**
**IACS Req. 2002/Rev.2 2004**

================================================================================
# FILE: UR_S/ur-s26rev5.md
================================================================================

S26
(Nov 2002)
(Rev.1 Nov 2003)
(Rev.2 July 2004)
(Rev.3 Aug 2006)
(Rev.4 May 2010)
(Rev.5 May 2023)

# S26 Strength and Securing of Small Hatches on the Exposed Fore Deck

## 1. General

1.1 The strength of, and securing devices for, small hatches fitted on the exposed fore deck are to comply with the requirements of this UR.

1.2 Small hatches in the context of this UR are hatches designed for access to spaces below the deck and are capable of being closed weather-tight or watertight, as applicable. Their opening is normally 2.5 square metres or less.

1.3 Hatches designed for emergency escape need not comply with the requirements 5.1 (i) and (ii), 6.3 and 7 of this UR.

1.4 Securing devices of hatches designed for emergency escape are to be of a quick-acting type (e.g., one action wheel handles are provided as central locking devices for latching/unlatching of hatch cover) operable from both sides of the hatch cover.

## 2. Application

2.1 For ships that are contracted for construction on or after 1 January 2004 on the exposed deck over the forward 0.25L, applicable to:

All ship types of sea going service of length 80 m or more, where the height of the exposed deck in way of the hatch is less than 0.1L or 22 m above the summer load waterline, whichever is the lesser.

2.2 For ships that are contracted for construction prior to 1 January 2004 only for hatches on the exposed deck giving access to spaces forward of the collision bulkhead, and to spaces which extend over this line aft-wards, applicable to:

Bulk carriers, ore carriers, and combination carriers (as defined in UR Z11) and general dry cargo ships (excluding container vessels, vehicle carriers, Ro-Ro ships and woodchip carriers), of length 100 m or more.

2.3 The ship length L is as defined in UR S2.

2.4 This UR does not apply to CSR Bulk Carriers and Oil Tankers.

2.5 This UR does not apply to small hatches on container ship giving access to a cargo hold which comply with UI LL64 except the requirement of clause 4 & 5. Such hatch covers are considered non-weathertight regardless of whether it is actually weathertight or not.

However, for scantlings of small hatches, the strength requirements in clause 4 of this UR could be applied instead of clause 6 of UI LL64.

**Note:**
1. The "contracted for construction" date means the date on which the contract to build the vessel is signed between the prospective owner and the shipbuilder. For further details regarding the date of "contract for construction", refer to IACS PR No. 29.
2. Changes introduced in Rev.5 are to be uniformly implemented by IACS Members for ships contracted for construction on or after 1 July 2024.

## 3. Implementation * (see footnote)

3.1 Ships that are described in paragraph 2.1 that are contracted for construction on or after 1 January 2004 are to comply by the time of delivery.

3.2 Ships described in paragraph 2.2 that are contracted for construction prior to 1 January 2004 are to comply:

i) for ships which will be 15 years of age or more on 1 January 2004 by the due date of the first intermediate or special survey after that date;

ii) for ships which will be 10 years of age or more on 1 January 2004 by the due date of the first special survey after that date;

iii) for ships which will be less than 10 years of age on 1 January 2004 by the date on which the ship reaches 10 years of age.

## 4. Strength

4.1 For small rectangular steel hatch covers, the plate thickness, stiffener arrangement and scantlings are to be in accordance with Table 1, and Figure 1. Stiffeners, where fitted, are to be aligned with the metal-to-metal contact points, required in 6.1, see Figure 1. Primary stiffeners are to be continuous. All stiffeners are to be welded to the inner edge stiffener, see Figure 2.

4.2 The upper edge of the hatchway coamings is to be suitably reinforced by a horizontal section, normally not more than 170 to 190 mm from the upper edge of the coamings.

4.3 For small hatch covers of circular or similar shape, the cover plate thickness and reinforcement is to be according to the requirements of each Society.

4.4 For small hatch covers constructed of materials other than steel, the required scantlings are to provide equivalent strength.

\* The requirements in 1.4, introduced in Rev. 3 of this UR, are to be uniformly applied by IACS Members and Associates:

(a) to new vessels, contracted for construction on or after 1 July 2007, by the time of delivery;

(b) to vessels contracted for construction prior to 1 July 2007, by the compliance date specified in Section 3 of this UR, or by the due date of the first special survey after 1 July 2007, whichever is later. Completion prior to 1 July 2007 of a special survey with a due date after 1 July 2007 cannot be used to postpone compliance.

## 5. Primary Securing Devices

5.1 Small hatches located on exposed fore deck subject to the application of this UR are to be fitted with primary securing devices such that their hatch covers can be secured in place and weather-tight by means of a mechanism employing any one of the following methods:

i) Butterfly nuts tightening onto forks (clamps),

ii) Quick acting cleats, or

iii) Central locking device.

5.2 Dogs (twist tightening handles) with wedges are not acceptable.

## 6. Requirements for Primary Securing

6.1 The hatch cover is to be fitted with a gasket of elastic material. This is to be designed to allow a metal to metal contact at a designed compression and to prevent over compression of the gasket by green sea forces that may cause the securing devices to be loosened or dislodged. The metal-to-metal contacts are to be arranged close to each securing device in accordance with Figure 1, and of sufficient capacity to withstand the bearing force.

6.2 The primary securing method is to be designed and manufactured such that the designed compression pressure is achieved by one person without the need of any tools.

6.3 For a primary securing method using butterfly nuts, the forks (clamps) are to be of robust design. They are to be designed to minimize the risk of butterfly nuts being dislodged while in use; by means of curving the forks upward, a raised surface on the free end, or a similar method. The plate thickness of unstiffened steel forks is not to be less than 16 mm. An example arrangement is shown in Figure 2.

6.4 For small hatch covers located on the exposed deck forward of the fore-most cargo hatch, the hinges are to be fitted such that the predominant direction of green sea will cause the cover to close, which means that the hinges are normally to be located on the fore edge.

6.5 On small hatches located between the main hatches, for example between Nos. 1 and 2, the hinges are to be placed on the fore edge or outboard edge, whichever is practicable for protection from green water in beam sea and bow quartering conditions.

## 7. Secondary Securing Device

Small hatches on the fore deck are to be fitted with an independent secondary securing device e.g. by means of a sliding bolt, a hasp or a backing bar of slack fit, which is capable of keeping the hatch cover in place, even in the event that the primary securing device became loosened or dislodged. It is to be fitted on the side opposite to the hatch cover hinges.

### Table 1: Scantlings for Small Steel Covers on the Fore Deck

| Nominal size (mm x mm) | Cover plate thickness (mm) | Primary stiffeners Flat Bar (mm x mm); number | Secondary stiffeners Flat Bar (mm x mm); number |
| :--- | :---: | :--- | :--- |
| 630 x 630 | 8 | - | - |
| 630 x 830 | 8 | 100 x 8 ; 1 | - |
| 830 x 630 | 8 | 100 x 8 ; 1 | - |
| 830 x 830 | 8 | 100 x 10 ; 1 | - |
| 1030 x 1030 | 8 | 120 x 12 ; 1 | 80 x 8 ; 2 |
| 1330 x 1330 | 8 | 150 x 12 ; 2 | 100 x 10 ; 2 |

![Figure 1: Arrangement of Stiffeners](Technical diagrams showing six different rectangular hatch cover configurations (nominal sizes 630x630, 630x830, 830x630, 830x830, 1030x1030, and 1330x1330) illustrating the placement of hinges, securing devices/metal-to-metal contact points, primary stiffeners (dashed lines), and secondary stiffeners (dash-dot lines).)

**Legend for Figure 1:**
- — Hinge
- ● Securing device / metal to metal contact
- \-\-\-\-\- Primary stiffener
- \-\-\cdot\-\-\cdot\- Secondary stiffener

![Figure 2: Example of a Primary Securing Device](A detailed cross-sectional technical diagram of a primary securing device for a hatch cover. It shows a butterfly nut (1) and bolt (2) assembly passing through a fork (clamp) plate (5) to secure the hatch cover (6) onto a hatch coaming (8). A gasket (7) is shown between the cover and coaming. Other parts include a pin (3), center of pin (4), a bearing pad (9) for metal-to-metal contact, a stiffener (10), and an inner edge stiffener (11). Dimensions are indicated in millimeters, including a 20mm offset for the pin and a minimum 16mm thickness for the fork plate.)

**Legend for Figure 2:**
1: butterfly nut
2: bolt
3: pin
4: center of pin
5: fork (clamp) plate
6: hatch cover
7: gasket
8: hatch coaming
9: bearing pad welded on the bracket of a toggle bolt for metal to metal contact
10: stiffener
11: inner edge stiffener

*(Note: Dimensions in millimeters)*

**End of Document**


================================================================================
# FILE: UR_S/ur-s27rev6.md
================================================================================

# S27 Strength Requirements for Fore Deck Fittings and Equipment

(Nov 2002)
(Rev.1 March 2003)
(Corr.1 July 2003)
(Rev.2 Nov 2003)
(Rev.3 July 2004)
(Rev.4 Nov 2004)
(Rev.5 May 2010)
(Rev.6 June 2013)

## 1. General

1.1 This UR S 27 provides strength requirements to resist green sea forces for the following items located within the forward quarter length:

air pipes, ventilator pipes and their closing devices, the securing of windlasses.

1.2 For windlasses, these requirements are additional to those appertaining to the anchor and chain performance criteria of each Society.

1.3 Where mooring winches are integral with the anchor windlass, they are to be considered as part of the windlass.

## 2. Application

2.1 For ships that are contracted for construction on or after 1 January 2004 on the exposed deck over the forward 0.25L, applicable to:

All ship types of sea going service of length 80 m or more, where the height of the exposed deck in way of the item is less than 0.1L or 22 m above the summer load waterline, whichever is the lesser.

2.2 For ships that are contracted for construction prior to 1 January 2004 only for air pipes, ventilator pipes and their closing devices on the exposed deck serving spaces forward of the collision bulkhead, and to spaces which extend over this line aft-wards, applicable to:

Bulk carriers, ore carriers, and combination carriers (as defined in UR Z11) and general dry cargo ships (excluding container vessels, vehicle carriers, Ro-Ro ships and woodchip carriers), of length 100m or more.

2.3 The ship length L is as defined in UR S2.

2.4 This UR does not apply to CSR Oil Tankers.

2.5 The requirements of this UR concerning windlasses do not apply to CSR Bulk Carriers.

**Note:**

1. The "contracted for construction" date means the date on which the contract to build the vessel is signed between the prospective owner and the shipbuilder. For further details regarding the date of "contract for construction", refer to IACS Procedural Requirement (PR) No. 29.
2. This UR does not apply to the cargo tank venting systems and the inert gas systems of tankers.
3. The changes introduced in Rev.6 apply to ships contracted for construction from 1 July 2014.

---

## 3. Implementation

3.1 Ships that are described in paragraph 2.1 that are contracted for construction on or after 1 January 2004 are to comply by the time of delivery.

3.2 Ships described in paragraph 2.2 that are contracted for construction prior to 1 January 2004 are to comply:

i) for ships which will be 15 years of age or more on 1 January 2004 by the due date of the first intermediate or special survey after that date;

ii) for ships which will be 10 years of age or more on 1 January 2004 by the due date of the first special survey after that date;

iii) for ships which will be less than 10 years of age on 1 January 2004 by the date on which the ship reaches 10 years of age.

Completion prior to 1 January 2004 of an intermediate or special survey with a due date after 1 January 2004 cannot be used to postpone compliance.
However, completion prior to 1 January 2004 of an intermediate survey the window for which straddles 1 January 2004 can be accepted.

## 4. Applied Loading

### 4.1 Air pipes, ventilator pipes and their closing devices

4.1.1 The pressures $p$, in kN/m² acting on air pipes, ventilator pipes and their closing devices may be calculated from:

$$p = 0.5 \rho V^2 C_d C_s C_p$$

where:

$\rho$ = density of sea water (1.025 t/m³)
$V$ = velocity of water over the fore deck
= 13.5 m/sec for $d \le 0.5 d_1$
= $13.5 \sqrt{2(1 - \frac{d}{d_1})}$ m/sec for $0.5 d_1 < d < d_1$
$d$ = distance from summer load waterline to exposed deck
$d_1$ = 0.1L or 22 m whichever is the lesser
$C_d$ = shape coefficient
= 0.5 for pipes, 1.3 for air pipe or ventilator heads in general, 0.8 for an air pipe or ventilator head of cylindrical form with its axis in the vertical direction.
$C_s$ = slamming coefficient (3.2)
$C_p$ = protection coefficient:
(0.7) for pipes and ventilator heads located immediately behind a breakwater or forecastle,
(1.0) elsewhere and immediately behind a bulwark.

4.1.2 Forces acting in the horizontal direction on the pipe and its closing device may be calculated from 4.1.1 using the largest projected area of each component.

---

### 4.2 Windlasses

4.2.1 The following pressures and associated areas are to be applied (see Figure 1):

- 200 kN/m² normal to the shaft axis and away from the forward perpendicular, over the projected area in this direction,
- 150 kN/m² parallel to the shaft axis and acting both inboard and outboard separately, over the multiple of $f$ times the projected area in this direction,
where $f$ is defined as:
$f = 1 + B/H$, but not greater than 2.5

where:
$B$ = width of windlass measured parallel to the shaft axis,
$H$ = overall height of windlass.

4.2.2 Forces in the bolts, chocks and stoppers securing the windlass to the deck are to be calculated. The windlass is supported by $N$ bolt groups, each containing one or more bolts, see Figure 2.

4.2.3 The axial force $R_i$ in bolt group (or bolt) $i$, positive in tension, may be calculated from:

$$R_{xi} = P_x h x_i A_i / I_x$$
$$R_{yi} = P_y h y_i A_i / I_y$$

and $R_i = R_{xi} + R_{yi} - R_{si}$

where:

$P_x$ = force (kN) acting normal to the shaft axis
$P_y$ = force (kN) acting parallel to the shaft axis, either inboard or outboard whichever gives the greater force in bolt group $i$
$h$ = shaft height above the windlass mounting (cm)
$x_i, y_i$ = $x$ and $y$ coordinates of bolt group $i$ from the centroid of all $N$ bolt groups, positive in the direction opposite to that of the applied force (cm)
$A_i$ = cross sectional area of all bolts in group $i$ (cm²)
$I_x = \sum A_i x_i^2$ for $N$ bolt groups
$I_y = \sum A_i y_i^2$ for $N$ bolt groups
$R_{si}$ = static reaction at bolt group $i$, due to weight of windlass.

4.2.4 Shear forces $F_{xi}, F_{yi}$ applied to the bolt group $i$, and the resultant combined force $F_i$ may be calculated from:

$$F_{xi} = (P_x - \alpha g M) / N$$
$$F_{yi} = (P_y - \alpha g M) / N$$

and

$$F_i = (F_{xi}^2 + F_{yi}^2)^{0.5}$$

where:

$\alpha$ = coefficient of friction (0.5)
$M$ = mass of windlass (tonnes)
$g$ = gravity acceleration (9.81 m/sec²)
$N$ = number of bolt groups.

4.2.5 Axial tensile and compressive forces in 4.2.3 and lateral forces in 4.2.4 are also to be considered in the design of the supporting structure.

## 5. Strength Requirements

### 5.1 Air pipes, ventilator pipes and their closing devices

5.1.1 These requirements are additional to IACS Unified Requirement P3 and Unified Interpretation LL36 (Footnote *).

5.1.2 Bending moments and stresses in air and ventilator pipes are to be calculated at critical positions: at penetration pieces, at weld or flange connections, at toes of supporting brackets. Bending stresses in the net section are not to exceed $0.8\sigma_y$, where $\sigma_y$ is the specified minimum yield stress or 0.2% proof stress of the steel at room temperature. Irrespective of corrosion protection, a corrosion addition to the net section of 2.0 mm is then to be applied.

5.1.3 For standard air pipes of 760 mm height closed by heads of not more than the tabulated projected area, pipe thicknesses and bracket heights are specified in Table 1. Where brackets are required, three or more radial brackets are to be fitted. Brackets are to be of gross thickness 8 mm or more, of minimum length 100 mm, and height according to Table 1 but need not extend over the joint flange for the head. Bracket toes at the deck are to be suitably supported.

5.1.4 For other configurations, loads according to 4.1 are to be applied, and means of support determined in order to comply with the requirements of 5.1.2. Brackets, where fitted, are to be of suitable thickness and length according to their height. Pipe thickness is not to be taken less than as indicated in IACS UI LL36.

5.1.5 For standard ventilators of 900 mm height closed by heads of not more than the tabulated projected area, pipe thicknesses and bracket heights are specified in Table 2. Brackets, where required are to be as specified in 5.1.3.

5.1.6 For ventilators of height greater than 900 mm, brackets or alternative means of support are to be fitted according to the requirements of each Society. Pipe thickness is not to be taken less than as indicated in IACS UI LL36.

5.1.7 All component parts and connections of the air pipe or ventilator are to be capable of withstanding the loads defined in 4.1.

5.1.8 Rotating type mushroom ventilator heads are unsuitable for application in the areas defined in 2.

### 5.2 Windlass Mounts

5.2.1 Tensile axial stresses in the individual bolts in each bolt group $i$ are to be calculated. The horizontal forces $F_{xi}$ and $F_{yi}$ are normally to be reacted by shear chocks. Where "fitted" bolts are designed to support these shear forces in one or both directions, the von Mises equivalent stresses in the individual bolts are to be calculated, and compared to the stress under proof load. Where pour-able resins are incorporated in the holding down arrangements, due account is to be taken in the calculations.

The safety factor against bolt proof strength is to be not less than 2.0.

5.2.2 The strength of above deck framing and hull structure supporting the windlass and its securing bolt loads as defined in 4.2 is to be according to the requirements of each Society.

**Footnote \*:** This does not mean that closing devices of air pipes on all existing ships subject to S27 need to be upgraded to comply with UR P3.

---

### Table 1: 760 mm Air Pipe Thickness and Bracket Standards

| Nominal pipe diameter (mm) | Minimum fitted gross thickness, LL36(c) (mm) | Maximum projected area of head (cm²) | Height (1) of brackets (mm) |
| :--- | :--- | :--- | :--- |
| 40A (3) | 6.0 | - | 520 |
| 50A (3) | 6.0 | - | 520 |
| 65A | 6.0 | - | 480 |
| 80A | 6.3 | - | 460 |
| 100A | 7.0 | - | 380 |
| 125A | 7.8 | - | 300 |
| 150A | 8.5 | - | 300 |
| 175A | 8.5 | - | 300 |
| 200A | 8.5 (2) | 1900 | 300 (2) |
| 250A | 8.5 (2) | 2500 | 300 (2) |
| 300A | 8.5 (2) | 3200 | 300 (2) |
| 350A | 8.5 (2) | 3800 | 300 (2) |
| 400A | 8.5 (2) | 4500 | 300 (2) |

(1) Brackets (see 5.1.3) need not extend over the joint flange for the head.
(2) Brackets are required where the as fitted (gross) thickness is less than 10.5 mm, or where the tabulated projected head area is exceeded.
(3) Not permitted for new ships - reference UR P1.
**Note:** For other air pipe heights, the relevant requirements of section 5 are to be applied.

---

### Table 2: 900 mm Ventilator Pipe Thickness and Bracket Standards

| Nominal pipe diameter (mm) | Minimum fitted gross thickness, LL36(c) (mm) | Maximum projected area of head (cm²) | Height of brackets (mm) |
| :--- | :--- | :--- | :--- |
| 80A | 6.3 | - | 460 |
| 100A | 7.0 | - | 380 |
| 150A | 8.5 | - | 300 |
| 200A | 8.5 | 550 | - |
| 250A | 8.5 | 880 | - |
| 300A | 8.5 | 1200 | - |
| 350A | 8.5 | 2000 | - |
| 400A | 8.5 | 2700 | - |
| 450A | 8.5 | 3300 | - |
| 500A | 8.5 | 4000 | - |

**Note:** For other ventilator heights, the relevant requirements of section 5 are to be applied.

---

![Figure 1: Direction of Forces and Weight](Side and top view diagrams of a windlass. The side view shows the overall height H, the shaft height h, and force vectors Px (horizontal) and W (vertical weight). The top view shows the width B, the center line of the vessel, the center line of the windlass at an angle, and force vectors Px (normal to shaft) and Py (parallel to shaft).)

![Figure 2: Sign Convention](Perspective diagram showing the windlass base on the deck. It illustrates the coordinate system (xi, yi) relative to the centroid of bolt groups. Force vectors Px and Py are shown applied to the windlass. Bolt groups are identified with coordinates like x3(-ve), y3(+ve), x1(+ve), y1(+ve), etc.)

**End of Document**


================================================================================
# FILE: UR_S/ur-s28rev3.md
================================================================================

# S28 Requirements for the Fitting of a Forecastle for Bulk Carriers, Ore Carriers and Combination Carriers

**S28**
(May 2003)
(Rev.1 July 2004)
(Rev.2 Sept 2005)
(Rev.3 May 2010)

### S28.1 Application and definitions

These requirements apply to all bulk carriers, ore carriers and combination carriers, as defined in UR Z11, which are contracted for construction on or after 1 January 2004.

Such ships are to be fitted with an enclosed forecastle on the freeboard deck.

The required dimensions of the forecastle are defined in S28.2.

The structural arrangements and scantlings of the forecastle are to comply with the relevant Society's requirements.

This UR does not apply to CSR Bulk Carriers.

### S28.2 Dimensions

The forecastle is to be located on the freeboard deck with its aft bulkhead fitted in way or aft of the forward bulkhead of the foremost hold, as shown in Figure 1.

However, if this requirement hinders hatch cover operation, the aft bulkhead of the forecastle may be fitted forward of the forward bulkhead of the foremost cargo hold provided the forecastle length is not less than 7% of ship length abaft the forward perpendicular where the ship length and forward perpendicular are defined in the International Convention on Load Line 1966 and its Protocol 1988.

The forecastle height $H_F$ above the main deck is to be not less than:

- the standard height of a superstructure as specified in the International Convention on Load Line 1966 and its Protocol of 1988, or
- $H_C + 0.5$ m, where $H_C$ is the height of the forward transverse hatch coaming of cargo hold No.1,

whichever is the greater.

All points of the aft edge of the forecastle deck are to be located at a distance $\ell_F$:

$$\ell_F \le 5\sqrt{H_F - H_C}$$

from the hatch coaming plate in order to apply the reduced loading to the No.1 forward transverse hatch coaming and No.1 hatch cover in applying S21.4.1 and S21.5.2, respectively, of UR S21(Rev.3).

A breakwater is not to be fitted on the forecastle deck with the purpose of protecting the hatch coaming or hatch covers. If fitted for other purposes, it is to be located such that its upper edge at centre line is not less than $H_B / \tan 20^\circ$ forward of the aft edge of the forecastle deck, where $H_B$ is the height of the breakwater above the forecastle (see Figure 1).

#### Figure 1

![Diagram showing relationship between hatch coaming height Hc, forecastle height Hf, distance lf, and breakwater height Hb](https://raw.githubusercontent.com/iacs-docs/images/main/s28_fig1.png)
*(Note: Figure 1 illustrates the vertical and horizontal dimensions of the forecastle and hatch coaming relative to the forward bulkhead.)*

---

**Note:**

1. The "contracted for construction" date means the date on which the contract to build the vessel is signed between the prospective owner and the shipbuilder. For further details regarding the date of "contract for construction", refer to IACS Procedural Requirement (PR) No. 29.


================================================================================
# FILE: UR_S/ur-s2rev2.md
================================================================================

# S2 Definition of Ship's Length L and of Block Coefficient $C_b$

**S2**
(1973)
(Rev.1 May 2010)
(Rev.2 June 2019)

### S2.0 Application
This UR does not apply to CSR Bulk Carriers and Oil Tankers.

### S2.1 Rule length $L$
The Rule length $L$ is the distance, in metres, measured on the waterline at the scantling draught from the fore side of the stem to the after side of the rudder post, or the centre of the rudder stock if there is no rudder post. $L$ is not to be less than 96%, and need not be greater than 97%, of the extreme length on the waterline at the scantling draught.

In ships without rudder stock (e.g. ships fitted with azimuth thrusters), the Rule length $L$ is to be taken equal to 97% of the extreme length on the waterline at the scantling draught.

In ships with unusual stern and bow arrangement the Rule length $L$ will be specially considered.

### S2.2 Block coefficient $C_b$
The block coefficient $C_b$ is the moulded block coefficient corresponding to the waterline at the scantling draught $Ts$, based on rule length $L$ and moulded breadth $B$:

$$C_b = \frac{\text{Moulded displacement } [m^3] \text{ at scantling draught } Ts}{L \cdot B \cdot Ts}$$

**Where:**
**B** : Greatest moulded breadth, in m, measured amidships at the scantling draught, $Ts$.
**Ts** : Scantling draught, in m, at which the strength requirements for the scantlings of the ship are met and represents the full load condition. The scantling draught is to be not less than that corresponding to the assigned freeboard.

***

**Note:**
1. Changes introduced in Rev.2 are to be uniformly implemented by IACS Members from 1 July 2020.

**End of Document**

***
**Page 1 of 1 | IACS Req. 1973/Rev.2 2019**


================================================================================
# FILE: UR_S/ur-s30corr1.md
================================================================================

# S30 Cargo Hatch Cover Securing Arrangements for Bulk Carriers not Built in accordance with UR S21 (Rev.3)

**S30**
(Jan 2003)
(Corr.1 May 2003)
(Rev.1 Aug 2003)
(Corr.1 Mar 2019)

## 1. Application and Implementation

1.1 These requirements apply to all bulk carriers, as defined in UR Z11.2.2, which were not built in accordance with UR S21(Rev.3) and are for steel hatch cover securing devices and stoppers for cargo hold hatchways No.1 and No.2 which are wholly or partially within 0.25L of the fore perpendicular, except pontoon type hatch cover.

1.2 All bulk carriers not built in accordance with UR S21 (Rev.3) are to comply with the requirements of this UR in accordance with the following schedule:

i. For ships which will be 15 years of age or more on 1 January 2004 by the due date of the first intermediate or special survey after that date;
ii. For ships which will be 10 years of age or more on 1 January 2004 by the due date of the first special survey after that date;
iii. For ships which will be less than 10 years of age on 1 January 2004 by the date on which the ship reaches 10 years of age.

1.3 Completion prior to 1 January 2004 of an intermediate or special survey with a due date after 1 January 2004 cannot be used to postpone compliance. However, completion prior to 1 January 2004 of an intermediate survey the window for which straddles 1 January 2004 can be accepted.

1.4 This UR is not applicable to self-unloading bulk carriers.

## 2. Securing Devices

2.1 The strength of securing devices is to comply with the following requirements:

2.1.1 Panel hatch covers are to be secured by appropriate devices (bolts, wedges or similar) suitably spaced alongside the coamings and between cover elements.

Arrangement and spacing are to be determined with due attention to the effectiveness for weather-tightness, depending upon the type and the size of the hatch cover, as well as on the stiffness of the cover edges between the securing devices.

2.1.2 The net sectional area of each securing device is not to be less than:

$$A = 1.4 \cdot a / f \text{ (cm}^2\text{)}$$

where:
$a$ = spacing between securing devices not to be taken less than 2 meters
$f$ = $(\sigma_Y / 235)^e$
$\sigma_Y$ = specified minimum upper yield stress in N/mm² of the steel used for fabrication, not to be taken greater than 70% of the ultimate tensile strength.
$e$ = 0.75 for $\sigma_Y > 235$
  = 1.0 for $\sigma_Y \le 235$

Rods or bolts are to have a net diameter not less than 19 mm for hatchways exceeding 5 m² in area.

2.1.3 Between cover and coaming and at cross-joints, a packing line pressure sufficient to obtain weathertightness is to be maintained by the securing devices.

For packing line pressures exceeding 5 N/mm, the cross section area is to be increased in direct proportion. The packing line pressure is to be specified.

2.1.4 The cover edge stiffness is to be sufficient to maintain adequate sealing pressure between securing devices. The moment of inertia, I, of edge elements is not to be less than:

$$I = 6 \cdot p \cdot a^4 \text{ (cm}^4\text{)}$$

where:
$p$ = packing line pressure in N/mm, minimum 5 N/mm
$a$ = spacing in m of securing devices.

2.1.5 Securing devices are to be of reliable construction and securely attached to the hatchway coamings, decks or covers. Individual securing devices on each cover are to have approximately the same stiffness characteristics.

2.1.6 Where rod cleats are fitted, resilient washers or cushions are to be incorporated.

2.1.7 Where hydraulic cleating is adopted, a positive means is to be provided to ensure that it remains mechanically locked in the closed position in the event of failure of the hydraulic system.

## 3. Stoppers

3.1 No. 1 and 2 hatch covers are to be effectively secured, by means of stoppers, against the transverse forces arising from a pressure of 175 kN/m².

3.2 No. 2 hatch covers are to be effectively secured, by means of stoppers, against the longitudinal forces acting on the forward end arising from a pressure of 175 kN/m².

3.3 No. 1 hatch cover is to be effectively secured, by means of stoppers, against the longitudinal forces acting on the forward end arising from a pressure of 230 kN/m². This pressure may be reduced to 175 kN/m² if a forecastle is fitted.

3.4 The equivalent stress:
i. in stoppers and their supporting structures, and
ii. calculated in the throat of the stopper welds is not to exceed the allowable value of $0.8 \sigma_Y$

## 4. Materials and Welding

Where stoppers or securing devices are fitted to comply with this UR, they are to be manufactured of materials, including welding electrodes, meeting relevant IACS requirements.


================================================================================
# FILE: UR_S/ur-s31rev4.md
================================================================================

# S 31 Renewal Criteria for Side Shell Frames and Brackets in Single Side Skin Bulk Carriers and Single Side Skin OBO Carriers not Built in accordance with UR S12 Rev.1 or subsequent revisions

(Nov. 2002) (Rev.1 June 2003) (Corr.1 July 2003) (Corr.2 Nov. 2003) (Corr.3 Jan 2004) (Rev.2 July 2004) (Rev.3 Nov. 2005) (Rev.4 Apr 2007)

## S31.1 Application and definitions

These requirements apply to the side shell frames and brackets of cargo holds bounded by the single side shell of bulk carriers constructed with single deck, topside tanks and hopper tanks in cargo spaces intended primarily to carry dry cargo in bulk, which were not built in accordance with UR S12 Rev. 1 or subsequent revisions.

In addition, these requirements also apply to the side shell frames and brackets of cargo holds bounded by the single side shell of Oil/Bulk/Ore(OBO) carriers, as defined in UR Z11 but of single side skin construction.

In the case a vessel as defined above does not satisfy above definition in one or more holds, the requirements in UR S31 do not apply to these individual holds.

For the purpose of this UR, "ships" means both "bulk carriers" and "OBO carriers" as defined above, unless otherwise specified.

**Bulk Carriers** subject to these requirements are to be assessed for compliance with the requirements of this UR and steel renewal, reinforcement or coating, where required in accordance with this UR, is to be carried out in accordance with the following schedule and at subsequent intermediate and special surveys.

i. For bulk carriers which will be 15 years of age or more on 1 January 2004 by the due date of the first intermediate or special survey after that date;

ii. For bulk carriers which will be 10 years of age or more on 1 January 2004 by the due date of the first special survey after that date;

iii. For bulk carriers which will be less than 10 years of age on 1 January 2004 by the date on which the ship reaches 10 years of age.

Completion prior to 1 January 2004 of an intermediate or special survey with a due date after 1 January 2004 cannot be used to postpone compliance. However, completion prior to 1 January 2004 of an intermediate survey the window for which straddles 1 January 2004 can be accepted.

**Note:**
1. This UR is to be applied to bulk carriers and OBO carriers of single side skin construction, as defined above, in conjunction with UR Z10.2 (Rev.15, 2003 and Corr.1, 2004). Z10.2.1.1.5 refers.
2. The changes introduced in Rev.3 are to be applied by IACS Members and Associates not later than on assessments for compliance commenced on or after 1 July 2006.
3. The changes introduced in Rev.4 are to be applied by IACS Members and Associates not later than on assessments for compliance commenced on or after 1 July 2008.

**OBO carriers** subject to these requirements are to be assessed for compliance with the requirements of this UR and steel renewal, reinforcement or coating, where required in accordance with this UR, is to be carried out in accordance with the following schedule and at subsequent intermediate and special surveys.

i. For OBO carriers which will be 15 years of age or more on 1 July 2005 by the due date of the first intermediate or special survey after that date;

ii. For OBO carriers which will be 10 years of age or more on 1 July 2005 by the due date of the first special survey after that date;

iii. For OBO carriers which will be less than 10 years of age on 1 July 2005 by the date on which the ship reaches 10 years of age.

Completion prior to 1 July 2005 of an intermediate or special survey with a due date after 1 July 2005 cannot be used to postpone compliance. However, completion prior to 1 July 2005 of an intermediate survey the window for which straddles 1 July 2005 can be accepted.

These requirements define steel renewal criteria or other measures to be taken for the webs and flanges of side shell frames and brackets as per S31.2.

Reinforcing measures of side frames are also defined as per S31.2.3.

Finite element or other numerical analysis or direct calculation procedures cannot be used as an alternative to compliance with the requirements of this UR, except in cases of unusual side structure arrangements or framing to which the requirements of this UR cannot be directly applied. In such cases, the analysis criteria and the strength check criteria are to be in accordance with each Society's Rules.

### S31.1.1 Ice strengthened ships

S31.1.1.1 Where ships are reinforced to comply with an ice class notation, the intermediate frames are not to be included when considering compliance with S31.

S31.1.1.2 The renewal thicknesses for the additional structure required to meet the ice strengthening notation are to be based on the class society's requirements.

S31.1.1.3 If the ice class notation is requested to be withdrawn, the additional ice strengthening structure, with the exception of tripping brackets (see S31.2.1.2.1.b and S31.2.3), is not to be considered to contribute to compliance with S31.

## S31.2 Renewal or other measures

### S31.2.1 Criteria for renewal or other measures

#### S31.2.1.1 Symbols used in S31.2.1

$t_M$ = thickness as measured, in mm
$t_{REN}$ = thickness at which renewal is required. See S31.2.1.2
$t_{REN,d/t}$ = thickness criteria based on d/t ratio. See S31.2.1.2.1
$t_{REN,S}$ = thickness criteria based on strength. See S31.2.1.2.2
$t_{COAT}$ = $0.75 \cdot t_{S12}$
$t_{S12}$ = thickness in mm as required by UR S12 (Rev.3) in S12.3 for frame webs and in S12.4 for upper and lower bracket webs
$t_{AB}$ = thickness as built, in mm
$t_C$ = See Table 1 below

**Table 1 - $t_C$ values, in mm**

| Ship's length $L$, in m | Holds other than No. 1: Span and upper brackets | Holds other than No. 1: Lower brackets | Hold No. 1: Span and upper brackets | Hold No. 1: Lower brackets |
| :--- | :--- | :--- | :--- | :--- |
| $\le 100$ | 2.0 | 2.5 | 2.0 | 3.0 |
| 150 | 2.0 | 3.0 | 3.0 | 3.5 |
| $\ge 200$ | 2.0 | 3.0 | 3.0 | 4.0 |

**Note:** For intermediate ship lengths, $t_C$ is obtained by linear interpolation between the above values.

#### S31.2.1.2 Criteria for webs (Shear and other checks)

The webs of side shell frames and brackets are to be renewed when the measured thickness ($t_M$) is equal to or less than the thickness ($t_{REN}$) as defined below:

$t_{REN}$ is the greatest of:
(a) $t_{COAT} - t_C$
(b) $0.75 \cdot t_{AB}$
(c) $t_{REN,d/t}$ (applicable to Zone A and B only)
(d) $t_{REN,S}$ (where required by S31.2.1.2.2)

##### S31.2.1.2.1 Thickness criteria based on d/t ratio

Subject to b) and c) below, $t_{REN,d/t}$ is given by the following equation:

$t_{REN,d/t} = (\text{web depth in mm}) / R$

where:

$R =$ for frames
- $65 \cdot k^{0.5}$ for symmetrically flanged frames
- $55 \cdot k^{0.5}$ for asymmetrically flanged frames

for lower brackets (see a) below):
- $87 \cdot k^{0.5}$ for symmetrically flanged frames
- $73 \cdot k^{0.5}$ for asymmetrically flanged frames

$k = 1.0$ for ordinary hull structural steel and according to UR S4 for higher tensile steel.

In no instance is $t_{REN,d/t}$ for lower integral brackets to be taken as less than $t_{REN,d/t}$ for the frames they support.

**a) Lower brackets**
Lower brackets are to be flanged or face plate is to be fitted, ref. S31.2.1.3.

In calculating the web depth of the lower brackets, the following will apply:
- The web depth of lower bracket may be measured from the intersection of the sloped bulkhead of the hopper tank and the side shell plate, perpendicularly to the face plate of the lower bracket (see Figure 3).
- Where stiffeners are fitted on the lower bracket plate, the web depth may be taken as the distance between the side shell and the stiffener, between the stiffeners or between the outermost stiffener and the face plate of the brackets, whichever is the greatest.

**b) Tripping bracket alternative**
When $t_M$ is less than $t_{REN,d/t}$ at section b of the side frames, tripping brackets in accordance with S31.2.3 may be fitted as an alternative to the requirements for the web depth to thickness ratio of side frames, in which case $t_{REN,d/t}$ may be disregarded in the determination of $t_{REN}$ in accordance with S31.2.1.2. The value of $t_M$ is to be based on zone B according to UR Z10.2, ANNEX V, see Figure 1.

**c) Immediately abaft collision bulkhead**
For the side frames, including the lower bracket, located immediately abaft the collision bulkheads, whose scantlings are increased in order that their moment of inertia is such to avoid undesirable flexibility of the side shell, when their web as built thickness $t_{AB}$ is greater than $1.65 \cdot t_{REN,S}$, the thickness $t_{REN,d/t}$ may be taken as the value $t'_{REN,d/t}$ obtained from the following equation:

$t'_{REN,d/t} = \sqrt[3]{t_{REN,d/t}^2 \cdot t_{REN,S}}$

where $t_{REN,S}$ is obtained from S31.3.3

##### S31.2.1.2.2 Thickness criteria based on shear strength check

Where $t_M$ in the lower part of side frames, as defined in Figure 1, is equal to or less than $t_{COAT}$, $t_{REN,S}$ is to be determined in accordance with S31.3.3.

##### S31.2.1.2.3 Thickness of renewed webs of frames and lower brackets

Where steel renewal is required, the renewed webs are to be of a thickness not less than $t_{AB}$, $1.2 \cdot t_{COAT}$ or $1.2 \cdot t_{REN}$, whichever is the greatest.

##### S31.2.1.2.4 Criteria for other measures

When $t_{REN} < t_M \le t_{COAT}$, measures are to be taken, consisting of all the following:

a) Sand blasting, or equivalent, and coating (see S31.2.2).
b) Fitting tripping brackets (see S31.2.3), when the above condition occurs for any of the side frame zones A, B, C and D, shown in Figure 1. Tripping brackets not connected to flanges are to have soft toe, and the distance between the bracket toe and the frame flange is not to be greater than about 50 mm, see Figure 4.
c) Maintaining the coating in "as-new" condition (i.e. without breakdown or rusting) at Special and Intermediate Surveys.

The above measures may be waived if the structural members show no thickness diminution with respect to the as built thicknesses and coating is in "as-new" condition (i.e. without breakdown or rusting).

When the measured frame webs thickness $t_M$ is such that $t_{REN} < t_M \le t_{COAT}$ and the coating is in GOOD condition, sand blasting and coating as required in a) above may be waived even if not found in "as-new" condition, as defined above, provided that tripping brackets are fitted and the coating damaged in way of the tripping bracket welding is repaired.

#### S31.2.1.3 Criteria for frames and brackets (Bending check)

When lower end brackets were not fitted with flanges at the design stage, flanges are to be fitted so as to meet the bending strength requirements in S31.3.4. The full width of the bracket flange is to extend up beyond the point at which the frame flange reaches full width. Adequate back-up structure in the hopper is to be ensured, and the bracket is to be aligned with the back-up structure.

Where the length or depth of the lower bracket does not meet the requirements in S12(Rev.3), a bending strength check in accordance with S31.3.4 is to be carried out and renewals or reinforcements of frames and/or brackets effected as required therein.

The bending check needs not to be carried out in the case the bracket geometry is modified so as to comply with S12(Rev.3) requirements.

### S31.2.2 Thickness measurements, steel renewal, sand blasting and coating

For the purpose of steel renewal, sand blasting and coating, four zones A, B, C and D are defined, as shown in Figure 1. When renewal is to be carried out, surface preparation and coating are required for the renewed structures as given in UR Z9 for cargo holds of new buildings.

Representative thickness measurements are to be taken for each zone and are to be assessed against the criteria in S31.2.1.

When zone B is made up of different plate thicknesses, the lesser thickness is to be used for the application of the requirements in S31.

In case of integral brackets, when the criteria in S31.2.1 are not satisfied for zone A or B, steel renewal, sand blasting and coating, as applicable, are to be done for both zones A and B.

In case of separate brackets, when the criteria in S31.2.1 are not satisfied for zone A or B, steel renewal, sand blasting and coating is to be done for each one of these zones, as applicable.

When steel renewal is required for zone C according to S31.2.1, it is to be done for both zones B and C. When sand blasting and coating is required for zone C according to S31.2.1, it is to be done for zones B, C and D.

When steel renewal is required for zone D according to S31.2.1, it needs only to be done for this zone. When sand blasting and coating is required for zone D according to S31.2.1, it is to be done for both zones C and D.

Special consideration may be given by the Society to zones previously renewed or re-coated, if found in "as-new" condition (i.e., without breakdown or rusting).

When adopted, on the basis of the renewal thickness criteria in S31.2.1, in general coating is to be applied in compliance with the requirements of UR Z9, as applicable.

Where, according to the requirements in S31.2.1, a limited number of side frames and brackets are shown to require coating over part of their length, the following criteria apply.

a) The part to be coated includes:
- the web and the face plate of the side frames and brackets,
- the hold surface of side shell, hopper tank and topside tank plating, as applicable, over a width not less than 100 mm from the web of the side frame.

b) Epoxy coating or equivalent is to be applied.

In all cases, all the surfaces to be coated are to be sand blasted prior to coating application.

When flanges of frames or brackets are to be renewed according to S31, the outstanding breadth to thickness ratio is to comply with the requirements in UR S12.5.

### S31.2.3 Reinforcing measures

Reinforcing measures are constituted by tripping brackets, located at the lower part and at midspan of side frames (see Figure 4). Tripping brackets may be located at every two frames, but lower and midspan brackets are to be fitted in line between alternate pairs of frames.

The thickness of the tripping brackets is to be not less than the as-built thickness of the side frame webs to which they are connected.

Double continuous welding is to be adopted for the connections of tripping brackets to the side shell frames and shell plating.

Where side frames and side shell are made of Higher Strength Steel (HSS), Normal Strength Steel (NSS) tripping brackets may be accepted, provided the electrodes used for welding are those required for the particular HSS grade, and the thickness of the tripping brackets is equal to the frame web thickness, regardless of the frame web material.

### S31.2.4 Weld throat thickness

In case of steel renewal the welded connections are to comply with UR S12.7 of UR S12(Rev.3).

### S31.2.5 Pitting and grooving

If pitting intensity is higher than 15% in area (see Figure 5), thickness measurement is to be taken to check pitting corrosion.

The minimum acceptable remaining thickness in pits or grooves is equal to:
- 75% of the as built thickness, for pitting or grooving in the frame and brackets webs and flanges
- 70% of the as built thickness, for pitting or grooving in the side shell, hopper tank and topside tank plating attached to the side frame, over a width up to 30 mm from each side of it.

### S31.2.6 Renewal of all frames in one or more cargo holds

When all frames in one or more holds are required to be renewed according to UR S31, the compliance with the requirements in URS 12 (Rev. 1) may be accepted in lieu of the compliance with the requirements in UR S31, provided that:
- It is applied at least to all the frames of the hold(s)
- The coating requirements for side frames of "new ships" are complied with
- The section modulus of side frames is calculated according to the Classification Society Rules.

### S31.2.7 Renewal of damaged frames

In case of renewal of a damaged frame already complying with S31, the following requirements apply:
- The conditions accepted in compliance with S31 are to be restored as a minimum.
- For localised damages, the extension of the renewal is to be carried out according to the standard practice of each Classification Society.

## S31.3 Strength check criteria

In general, loads are to be calculated and strength checks are to be carried out for the aft, middle and forward frames of each hold. The scantlings required for frames in intermediate positions are to be obtained by linear interpolation between the results obtained for the above frames.

When scantlings of side frames vary within a hold, the required scantlings are also to be calculated for the mid frame of each group of frames having the same scantlings. The scantlings required for frames in intermediate positions are to be obtained by linear interpolation between the results obtained for the calculated frames.

### S31.3.1 Load model

The following loading conditions are to be considered:
- Homogeneous heavy cargo (density greater than 1,78 $t/m^3$)
- Homogeneous light cargo (density less than 1,78 $t/m^3$)
- Non homogeneous heavy cargo, if allowed
- Multi port loading/unloading conditions need not be considered.

#### S31.3.1.1 Forces

The forces $P_{fr,a}$ and $P_{fr,b}$, in kN, to be considered for the strength checks at sections a) and b) of side frames (specified in Figure 2; in the case of separate lower brackets, section b) is at the top of the lower bracket), are given by:

$P_{fr,a} = P_S + \max(P_1, P_2)$
$P_{fr,b} = P_{fr,a} \cdot \frac{h - 2h_B}{h}$

where:

$P_S$ = still water force, in kN
$= s \cdot h \cdot \left( \frac{p_{S,U} + p_{S,L}}{2} \right)$ when the upper end of the side frame span $h$ (see Figure 1) is below the load water line
$= s \cdot h' \cdot \left( \frac{p_{S,L}}{2} \right)$ when the upper end of the side frame span $h$ (see Figure 1) is at or above the load water line

$P_1$ = wave force, in kN, in head sea
$= s \cdot h \cdot \left( \frac{p_{1,U} + p_{1,L}}{2} \right)$

$P_2$ = wave force, in kN, in beam sea
$= s \cdot h \cdot \left( \frac{p_{2,U} + p_{2,L}}{2} \right)$

$h, h_B$ = side frame span and lower bracket length, in m, defined in Figures 1 and 2, respectively
$h'$ = distance, in m, between the lower end of side frame span $h$ (see Figure 1) and the load water line
$s$ = frame spacing, in m
$p_{S,U}, p_{S,L}$ = still water pressure, in $kN/m^2$, at the upper and lower end of the side frame span $h$ (see Figure 1), respectively
$p_{1,U}, p_{1,L}$ = wave pressure, in $kN/m^2$, as defined in S31.3.1.2.1) below for the upper and lower end of the side frame span $h$, respectively
$p_{2,U}, p_{2,L}$ = wave pressure, in $kN/m^2$, as defined in S31.3.1.2.2) below for the upper and lower end of the side frame span $h$, respectively

#### S31.3.1.2 Wave Pressure

**1) Wave pressure $p_1$**
- The wave pressure $p_1$, in $kN/m^2$, at and below the waterline is given by:
$p_1 = 1.50 \cdot \left[ p_{11} + 135 \cdot \frac{B}{2(B + 75)} - 1.2(T - z) \right]$
$p_{11} = 3 \cdot k_S \cdot C + k_f$
- The wave pressure $p_1$, in $kN/m^2$, above the water line is given by:
$p_1 = p_{1wl} - 7.50(z - T)$

**2) Wave pressure $p_2$**
- The wave pressure $p_2$, in $kN/m^2$, at and below the waterline is given by:
$p_2 = 13.0 \cdot \left[ 0.5 \cdot B \cdot \frac{50 \cdot c_r}{2(B + 75)} + C_B \cdot \frac{0.5 \cdot B + k_f}{14} \cdot (0.7 + 2 \frac{z}{T}) \right]$
- The wave pressure $p_2$, in $kN/m^2$, above the water line is given by:
$p_2 = p_{2wl} - 5.0(z - T)$

where:
$p_{1wl}$ = $p_1$ wave sea pressure at the waterline
$p_{2wl}$ = $p_2$ wave sea pressure at the waterline
$L$ = Rule length, in m, as defined in UR S2
$B$ = greatest moulded breadth, in m
$C_B$ = block coefficient, as defined in UR S2, but not to be taken less than 0.6
$T$ = maximum design draught, in m
$C$ = coefficient
$= 10.75 - \left( \frac{300 - L}{100} \right)^{1.5}$ for $90 \le L \le 300$ m
$= 10.75$ for $300$ m $< L$
$c_r = (1.25 - 0.025 \cdot \frac{2 \cdot k_r}{\sqrt{GM}}) \cdot k$
$k = 1.2$ for ships without bilge keel
$= 1.0$ for ships with bilge keel
$k_r$ = roll radius of gyration. If the actual value of $k_r$ is not available
$= 0.39 \cdot B$ for ships with even distribution of mass in transverse section (e.g. alternate heavy cargo loading or homogeneous light cargo loading)
$= 0.25 \cdot B$ for ships with uneven distribution of mass in transverse section (e.g. homogeneous heavy cargo distribution)
$GM = 0.12 \cdot B$ if the actual value of $GM$ is not available
$z$ = vertical distance, in m, from the baseline to the load point
$k_s = C_B + \frac{0.83}{\sqrt{C_B}}$ at aft end of $L$
$= C_B$ between $0.2 \cdot L$ and $0.6 \cdot L$ from aft end of $L$
$= C_B + \frac{1.33}{C_B}$ at forward end of $L$
Between the above specified points, $k_s$ is to be interpolated linearly.
$k_f = 0.8 \cdot C$

### S31.3.2 Allowable stresses

The allowable normal and shear stresses $\sigma_a$ and $\tau_a$, in $N/mm^2$, in the side shell frames and brackets are given by:

$\sigma_a = 0.90 \cdot \sigma_F$
$\tau_a = 0.40 \cdot \sigma_F$

where $\sigma_F$ is the minimum upper yield stress, in $N/mm^2$, of the material.

### S31.3.3 Shear strength check

Where $t_M$ in the lower part of side frames, as defined in Figure 1, is equal to or less than $t_{COAT}$, shear strength check is to be carried out in accordance with the following.

The thickness $t_{REN,S}$, in mm, is the greater of the thicknesses $t_{REN,Sa}$ and $t_{REN,Sb}$ obtained from the shear strength check at sections a) and b) (see Figure 2 and S31.3.1) given by the following, but need not be taken in excess of $0.75 \cdot t_{S12}$.

- at section a): $t_{REN,Sa} = \frac{1000 \cdot k_S \cdot P_{fr,a}}{d_a \cdot \sin\phi \cdot \tau_a}$
- at section b): $t_{REN,Sb} = \frac{1000 \cdot k_S \cdot P_{fr,b}}{d_b \cdot \sin\phi \cdot \tau_a}$

where:
$k_S$ = shear force distribution factor, to be taken equal to 0.6
$P_{fr,a}, P_{fr,b}$ = pressures forces defined in S31.3.1.1
$d_a, d_b$ = bracket and frame web depth, in mm, at sections a) and b), respectively (see Figure 2); in case of separate (non integral) brackets, $d_b$ is to be taken as the minimum web depth deducing possible scallops
$\phi$ = angle between frame web and shell plate
$\tau_a$ = allowable shear stress, in $N/mm^2$, defined in S31.3.2.

### S31.3.4 Bending strength check

Where the lower bracket length or depth does not meet the requirements in UR S12(Rev.3), the actual section modulus, in $cm^3$, of the brackets and side frames at sections a) and b) is to be not less than:

- at section a): $Z_a = \frac{1000 \cdot P_{fr,a} \cdot h}{m_a \cdot \sigma_a}$
- at section b): $Z_b = \frac{1000 \cdot P_{fr,a} \cdot h}{m_b \cdot \sigma_a}$

where:
$P_{fr,a}$ = pressures force defined in S31.3.1.1
$h$ = side frame span, in m, defined in Figure 1
$\sigma_a$ = allowable normal stress, in $N/mm^2$, defined in S31.3.2
$m_a, m_b$ = bending moment coefficients defined in Table 2

The actual section modulus of the brackets and side frames is to be calculated about an axis parallel to the attached plate, based on the measured thicknesses. For pre-calculations, alternative thickness values may be used, provided they are not less than:
- $t_{REN}$, for the web thickness
- the minimum thicknesses allowed by the Society renewal criteria for flange and attached plating.

The attached plate breadth is equal to the frame spacing, measured along the shell at midspan of $h$.

If the actual section moduli at sections a) and b) are less than the values $Z_a$ and $Z_b$, the frames and brackets are to be renewed or reinforced in order to obtain actual section moduli not less than $1.2 \cdot Z_a$ and $1.2 \cdot Z_b$, respectively.

In such a case, renewal or reinforcements of the flange are to be extended over the lower part of side frames, as defined in Figure 1.

**Table 2 – Bending moment coefficients $m_a$ and $m_b$**

| | $m_a$ | $m_b$: $h_B \le 0.08h$ | $m_b$: $h_B = 0.1h$ | $m_b$: $h_B \ge 0.125h$ |
| :--- | :--- | :--- | :--- | :--- |
| Empty holds of ships approved to operate in non homogeneous loading conditions | 10 | 17 | 19 | 22 |
| Other cases | 12 | 20 | 22 | 26 |

**Note 1:** Non homogeneous loading condition means a loading condition in which the ratio between the highest and the lowest filling ratio, evaluated for each hold, exceeds 1.20 corrected for different cargo densities.
**Note 2:** For intermediate values of the bracket length $h_B$, the coefficient $m_b$ is obtained by linear interpolation between the table values.

![Figure 1: Lower part and zones of side frames](A diagram showing a side shell frame of a bulk carrier cargo hold. It identifies four zones: A (lower bracket), B (lower part of the frame, $0.25h$ from bottom), C (mid part of the frame), and D (upper bracket/part, $0.25h$ from top). The total span of the frame is labeled $h$.)

![Figure 2 – Sections a) and b)](Two technical diagrams showing the geometry of the side frame and lower bracket. Section 'a' is at the connection of the bracket to the frame, and section 'b' is on the frame above the bracket. It labels depths $d_a$, $d_b$ and lengths $h, h_B$.)

![Figure 3 – Definition of the lower bracket web depth for determining $t_{REN, d/t}$](A technical drawing showing how to measure the web depth of a lower bracket at a 90-degree angle from the intersection of the sloped bulkhead of the hopper tank and the side shell plate to the face plate of the bracket. A 'soft toe' is also indicated at the end of the bracket.)

![Figure 4 – Tripping brackets](Diagrams showing the installation details of tripping brackets on side frames. It specifies that the distance from the knuckle should not be greater than 200 mm. It also shows a gap of approximately 50 mm between the tripping bracket toe and the frame flange when the bracket is not welded to the flange.)

![Figure 5 - Pitting intensity diagrams (from 5% to 25% intensity)](Five rectangular panels showing visual representations of different levels of pitting corrosion: 5% scattered, 10% scattered, 15% scattered, 20% scattered, and 25% scattered. The black dots represent the density of pits.)

Page 18 of 18
IACS Req. 2002/Rev.4, 2007
End of Document


================================================================================
# FILE: UR_S/ur-s32-draft-del-may-2010.md
================================================================================

[S32]

# [S32] Draft: Local Scantlings of Double Side Skin Structure of Bulk Carriers

**29/11/2004**
**Deleted May 2010.**

> Please note that draft UR S32 was never issued (although the draft was made available on the IACS website for public information) since it was superseded by the IACS Common Structural Rules for Bulk Carriers produced by the IACS Joint Bulker Project (JBP).

***

**End of Document**

***
Page 1 of 1 | IACS Req. 2004


================================================================================
# FILE: UR_S/ur-s33rev3.md
================================================================================

# S33 Requirements for Use of Extremely Thick Steel Plates in Container Ships

**S33**
(Jan 2013)
(Rev.1 Sept 2015)
(Rev.2 Dec 2019)
(Rev.3 Feb 2020)

## 1. Application

### 1.1 General

1.1.1 This UR is to be complied with for container ships incorporating extremely thick steel plates having steel grade and thickness in accordance with 1.2 and 1.3 respectively.

1.1.2 This UR identifies when measures for the prevention of brittle fracture of extremely thick steel plates are required for longitudinal structural members.

1.1.3 This UR defines the following methods to apply to the extremely thick plates of container ships for preventing the crack initiation and propagation:

*   Non-Destructive Testing (NDT) during construction detailed in 2,
*   Periodic NDT after delivery detailed in 3,
*   Brittle crack arrest design detailed in 4.

The application of the measures specified in 2, 3 and 4 is to be in accordance with Annex 1.

1.1.4 This UR gives the basic concepts for application of extremely thick steel plates to longitudinal structural members in the upper deck region.

1.1.5 For the application of this UR, the upper deck region means the upper deck plating, hatch side coaming plating, hatch coaming top plating and their attached longitudinals.

### 1.2 Steel Grade

1.2.1 This UR is to be applied when any of YP36, YP40 and YP47 steel plates are used for the longitudinal structural members in the upper deck region.

*Note: YP36 YP40 and YP47 refers to the minimum specified yield strength of steel 355, 390 and 460 N/mm², respectively as defined in UR W11 and W31.*

1.2.2 In case YP47 steel plates are used for longitudinal structural members in the upper deck region, the steel plates are to be of EH47 grade as specified in UR W31.

### 1.3 Thickness

1.3.1 For steel plates with thickness of over 50 mm and not greater than 100 mm, the measures for prevention of brittle crack initiation and propagation specified in 2, 3 and 4 are to be taken.

1.3.2 For steel plates with thickness exceeding 100 mm, appropriate measures for prevention of brittle crack initiation and propagation are to be taken in accordance with the Classification Society's procedures.

### 1.4 Hull structures (for the purpose of design)

#### 1.4.1 Material factor k

The material factors of YP36 and YP40 steels are defined in UR S4.

The material factor of YP47 steel for the assessment of hull girder strength is to be taken as k = 0.62.

#### 1.4.2 Fatigue assessment

The fatigue assessment of the longitudinal structural members is to be performed in accordance with the Classification Society's procedures.

#### 1.4.3 Details of construction design

Special consideration is to be paid to the construction details where extremely thick steel plates are applied to structural members such as connections between outfitting and hull structures. Connections details are to be in accordance with the Classification Society's requirements.

---

## 2. Non-Destructive Testing during construction (Measure No.1 of Annex 1)

Where non-destructive testing (NDT) during construction is required in Annex 1, the NDT is to be in accordance with 2.1 and 2.2. Enhanced NDT as specified in 4.3.1(e) is to be carried out in accordance with an appropriate standard.

### 2.1 General

2.1.1 Ultrasonic testing (UT) in accordance with UR W33 is to be carried out on all block-to-block butt joints of all upper flange longitudinal structural members in the cargo hold region. Upper flange longitudinal structural members include the topmost strakes of the inner hull/bulkhead, the sheer strake, main deck, coaming plate, coaming top plate, and all attached longitudinal stiffeners. These members are defined in Fig.1.

![Figure 1: Upper Flange Longitudinal Structural Members](A schematic diagram showing a cross-section of a ship's upper structure with labels for deck longitudinals, side longitudinals, inner hull longitudinals, and bulkhead longitudinals.)

### 2.2 Acceptance criteria of UT

2.2.1 Acceptance criteria of UT are to be in accordance with UR W33.

2.2.2 The acceptance criteria may be adjusted under consideration of the appertaining brittle crack initiation prevention procedure and where this is more severe than that found in UR W33, the UT procedure is to be amended accordingly to a more severe sensitivity.

---

## 3. Periodic NDT after delivery (Measure No.2 of Annex 1)

Where periodic NDT after delivery is required, the NDT is to be in accordance with 3.1, 3.2 and 3.3.

### 3.1 General

3.1.1 The procedure of the NDT is to be in accordance with UR W33, irrespective of the applicability clause for new building in paragraph 1.1 of UR W33.

### 3.2 Timing of UT

3.2.1 Where UT is carried out, the frequency of survey is to be in accordance with the Classification Society requirements.

### 3.3 Acceptance criteria of UT

3.3.1 Where UT is carried out, acceptance criteria of UT are to be in accordance with UR W33, irrespective of the applicability clause for new building in paragraph 1.1 of UR W33.

---

## 4. Brittle crack arrest design (Measures No.3, 4 and 5 of Annex 1)

### 4.1 General

4.1.1 The brittle crack arrest steel method detailed in 4 may be used when the measures No.3, 4 and 5 of Annex 1 are applied and the steel grade material of the upper deck is not higher than YP40. Otherwise other means for preventing the crack initiation and propagation shall be agreed with the Classification Society.

4.1.2 Measures for prevention of brittle crack propagation, are to be taken within the cargo hold region. A brittle crack arrest design means a design using these measures.

4.1.3 The measures given in section 4 generally apply to the block-to-block joints but it should be noted that cracks can initiate and propagate away from such joints. Therefore, appropriate measures should also be considered for the cases specified in 4.2.1 (b) (ii).

4.1.4 Brittle crack arrest steels are defined in UR W31.

### 4.2 Functional requirements of brittle crack arrest design

4.2.1 The purpose of the brittle crack arrest design is to arrest propagation of a crack at a proper position and to prevent large scale fracture of the hull girder.

(a) The locations of most concern for brittle crack initiation and propagation are the block-to-block butt weld joints either on hatch side coaming or on upper deck plating. Other locations in block fabrication where joints are aligned may also present higher opportunity for crack initiation and propagation along butt weld joints.

(b) Both of the following cases are to be considered:
(i) where the brittle crack runs straight along the butt joint, and
(ii) where the brittle crack initiates in the butt joint but deviates away from the weld and into the plate, or where the brittle crack initiates from any other weld (see the figure below for definition of other welds) and propagates into the plate.

"Other weld" includes the following (refer to Fig.2):
1. Fillet weld between hatch side coaming plating, including top plating, and longitudinals;
2. Fillet weld between hatch side coaming plating, including top plating and longitudinals, and attachments. (e.g., Fillet weld between hatch side top plating and hatch cover pad plating.);
3. Fillet weld between hatch side coaming top plating and hatch side coaming plating;
4. Fillet weld between hatch side coaming plating and upper deck plating;
5. Fillet weld between upper deck plating and inner hull/bulkheads;
6. Fillet weld between upper deck plating and longitudinal; and
7. Fillet weld between sheer strakes and upper deck plating.

![Figure 2: Other Weld Areas](A diagram illustrating various structural connection points labeled 1 through 7, including hatch side coaming, top plating, upper deck, attachments like pad plates, and longitudinals, showing potential crack initiation locations.)

### 4.3 Concept examples of brittle crack arrest design

4.3.1 The followings are considered acceptable examples of measures that can be used on a brittle crack arrest-design to prevent brittle crack propagations. The detail design arrangements are to be submitted to the Classification Society for their approval. Other measures may be considered and accepted for review by the Classification Society.

**Brittle crack arrest design for 4.2.1(b) (ii):**

(a) Brittle crack arrest steel is to be used for the upper deck plating along the cargo hold region in a way suitable to arrest a brittle crack initiating from the coaming and propagating into the structure below.

**Brittle crack arrest design for 4.2.1(b) (i):**

(b) Where the block to block butt welds of the hatch side coaming and those of the upper deck are shifted, this shift is to be greater than or equal to 300mm. Brittle crack arrest steel is to be provided for the hatch side coaming plating.

(c) Where crack arrest holes are provided in way of the block-to-block butt welds at the region where hatch side coaming weld meets the deck weld, the fatigue strength of the lower end of the butt weld is to be assessed. Additional countermeasures are to be taken for the possibility that a running brittle crack may deviate from the weld line into upper deck or hatch side coaming. These countermeasures are to include the application of brittle crack arrest steel in hatch side coaming plating.

(d) Where arrest insert plates of brittle crack arrest steel or weld metal inserts with high crack arrest toughness properties are provided in way of the block-to-block butt welds at the region where hatch side coaming weld meets the deck weld, additional countermeasures are to be taken for the possibility that a running brittle crack may deviate from the weld line into upper deck or hatch side coaming. These countermeasures are to include the application of brittle crack arrest steel in hatch side coaming plating.

(e) The application of enhanced NDT particularly time of flight diffraction (TOFD) technique using stricter defect acceptance in lieu of standard UT technique specified in 2 can be an alternative to (b), (c) and (d).

### 4.4 Selection of brittle crack arrest steels

4.4.1 The brittle crack arrest steels fitted in the upper deck region of container ships are to comply with Table 1 where suffixes BCA1 and BCA2 are defined in UR W31.

4.4.2 The brittle crack arrest steel property is to be selected for each individual structural member with thickness above 50 mm according to Table 1.

**Table 1: Brittle crack arrest steel requirement in function of structural members and thickness**

| Structural Members plating (*) | Thickness (mm) | Brittle crack arrest steel requirement |
| :--- | :--- | :--- |
| Upper deck | 50 < t ≤ 100 | Steel grade YP36 or 40 with suffix BCA1 |
| Hatch coaming side | 50 < t ≤ 80 | Steel grade YP 40 or 47 with suffix BCA1 |
| | 80 < t ≤ 100 | Steel grade YP 40 or 47 with suffix BCA2 |

(*) Excluding their attached longitudinals

4.4.3 When brittle crack arrest steels as specified in Table 1 are used, the weld joints between the hatch coaming side and the upper deck are to be partial penetration weld details approved by the Classification Society.

In the vicinity of ship block joints, alternative weld details may be used for the deck and hatch coaming side connection provided additional means for preventing the crack propagation are implemented and agreed by the Classification Society in this connection area.

---

## Annex 1: Measures for Extremely Thick Steel Plates

The thickness and the yield strength shown in the following table apply to the hatch coaming top plating and side plating, and are the controlling parameters for the application of the countermeasures given in S33.4.3.1. These controlling parameters are not applicable for the upper deck.

If the as built thickness of the hatch coaming top plating and side plating is below the values contained in the table, countermeasures are not necessary regardless of the thickness and yield strength of the upper deck plating.

| Yield Strength (kgf/mm²) | Thickness (mm) | Option | Measure 1 | Measure 2 | Measure 3+4 | Measure 5 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 36 | 50 < t ≤ 85 | - | N.A. | N.A. | N.A. | N.A. |
| | 85 < t ≤ 100 | - | X | N.A. | N.A. | N.A. |
| 40 | 50 < t ≤ 85 | - | X | N.A. | N.A. | N.A. |
| | 85 < t ≤ 100 | A | X | N.A. | X | X |
| | | B | X * | N.A. ** | N.A. | X |
| 47 (FCAW) | 50 < t ≤ 100 | A | X | N.A. | X | X |
| | | B | X * | N.A. ** | N.A. | X |
| 47 (EGW) | 50 < t ≤ 100 | - | X | N.A. | X | X |

"X" means "To be applied"
"N.A." means "Need not to be applied"
"A", "B": selectable options
*: See 4.3.1 (e) of UR S33.
**: may be required at the discretion of the Classification Society

**Measures:**

1.  NDT other than visual inspection on all target block joints (during construction): See S33.2.
2.  Periodic NDT other than visual inspection on all target block joints (after delivery): See S33.3.
3.  Brittle crack arrest design against straight propagation of brittle crack along weldline to be taken (during construction): See S33.4.3.1 (b), (c) and (d).
4.  Brittle crack arrest design against deviation of brittle crack from weldline (during construction): See S33.4.3.1 (a).
5.  Brittle crack arrest design against propagation of cracks from other welds such as fillets and attachment welds, as defined in S33.4.2.1 (b), (during construction): See S33.4.3.1 (a).

**Notes:**
1. This UR is to be applied by IACS Societies to ships contracted for construction on or after 1 January 2014.
2. Revision 1 of this UR is to be applied by IACS Societies to ships contracted for construction on or after 1 January 2017.
3. The "contracted for construction" date means the date on which the contract to build the vessel is signed between the prospective owner and the shipbuilder. For further details regarding the date of "contract for construction", refer to IACS Procedural Requirement (PR) No. 29.
4. Revision 2 of this UR is to be applied by IACS Societies to ships contracted for construction on or after 1 January 2021.
5. Revision 3 of this UR is to be applied by IACS Societies to ships contracted for construction on or after 1 July 2021.

**End of Document**


================================================================================
# FILE: UR_S/ur-s34.md
================================================================================

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


================================================================================
# FILE: UR_S/ur-s3rev2.md
================================================================================

# S3 Strength of End Bulkheads of Superstructures and Deckhouses

**S3**
(1973)
(Rev.1 May 2010)
(Rev.2 June 2023)

### S3.1 Scope

The following proposal applies to bulkheads forming the only protection for openings as per Regulation 18 of LLC 1966 and for accommodations. These requirements define minimum scantlings based upon local lateral loads and it may be required that they be increased in individual cases. Scantlings of tiers not specifically mentioned in this proposal are left to the discretion of individual Classification Societies.

This UR does not apply to CSR Bulk Carriers.

**Note:**

1. Changes introduced in Rev.2 are to be uniformly implemented by IACS Members for ships contracted for construction on or after 1 July 2024.
2. The "contracted for construction" date means the date on which the contract to build the vessel is signed between the prospective owner and the shipbuilder. For further details regarding the date of "contract for construction", refer to IACS Procedural Requirement (PR) No. 29.

***

### S3.2 Design pressure head

$$p = \frac{a}{100} (bf - y)c$$

where

$p$ = design pressure in N/mm² (MPa)

$a = 2.0 + \frac{L_1}{120}$ for lowest tier of unprotected fronts

The lowest tier is normally that tier which is directly situated above the uppermost continuous deck to which the rule depth $D$ is to be measured. However, where the freeboard is excessive, it may be left to each individual Classification Society to define this tier as an upper tier. It is recommended that 'excessive freeboard' is that which exceeds the minimum tabular freeboard by more than one standard superstructure height.

$a = 1.0 + \frac{L_1}{120}$ for 2nd tier of unprotected fronts

$a = 0.5 + \frac{L_1}{150}$ for 3rd tier of unprotected fronts and for sides and protected fronts

$a = 0.7 + \frac{L_1}{1000} - 0.8 \frac{x}{L}$ for aft ends aft of amidships

$a = 0.5 + \frac{L_1}{1000} - 0.4 \frac{x}{L}$ for aft ends forward of amidships

$L, L_1$ = length of ships in metres, $L_1$ need not be taken greater than 300 m

$b = 1.0 + \left( \frac{x/L - 0.45}{C_b + 0.2} \right)^2$ for $x / L \le 0.45$

$b = 1.0 + 1.5 \left( \frac{x/L - 0.45}{C_b + 0.2} \right)^2$ for $x / L > 0.45$

$C_b$ = block coefficient, $0.60 < C_b < 0.80$
when determining aft ends forward of amidships, $C_b$ need not be taken less than 0.80

$x$ = distance in metres between bulkhead considered and AP
When determining sides of a deckhouse, the deckhouse is to be subdivided into parts of approximately equal length, not exceeding $0.15L$ each and $x$ is to be taken as the distance between AP and the centre of each part considered.

***

$f = \frac{L}{10} e^{-L/300} - \left[ 1 - \left( \frac{L}{150} \right)^2 \right]$ for $L < 150$ m

$f = \frac{L}{10} e^{-L/300}$ for $150 \text{ m} < L < 300$ m

$f = 11.03$ for $L > 300$ m

$y$ = vertical distance in metres from summer waterline to midpoint of stiffener span

$c = \left( 0.3 + 0.7 \frac{b'}{B'} \right)$

$b'$ = breadth of deckhouse at the position considered

$B'$ = actual maximum breadth of ship on the exposed weather deck at the position considered

For exposed parts of machinery casings $c$ is not to be taken less than 1.0

The design pressure $p$ is not to be taken less than the minimum values given in Table 1.

**Table 1**

| $L(\text{m})$ | $p$ (N/mm² or MPa) Lowest tier of unprotected fronts | $p$ (N/mm² or MPa) Elsewhere |
| :--- | :--- | :--- |
| $L \le 50$ | 0.03 | 0.015 |
| $50 < L < 250$ | $0.025 + 10^{-4}L$ | $0.0125 + 0.5 \times 10^{-4}L$ |
| $L \ge 250$ | 0.05 | 0.025 |

### S3.3 Stiffener modulus

$$W = 350 s l^2 p$$

where

$W$ = stiffener modulus (cm³)

$s$ = spacing of stiffeners (m), measured along the plating

$l$ = unsupported span (m), which is to be taken as the 'tween deck height $l_{min} = 2.0$ m

$p$ = pressure in N/mm² (MPa) as defined above.

***

The section modulus of house side stiffeners need not be greater than that of side frames on the deck situated directly below, taking account of spacing and span.

These requirements assume the webs of lower tier stiffeners to be efficiently welded to the decks.

Scantlings for other types of end connections may be specially considered.

### S3.4 Thickness of plating

$$t = 30 s \sqrt{p}$$

where

$t$ = thickness of plating (mm), not less than the minimum thickness as follows:

$t_{min} = 5.0 + L_1/100$ for lowest tier
$t_{min} = 4.0 + L_1/100$ for upper tiers, but not less than 5.0 mm

For ships with $L_1 < 65\text{m}$, the minimum thickness of plating should be as follows:

$t_{min} = 5\text{mm}$ for the lowest unprotected front
$t_{min} = 4\text{mm}$ for all other cases

$s$ and $p$ are as defined above.

When determining $p$, $y$ is to be measured to middle of the plate field.

**End of Document**


================================================================================
# FILE: UR_S/ur-s4-rev4-apr-2017-cln.md
================================================================================

# S4 Criteria for the Use of High Tensile Steel with Minimum Yield Stress of 315 N/mm², 355 N/mm² and 390 N/mm²

**S4**
(1973)
(Rev.1 1974)
(Rev.2 Apr 2007)
(Rev.3 May 2010)
(Rev.4 Apr 2017)

This UR does not apply to CSR Bulk Carriers and Oil Tankers.

The material factor $k$ is defined as follows:

$k$ = 0.78 for steel with $R_{eH}$ = 315 N/mm²
$k$ = 0.72 for steel with $R_{eH}$ = 355 N/mm²
$k$ = 0.66 for steel with $R_{eH}$ = 390 N/mm² provided that a fatigue assessment of the structure is performed to verify compliance with the requirements of the Society,
$k$ = 0.68 for steel with $R_{eH}$ = 390 N/mm² in other cases.

Where:

$R_{eH}$ : Minimum yield stress, in N/mm²

***

| End of Document |
| :--- |

***

**Page 1 of 1** | **IACS Req. 1973/Rev.4 2017**


================================================================================
# FILE: UR_S/ur-s5corr1.md
================================================================================

# S5 Calculation of Midship Section Moduli for Conventional Ship for Ship's Scantlings

**S5**
(1975)
(Rev.1 May 2010)
(Corr.1 June 2019)

This UR does not apply to CSR Bulk Carriers and Oil Tankers.

When calculating the midship section modulus within $0.4L$ amidships the sectional area of all continuous longitudinal strength members is to be taken into account.

Large openings, i.e. openings exceeding 2.5 m in length or 1.2 m in breadth and scallops, where scallop-welding is applied, are always to be deducted from the sectional areas used in the section modulus calculation.

Smaller openings (manholes, lightening holes, single scallops in way of seams, etc.) need not be deducted provided that the sum of their breadths or shadow area breadths in one transverse section does not reduce the section modulus at deck or bottom by more than 3% and provided that the height of lightening holes, draining holes and single scallops in longitudinals or longitudinal girders does not exceed 25% of the web depth, for scallops maximum 75 mm.

A deduction-free sum of smaller opening breadths in one transverse section in the bottom or deck area of $0.06 (B - \sum b)$ (where $B$ = breadth of ship, $\sum b$ = total breadth of large openings) may be considered equivalent to the above reduction in section modulus.

The shadow area will be obtained by drawing two tangent lines with an opening angle of 30°.

The deck modulus is related to the moulded deck line at side.

The bottom modulus is related to the base line.

Continuous trunks and longitudinal hatch coamings are to be included in the longitudinal sectional area provided they are effectively supported by longitudinal bulkheads or deep girders. The deck modulus is then to be calculated by dividing the moment of inertia by the following distance, provided this is greater than the distance to the deck line at side:

$$y_t = y \left( 0.9 + 0.2 \frac{x}{B} \right)$$

where:
*   $y$ = distance from neutral axis to top of continuous strength member
*   $x$ = distance from top of continuous strength member to centreline of the ship

$x$ and $y$ to be measured to the point giving the largest value of $y_t$.

Longitudinal girders between multi-hatchways will be considered by special calculations.

***

**End of Document**

Page 1 of 1
IACS Req. 1975/Corr.1 2019


================================================================================
# FILE: UR_S/ur-s6rev9corr2.md
================================================================================

# S6 Use of Steel Grades for Various Hull Members - Ships of 90 m in Length and Above

**(1978)**
**(Rev.1 1980)**
**(Rev.2 1996)**
**(Rev.3 May 2002)**
**Rev.4 July 2003)**
**(Rev.5 Sept 2007)**
**(Rev.6 May 2010)**
**(Rev.7 Apr 2013)**
**(Rev.8 Dec 2015)**
**(Rev.9 July 2018)**
**(Corr.1 Mar 2021)**
**(Corr.2 Nov 2021)**

## S6.0 Application

This UR does not apply to CSR Bulk Carriers and Oil Tankers.

## S6.1 Ships in normal worldwide service

Materials in the various strength members are not to be of lower grade than those corresponding to the material classes and grades specified in Table 1 to Table 7. General requirements are given in Table 1, while additional minimum requirements are given in the following:

*   **Table 2:** for ships, excluding liquefied gas carriers covered in Table 3, with length exceeding 150 m and single strength deck,
*   **Table 3:** for membrane type liquefied gas carriers with length exceeding 150 m,
*   **Table 4:** for ships with length exceeding 250 m,
*   **Table 5:** for single side bulk carriers subjected to SOLAS regulation XII/6.4,
*   **Table 6:** for ships with ice strengthening.

The material grade requirements for hull members of each class depending on the thickness are defined in Table 7.

For strength members not mentioned in Tables 1 to 6, Grade A/AH may generally be used. The steel grade is to correspond to the as-built plate thickness and material class.

Plating materials for sternframes supporting the rudder and propeller boss, rudders, rudder horns and shaft brackets are in general not to be of lower grades than corresponding to Class II. For rudder and rudder body plates subjected to stress concentrations (e.g. in way of lower support of semi-spade rudders or at upper part of spade rudders) Class III is to be applied.

***

**Notes:**

1.  Changes introduced in Rev.5 are to be uniformly implemented by IACS Members and Associates from 1 July 2008.
2.  Changes introduced in Rev.7 are to be uniformly implemented by IACS Members from 1 July 2014.
3.  Changes introduced in Rev.8 are to be uniformly implemented by IACS Members from 1 January 2017.
4.  Changes introduced in Rev.9 are to be uniformly implemented by IACS Members from 1 July 2019.

Page 1 of 10 IACS Req. 1978/Rev.9 Corr.2 2021

---

### Table 1 - Material Classes and Grades for ships in general

| Structural member category | Material class/grade |
| :--- | :--- |
| **SECONDARY:** | - Class I within 0.4L amidships<br>- Grade A/AH outside 0.4L amidships |
| A1. Longitudinal bulkhead strakes, other than that belonging to the Primary category | |
| A2. Deck plating exposed to weather, other than that belonging to the Primary or Special category | |
| A3. Side plating | |
| **PRIMARY:** | - Class II within 0.4L amidships<br>- Grade A/AH outside 0.4L amidships |
| B1. Bottom plating, including keel plate | |
| B2. Strength deck plating, excluding that belonging to the Special category | |
| B3. Continuous longitudinal plating of strength members above strength deck, excluding hatch coamings | |
| B4. Uppermost strake in longitudinal bulkhead | |
| B5. Vertical strake (hatch side girder) and uppermost sloped strake in top wing tank | |
| **SPECIAL:** | - Class III within 0.4L amidships<br>- Class II outside 0.4L amidships<br>- Class I outside 0.6L amidships |
| C1. Sheer strake at strength deck (*) | |
| C2. Stringer plate in strength deck (*) | |
| C3. Deck strake at longitudinal bulkhead, excluding deck plating in way of inner-skin bulkhead of double-hull ships (*) | |
| C4. Strength deck plating at outboard corners of cargo hatch openings in container carriers and other ships with similar hatch opening configurations | - Class III within 0.4L amidships<br>- Class II outside 0.4L amidships<br>- Class I outside 0.6L amidships<br>- Min. Class III within cargo region |
| C5. Strength deck plating at corners of cargo hatch openings in bulk carriers, ore carriers combination carriers and other ships with similar hatch opening configurations | - Class III within 0.6L amidships<br>- Class II within rest of cargo region |
| C5.1 Trunk deck and inner deck plating at corners of openings for liquid and gas domes in membrane type liquefied gas carriers | |
| C6. Bilge strake in ships with double bottom over the full breadth and length less than 150 m | - Class II within 0.6L amidships<br>- Class I outside 0.6L amidships |
| C7. Bilge strake in other ships (*) | - Class III within 0.4L amidships<br>- Class II outside 0.4L amidships<br>- Class I outside 0.6L amidships |
| C8. Longitudinal hatch coamings of length greater than 0.15L including coaming top plate and flange | - Class III within 0.4L amidships<br>- Class II outside 0.4L amidships<br>- Class I outside 0.6L amidships |
| C9. End brackets and deck house transition of longitudinal cargo hatch coamings | - Not to be less than Grade D/DH |

(*) Single strakes required to be of Class III within 0.4L amidships are to have breadths not less than 800+5L (mm), need not be greater than 1800 (mm), unless limited by the geometry of the ship's design.

Page 2 of 10 IACS Req. 1978/Rev.9 Corr.2 2021

---

### Table 2 - Minimum Material Grades for ships, excluding liquefied gas carriers covered in Table 3, with length exceeding 150 m and single strength deck

| Structural member category | Material grade |
| :--- | :--- |
| • Longitudinal plating of strength deck where contributing to the longitudinal strength | Grade B/AH within 0.4L amidships |
| • Continuous longitudinal plating of strength members above strength deck | |
| Single side strakes for ships without inner continuous longitudinal bulkhead(s) between bottom and the strength deck | Grade B/AH within cargo region |

### Table 3 - Minimum Material Grades for membrane type liquefied gas carriers with length exceeding 150 m *

| Structural member category | Material grade |
| :--- | :--- |
| Longitudinal plating of strength deck where contributing to the longitudinal strength | Grade B/AH within 0.4L amidships |
| Continuous longitudinal plating of strength members above the strength deck | |
| - Trunk deck plating | Class II within 0.4L amidships |
| - Inner deck plating | Grade B/AH within 0.4L amidships |
| - Longitudinal strength member plating between the trunk deck and inner deck | Grade B/AH within 0.4L amidships |

(*) Table 3 is applicable to membrane type liquefied gas carriers with deck arrangements as shown in Fig. 1. Table 3 may apply to similar ship types with a "double deck" arrangement above the strength deck.

Page 3 of 10 IACS Req. 1978/Rev.9 Corr.2 2021

---

![Figure 1: Typical deck arrangement for membrane type Liquefied Natural Gas Carriers showing the relative positions of the Trunk Deck, Inner Deck, Strength Deck, Sheer Strake, Stringer Plate, and Bilge Strake.](A cross-sectional diagram of a ship's hull showing the upper deck structure. It labels the Trunk Deck at the top, the Inner Deck below it, and the Strength Deck. On the side, it identifies the Stringer Plate, Sheer Strake, and further down, the Bilge Strake.)

**Fig. 1 Typical deck arrangement for membrane type Liquefied Natural Gas Carriers**

### Table 4 - Minimum Material Grades for ships with length exceeding 250 m

| Structural member category | Material grade |
| :--- | :--- |
| Sheer strake at strength deck (*) | Grade E/EH within 0.4L amidships |
| Stringer plate in strength deck (*) | Grade E/EH within 0.4L amidships |
| Bilge strake (*) | Grade D/DH within 0.4L amidships |

(*) Single strakes required to be of Grade D/DH or Grade E/EH as shown in the above table and within 0.4L amidships are to have breadths not less than 800+5L (mm), need not be greater than 1800 (mm), unless limited by the geometry of the ship's design.

Page 4 of 10 IACS Req. 1978/Rev.9 Corr.2 2021

---

### Table 5 - Minimum Material Grades for single-side skin bulk carriers subjected to SOLAS regulation XII/6.4

| Structural member category | Material grade |
| :--- | :--- |
| Lower bracket of ordinary side frame (*), (**) | Grade D/DH |
| Side shell strakes included totally or partially between the two points located to 0.125$\ell$ above and below the intersection of side shell and bilge hopper sloping plate or inner bottom plate (**) | Grade D/DH |

(*) The term "lower bracket" means webs of lower brackets and webs of the lower part of side frames up to the point of 0.125$\ell$ above the intersection of side shell and bilge hopper sloping plate or inner bottom plate.

(**) The span of the side frame, $\ell$, is defined as the distance between the supporting structures.

### Table 6 - Minimum Material Grades for ships with ice strengthening

| Structural member category | Material grade |
| :--- | :--- |
| Shell strakes in way of ice strengthening area for plates | Grade B/AH |

Page 5 of 10 IACS Req. 1978/Rev.9 Corr.2 2021

---

### Table 7 - Material Grade Requirements for Classes I, II and III

| Class | | I | | II | | III | |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Thickness, in mm** | | **MS** | **HT** | **MS** | **HT** | **MS** | **HT** |
| $t \leq 15$ | | A | AH | A | AH | A | AH |
| $15 < t \leq 20$ | | A | AH | A | AH | B | AH |
| $20 < t \leq 25$ | | A | AH | B | AH | D | DH |
| $25 < t \leq 30$ | | A | AH | D | DH | D | DH |
| $30 < t \leq 35$ | | B | AH | D | DH | E | EH |
| $35 < t \leq 40$ | | B | AH | D | DH | E | EH |
| $40 < t \leq 50$ | | D | DH | E | EH | E | EH |

## S6.2 Ships exposed to low air temperatures

For ships intended to operate in areas with low air temperatures (below -10ºC), e.g. regular service during winter seasons to Arctic or Antarctic waters, the materials in exposed structures are to be selected based on the design temperature $t_D$, to be taken as defined in S6.3.

Materials in the various strength members above the lowest ballast water line (BWL) exposed to air (including the structural members covered by the Note [5] of Table 8) and materials of cargo tank boundary plating for which S6.4 is applicable are not to be of lower grades than those corresponding to Classes I, II and III, as given in Table 8, depending on the categories of structural members (SECONDARY, PRIMARY and SPECIAL). For non-exposed structures (except as indicated in Note [5] of Table 8) and structures below the lowest ballast water line, S6.1 applies.

Page 6 of 10 IACS Req. 1978/Rev.9 Corr.2 2021

---

### Table 8 - Application of Material Classes and Grades – Structures Exposed at Low Temperatures

| Structural member category | Material class | |
| :--- | :--- | :--- |
| | **Within 0.4L amidships** | **Outside 0.4L amidships** |
| **SECONDARY:** | | |
| Deck plating exposed to weather, in general | I | I |
| Side plating above BWL | | |
| Transverse bulkheads above BWL$^{[5]}$ | | |
| Cargo tank boundary plating exposed to cold cargo $^{[6]}$ | | |
| **PRIMARY:** | | |
| Strength deck plating $^{[1]}$ | II | I |
| Continuous longitudinal members above strength deck, excluding longitudinal hatch coamings | | |
| Longitudinal bulkhead above BWL$^{[5]}$ | | |
| Top wing tank bulkhead above BWL$^{[5]}$ | | |
| **SPECIAL:** | | |
| Sheer strake at strength deck $^{[2]}$ | III | II |
| Stringer plate in strength deck $^{[2]}$ | | |
| Deck strake at longitudinal bulkhead $^{[3]}$ | | |
| Continuous longitudinal hatch coamings $^{[4]}$ | | |

**Notes:**

[1] Plating at corners of large hatch openings to be specially considered. Class III or Grade E/EH to be applied in positions where high local stresses may occur.

[2] Not to be less than Grade E/EH within 0.4L amidships in ships with length exceeding 250 metres.

[3] In ships with breadth exceeding 70 metres at least three deck strakes to be Class III.

[4] Not to be less than Grade D/DH.

[5] Applicable to plating attached to hull envelope plating exposed to low air temperature. At least one strake is to be considered in the same way as exposed plating and the strake width is to be at least 600 mm.

[6] For cargo tank boundary plating exposed to cold cargo for ships other than liquefied gas carriers, see S6.4.

The material grade requirements for hull members of each class depending on thickness and design temperature are defined in Table 9. For design temperatures $t_D < -55ºC$, materials are to be specially considered by each Classification Society.

Page 7 of 10 IACS Req. 1978/Rev.9 Corr.2 2021

---

### Table 9 - Material Grade Requirements for Classes I, II and III at Low Temperatures

#### Class I

| Plate thickness, in mm | -11/-15ºC | | -16/-25ºC | | -26/-35ºC | | -36/-45ºC | | -46/-55ºC | |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| | **MS** | **HT** | **MS** | **HT** | **MS** | **HT** | **MS** | **HT** | **MS** | **HT** |
| $t \leq 10$ | A | AH | A | AH | B | AH | D | DH | D | DH |
| $10 < t \leq 15$ | A | AH | B | AH | D | DH | D | DH | D | DH |
| $15 < t \leq 20$ | A | AH | B | AH | D | DH | D | DH | E | EH |
| $20 < t \leq 25$ | B | AH | D | DH | D | DH | D | DH | E | EH |
| $25 < t \leq 30$ | B | AH | D | DH | D | DH | E | EH | E | EH |
| $30 < t \leq 35$ | D | DH | D | DH | D | DH | E | EH | E | EH |
| $35 < t \leq 45$ | D | DH | D | DH | E | EH | E | EH | $\emptyset$ | FH |
| $45 < t \leq 50$ | D | DH | E | EH | E | EH | $\emptyset$ | FH | $\emptyset$ | FH |

$\emptyset$ = Not applicable

#### Class II

| Plate thickness, in mm | -11/-15ºC | | -16/-25ºC | | -26/-35ºC | | -36/-45ºC | | -46/-55ºC | |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| | **MS** | **HT** | **MS** | **HT** | **MS** | **HT** | **MS** | **HT** | **MS** | **HT** |
| $t \leq 10$ | A | AH | B | AH | D | DH | D | DH | E | EH |
| $10 < t \leq 20$ | B | AH | D | DH | D | DH | E | EH | E | EH |
| $20 < t \leq 30$ | D | DH | D | DH | E | EH | E | EH | $\emptyset$ | FH |
| $30 < t \leq 40$ | D | DH | E | EH | E | EH | $\emptyset$ | FH | $\emptyset$ | FH |
| $40 < t \leq 45$ | E | EH | E | EH | $\emptyset$ | FH | $\emptyset$ | FH | $\emptyset$ | $\emptyset$ |
| $45 < t \leq 50$ | E | EH | E | EH | $\emptyset$ | FH | $\emptyset$ | FH | $\emptyset$ | $\emptyset$ |

$\emptyset$ = Not applicable

#### Class III

| Plate thickness, in mm | -11/-15ºC | | -16/-25ºC | | -26/-35ºC | | -36/-45ºC | | -46/-55ºC | |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| | **MS** | **HT** | **MS** | **HT** | **MS** | **HT** | **MS** | **HT** | **MS** | **HT** |
| $t \leq 10$ | B | AH | D | DH | D | DH | E | EH | E | EH |
| $10 < t \leq 20$ | D | DH | D | DH | E | EH | E | EH | $\emptyset$ | FH |
| $20 < t \leq 25$ | D | DH | E | EH | E | EH | E | FH | $\emptyset$ | FH |
| $25 < t \leq 30$ | D | DH | E | EH | E | EH | $\emptyset$ | FH | $\emptyset$ | FH |
| $30 < t \leq 35$ | E | EH | E | EH | $\emptyset$ | FH | $\emptyset$ | FH | $\emptyset$ | $\emptyset$ |
| $35 < t \leq 40$ | E | EH | E | EH | $\emptyset$ | FH | $\emptyset$ | FH | $\emptyset$ | $\emptyset$ |
| $40 < t \leq 50$ | E | EH | $\emptyset$ | FH | $\emptyset$ | FH | $\emptyset$ | $\emptyset$ | $\emptyset$ | $\emptyset$ |

$\emptyset$ = Not applicable

Single strakes required to be of Class III or of Grade E/EH or FH are to have breadths not less than 800+ 5L mm, maximum 1800 mm.

Plating materials for sternframes, rudder horns, rudders and shaft brackets are not to be of lower grades than those corresponding to the material classes given in 6.1.

Page 8 of 10 IACS Req. 1978/Rev.9 Corr.2 2021

---

## S6.3 Design temperature $t_D$

The design temperature $t_D$ is to be taken as the lowest mean daily average air temperature in the area of operation.

**Mean:** Statistical mean over observation period
**Average:** Average during one day and night
**Lowest:** Lowest during year

For seasonally restricted service the lowest value within the period of operation applies.

For the purpose of issuing a Polar Ship Certificate in accordance with the Polar Code, the design temperature $t_D$ shall be no more than 13ºC higher than the Polar Service Temperature (PST) of the ship.

In the Polar Regions, the statistical mean over observation period is to be determined for a period of at least 10 years.

Fig. 2 illustrates the temperature definition.

![Figure 2: Commonly used definitions of temperatures showing MDHT (Mean Daily High), MDAT (Mean Daily Average), and MDLT (Mean Daily Low) over a 12-month period.](A line graph with 'Air Temp' on the Y-axis and 'Month' (J F M A M J J A S O N D J) on the X-axis. Three sinusoidal curves represent MDHT at the top, MDAT in the middle, and MDLT at the bottom. An arrow points to the lowest point of the MDAT curve, labeled 'Lowest mean daily average temperature', and another arrow points to the lowest point of the MDLT curve, labeled 'Lowest mean daily low temperature'.)

**Fig. 2 Commonly used definitions of temperatures**

MDHT = Mean Daily High (or maximum) Temperature
MDAT = Mean Daily Average Temperature
MDLT = Mean Daily Low (or minimum) Temperature

Page 9 of 10 IACS Req. 1978/Rev.9 Corr.2 2021

---

## S6.4 Cold cargo for ships other than liquefied gas carriers

For ships other than liquefied gas carriers, intended to be loaded with liquid cargo having a temperature below -10º C, e.g. loading from cold onshore storage tanks during winter conditions, the material grade of cargo tank boundary plating is defined in Table 9 based on the following:

- $t_c$ design minimum cargo temperature in ºC
- steel grade corresponding to Class I as given in Table 8

The design minimum cargo temperature, $t_c$ is to be specified in the loading manual.

**End of Document**

Page 10 of 10 IACS Req. 1978/Rev.9 Corr.2 2021


================================================================================
# FILE: UR_S/ur-s7rev4.md
================================================================================

# S7 Minimum Longitudinal Strength Standards†

(1973)
(Rev.1 1976)
(Rev.2 1978)
(Rev.3 1989)
(Rev.4 May 2010)

### S7.0 Application

This UR does not apply to CSR Bulk Carriers and Oil Tankers.

### S7.1

The minimum midship section modulus at deck and keel for ships $90 \text{ m} \le L \le 500 \text{ m}$ and made of hull structural steel is

$$W_{min} = c L^2 B (C_b + 0.7) k \quad (\text{cm}^3)$$

where:
$L = \text{Rule length (m)}$
$B = \text{Rule breadth (m)}$
$C_b = \text{Rule block coefficient; } C_b \text{ is not to be taken less than 0.60}$
$c = c_n \text{ for new ships}$
$c = c_s \text{ for ships in service} = 0.9 c_n$

$$
c_n =
\begin{cases}
10.75 - \left( \frac{300 - L}{100} \right)^{3/2} & \text{for } 90 \text{ m} \le L \le 300 \text{ m} \\
10.75 & \text{for } 300 \text{ m} < L < 350 \text{ m} \\
10.75 - \left( \frac{L - 350}{150} \right)^{3/2} & \text{for } 350 \text{ m} \le L \le 500 \text{ m}
\end{cases}
$$

$k = \text{material factor}$
$k = 1.0 \text{ for ordinary hull structural steel,}$
$k < 1.0 \text{ for higher tensile steel according to S4.}$

### S7.2

Scantlings of all continuous longitudinal members of hull girder based on the section modulus requirement in S7.1 are to be maintained within $0.4 L$ amidships.

However, in special cases, based on consideration of type of ship, hull form and loading conditions, the scantlings may be gradually reduced towards the end of the $0.4 L$ part, bearing in mind the desire not to inhibit the vessel's loading flexibility.

### S7.3

In ships where part of the longitudinal strength material in the deck or bottom area are forming boundaries of tanks for oil cargoes or ballast water and such tanks are provided with an effective corrosion protection system, certain reductions in the scantlings of these boundaries are allowed. These reductions, however, should in no case reduce the minimum hull girder section modulus for a new ship by more than 5%.

### NOTE

The above standard refers in unrestricted service with minimum midship section modulus only. However, it may not be applicable to ships of unusual type or design, e.g. for ships of unusual main proportions and/or weight distributions.

'New Ships' are ships in the stage directly after completion.

† This Requirement is subject to periodical updating.

***

**Page 1 of 1 | IACS Req. 1973/Rev.4 2010**


================================================================================
# FILE: UR_S/ur-s8rev4.md
================================================================================

# S8 Bow Doors and Inner Doors

(1982)
(Rev. 2 1995)
(Corr. 1997)
(Rev. 3 Nov 2003)
(Rev. 4 Dec 2010)

## S8.1 General

### S8.1.1 Application

S8.1.1a These requirements are for the arrangement, strength and securing of bow doors and inner doors leading to a complete or long forward enclosed superstructures, or to a long non-enclosed superstructure, where fitted to attain minimum bow height equivalence.

The requirements apply to all ro-ro passenger ships and ro-ro cargo ships engaged on international voyages and also to ro-ro passenger ships and ro-ro cargo ships engaged only in domestic (non-international) voyages, except where specifically indicated otherwise herein.

The requirements are not applicable to high speed, light displacement craft as defined in the IMO Code of Safety for High Speed Craft.

S8.1.1b Two types of bow door are provided for:

- **Visor doors** opened by rotating upwards and outwards about a horizontal axis through two or more hinges located near the top of the door and connected to the primary structure of the door by longitudinally arranged lifting arms,
- **Side-opening doors** opened either by rotating outwards about a vertical axis through two or more hinges located near the outboard edges or by horizontal translation by means of linking arms arranged with pivoted attachments to the door and the ship. It is anticipated that side-opening bow doors are arranged in pairs.

Other types of bow door will be specially considered in association with the applicable requirements of these rules.

### S8.1.2 Arrangement

S8.1.2a Bow doors are to be situated above the freeboard deck. A watertight recess in the freeboard deck located forward of the collision bulkhead and above the deepest waterline fitted for arrangement of ramps or other related mechanical devices may be regarded as a part of the freeboard deck for the purpose of this requirement.

S8.1.2b An inner door is to be fitted. The inner door is to be part of the collision bulkhead. The inner door needs not be fitted directly above the bulkhead below, provided it is located within the limits specified for the position of the collision bulkhead, refer to regulation II-1/12 of the SOLAS Convention. A vehicle ramp may be arranged for this purpose, provided its position complies with regulation II-1/12 of the SOLAS Convention. If this is not possible a separate inner weathertight door is to be installed, as far as practicable within the limits specified for the position of the collision bulkhead.

S8.1.2c Bow doors are to be so fitted as to ensure tightness consistent with operational conditions and to give effective protection to inner doors. Inner doors forming part of the collision bulkhead are to be weathertight over the full height of the cargo space and arranged with fixed sealing supports on the aft side of the doors.

S8.1.2d Bow doors and inner doors are to be arranged so as to preclude the possibility of the bow door causing structural damage to the inner door or to the collision bulkhead in the case of damage to or detachment of the bow door. If this is not possible, a separate inner weathertight door is to be installed, as indicated in S8.1.2b.

S8.1.2e The requirements for inner doors are based on the assumption that vehicle are effectively lashed and secured against movement in stowed position.

### S8.1.3 Definitions

- **Securing device**: a device used to keep the door closed by preventing it from rotating about its hinges.
- **Supporting device**: a device used to transmit external or internal loads from the door to a securing device and from the securing device to the ship's structure, or a device other than a securing device, such as a hinge, stopper or other fixed device, that transmits loads from the door to the ship's structure.
- **Locking device**: a device that locks a securing device in the closed position.
- **Ro-ro passenger ship**: a passenger ship with ro-ro spaces or special category spaces.
- **Ro-ro spaces**: are spaces not normally sub-divided in any way and normally extending to either a substantial length or the entire length of the ship, in which motor vehicles with fuel in their tanks for their own propulsion and/or goods (packaged or in bulk, in or on rail or road cars, vehicles (including road or rail tankers), trailers, containers, pallets, demountable tanks or in or on similar stowage units or, other receptacles) can be loaded and unloaded normally in a horizontal direction.
- **Special category spaces**: are those enclosed vehicle spaces above or below the bulkhead deck, into and from which vehicles can be driven and to which passengers have access. Special category spaces may be accommodated on more than one deck provided that the total overall clear height for vehicles does not exceed 10m.

---

## S8.2 Strength Criteria

### S8.2.1 Primary structure and Securing and Supporting devices

S8.2.1a Scantlings of the primary members, securing and supporting devices of bow doors and inner doors are to be determined to withstand the design loads defined in S8.3, using the following permissible stresses:

- **sheer stress**: $\tau = \frac{80}{k} \text{ N/mm}^2$
- **bending stress**: $\sigma = \frac{120}{k} \text{ N/mm}^2$
- **equivalent stress**: $\sigma_c = \sqrt{\sigma^2 + 3\tau^2} = \frac{150}{k} \text{ N/mm}^2$

where $k$ is the material factor as given in S4, but is not to be taken less than 0.72 unless a direct fatigue analysis is carried out.

S8.2.1b The buckling strength of primary members is to be verified as being adequate.

S8.2.1c For steel to steel bearings in securing and supporting devices, the nominal bearing pressure calculated by dividing the design force by the projected bearing area is not to exceed $0.8 \sigma_F$, where $\sigma_F$ is the yield stress of the bearing material. For other bearing materials, the permissible bearing pressure is to be determined according to the manufacturer's specification.

S8.2.1d The arrangement of securing and supporting devices is to be such that threaded bolts do not carry support forces. The maximum tension in way of threads of bolts not carrying support forces is not to exceed:
$$\frac{125}{k} \text{ N/mm}^2$$

---

## S8.3 Design loads

### S8.3.1 Bow doors

S8.3.1a The design external pressure, in $\text{kN/m}^2$, to be considered for the scantlings of primary members, securing and supporting devices of bow doors is not to be less than the pressure normally used by the Society nor than:
$$P_e = 2.75 \lambda C_H (0.22 + 0.15 \tan \alpha) (0.4V \sin \beta + 0.6L^{0.5})^2$$

where:
- $V$: contractual ship's speed, in knots,
- $L$: ship's length, in m, but need not be taken greater than 200 metres,
- $\lambda$: coefficient depending on the area where the ship is intended to be operated:
  - $\lambda = 1$ for seagoing ships,
  - $\lambda = 0.8$ for ships operated in coastal waters,
  - $\lambda = 0.5$ for ships operated in sheltered waters,

*Note: Coastal waters and sheltered waters are defined according to the practice of each Classification Society. As an example, coastal waters may be defined as areas where significant wave heights do not exceed 4m for more than three hours a year and sheltered waters as areas where significant wave heights do not exceed 2m for more than three hours a year.*

- $C_H$:
  - $= 0.0125 L$ for $L < 80\text{m}$
  - $= 1$ for $L \ge 80\text{m}$
- $\alpha$: flare angle at the point to be considered, defined as the angle between a vertical line and the tangent to the side shell plating, measured in a vertical plane normal to the horizontal tangent to the shell plating,
- $\beta$: entry angle at the point to be considered, defined as the angle between a longitudinal line parallel to the centreline and the tangent to the shell plating in a horizontal plane.

S8.3.1b The design external forces, in kN, considered for the scantlings of securing and supporting devices of bow doors are not to be less than:
- $F_x = P_e A_x$
- $F_y = P_e A_y$
- $F_z = P_e A_z$

where:
- $A_x$: area, in $\text{m}^2$, of the transverse vertical projection of the door between the levels of the bottom of the door and the top of the upper deck bulwark, or between the bottom of the door and the top of the door, including the bulwark, where it is part of the door, whichever is lesser. Where the flare angle of the bulwark is at least 15 degrees less than the flare angle of the adjacent shell plating, the height from the bottom of the door may be measured to the upper deck or to the top of the door, whichever is lesser. In determining the height from the bottom of the door to the upper deck or to the top of the door, the bulwark is to be excluded.
- $A_y$: area, in $\text{m}^2$, of the longitudinal vertical projection of the door between the levels of the bottom of the door and the top of the upper deck bulwark, or between the bottom of the door and the top of the door, including the bulwark, where it is part of the door, whichever is lesser. Where the flare angle of the bulwark is at least 15 degrees less than the flare angle of the adjacent shell plating, the height from the bottom of the door may be measured to the upper deck or to the top of the door, whichever is lesser.
- $A_z$: area, in $\text{m}^2$, of the horizontal projection of the door between the bottom of the door and the top of the upper deck bulwark, or between the bottom of the door and the top of the door, including the bulwark, where it is part of the door, whichever is the lesser. Where the flare angle of the bulwark is at least 15 degrees less than the flare angle of the adjacent shell plating, the height from the bottom of the door may be measured to the upper deck or to the top of the door, whichever is lesser.
- $h$: height, in m, of the door between the levels of the bottom of the door and the upper deck or between the bottom of the door and the top of the door, whichever is the lesser,
- $l$: length, in m, of the door at a height $h/2$ above the bottom of the door,
- $W$: breadth, in m, of the door at a height $h/2$ above the bottom of the door,
- $P_e$: external pressure, in $\text{kN/m}^2$, as given in S8.3.1a with angles $\alpha$ and $\beta$ defined as follows:
  - $\alpha$: flare angle measured at the point on the bow door, $l / 2$ aft of the stem line on the plane $h/2$ above the bottom of the door, as shown in Figure 1,
  - $\beta$: entry angle measured at the same point as $\alpha$.

For bow doors, including bulwark, of unusual form or proportions, e.g. ships with a rounded nose and large stem angles, the areas and angles used for determination of the design values of external forces may require to be specially considered.

S8.3.1c For visor doors the closing moment $M_y$ under external loads, in kN.m, is to be taken as:
$$M_y = F_x a + 10 W c - F_z b$$

where:
- $W$: mass of the visor door, in t,
- $a$: vertical distance, in m, from visor pivot to the centroid of the transverse vertical projected area of the visor door, as shown in Figure 2,
- $b$: horizontal distance, in m, from visor pivot to the centroid of the horizontal projected area of the visor door, as shown in Figure 2,
- $c$: horizontal distance, in m, from visor pivot to the centre of gravity of visor mass, as shown in Figure 2.

S8.3.1d Moreover, the lifting arms of a visor door and its supports are to be dimensioned for the static and dynamic forces applied during the lifting and lowering operations, and a minimum wind pressure of $1.5 \text{kN/m}^2$ is to be taken into account.

### S8.3.2 Inner doors

S8.3.2a The design external pressure $p_e$, in $\text{kN/m}^2$, considered for the scantlings of primary members, securing and supporting devices and surrounding structure of inner doors is to be taken as the greater of the following:
- $p_e = 0.45 L$
- hydrostatic pressure $p_h = 10h$, where $h$ is the distance, in m, from the load point to the top of the cargo space,

where $L$ is the ship's length, as defined in S8.3.1a.

S8.3.2b The design internal pressure $p_i$, in $\text{kN/m}^2$, considered for the scantlings of securing devices of inner doors is not to be less than:
$$p_i = 25$$

---

## S8.4 Scantlings of bow doors

S8.4.1a The strength of bow doors is to be commensurate with that of the surrounding structure.

S8.4.1b Bow doors are to be adequately stiffened and means are to be provided to prevent lateral or vertical movement of the doors when closed. For visor doors adequate strength for the opening and closing operations is to be provided in the connections of the lifting arms to the door structure and to the ship structure.

### S8.4.2 Plating and secondary stiffeners

S8.4.2a The thickness of the bow door plating is not to be less than that required for the side shell plating, using bow door stiffener spacing, but in no case less than the minimum required thickness of fore end shell plating.

S8.4.2b The section modulus of horizontal or vertical stiffeners is not to be less than that required for end framing. Consideration is to be given, where necessary, to differences in fixity between ship's frames and bow doors stiffeners.

S8.4.2c The stiffener webs are to have a net sectional area, in $\text{cm}^2$, not less than:
$$A = \frac{Qk}{10}$$

where:
- $Q$: shear force, in kN, in the stiffener calculated by using uniformly distributed external pressure $p_e$ as given in S8.3.1a.

### S8.4.3 Primary structure

S8.4.3a The bow door secondary stiffeners are to be supported by primary members constituting the main stiffening of the door.

S8.4.3b The primary members of the bow door and the hull structure in way are to have sufficient stiffness to ensure integrity of the boundary support of the door.

S8.4.3c Scantlings of the primary members are generally to be supported by direct strength calculations in association with the external pressure given in S8.3.1a and permissible stresses given in S8.2.1a. Normally, formulae for simple beam theory may be applied to determine the bending stress. Members are to be considered to have simply supported end connections.

---

## S8.5 Scantlings of inner doors

### S8.5.1 General

S8.5.1a Scantlings of the primary members are generally to be supported by direct strength calculations in association with the external pressure given in S8.3.2a and permissible stresses given in S8.2.1a. Normally, formulae for simple beam theory may be applied.

S8.5.1b Where inner doors also serve as a vehicle ramps, the scantlings are not to be less than those required for vehicle decks.

S8.5.1c The distribution of the forces acting on the securing and supporting devices is generally to be supported by direct calculations taking into account the flexibility of the structure and the actual position and stiffness of the supports.

---

## S8.6 Securing and supporting of bow doors

### S8.6.1 General

S8.6.1a Bow doors are to be fitted with adequate means of securing and supporting so as to be commensurate with the strength and stiffness of the surrounding structure. The hull supporting structure in way of the bow doors is to be suitable for the same design loads and design stresses as the securing and supporting devices. Where packing is required, the packing material is to be of a comparatively soft type, and the supporting forces are to be carried by the steel structure only. Other types of packing may be considered. Maximum design clearance between securing and supporting devices is not generally to exceed 3 mm. A means is to be provided for mechanically fixing the door in the open position.

S8.6.1b Only the active supporting and securing devices having an effective stiffness in the relevant direction are to be included and considered to calculate the reaction forces acting on the devices. Small and/or flexible devices such as cleats intended to provide load compression of the packing material are not generally to be included in the calculations called for in S8.6.2e. The number of securing and supporting devices are generally to be the minimum practical whilst taking into account the requirements for redundant provision given in S8.6.2f and S8.6.2g and the available space for adequate support in the hull structure.

S8.6.1c For opening outwards visor doors, the pivot arrangement is generally to be such that the visor is self closing under external loads, that is $M_y > 0$. Moreover, the closing moment $M_y$ as given in S8.3.1c is to be not less than:
$$M_{yo} = 10 W c + 0.1(a^2 + b^2)^{0.5} (F_x^2 + F_z^2)^{0.5}$$

### S8.6.2 Scantlings

S8.6.2a Securing and supporting devices are to be adequately designed so that they can withstand the reaction forces within the permissible stresses given in S8.2.1a.

S8.6.2b For visor doors the reaction forces applied on the effective securing and supporting devices assuming the door as a rigid body are determined for the following combination of external loads acting simultaneously together with the self weight of the door:
- i) case 1: $F_x$ and $F_z$
- ii) case 2: $0.7 F_y$ acting on each side separately together with $0.7 F_x$ and $0.7 F_z$

where $F_x, F_y$ and $F_z$ are determined as indicated in S8.3.1b and applied at the centroid of projected areas.

S8.6.2c For side-opening doors the reaction forces applied on the effective securing and supporting devices assuming the door as a rigid body are determined for the following combination of external loads acting simultaneously together with the self weight of the door:
- i) case 1: $F_x, F_y$ and $F_z$ acting on both doors
- ii) case 2: $0.7 F_x$ and $0.7 F_z$ acting on both doors and $0.7 F_y$ acting on each door separately,

where $F_x, F_y$ and $F_z$ are determined as indicated in S8.3.1b and applied at the centroid of projected areas.

S8.6.2d The support forces as determined according to S8.6.2b i) and S8.6.2c i) shall generally give rise to a zero moment about the transverse axis through the centroid of the area $A_x$. For visor doors, longitudinal reaction forces of pin and/or wedge supports at the door base contributing to this moment are not to be of the forward direction.

S8.6.2e The distribution of the reaction forces acting on the securing and supporting devices may require to be supported by direct calculations taking into account the flexibility of the hull structure and the actual position and stiffness of the supports.

S8.6.2f The arrangement of securing and supporting devices in way of these securing devices is to be designed with redundancy so that in the event of failure of any single securing or supporting device the remaining devices are capable to withstand the reaction forces without exceeding by more than 20 per cent the permissible stresses as given in S8.2.1.

S8.6.2g For visor doors, two securing devices are to be provided at the lower part of the door, each capable of providing the full reaction force required to prevent opening of the door within the permissible stresses given in S8.2.1a. The opening moment $M_o$, in kN.m, to be balanced by this reaction force, is not to be taken less than:
$$M_o = 10 W d + 5 A_x a$$

where:
- $d$: vertical distance, in m, from the hinge axis to the centre of gravity of the door, as shown in Figure 2,
- $a$: as defined in S8.3.1c.

S8.6.2h For visor doors, the securing and supporting devices excluding the hinges should be capable of resisting the vertical design force $(F_z - 10W)$, in kN, within the permissible stresses given in S8.2.1a.

S8.6.2i All load transmitting elements in the design load path, from door through securing and supporting devices into the ship structure, including welded connections, are to be to the same strength standard as required for the securing and supporting devices. These elements include pins, supporting brackets and back-up brackets.

S8.6.2j For side-opening doors, thrust bearing has to be provided in way of girder ends at the closing of the two leaves to prevent one leaf to shift towards the other one under effect of unsymmetrical pressure (see example of Figure 3). Each part of the thrust bearing has to be kept secured on the other part by means of securing devices. Any other arrangement serving the same purpose may be proposed.

---

## S8.7 Securing and locking arrangement

### S8.7.1 Systems for operation

S8.7.1a Securing devices are to be simple to operate and easily accessible.

Securing devices are to be equipped with mechanical locking arrangement (self locking or separate arrangement), or to be of the gravity type. The opening and closing systems as well as securing and locking devices are to be interlocked in such a way that they can only operate in the proper sequence.

S8.7.1b Bow doors and inner doors giving access to vehicle decks are to be provided with an arrangement for remote control, from a position above the freeboard deck, of:
- the closing and opening of the doors, and
- associated securing and locking devices for every door.

Indication of the open/closed position of every door and every securing and locking device is to be provided at the remote control stations. The operating panels for operation of doors are to be inaccessible to unauthorized persons. A notice plate, giving instructions to the effect that all securing devices are to be closed and locked before leaving harbour, is to be placed at each operating panel and is to be supplemented by warning indicator lights.

S8.7.1c Where hydraulic securing devices are applied, the system is to be mechanically lockable in closed position. This means that, in the event of loss of the hydraulic fluid, the securing devices remain locked.

The hydraulic system for securing and locking devices is to be isolated from other hydraulic circuits, when in closed position.

### S8.7.2 Systems for indication/monitoring

S8.7.2a Separate indicator lights and audible alarms are to be provided on the navigation bridge and on the operating panel to show that the bow door and inner door are closed and that their securing and locking devices are properly positioned.

The indication panel is to be provided with a lamp test function. It shall not be possible to turn off the indicator light.

S8.7.2b The indicator system is to be designed on the fail safe principle and is to show by visual alarms if the door is not fully closed and not fully locked and by audible alarms if securing devices become open or locking devices become unsecured. The power supply for the indicator system for operating and closing doors is to be independent of the power supply for operating and closing the doors and is to be provided with a back-up power supply from the emergency source of power or other secure power supply e.g. UPS. The sensors of the indicator system are to be protected from water, ice formation and mechanical damage.

Note: The indicator system is considered designed on the fail - safe principal when:
1) The indication panel is provided with:
   - a power failure alarm
   - an earth failure alarm
   - a lamp test
   - separate indication for door closed, door locked, door not closed and door not locked.
2) Limit switches electrically closed when the door is closed (when more limit switches are provided they may be connected in series).
3) Limit switches electrically closed when securing arrangements are in place (when more limit switches are provided they may be connected in series).
4) Two electrical circuits (also in one multicore cable), one for the indication of door closed / not closed and the other for door locked / not locked.
5) In case of dislocation of limit switches, indication to show: not closed / not locked / securing arrangement not in place - as appropriate.

S8.7.2c The indication panel on the navigation bridge is to be equipped with a mode selection function "harbour/sea voyage", so arranged that audible alarm is given on the navigation bridge if the vessel leaves harbour with the bow door or inner door not closed or with any of the securing devices not in the correct position.

S8.7.2d A water leakage detection system with audible alarm and television surveillance is to be arranged to provide an indication to the navigation bridge and to the engine control room of leakage through the inner door.

S8.7.2e Between the bow door and the inner door a television surveillance system is to be fitted with a monitor on the navigation bridge and in the engine control room. The system is to monitor the position of the doors and a sufficient number of their securing devices. Special consideration is to be given for the lighting and contrasting colour of objects under surveillance.

S8.7.2f A drainage system is to be arranged in the area between bow door and ramp, or where no ramp is fitted, between the bow door and inner door. The system is to be equipped with an audible alarm function to the navigation bridge being set off when the water levels in these areas exceed 0.5m or the high water level alarm, whichever is lesser.

S8.7.2.g For ro-ro passenger ships on international voyages, the special category spaces and ro-ro spaces are to be continuously patrolled or monitored by effective means, such as television surveillance, so that any movement of vehicles in adverse weather conditions or unauthorized access by passengers thereto, can be detected whilst the ship is underway.

---

## S8.8 Operating and Maintenance Manual

S8.8.1 An Operating and Maintenance Manual for the bow door and inner door is to be provided on board and is to contain necessary information on:
- main particulars and design drawings
- special safety precautions
- details of vessel
- equipment and design loading (for ramps)
- key plan of equipment (doors and ramps)
- manufacturer's recommended testing for equipment
- description of equipment for
  - bow doors
  - inner bow doors
  - bow ramp/doors
  - side doors
  - stern doors
  - central power pack
  - bridge panel
  - engine control room panel
- service conditions
  - limiting heel and trim of ship for loading/unloading
  - limiting heel and trim for door operations
  - doors/ramps operating instructions
  - doors/ramps emergency operating instructions
- maintenance
  - schedule and extent of maintenance
  - trouble shooting and acceptable clearances
  - manufacturer's maintenance procedures
- register of inspections, including inspection of locking, securing and supporting devices, repairs and renewals.

This Manual is to be submitted for approval that the above mentioned items are contained in the OMM and that the maintenance part includes the necessary information with regard to inspections, troubleshooting and acceptance / rejection criteria.

Note: It is recommended that recorded inspections of the door supporting and securing devices be carried out by the ship's staff at monthly intervals or following incidents that could result in damage, including heavy weather or contact in the region of the shell doors. Any damages recorded during such inspections are to be reported to the Classification Society.

S8.8.2 Documented operating procedures for closing and securing the bow door and inner door are to be kept on board and posted at appropriate place.

---

![Figure 1: Definition of alpha and beta](Figure 1 showing side and top views of a bow door. The side view defines height h and shows the h/2 plane. Section A-A is a horizontal cut showing the entry angle beta relative to the centerline. Section B-B is a vertical cut showing the flare angle alpha relative to a vertical line.)

![Figure 2: Bow Door of Visor Type](Figure 2 showing elevation and plan views of a visor-type bow door. Elevation view shows pivot points, distances a, b, c, d relative to the pivot and center of gravity, and forces Fx, Fz. Plan view shows area Az and force Fy. Projected areas Ax and Ay are also indicated.)

![Figure 3: Thrust Bearing](Figure 3 showing a technical diagram of a thrust bearing arrangement for side-opening doors. It illustrates a pin or shaft assembly passing through structural plates with a conical bearing interface to resist lateral movement.)

---
**Footnote:**
It was agreed by IACS Council in August 1995 that this UR S8 should be uniformly applied by IACS Members to new ships as soon as possible but not later than 1 July 1996 and, with immediate effect, when approving plans for bow arrangements on new ships, Members should strongly recommend that the requirements as set out in the revised UR S8 are complied in full.

**Note:**
Changes introduced in Rev.4 are to be uniformly implemented by IACS Members from 1 January 2012.


================================================================================
# FILE: UR_S/ur-s9rev6.md
================================================================================

# S9 Side Shell Doors and Stern Doors

**(1984)**
**(Rev.1 1990)**
**(Rev.2 1993)**
**(Rev.3 1996)**
**(Rev.4 1996)**
**(Rev.5 Nov 2003)**
**(Rev.6 Dec 2010)**

## S9.1 General

### S9.1.1 Application

S9.1.1a These requirements are for the arrangement, strength and securing of side shell doors, abaft the collision bulkhead, and of stern doors leading to enclosed spaces.

The requirements apply to all ro-ro passenger ships and ro-ro cargo ships engaged on international voyages and also to ro-ro passenger ships and ro-ro cargo ships engaged only in domestic (non international) voyages, except where specifically indicated otherwise herein. The requirements are not applicable to high speed, light displacement craft as defined in the IMO Code of Safety for High Speed Craft.

### S9.1.2 Arrangement

S9.1.2a Stern doors for passenger vessels are to be situated above the freeboard deck. Stern doors for Ro-Ro cargo ships and side shell doors may be either below or above the freeboard deck.

S9.1.2b Side shell doors and stern doors are to be so fitted as to ensure tightness and structural integrity commensurate with their location and the surrounding structure.

S9.1.2c Where the sill of any side shell door is below the uppermost load line, the arrangement is to be specially considered (see IACS Interpretation LL 21).

S9.1.2d Doors should preferably open outwards.

### S9.1.3 Definitions

**Securing device** - a device used to keep the door closed by preventing it from rotating about its hinges or about pivotted attachments to the ship.

**Supporting device** - a device used to transmit external or internal loads from the door to a securing device and from the securing device to the ship's structure, or a device other than a securing device, such as a hinge, stopper or other fixed device, that transmits loads from the door to the ship's structure.

**Locking device** - a device that locks a securing device in the closed position.

**Notes:**

1. Revision 4 of the UR is applicable to new ships for which the request for classification is received on or after 1 July 1997.
2. Changes introduced in Rev.6 are to be uniformly implemented by IACS Members from 1 January 2012.

**Ro-ro passenger ship** - a passenger ship with ro-ro spaces or special category spaces.

**Ro-ro spaces** - are spaces not normally sub-divided in any way and extending to either a substantial length or the entire length of the ship, in which motor vehicles with fuel in their tanks for their own propulsion and/or goods (packaged or in bulk, in or on rail or road cars, vehicles (including road or rail tankers), trailers, containers, pallets, demountable tanks or in or on similar stowage units or, other receptacles) can be loaded and unloaded normally in a horizontal direction.

**Special category spaces** - are those enclosed vehicle spaces above or below the bulkhead deck, into and from which vehicles can be driven and to which passengers have access. Special category spaces may be accommodated on more than one deck provided that the total overall clear height for vehicles does not exceed 10m.

---

## S9.2 Strength Criteria

### S9.2.1 Primary structure and Securing and Supporting devices

S9.2.1a Scantlings of the primary members, securing and supporting devices of side shell doors and stern doors are to be determined to withstand the design loads defined in S9.3, using the following permissible stresses:

sheer stress: $\tau = \frac{80}{k} N/mm^2$

bending stress: $\sigma = \frac{120}{k} N/mm^2$

equivalent stress: $\sigma_c = \sqrt{\sigma^2 + 3\tau^2} = \frac{150}{k} N/mm^2$

where k is the material factor as given in S4, but is not to be taken less than 0.72 unless a direct strength analysis with regard to relevant modes of failures is carried out.

S9.2.1b The buckling strength of primary members is to be verified as being adequate.

S9.2.1c For steel to steel bearings in securing and supporting devices, the nominal bearing pressure calculated by dividing the design force by the projected bearing area is not to exceed $0.8 \sigma_F$, where $\sigma_F$ is the yield stress of the bearing material. For other bearing materials, the permissible bearing pressure is to be determined according to the manufacturer's specification.

S9.2.1d The arrangement of securing and supporting devices is to be such that threaded bolts do not carry support forces. The maximum tension in way of threads of bolts not carrying support forces is not to exceed $125/k N/mm^2$, with k defined in S9.2.1a.

---

## S9.3 Design loads

S9.3.1 The design forces, in kN, considered for the scantlings of primary members, securing and supporting devices of side shell doors and stern doors are to be not less than:

(i) Design forces for securing or supporting devices of doors opening inwards:
. external force: $F_e = A p_e + F_p$
. internal force: $F_i = F_o + 10 W$

(ii) Design forces for securing or supporting devices of doors opening outwards:
. external force: $F_e = A p_e$
. internal force: $F_i = F_o + 10 W + F_p$

(iii) Design forces for primary members:
. external force: $F_e = A p_e$
. internal force: $F_i = F_o + 10 W$

whichever is the greater,

where:

$A$ area, in $m^2$, of the door opening,

$W$ mass of the door, in t,

$F_p$ total packing force in kN. Packing line pressure is normally not to be taken less than 5N/mm,

$F_o$ the greater of $F_c$ and $5 A$ (kN),

$F_c$ accidental force, in kN, due to loose of cargo etc., to be uniformly distributed over the area A and not to be taken less than 300kN. For small doors such as bunker doors and pilot doors, the value of $F_c$ may be appropriately reduced. However, the value of $F_c$ may be taken as zero, provided an additional structure such as an inner ramp is fitted, which is capable of protecting the door from accidental forces due to loose cargoes.

$p_e$ external design pressure, in $kN/m^2$, determined at the centre of gravity of the door opening and not taken less than:

$10 ( T - Z_G ) + 25$ for $Z_G < T$
$25$ for $Z_G \ge T$

Moreover, for stern doors of ships fitted with bow doors, $p_e$ is not to be taken less than:

$P_e = 0.6 \lambda C_H (0.8 + 0.6L^{0.5})^2$

$\lambda$ coefficient depending on the area where the ship is intended to be operated:
$\lambda = 1$ for sea going ships,
$\lambda = 0.8$ for ships operated in coastal waters,
$\lambda = 0.5$ for ships operated in sheltered waters.

Note: Coastal waters and sheltered waters are defined according to the practice of each Classification Society. As an example, coastal waters may be defined as areas where significant wave heights do not exceed 4m for more than three hours a year and sheltered waters as areas where significant wave heights do not exceed 2m for more than three hours a year.

$C_H = 0.0125 L$ for $L < 80m$
$= 1$ for $L \ge 80m$

$L$ ship's length, in m, but need not be taken greater than 200 metres,

$T$ draught, in m, at the highest subdivision load line,

$Z_G$ height of the centre of area of the door, in m, above the baseline.

---

## S9.4 Scantlings of side shell doors and stern doors

### S9.4.1 General

S9.4.1a The strength of side shell doors and stern doors is to be commensurate with that of the surrounding structure.

S9.4.1b Side shell doors and stern doors are to be adequately stiffened and means are to be provided to prevent any lateral or vertical movement of the doors when closed. Adequate strength is to be provided in the connections of the lifting/manoeuvring arms and hinges to the door structure and to the ship's structure.

S9.4.1c Where doors also serve as vehicle ramps, the design of the hinges should take into account the ship angle of trim and heel which may result in uneven loading on the hinges.

S9.4.1d Shell door openings are to have well-rounded corners and adequate compensation is to be arranged with web frames at sides and stringers or equivalent above and below.

### S9.4.2 Plating and secondary stiffeners

S9.4.2a The thickness of the door plating is not to be less than the required thickness for the side shell plating, using the door stiffener spacing, but in no case less than the minimum required thickness of shell plating.

Where doors serve as vehicle ramps, the plating thickness is to be not less than required for vehicle decks.

S9.4.2b The section modulus of horizontal or vertical stiffeners is not to be less than that required for side framing. Consideration is to be given, where necessary, to differences in fixity between ship's frames and door stiffeners.

Where doors serve as vehicle ramps, the stiffener scantlings are not to be less than required for vehicle decks.

### S9.4.3 Primary Structure

S9.4.3a The secondary stiffeners are to be supported by primary members constituting the main stiffening of the door.

S9.4.3b The primary members and the hull structure in way are to have sufficient stiffness to ensure structural integrity of the boundary of the door.

S9.4.3c Scantlings of the primary members are generally to be supported by direct strength calculations in association with the design forces given in S9.3 and permissible stresses given in S9.2.1a. Normally, formulae for simple beam theory may be applied to determine the bending stresses. Members are to be considered to have simply supported end connections.

---

## S9.5 Securing and Supporting of Doors

### S9.5.1 General

S9.5.1a Side shell doors and stern doors are to be fitted with adequate means of securing and supporting so as to be commensurate with the strength and stiffness of the surrounding structure. The hull supporting structure in way of the doors is to be suitable for the same design loads and design stresses as the securing and supporting devices.

Where packing is required, the packing material is to be of a comparatively soft type, and the supporting forces are to be carried by the steel structure only. Other types of packing may be considered.

Maximum design clearance between securing and supporting devices is not generally to exceed 3mm.

A means is to be provided for mechanically fixing the door in the open position.

S9.5.1b Only the active supporting and securing devices having an effective stiffness in the relevant direction are to be included and considered to calculate the reaction forces acting on the devices. Small and/or flexible devices such as cleats intended to provide local compression of the packing material are not generally to be included in the calculations called for in S9.5.2b. The number of securing and supporting devices are generally to be the minimum practical whilst taking into account the requirement for redundant provision given in S9.5.2c and the available space for adequate support in the hull structure.

### S9.5.2 Scantlings

S9.5.2a Securing and supporting devices are to be adequately designed so that they can withstand the reaction forces within the permissible stresses given in S9.2.1a.

S9.5.2b The distribution of the reaction forces acting on the securing devices and supporting devices may require to be supported by direct calculations taking into account the flexibility of the hull structure and the actual position of the supports.

S9.5.2c The arrangement of securing devices and supporting devices in way of these securing devices is to be designed with redundancy so that in the event of failure of any single securing or supporting device the remaining devices are capable to withstand the reaction forces without exceeding by more than 20 per cent the permissible stresses as given in S9.2.1a.

S9.5.2d All load transmitting elements in the design load path, from the door through securing and supporting devices into the ship's structure, including welded connections, are to be to the same strength standard as required for the securing and supporting devices. These elements include pins, support brackets and back-up brackets.

---

## S9.6 Securing and Locking Arrangement

### S9.6.1 Systems for operation

S9.6.1a Securing devices are to be simple to operate and easily accessible.

Securing devices are to be equipped with mechanical locking arrangement (self locking or separate arrangement), or are to be of the gravity type. The opening and closing systems as well as securing and locking devices are to be interlocked in such a way that they can only operate in the proper sequence.

S9.6.1b Doors which are located partly or totally below the freeboard deck with a clear opening area greater than $6m^2$ are to be provided with an arrangement for remote control, from a position above the freeboard deck, of:
• the closing and opening of the doors,
• associated securing and locking devices.

For doors which are required to be equipped with a remote control arrangement, indication of the open/closed position of the door and the securing and locking device is to be provided at the remote control stations. The operating panels for operation of doors are to be inaccessible to unauthorized persons. A notice plate, giving instructions to the effect that all securing devices are to be closed and locked before leaving harbour, is to be placed at each operating panel and is to be supplemented by warning indicator lights.

S9.6.1c Where hydraulic securing devices are applied, the system is to be mechanically lockable in closed position. This means that, in the event of loss of the hydraulic fluid, the securing devices remain locked.

The hydraulic system for securing and locking devices is to be isolated from other hydraulic circuits, when closed position.

### S9.6.2 Systems for indication/monitoring

S9.6.2a The following requirements apply to doors in the boundary of special category spaces or ro-ro spaces, as defined in S9.1.3, through which such spaces may be flooded. For cargo ships, where no part of the door is below the uppermost waterline and the area of the door opening is not greater than $6m^2$, then the requirements of this section need not be applied.

S9.6.2b Separate indicator lights and audible alarms are to be provided on the navigation bridge and on each operating panel to indicate that the doors are closed and that their securing and locking devices are properly positioned.

The indication panel is to be provided with a lamp test function. It shall not be possible to turn off the indicator light.

S9.6.2c The indicator system is to be designed on the fail safe principle and is to show by visual alarms if the door is not fully closed and not fully locked and by audible alarms if securing devices become open or locking devices become unsecured. The power supply for the indicator system is to be independent of the power supply for operating and closing the doors and is to be provided with a backup power supply from the emergency source of power or secure power supply e.g. UPS.

Note: see 8.7.2b for fail safe principal design.

The sensors of the indicator system are to be protected from water, ice formation and mechanical damages.

S9.6.2d The indication panel on the navigation bridge is to be equipped with a mode selection function "harbour/sea voyage", so arranged that audible alarm is given on the navigation bridge if the vessel leaves harbour with any side shell or stern door not closed or with any of the securing devices not in the correct position.

S9.6.2e For passenger ships, a water leakage detection system with audible alarm and television surveillance is to be arranged to provide an indication to the navigation bridge and to the engine control room of any leakage through the doors.

For cargo ships, a water leakage detection system with audible alarm is to be arranged to provide an indication to the navigation bridge.

S9.6.2f For ro-ro passenger ships, on international voyages, the special category spaces and ro-ro spaces are to be continuously patrolled or monitored by effective means, such as television surveillance, so that any movement of vehicles in adverse weather conditions and unauthorized access by passengers thereto, can be detected whilst the ship is underway.

---

## S9.7 Operating and Maintenance Manual

S9.7.1 An Operating and Maintenance Manual for the side shell doors and stern doors is to be provided on board and is to contain the necessary information on:

• main particulars and design drawings
special safety precautions
details of vessel
equipment and design loading (for ramps)
key plan of equipment (doors and ramps)
manufacturer's recommended testing for equipment
description of equipment for
bow doors
inner bow doors
bow ramp/doors
side doors
stern doors
central power pack
bridge panel
engine control room panel

• service conditions
limiting heel and trim of ship for loading/unloading
limiting heel and trim for door operations
doors/ramps operating instructions
doors/ramps emergency operating instructions

• maintenance
schedule and extent of maintenance
trouble shooting and acceptable clearances
manufacturer's maintenance procedures

• register of inspections, including inspection of locking, securing and supporting devices, repairs and renewals.

This Manual is to be submitted for approval that the above mentioned items are contained in the OMM and that the maintenance part includes the necessary information with regard to inspections, troubleshooting and acceptance / rejection criteria.

Note: It is recommended that recorded inspections of the door supporting and securing devices be carried out by the ship's staff at monthly intervals or following incidents that could result in damage, including heavy weather or contact in the region of side shell and stern doors. Any damage recorded during such inspections is to be reported to the Classification Society.

S9.7.2 Documented operating procedures for closing and securing side shell and stern doors are to be kept on board and posted at the appropriate places.

---

## Explanatory Note

The external pressure applied on stern doors is derived from the formula considered in UR S8 for bow doors, assuming:

$\alpha = 0$ degree
$\beta = 90$ degrees
$V = 2$ knots

**End of Document**


================================================================================
# FILE: UR_W/UR-W24-Rev.5-Corr.1-Dec-2024-CLN-2.md
================================================================================

# W24 Cast Copper Alloy Propellers

(1996)
(Rev.1 1997)
(Rev.2 May 2004)
(Rev.3 May 2012)
(Corr.1 Jan 2013)
(Rev.4 July 2020)
(Rev.5 Sep 2023)
(Corr.1 Dec 2024)

## 1. Scope

1.1 These unified requirements are applicable to the manufacture, inspection and repair procedures of cast copper alloy propellers, blades and bosses.

1.2 Where the use of alternative alloys is proposed, particulars of chemical composition, mechanical properties and heat treatment are to be submitted for approval.

1.3 These requirements may also be used for the repair of propellers damaged in service, subject to prior agreement with the Classification Society.

**Notes:**

1.  New version of this UR supersedes the IACS unified requirements nos. K1 and K2 as well as the IACS Recommendation no. 4.
2.  Rev.3 of this UR is applicable to the moulding, casting, inspection and repair procedures of cast copper alloy propellers, blades and bosses from 1 July 2013.
3.  Changes introduced in Rev.4 are to be uniformly implemented by IACS Societies on ships contracted for construction on or after 1 July 2021, or when the application for certification of cast copper alloy propellers is dated on or after 1 July 2021, or the application for certification of manufacturer approval is dated on or after 1 July 2021.
4.  Changes introduced in Rev.5 are to be uniformly implemented by IACS Societies on ships contracted for construction on or after 1 January 2025, or when the application for certification of cast copper alloy propellers is dated on or after 1 January 2025, or the application for certification of manufacturer approval is dated on or after 1 January 2025.
5.  The "contracted for construction" date means the date on which the contract to build the vessel is signed between the prospective owner and the shipbuilder. For further details regarding the date of "contract for construction", refer to IACS Procedural Requirement (PR) No.29.

---

## 2. Foundry approval

### 2.1 Approval

All propellers and propeller components are to be manufactured by foundries approved by the Classification Society. The castings are to be manufactured and tested in accordance with the requirements of these rules.

### 2.2 Application for approval

It is the manufacturer's responsibility to assure that effective quality, process and production controls during manufacturing are adhered to within the manufacturing specification. The manufacturing specification shall be submitted to the Classification Society at the time of initial approval, and shall at least include the following particulars: description of the foundry facilities, copper alloy material specification, runner and feeder arrangements, manufacturing procedures, non-destructive testing and repair procedures.

### 2.3 Scope of the approval test

The scope of the approval test is to be agreed with the Classification Society. This should include the presentation of cast test coupons of the propeller materials in question for approval testing in order to verify that the chemical composition and the mechanical properties of these materials comply with these rules.

### 2.4 Inspection facilities

The foundry is to have an adequately equipped laboratory, manned by experienced personnel, for the testing of moulding materials chemical analyses, mechanical testing, microstructural testing of metallic materials and non-destructive testing. Where testing activities are assigned to other companies or other laboratory, additional information required by the Society is to be included.

## 3. Moulding and casting

### 3.1 Pouring

The pouring must be carried out into dried moulds using degassed liquid metal. The pouring is to be controlled as to avoid turbulences of flow. Special devices and/or procedures must prevent slag flowing into the mould.

### 3.2 Stress relieving

Subsequent stress relieving heat treatment may be performed to reduce the residual stresses. For this purpose, the manufacturer shall submit a specification containing the details of the heat treatment to the Classification Society for approval. For stress relieving temperatures and holding times see tables 4 and 5.

## 4. Quality of castings

### 4.1 Freedom from defects

All castings must have a workmanlike finish and must be free from defects which would be prejudicial to their proper application in service. Minor casting defects which may still be visible after machining such as small sand and slag inclusions, small cold shuts and scabs shall be trimmed off by the manufacturer in accordance with W24.11.

---

### 4.2 Removal of defects

Casting defects which may impair the serviceability of the castings, e.g. major non-metallic inclusions, shrinkage cavities, blow holes and cracks, are not permitted. They may be removed by one of the methods described in W24.11 and repaired within the limits and restrictions for the severity zones. Full description and documentation are to be available for the surveyor.

## 5. Dimensions, dimensional and geometrical tolerances

5.1 The verification of dimensions, the dimensional and geometrical tolerances is the responsibility of the manufacturer.

The report on the relevant examinations is to be submitted to the Surveyor, who may require checks to be made in his presence.

5.2 Static balancing is to be carried out on all propellers in accordance with the approved drawing. Dynamic balancing is necessary for propellers running above 500 rpm.

## 6. Chemical composition and metallurgical characteristics

### 6.1 Chemical composition

Typical copper propeller alloys are grouped into the four types CU 1, CU 2, CU 3 and CU 4 depending on their chemical composition as given in table 1. Copper alloys whose chemical composition deviate from the typical values of Table 1 must be specially approved by the Classification Society.

**Table 1: Typical chemical compositions of cast copper alloys for propellers**

| Alloy type | Cu(%) | Al(%) | Mn(%) | Zn(%) | Fe(%) | Ni(%) | Sn(%) | Pb(%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **CU1** | 52-62 | 0,5-3,0 | 0,5-4,0 | 35-40 | 0,5-2,5 | max 1,0 | max 1,5 | max 0,5 |
| **CU2** | 50-57 | 0,5-2.0 | 1,0-4,0 | 33-38 | 0,5-2,5 | 3,0-8,0 | max 1,5 | max 0,5 |
| **CU3** | 77-82 | 7,0-11,0 | 0,5-4,0 | max 1,0 | 2,0-6,0 | 3,0-6,0 | max 0,1 | max 0,03 |
| **CU4** | 70-80 | 6,5-9,0 | 8,0-20,0 | max 6,0 | 2,0-5,0 | 1,5-3,0 | max 1,0 | max 0,05 |

The manufacturer is to maintain records of the chemical analyses of the production casts, which are to be made available to the Surveyor.

### 6.2 Metallurgical characteristics

**Note:**

"The main constituents of the microstructure in the copper-based alloys categories CU 1 and CU 2 are alpha and beta phase.

Important properties such as ductility and resistance to corrosion fatigue are strongly influenced by the relative proportion of beta phase (too high a percentage of beta phase having a negative effect on these properties). To ensure adequate cold ductility and corrosion fatigue resistance, the proportion of beta phase is to be kept low. The concept of the zinc equivalent should be used as control since it summarizes the effect of the tendency of various chemical elements to produce beta phase in the structure."

The structure of CU 1 and CU 2 type alloys must contain an alpha phase component of at least 25 % as measured on a test bar by the manufacturer. To ensure adequate ductility and corrosion fatigue resistance, the proportion of beta phase is to be kept low. For this purpose, the zinc equivalent defined by the following formula shall not exceed a value of 45 %:

$$Zinc\ equivalent\ (\%)\ =\ 100\ -\ \frac{100\ \cdot\ \%Cu}{100\ +\ A}$$

In which $A = \%Sn + 5 \times \%Al - 0,5 \times \%Mn - 0,1 \times \%Fe - 2,3 \times \%Ni$.

**Note:**
The negative sign in front of the elements Mn, Fe and Ni signifies that these elements tend to reduce the proportion of beta phase.

The micro structure of alloy types CU 1 and CU 2 shall be verified by determining the proportion of alpha phase. For this purpose, at least one specimen shall be taken from each heat. The proportion of alpha phase shall be determined as the average value of 5 counts.

---

## 7. Mechanical properties and tests

### 7.1 Standardized alloys

The mechanical properties are to comply with the values given in table 2. These values are applicable to test specimens taken from separately cast samples in accordance with Fig. 1, or with a recognized standard.

**Note:**
These properties are a measure of the mechanical quality of the metal in each heat; and they are generally not representative of the mechanical properties of the propeller casting itself, which may be up to 30 % lower than that of a separately cast test coupon.

For integrally cast test specimens the requirements are specially to be agreed with the Classification Society.

**Table 2: Mechanical properties of cast copper alloys for propellers (separately cast test coupons)**

| Alloy type | Proof stress $R_{p\ 0,2}$ [N/mm²] min. | Tensile strength $R_m$ [N/mm²] min. | Elongation $A_5$ [%] min. |
| :--- | :---: | :---: | :---: |
| **CU1** | 175 | 440 | 20 |
| **CU2** | 175 | 440 | 20 |
| **CU3** | 245 | 590 | 16 |
| **CU4** | 275 | 630 | 18 |

---

![Figure 1: Test sample casting](A diagram showing the dimensions and shape of a test sample casting for propeller materials. Dimensions: H ≥ 100 mm, B ≥ 50 mm, L > 150 mm, T ≥ 15 mm, D ≥ 25 mm.)

### 7.2 Other alloys

The mechanical properties of alloys not meeting the minimum values of Table 2 are to comply with a specification approved by the Classification Society.

### 7.3 Tensile tests and specimens

Tensile tests and specimens are to be in accordance with UR W2.

Generally, the specimens shall be taken from separately cast sample pieces in accordance with W24.7.1. The test samples shall be cast in moulds made of the same material as the mould for the propeller and they must be cooled down under the same conditions as the propeller. At least one tensile test specimen shall be taken from each ladle.

If propellers are subjected to a heat treatment the test samples are to be heat treated together with them.

Where test specimens are to be taken from integrally cast test samples, this shall be the subject of special agreement with the Classification Society. Wherever possible, the test samples shall be located on the blades in an area lying between 0,5 to 0,6 R, where R is the radius of the propeller. The test sample material must be removed from the casting by non thermal procedures.

---

## 8. Definition of skew, severity zones

### 8.1 Definition of skew

The skew of a propeller is defined as follows:

The maximum skew angle of a propeller blade is defined as the angle, in projected view of the blade, between a line drawn through the blade tip and the shaft centreline and a second line through the shaft centreline which acts as a tangent to the locus of the mid-points of the helical blade section, see Fig 2.

High skew propellers have a skew angle greater than 25°, low skew propellers a skew angle of up to 25°.

![Figure 2: Definition of skew angle](A schematic diagram illustrating the definition of the skew angle of a propeller blade, showing the locus of mid-chord line, leading edge, and projected view.)

### 8.2 Severity zones

In order to relate the degree of inspection to the criticality of defects in propeller blades and to help reduce the risk of failure by fatigue cracking after repair, propeller blades are divided into the three severity zones designated A, B and C.

**Zone A** is the region carrying the highest operating stresses and which, therefore, requires the highest degree of inspection. Generally, the blade thicknesses are greatest in this area giving the greatest degree of restraint in repair welds and this in turn leads to the highest residual stresses in and around any repair welds. High residual tensile stresses frequently lead to fatigue cracking during subsequent service so that relief of these stresses by heat treatment is essential for any welds made in this zone. Welding is generally not permitted in Zone A and will only be allowed after special consideration by the Classification Society. Every effort should be made to rectify a propeller which is either defective or damaged in this area without recourse to welding even to the extent of reducing the scantlings, if this is acceptable. If a repair using welding is agreed, postweld stress relief heat treatment is mandatory.

**Zone B** is a region where the operation stresses may be high. Welding should preferably be avoided but generally is allowed subject to prior approval from the Classification Society. Complete details of the defect / damage and the intended repair procedure are to be submitted for each instance in order to obtain such approval.

---

**Zone C** is a region in which the operation stresses are low and where the blade thicknesses are relatively small so that repair welding is safer and, if made in accordance with an approved procedure is freely permitted.

### 8.2.1 Low-skew propellers

Zone A is in the area on the pressure side of the blade, from and including the fillet to 0,4R, and bounded on either side by lines at a distance 0,15 times the chord length $C_r$ from the leading edge and 0,2 times $C_r$ from the trailing edge, respectively (see Fig. 3). Where the hub radius ($R_b$) exceeds 0,27R, the other boundary of zone A is to be increased to 1,5$R_b$.

Zone A also includes the parts of the separate cast propeller hub which lie in the area of the windows as described in Fig. 5 and the flange and fillet area of controllable pitch and built-up propeller blades as described in Fig. 6.

Zone B is on the pressure side the remaining area up to 0,7R and on the suction side the area from the fillet to 0,7R (see Fig. 2).

Zone C is the area outside 0,7R on both sides of the blade. It also includes the surface of the hub of a monoblock propeller and all the surfaces of the hub of a controllable pitch propeller other than those designated Zone A above.

![Figure 3: Severity zones for integrally cast low skew propellers](A diagram showing the pressure side and suction side of a low skew propeller blade with severity zones A, B, and C marked based on radial distance and chord length fractions.)

### 8.2.2 High-skew propellers

Zone A is the area on the pressure face contained within the blade root-fillet and a line running from the junction of the leading edge with the root fillet to the trailing edge at 0.9 R and at passing through the mid-point of the blade chord at 0.7 R and a point situated at 0.3 of the chord length from the leading edge at 0.4 R. It also includes an area along the trailing edge on the suction side of the blade from the root to 0.9 R and with its inner boundary at 0.15 of the chord lengths from the trailing edge. Zone B constitutes the whole of the remaining blade surfaces. Zone A and B are illustrated in Fig. 4.

---

![Figure 4: Severity zones in blades with skew angles greater than 25°](A diagram showing the pressure side and suction side of a high skew propeller blade with severity zones A and B marked.)

![Figure 5: Severity zones for controllable pitch propeller boss](A diagram showing the severity zones A and C for a controllable pitch propeller boss, with zone A indicated inside and outside certain boundaries.)

---

![Figure 6: Severity zones for controllable pitch and built-up propeller](A series of diagrams (sections a-a, b-b and plan view) showing severity zones A and B for controllable pitch and built-up propellers, including flange and bore hole areas.)

**Note:**
The remaining surface of the propeller blades is to be divided into the severity zones as given for solid cast propellers (cf. Fig. 3 and Fig. 4)

---

## 9. Non-destructive testing

### 9.1 Qualification of personnel involved in NDT

For the qualification of personnel refer to UR W35.

### 9.2 Visual testing

All finished castings are to be 100% visually inspected by the manufacturer. Castings are to be free from cracks, hot tears or other imperfections which, due to their nature, degree or extent, will interfere with the use of the castings. A general visual examination is to be carried out by the Surveyor.

### 9.3 Liquid penetrant testing

Liquid penetrant testing procedure is to be submitted to the Society and is to be in accordance with ISO 3452-1:2013 or a recognized standard. The acceptance criteria are specified in W24.10.

The severity zone A is to be subjected to a liquid penetrant testing in the presence of the Surveyor.

In zones B and C the liquid penetrant testing is to be performed by the manufacturer and may be witnessed by the Surveyor upon his request.

If repairs have been made either by grinding, straightening or by welding the repaired areas are additionally to be subjected to the liquid penetrant testing independent of their location and/or severity zone.

### 9.4 Radiographic and ultrasonic testing

When required by the Society or when deemed necessary by the manufacturer, further non-destructive testing (e.g. radiographic and/or ultrasonic testing) are to be carried out. The acceptance criteria or applied quality levels are to be agreed between the manufacturer and the Classification Society in accordance with a recognized standard.

**Note:** due to the attenuating effect of ultrasound within cast copper alloys, ultrasonic testing may not be practical in some cases, depending on the shape/type/thickness, and grain growth direction of the casting.

In such cases, effective ultrasound penetration into the casting should be practically demonstrated on the item. This would normally be determined by way of back-wall reflection, and/or target features within the casting.

## 10. Acceptance criteria for liquid penetrant testing

### 10.1 Definitions of liquid penetrant indications

**Indication:** In the liquid penetrant testing an indication is the presence of detectable bleed-out of the penetrant liquid from the material discontinuities appearing at least 10 minutes after the developer has been applied.

**Relevant indication:** Only indications which have any dimension greater than 1.5mm shall be considered relevant for the categorization of indications.

**Non-linear indication:** indication having a length less than or equal to three times its width (i.e., $l \le 3 w$).

**Linear indication:** indication having a length greater than three times its width (i.e., $l > 3 w$).

**Aligned indications:**

a) Non-linear indications form an alignment when the distance between indications is less than 2mm and at least three indications are aligned. An alignment of indications is considered to be a unique indication and its length is equal to the overall length of the alignment.

b) Linear indications form an alignment when the distance between two indications is smaller than the length of the longest indication.

---

Illustration of liquid penetrant indication is given in Fig. 7.

![Figure 7: Shape of indications](Diagrams showing non-linear, linear, and aligned (both non-linear and linear) liquid penetrant indications with their defining dimensions $l, w, d_i, d_n$.)

### 10.2 Acceptance standard

The surface to be inspected is to be divided into reference areas of 100 cm². Each reference area may be square or rectangular with the major dimension not exceeding 250mm.

The area shall be taken in the most unfavourable location relative to the indication being evaluated.

The relevant indications detected shall, with respect to their size and number, not exceed the values given in the Table 3.

---

**Table 3: Allowable number and size of relevant indications in a reference area of 100 cm², depending on severity zones¹)**

| Severity zones | Max. total number of indications | Type of indication | Max. number of each type¹)²⁾ | Max. acceptable value for "l" of indications [mm] |
| :---: | :---: | :--- | :---: | :---: |
| **A** | 7 | Non-linear | 5 | 4 |
| | | Linear | 2 | 3 |
| | | Aligned | 2 | 3 |
| **B** | 14 | Non-linear | 10 | 6 |
| | | Linear | 4 | 6 |
| | | Aligned | 4 | 6 |
| **C** | 20 | Non-linear | 14 | 8 |
| | | Linear | 6 | 6 |
| | | Aligned | 6 | 6 |

**Notes:**
1) Singular non-linear indications less than 2 mm for zone A and less than 3 mm for the other zones are not considered relevant.
2) The total number of non-linear indications may be increased to the max. total number, or part thereof, represented by the absence of linear or aligned indications.

Areas which are prepared for welding are independent of their location always to be assessed according to zone A. The same applies to the welded areas after being finished machined and/or grinded.

---

## 11. Repair of defects

### 11.1 Definition

Indications exceeding the acceptance standard of Table 3, cracks, shrinkage cavities, sand, slag and other non-metallic inclusions, blow holes and other discontinuities which may impair the safe service of the propeller are defined as defects and must be repaired.

### 11.2 Repair procedures

In general the repairs shall be carried out by mechanical means, e. g. by grinding, chipping or milling. Welding may be applied subject to the agreement of the Classification Society if the requirements of URW24.11.3, 11.4 and / or 11.5 will be complied with.

After milling or chipping grinding is to be applied for such defects which are not to be welded. Grinding is to be carried out in such a manner that the contour of the ground depression is as smooth as possible in order to avoid stress concentrations or to minimise cavitation corrosion. Complete elimination of the defective material is to be verified by liquid penetrant testing.

Welding of areas less than 5 cm² is to be avoided.

### 11.3 Repair of defects in zone A

In zone A, repair welding will generally not be allowed unless specially approved by the Classification Society. Grinding may be carried out to an extent which maintains the blade thickness of the approved drawing.

The possible repair of defects which are deeper than those referred to above is to be considered by the Classification Society.

### 11.4 Repair of defects in zone B

Defects that are not deeper than $d_B$ (depth in zone B) = $(t/40)$ mm or 2 mm (whichever is greatest) should be removed by grinding.
**Note:** $t$ = min. local thickness in mm according to the Rules of the Classification Society

Those defects that are deeper than allowable for removal by grinding may be repaired by welding.

### 11.5 Repair of defects in zone C

In zone C, repair welds are generally permitted.

### 11.6 Repair documentation

The foundry is to maintain records of inspections, welding, and any subsequent heat treatment, traceable to each casting.

Before welding is started, full details of the extent and location of the repair, the proposed welding procedure, heat treatment and subsequent inspection procedures are to be submitted to the Classification Society for approval.

---

## 12. Welding repair procedure

### 12.1 General

Before welding is started, manufacturer shall submit to the Classification Society a detailed welding procedure specification covering the weld preparation, welding parameters, filler metals, preheating, post weld heat treatment and inspection procedures.

All weld repairs are to be carried out in accordance with qualified procedures, and, by welders who are qualified to a recognized standard. Welding Procedure Qualification Tests are to be carried out in accordance with Appendix A and witnessed by the Surveyor.

### 12.2 Preparation of welding repair

Defects to be repaired by welding are to be ground to sound material according to W24.11.2.

The welding grooves are to be prepared in such a manner which will allow a good fusion of the groove bottom.

The resulting ground areas are to be examined in the presence of the Surveyor by liquid penetrant testing in order to verify the complete elimination of defective material.

### 12.3 Welding repair procedure

Metal arc welding is to be used for all types of welding repair on cast copper alloy propellers.

Arc welding with coated electrodes and gas-shielded metal arc process (GMAW) are generally to be applied. Argon-shielded tungsten welding (GTAW) should be used with care due to the higher specific heat input of this process. Recommended filler metals, pre-heating and stress relieving temperatures are listed in Table 4.

All propeller alloys are generally to be welded in down-hand (flat) position. Where this cannot be done, gas-shielded metal arc welding should be carried out.

The section to be welded is to be clean and dry. Flux-coated electrodes are to be dried before welding according to the maker's instructions.

To minimize distortion and the risk of cracking, interpass temperatures are to be kept low. This is especially the case with CU 3 alloys.

Slag, undercuts and other defects are to be removed before depositing the next run.

All welding work is to be carried out preferably in the shop free from draughts and influence of the weather.

With the exception of alloy CU 3 (Ni-Al-bronze) all weld repairs are to be stress relief heat treated, in order to avoid stress corrosion cracking. However, stress relief heat treatment of alloy CU 3 propeller castings may be required after major repairs in zone B (and specially approved welding in Zone A) or if a welding consumable susceptible to stress corrosion cracking is used. In such cases the propeller is to be either stress relief heat treated in the temperature 450 to 500°C or annealed in the temperature range 650-800°C, depending on the extent of repair, c. f. Table 4.

The soaking times for stress relief heat treatment of copper alloy propellers should be in accordance with Table 5. The heating and cooling is to be carried out slowly under controlled conditions. The cooling rate after any stress relieving heat treatment shall not exceed 50°C/h until the temperature of 200°C is reached.

---

**Table 4: Recommended filler metals and heat treatments**

| Alloy type | Filler metal | Preheat temperature °C [min] | Interpass temperature °C [max] | Stress relief temperature °C | Hot straightening temperature °C |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **CU1** | Al-bronze¹⁾ Mn-bronze | 150 | 300 | 350-500 | 500-800 |
| **CU2** | Al-bronze Ni-Mn-bronze | 150 | 300 | 350-550 | 500-800 |
| **CU3** | Al-bronze Ni-Al-bronze²⁾ Mn-Al-bronze | 50 | 250 | 450-500 | 700-900 |
| **CU4** | Mn-Al-bronze | 100 | 300 | 450-600 | 700-850 |

**Notes:**
1) Ni-Al-bronze and Mn-Al-bronze are acceptable.
2) Stress relieving not required, if filler metal Ni-Al-bronze is used.

---

**Table 5: Soaking times for stress relief heat treatment of copper alloy propellers**

| Stress relief temperature [°C] | Alloy grade CU1 and CU2 - Hours per 25 mm thickness | Alloy grade CU1 and CU2 - Max. recommended total time hours | Alloy grade CU3 and CU4 - Hours per 25 mm thickness | Alloy grade CU3 and CU4 - Max. recommended total time hours |
| :---: | :---: | :---: | :---: | :---: |
| **350** | 5 | 15 | - | - |
| **400** | 1 | 5 | - | - |
| **450** | 1/2 | 2 | 5 | 15 |
| **500** | 1/4 | 1 | 1 | 5 |
| **550** | 1/4¹⁾ | 1/2¹⁾ | 1/2²⁾ | 2²⁾ |
| **600** | - | - | 1/4²⁾ | 1²⁾ |

**Note:**
1) 550°C only applicable for CU 2 alloys.
2) 550°C and 600°C only applicable for CU 4 alloys.

## 13. Straightening

### 13.1 Application of load

For hot and cold straightening purposes, static loading only is to be used.

### 13.2 Hot straightening

Weld repaired areas may be subject to hot straightening, provided it can be demonstrated that weld properties are not impaired by the hot straightening operations.

Straightening of a bent propeller blade or a pitch modification should be carried out after heating the bent region and approximately 500 mm wide zones on either side of it to the suggested temperature range given in Table 4.

The heating should be slow and uniform and the concentrated flames such as oxy-acetylene and oxy-propane should not be used. Sufficient time should be allowed for the temperature to become fairly uniform through the full thickness of the blade section. The temperature must be maintained within the suggested range throughout the straightening operation. A thermocouple instrument or temperature indicating crayons should be used for measuring the temperature.

### 13.3 Cold straightening

Cold straightening should be used for minor repairs of tips and edges only. Cold straightening on CU 1, CU 2 and CU 4 bronze should always be followed by a stress relieving heat treatment, see Table 4.

## 14. Identification and marking

### 14.1 Identifications

The manufacturer is to adopt a system for the identification of all castings, which enable the material to be traced to its original cast. The Surveyor is to be given full facilities for so tracing the castings when required.

---

### 14.2 Marking

Each finished casting propeller shall be marked by the manufacturer at least with the following particulars:

a) Grade of cast material or corresponding abbreviated designation
b) Manufacturer's mark
c) Heat number, casting number or another identification mark enabling the manufacturing process to be traced back
d) Date of final inspection
e) Number of the Society's certificate
f) Ice class symbol, where applicable
g) Skew angle for high skew propellers.

## 15. Manufacturer's certificates

For each casting propeller the manufacturer is to supply to the Surveyor a certificate containing the following details:

a) Purchaser and order number
b) Shipbuilding project number, if known
c) Description of the casting with drawing number
d) Diameter, number of blades, pitch, direction of turning
e) Grade of alloy and chemical composition of each heat
f) Heat or casting number
g) Final weight
h) Results of non-destructive tests and details of test procedure where applicable
i) Portion of alpha-structure for CU 1 and CU 2 alloys
j) Results of the mechanical tests
k) Casting identification No.
l) Skew angle for high skew propellers, see W24.8.1

---

# Appendix A: Welding procedure qualification tests for repair of cast copper alloy propeller

## 1. General

1.1 This document gives requirements for qualification tests of welding procedures intended for the repair of cast copper alloy propellers.

1.2 For the welding procedure approval the welding procedure qualification tests are to be carried out with satisfactory results. The qualification tests are to be carried out with the same welding process, filler metal, preheating and stress-relieving treatment as those intended applied by the actual repair work. Welding procedure specification (WPS) is to refer to the test results achieved during welding procedure qualification testing.

1.3 Welding procedures qualified at a manufacturer are valid for welding in workshops under the same technical and quality management.

## 2. Test piece and welding of sample

2.1 The test assembly, consisting of cast samples, is to be of a size sufficient to ensure a reasonable heat distribution and according to Fig. A.1 with the minimum dimensions:

![Figure A.1: Test piece for welding repair procedure](A diagram showing a test assembly for welding repair procedure qualification. Two cast plates are joined by a weld. Dimensions: a: minimum value 150mm; b: minimum value 300mm; t: material thickness. 1 indicates joint preparation.)

1: Joint preparation and fit-up as detailed in the preliminary welding procedure specification
a: minimum value 150mm
b: minimum value 300mm
t: material thickness.

A test sample of minimum 30mm thickness is to be used.

2.2 Preparation and welding of test pieces are to be carried out in accordance with the general condition of repair welding work which it represents.

2.3 Welding of the test assemblies and testing of test specimens are to be witnessed by the Surveyor.

---

## 3. Examinations and tests

3.1 Test assembly is to be examined non-destructively and destructively in accordance with the Table A.1 and Fig. A.2:

**Table A.1: Type of tests and extent of testing**

| Type of test (1) | Extent of testing |
| :--- | :--- |
| Visual testing | 100% as per article 3.2 |
| Liquid penetrant testing | 100% as per article 3.2 |
| Transverse tensile test | Two specimens as per article 3.3 |
| Macro examination | Three specimens as per article 3.4 |

**Note 1:** bend or fracture test are at the discretion of the Classification Society

![Figure A.2: Test Specimen](A diagram showing the layout for cutting test specimens from the weld assembly. It shows areas for Discard, Macro specimens, and Tensile test specimens across a 300mm x 300mm area.)

### 3.2 Non-destructive testing

Test assembly is to be examined by visual and liquid penetrant testing prior to the cutting of test specimen. In case, that any post-weld heat treatment is required or specified, non-destructive testing is to be performed after heat treatment.

No cracks are permitted. Imperfections detected by liquid penetrant testing are to be assessed in accordance with W24.10.

---

### 3.3 Tensile test:

Two tensile tests are to be prepared as shown in UR W2 2.4.2.8 b). Alternatively tensile test specimens according to recognized standards acceptable to the Classification Society may be used. The tensile strength shall meet the values given in Table A.2.

**Table A.2: Required tensile strength values**

| Alloy Type | Tensile Strength $R_m$ (N/mm²) min. |
| :---: | :---: |
| **CU1** | 370 |
| **CU2** | 410 |
| **CU3** | 500 |
| **CU4** | 550 |

### 3.4 Macroscopic examination

Three test specimens are to be prepared and etched on one side to clearly reveal the weld metal, the fusion line and the heat affected zone (see Fig. 9).

A suitable etchant for this purpose is:

*   5 g iron (III) chloride
*   30 ml hydrochloric acid (cone)
*   100 ml water.

The test specimens are to be examined for imperfections present in the weld metal and the heat affected zone. Cracks and lack of fusion are not permitted. Imperfections such as pores, or slag inclusions, greater than 3 mm are not permitted.

### 3.5 Re-testing

If the test piece fails to comply with any of the requirements of this Appendix, reference is made to re-test procedures given in UR W28.

## 4. Test record

4.1 Welding conditions for test assemblies and test results are to be recorded in welding procedure qualification record. Forms of welding procedure qualification records can be taken from the Society's rules or from relevant standards.

4.2 A statement of the results of assessing each test piece, including repeat tests, is to be made for each welding procedure qualification record. The relevant items listed for the WPS are to be included.

4.3 The welding procedure qualification record is to be signed by the Surveyor witnessing the test and is to include the Society's identification.

---

## 5. Range of approval

### 5.1 General

All the conditions of validity stated below are to be met independently of each other. Changes outside of the ranges specified are to require a new welding procedure test.

A qualification of a WPS obtained by a manufacturer is valid for welding in workshops or sites under the same technical and quality control of that manufacturer.

### 5.2 Base metal

The range of qualification related to base metal is given in Table A.3.

**Table A.3: Range of qualification for base metal**

| Copper alloy material grade used for qualification | Range of approval |
| :---: | :---: |
| **CU1** | CU1 |
| **CU2** | CU1; CU2 |
| **CU3** | CU3 |
| **CU4** | CU4 |

### 5.3 Thickness

The qualification of a WPS carried out on a weld assembly of thickness $t$ is valid for the thickness range given in Table A.4.

**Table A.4: Range of qualification for thickness**

| Thickness of the test piece, $t$ (mm) | Range of approval |
| :---: | :---: |
| $30 \le t$ | $\ge 3\ mm$ |

### 5.4 Welding position

Approval for a test made in any position is restricted to that position.

### 5.5 Welding process

5.5.1 The approval is only valid for the welding process used in the welding procedure test. Single run is not qualified by multi-run butt weld test used in this UR.

---

### 5.6 Filler metal

The approval is only valid for the filler metal used in the welding procedure test.

### 5.7 Heat input

The upper limit of heat input approved is 25% greater than that used in welding the test piece. The lower limit of heat input approved is 25% lower than that used in welding the test piece.

### 5.8 Preheating and interpass temperature

The minimum preheating temperature is not to be less than that used in the qualification test. The maximum interpass temperature is not to be higher than that used in the qualification test.

### 5.9 Post-weld heat treatment

The heat treatment used in the qualification test is to be specified in pWPS. Soaking time may be adjusted as a function of thickness.

**End of Document**


================================================================================
# FILE: UR_W/UR-W27-Rev.3-Corr.1-Dec-2024-CLN.md
================================================================================

# W27 Cast Steel Propellers

(May 2000)
(Rev.1 May 2004)
(Rev.2 July 2020)
(Corr.1 Sep 2020)
(Rev.3 Sep 2023)
(Corr.1 Dec 2024)

## 1. Scope

1.1 These unified requirements are applicable to the manufacture, inspection and repair procedures of cast steel propellers, blades and bosses.

1.2 Where the use of alternative alloys is proposed, particulars of chemical composition, mechanical properties and heat treatment are to be submitted for approval.

1.3 These requirements may also be used for the repair of propellers damaged in service, subject to prior agreement with the Classification Society.

---

**Notes:**

1. Changes introduced in Rev.2 are to be uniformly implemented by IACS Societies on ships contracted for construction on or after 1 July 2021, or when the application for certification of cast steel propellers is dated on or after 1 July 2021, or the application for certification of manufacturer approval is dated on or after 1 July 2021.
2. Changes introduced in Rev.3 are to be uniformly implemented by IACS Societies on ships contracted for construction on or after 1 January 2025, or when the application for certification of cast steel propellers is dated on or after 1 January 2025, or the application for certification of manufacturer approval is dated on or after 1 January 2025.
3. The "contracted for construction" date means the date on which the contract to build the vessel is signed between the prospective owner and the shipbuilder. For further details regarding the date of "contract for construction", refer to IACS Procedural Requirement (PR) No.29.

---
Page 1 of 16 IACS Req. 2000/ Corr.1 Dec 2024

## 2. Foundry approval

### 2.1 General

All propellers, blades and bosses are to be manufactured by foundries approved by the Classification Society. The castings are to be manufactured and tested in accordance with the requirements of these rules.

### 2.2 Application for approval

It is the manufacturer's responsibility to assure that effective quality, process and production controls during manufacturing are adhered to within the manufacturing specification. The manufacturing specification shall be submitted to the Classification Society at the time of initial approval, and shall at least include the following particulars: description of the foundry facilities, steel material specification, runner and feeder arrangements, manufacturing procedures, non-destructive testing and repair procedures.

### 2.3 Scope of the approval test

The scope of the approval test is to be agreed with the Classification Society. This should include the presentation of cast test coupons of the propeller materials in question for approval testing in order to verify that the chemical composition and the mechanical properties of these materials comply with these rules.

### 2.4 Inspection facilities

The foundry is to have an adequately equipped laboratory, manned by experienced personnel, for the testing of moulding materials chemical analyses, mechanical testing, microstructural testing of metallic materials and non-destructive testing. Where testing activities are assigned to other companies or other laboratory, additional information required by the Society is to be included.

## 3. Quality of castings

### 3.1 Freedom from defects

All castings are to have a workmanlike finish and are to be free from imperfections defects which would be prejudicial to their proper application in service.

Minor casting defects which may still be visible after machining such as small sand and slag inclusions, small cold shuts and scabs shall be trimmed off by the manufacturer in accordance with W27.11.

### 3.2 Removal of defects

Casting defects which may impair the serviceability of the castings, e.g. major non-metallic inclusions, shrinkage cavities, blow holes and cracks, are not permitted. They may be removed by one of the methods described in W27.11 and repaired within the limits and restrictions for the severity zones. Full description and documentation must be available for the surveyor.

---
Page 2 of 16 IACS Req. 2000/ Corr.1 Dec 2024

## 4. Dimensions, dimensional and geometrical tolerances

4.1 The verification of dimensions, the dimensional and geometrical tolerances is the responsibility of the manufacturer.

The report on the relevant examinations is to be submitted to the Surveyor, who may require checks to be made in his presence.

4.2 Static balancing is to be carried out on all propellers in accordance with the approved drawing. Dynamic balancing may be necessary for propellers running above 500 rpm.

## 5. Chemical composition

5.1 Typical cast steel propeller alloys are grouped into four types depending on their chemical composition as given in Table 1. Cast steel whose chemical composition deviate from the typical values of Table 1 must be specially approved by the Classification Society.

**Table 1 - Typical chemical composition for steel propeller castings**

| Alloy type | C Max. (%) | Mn Max. (%) | Cr (%) | Mo¹⁾ Max. (%) | Ni (%) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Martensitic (12 Cr 1 Ni) | 0,15 | 2,0 | 11,5-17,0 | 0,5 | Max. 2,0 |
| Martensitic (13 Cr 4 Ni) | 0,06 | 2,0 | 11,5-17,0 | 1,0 | 3,5-5,0 |
| Martensitic (16 Cr 5 Ni) | 0,06 | 2,0 | 15,0-17,5 | 1,5 | 3,5-6,0 |
| Austenitic (19 Cr 11 Ni) | 0,12 | 1,6 | 16,0-21,0 | 4,0 | 8,0-13,0 |

**Note:** 1) Minimum values are to be in accordance with recognised national or international standards.

5.2 The manufacturer is to maintain records of the chemical analyses of the production casts, which are to be made available to the Surveyor so that he can satisfy himself that the chemical composition of each casting is within the specified limits.

## 6. Heat treatment

Martensitic castings are to be austenitized and tempered. Austenitic castings should be solution treated.

## 7. Mechanical properties

7.1 The mechanical properties are to comply with values given in Table 2. These values refer to the test specimens machined from integrally cast test coupons attached to the hub or on the blade. The thickness of test coupon is to be in accordance with a recognized standard.

---
Page 3 of 16 IACS Req. 2000/ Corr.1 Dec 2024
Page 4 of 16 IACS Req. 2000/ Corr.1 Dec 2024

**Table 2 – Mechanical Properties for steel propeller castings**

| Alloy type | Proof stress Rp0.2 min. (N/mm²) | Tensile strength Rm min. (N/mm²) | Elongation A5 min. (%) | Red. of area Z min. (%) | Charpy V-notch¹⁾ Energy min. (J) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| 12 Cr 1Ni | 440 | 590 | 15 | 30 | 20 |
| 13 Cr 4Ni | 550 | 750 | 15 | 35 | 30 |
| 16 Cr 5Ni | 540 | 760 | 15 | 35 | 30 |
| 19 Cr 11Ni | 180²⁾ | 440 | 30 | 40 | - |

¹⁾ Not required for general service and the lowest Ice class notations. For other Ice class notations, tests are to be made at -10°C.
²⁾ Rp1,0 value is 205 N/mm².

7.2 Where possible, the test coupons attached on blades are to be located in an area between 0.5 to 0.6R, where R is the radius of the propeller.

7.3 The test bars are not to be detached from the casting until the final heat treatment has been carried out. Removal is to be by non-thermal procedures.

7.4 Separately cast test bars may be used subject to prior approval of the Classification Society. The test bars are to be cast from the same heat as the castings represented and heat treated with the castings represented.

7.5 At least one set of mechanical tests is to be made on material representing each casting in accordance with UR W2.

7.6 As an alternative to 7.5, where a number of small propellers of about the same size, and less than 1m in diameter, are made from one cast and heat treated in the same furnace charge, a batch testing procedure may be adopted using separately cast test samples of suitable dimensions. At least one set of mechanical tests is to be provided for each multiple of five castings in the batch.

## 8. Definition of skew, severity zones

8.1 In order to relate the degree of inspection to the criticality of imperfections in propeller blades and to help reduce the risk of failure by fatigue cracking after repair, propeller blades are divided into three severity zones designated A, B and C. Definition of skew, and, severity zones are given in UR W24.

## 9. Non-destructive testing

### 9.1 Qualification of personnel involved in NDT

For the qualification of personnel refer to UR W35.

---
Page 5 of 16 IACS Req. 2000/ Corr.1 Dec 2024

### 9.2 Visual testing

All finished castings are to be 100% visually inspected by the manufacturer. Castings are to be free from cracks, hot tears or other imperfections which, due to their nature, degree or extent, will interfere with the use of the castings. A general visual examination is to be carried out by the Surveyor.

### 9.3 Liquid penetrant testing

Liquid penetrant testing procedure is to be submitted to the Classification Society and is to be in accordance with ISO 3452-1:2013 or a recognized standard. The acceptance criteria are specified in W27.10.

For all propellers, separately cast blades and hubs, the surfaces covered by severity zones A, B and C are to be liquid penetrant tested. Testing of zone A is to be undertaken in the presence of the Surveyor, whilst testing of zone B and C may be witnessed by the Surveyor upon his request.

If repairs have been made either by grinding or by welding, the repaired areas are additionally to be subjected to the liquid penetrant testing independent of their location and/or severity zone. Weld repairs are, independent of their location, always to be assessed according to zone A.

### 9.4 Magnetic particle testing

Magnetic particle testing may be used in lieu of liquid penetrant testing for examination of martensitic stainless steels castings.

Magnetic particle testing procedure is to be submitted to the Classification Society and is to be in accordance with ISO 9934-1:2016 or a recognized standard.

### 9.5 Radiographic and ultrasonic testing

When required by the Classification Society or when deemed necessary by the manufacturer, further non-destructive testing (e.g. radiographic and/or ultrasonic testing) are to be carried out. The acceptance criteria or applied quality levels are then to be agreed between the manufacturer and the Classification Society in accordance with a recognized standard.

**Note:** due to the attenuating effect of ultrasound within austenitic steel castings, ultrasonic testing may not be practical in some cases, depending on the shape/type/thickness, and grain-growth direction of the casting.

## 10. Acceptance criteria for liquid penetrant testing and magnetic particle testing

### 10.1 Definitions of liquid penetrant indications

**Indication:** In the liquid penetrant testing an indication is the presence of detectable bleed-out of the penetrant liquid from the material discontinuities appearing at least 10 minutes after the developer has been applied.

**Relevant indication:** only indications which have any dimension greater than 1.5mm shall be considered relevant for the categorization of indications.

---
Page 6 of 16 IACS Req. 2000/ Corr.1 Dec 2024

**Non-linear indication:** indication having a length less than or equal to three times its width (i.e. $l \le 3w$)

**Linear indication:** indication having a length greater than three times its width (i.e. $l > 3w$).

**Aligned indications:**

a) Non-linear indications form an alignment when the distance between indications is less than 2mm and at least three indications are aligned. An alignment of indications is considered to be a unique indication and its length is equal to the overall length of the alignment.

b) Linear indications form an alignment when the distance between two indications is smaller than the length of the longest indication.

Illustration of liquid penetrant indications is given in Fig. 1.

![Figure 1: Shape of indications](Diagram showing non-linear, linear, and aligned liquid penetrant indications with labels for length (l), width (w), and distance between indications (d).)

---
Page 7 of 16 IACS Req. 2000/ Corr.1 Dec 2024

### 10.2 Acceptance standard

The surface to be inspected is to be divided into reference areas of 100 cm². Each reference area may be square or rectangular with the major dimension not exceeding 250mm.

The area shall be taken in the most unfavourable location relative to the indication being evaluated.

The relevant indications detected shall with respect to their size and number, not exceed the values given in the Table 3.

Areas which are prepared for welding are independent of their location always to be assessed according to zone A. The same applies to the welded areas after being finished machined and/or grinded.

**Table 3 – Allowable number and size of relevant indications in a reference area of 100 cm², depending on severity zones¹⁾**

| Severity zones | Max. total number of indications | Type of indication | Max. number for each type ¹⁾ ²⁾ | Max. dimension of indication (mm) |
| :---: | :---: | :---: | :---: | :---: |
| A | 7 | Non-linear | 5 | 4 |
| | | Linear | 2 | 3 |
| | | Aligned | 2 | 3 |
| B | 14 | Non-linear | 10 | 6 |
| | | Linear | 4 | 6 |
| | | Aligned | 4 | 6 |
| C | 20 | Non-linear | 14 | 8 |
| | | Linear | 6 | 6 |
| | | Aligned | 6 | 6 |

¹⁾ Single non-linear indications less than 2mm in zone A and less than 3mm in for the other zones are not considered relevant.
²⁾ The total number of non-linear indications may be increased to the maximum total number, or part thereof, represented by the absence of linear or aligned indications.

## 11. Repair of defects

11.1 Defective castings are to be repaired in accordance with the requirements given in 11.2 to 11.7 and, where applicable, the requirements of W27.12.

11.2 In general the repairs are to be carried out by mechanical means, e.g. by grinding, chipping or milling. The resulting grooves are to be blended into the surrounding surface so as to avoid any sharp contours. Complete elimination of the defective material is to be verified by liquid penetrant testing, or magnetic particle testing if applicable.

11.3 Weld repairs are to be undertaken only when they are considered to be necessary and have prior approval of the Surveyor.

11.4 The excavations are to be suitably shaped to allow good access for welding. The resulting grooves are to be subsequently ground smooth and complete elimination of the defective material is to be verified by liquid penetrant testing. Welds having an area less than 5cm² are to be avoided.

---
Page 8 of 16 IACS Req. 2000/ Corr.1 Dec 2024

11.5 Grinding in severity zone A may be carried out to an extent that maintains the blade thickness. Repair welding is generally not permitted in severity Zone A and will only be allowed after special consideration by the Classification Society.

11.6 Defects in severity zone B that are not deeper than $t/40$ mm ("t" is the minimum local thickness according to the Rules) or 2mm, whichever is greatest, are to be removed by grinding. Those defects that are deeper may be repaired by welding subject to prior approval from the Classification Society.

11.7 Repair welding is generally permitted in severity zone C.

### 11.8 Repair documentation

The foundry is to maintain records of inspections, welding, and any subsequent heat treatment, traceable to each casting.

Before welding is started, full details of the extent and location of the repair, the proposed welding procedure, heat treatment and subsequent inspection procedures are to be submitted to the Classification Society for approval.

## 12. Welding repair procedure

12.1 Before welding is started, manufacturer shall submit to the Classification Society a detailed welding procedure specification covering the weld preparation, welding parameters, filler metals, preheating and post weld heat treatment and inspection procedures.

12.2 All weld repairs are to be carried out in accordance with qualified procedures, and, by welders who are qualified to a recognized standard. Welding Procedure Qualification Tests are to be carried out in accordance with Appendix A and witnessed by the Surveyor.

Defects to be repaired by welding are to be ground to sound material according to W27.10.

The welding grooves are to be prepared in such a manner which will allow a good fusion of the groove bottom.

The resulting ground areas are to be examined in the presence of the Surveyor by liquid penetrant testing in order to verify the complete elimination of defective material.

12.3 Welding is to be done under controlled conditions free from draughts and adverse weather.

12.4 Metal arc welding with electrodes or filler wire used in the procedure tests is to be used. The welding consumables are to be stored and handled in accordance with the manufacturer's recommendations.

12.5 Slag, undercuts and other imperfections are to be removed before depositing the next run.

12.6 The martensitic steels are to be furnace re-tempered after weld repair. Subject to prior approval, however, local stress relieving may be considered for minor repairs.

12.7 On completion of heat treatment of martensitic steels the weld repairs and adjacent material are to be ground smooth. All weld repairs are to be liquid penetrant tested.

---
Page 9 of 16 IACS Req. 2000/ Corr.1 Dec 2024

## 13. Identification and marking

13.1 The manufacturer is to adopt a system for the identification of all castings, which enable the material to be traced to its original cast. The Surveyor is to be given full facilities for so tracing the castings when required.

Each finished casting propeller shall be marked by the manufacturer at least with the following particulars:

a) Heat number or other marking which will enable the full history of the casting to be traced;
b) Grade of cast material or corresponding abbreviated designation
c) The Society's certificate number;
d) Ice class symbol, where applicable;
e) Skew angle for high skew propellers,
f) Date of final inspection.

13.2 The Society's stamp is to be put on when the casting has been accepted.

## 14. Document and certification

14.1 The manufacturer is to provide the Surveyor with an inspection certificate giving the following particulars for each casting which has been accepted:

a) Purchaser's name and order number;
b) Vessel identification, where known;
c) Description of the casting with drawing number;
d) Diameter, number of blades, pitch, direction of turning;
e) Skew angle for high skew propellers;
f) Final weight;
g) Alloy type, heat number and chemical composition;
h) Casting identification number;
i) Details of time and temperature of heat treatment,
j) Results of the mechanical tests,
k) Results of non-destructive tests and details of test procedure where applicable.

---
Page 10 of 16 IACS Req. 2000/ Corr.1 Dec 2024

## Appendix A: Welding procedure qualification tests for repair of cast steel propeller

### 1. General

1.1 This document gives requirements for qualification tests of welding procedures intended for the repair of cast steel propellers.

1.2 For the welding procedure approval the welding procedure qualification tests are to be carried out with satisfactory results. The qualification tests are to be carried out with the same welding process, filler metal, preheating and stress-relieving treatment as those intended applied by the actual repair work. Welding procedure specification is to refer to the test results achieved during welding procedure qualification testing.

1.3 Welding procedures qualified at a manufacturer are valid for welding in workshops under the same technical and quality management.

### 2. Test piece and welding of sample

2.1 The test assembly, consisting of cast samples, is to be of a size sufficient to ensure a reasonable heat distribution and according to Fig.A.1 with the minimum dimensions:

![Fig.A.1 Test piece for welding repair procedure](Diagram showing two cast plates joined by a weld with dimensions labeled 'a', 'b', and 't'. 1 indicates the joint preparation.)

1: Joint preparation and fit-up as detailed in the preliminary Welding Procedure Specification
a: minimum value 150mm
b: minimum value 300mm
t: material thickness

The dimensions and shape of the groove shall be representative of the actual repair work.

2.2 Preparation and welding of test pieces are to be carried out in accordance with the general condition of repair welding work which it represents.

2.3 Welding of the test assemblies and testing of test specimens are to be witnessed by the Surveyor.

---
Page 11 of 16 IACS Req. 2000/ Corr.1 Dec 2024

### 3. Examinations and tests

3.1 Test assembly is to be examined non-destructively and destructively in accordance with Table A.1 and Fig.A.2:

**Table A.1 Type of tests and extent of testing**

| Type of test | Extent of testing |
| :--- | :--- |
| Visual testing | 100% as per article 3.2 |
| Liquid penetrant testing (1) | 100% as per article 3.2 |
| Transverse tensile test | Two specimens as per article 3.3 |
| Bend test (2) | Two root and two face specimens as per article 3.4 |
| Macro examination | Three specimens as per article 3.5 |
| Impact test | Two sets of three specimens as per article 3.6 |
| Hardness test | As per article 3.7 |

(1) Magnetic particle testing may be used in lieu of liquid penetrant testing for martensitic stainless steels.
(2) For $t \ge 12$mm, the face and root bend may be substituted by 4 side bend test specimens.

### 3.2 Non-destructive testing

Test assembly is to be examined by visual and liquid penetrant testing, or magnetic particle testing if applicable, prior to the cutting of test specimen. In case, that any post-weld heat treatment is required or specified, non-destructive testing is to be performed after heat treatment.

No cracks are permitted. Imperfections detected by liquid penetrant testing, or magnetic particle testing if applicable, are to be assessed in accordance with W27.10.

### 3.3 Tensile test

Two flat transverse tensile test specimens shall be prepared. Testing procedures shall be in accordance with IACS UR W2 2.4.2.8 b). Alternatively tensile test specimens according to recognized standards acceptable to the Classification Society may be used.
The tensile strength shall meet the specified minimum value of the base material. The location of fracture is to be reported, i.e. weld metal, HAZ or base material.

### 3.4 Bend test

Transverse bend tests for butt joints are to be in accordance with UR W2 or, according to a recognized standard. The mandrel diameter shall be 4 x thickness except for austenitic steels, in which case the mandrel diameter shall be 3 x thickness.

The bending angle is to be 180°. After testing, the test specimens are not to reveal any open defects in any direction greater than 3 mm. Defects appearing at the corners of a test specimen during testing are to be investigated case by case.

---
Page 12 of 16 IACS Req. 2000/ Corr.1 Dec 2024

Two root and two face bend specimens are to be tested. For thickness 12 mm and over, four side bend specimens may alternatively be tested.

### 3.5 Macro-examination

Three macro-sections shall be prepared and etched on one side to clearly reveal the weld metal, the fusion line, and the heat affected zone. Cracks and lack of fusion are not permitted. Imperfections such as slag inclusions, and pores greater than 3mm are not permitted.

### 3.6 Impact test

Impact test is required, where the base material is impact tested. Charpy V-notch test specimens shall be in accordance with IACS UR W2. Two sets shall be taken, one set with the notch positioned in the center of the weld and one set with the notch positioned in the HAZ (i.e. the mid-point of the notch shall be at 1mm to 2mm from the fusion line), respectively.

The test temperature, and impact energy shall comply with the requirement specified for the base material.

### 3.7 Hardness test

The macro-section representing the start of welding shall be used for HV 10 hardness testing. Indentations shall traverse 2mm below the surface. At least three individual indentations are to be made in the weld metal, the HAZ (both sides) and in the base metal (both sides). The values are to be reported for information.

### 3.8 Re-testing

If the test piece fails to comply with any of the requirements of this Appendix, reference is made to re-test procedures given in UR W28.

---
Page 13 of 16 IACS Req. 2000/ Corr.1 Dec 2024

![Fig.A.2 Weld test assembly](Layout of the weld test assembly (~300mm x ~300mm) showing the location of specimens to be removed: Discard (top), Macro specimen, Tensile test specimen, Bend test specimen, Macro specimen, CVN test specimens (center), Bend test specimen, Tensile test specimen, Macro specimen, Discard (bottom). A cross-section below shows the weld profile with thickness 't'.)

---
Page 14 of 16 IACS Req. 2000/ Corr.1 Dec 2024

### 4. Test record

4.1 Welding conditions for test assemblies and test results are to be recorded in welding procedure qualification. Forms of welding procedure qualification records can be taken from the Society's rules or from relevant standards.

4.2 A statement of the results of assessing each test piece, including repeat tests, is to be made for each welding procedure qualification records. The relevant items listed for the WPS are to be included.

4.3 The welding procedure qualification record is to be signed by the Surveyor witnessing the test and is to include the Society´s identification.

### 5. Range of approval

### 5.1 General

All the conditions of validity stated below are to be met independently of each other. Changes outside of the ranges specified are to require a new welding procedure test.

A qualification of a WPS obtained by a manufacturer is valid for welding in workshops or sites under the same technical and quality control of that manufacturer.

### 5.2 Base metal

Range of approval for steel cast propeller is limited to steel grade tested.

### 5.3 Thickness

The qualification of a WPS carried out on a weld assembly of thickness t is valid for the thickness range given in Table A.2.

**Table A.2 Range of qualification for thickness**

| Thickness of the test piece, t (mm) | Range of approval |
| :--- | :--- |
| $15 < t \le 30$ | 3mm to 2t |
| $t > 30$ | 0,5t to 2t or 200mm, whichever is the greater |

### 5.4 Welding position

Approval for a test made in any position is restricted to that position.

### 5.5 Welding process

5.5.1 The approval is only valid for the welding process used in the welding procedure test. Single run is not qualified by multi-run butt weld test used in this UR.

### 5.6 Filler metal

The approval is only valid for the filler metal used in the welding procedure test.

### 5.7 Heat input

---
Page 15 of 16 IACS Req. 2000/ Corr.1 Dec 2024

The upper limit of heat input approved is 15% greater than that used in welding the test piece. The lower limit of heat input approved is 15% lower than that used in welding the test piece.

### 5.8 Preheating and interpass temperature

The minimum preheating temperature is not to be less than that used in the qualification test. The maximum interpass temperature is not to be higher than that used in the qualification test.

### 5.9 Post-weld heat treatment

The heat treatment used in the qualification test is to be specified in pWPS. Holding time may be adjusted as a function of thickness.

---
**End of Document**

Page 16 of 16 IACS Req. 2000/ Corr.1 Dec 2024


================================================================================
# FILE: UR_W/UR-W35-Rev.1-Oct-2023-CLN.md
================================================================================

# W35 Requirements for NDT Service Suppliers

**(June 2019)**
**(Rev.1 Oct 2023)**

## 1. General

### 1.1 Scope

(i) Firms providing Non-Destructive Testing (NDT) and Advanced Non-Destructive Testing (ANDT$^1$) Services on the new construction of ships and offshore structures subject to classification, need to fulfil the requirements set out in this UR. In this document, such firms will be referred to as the NDT Service Supplier.

Note 1 – for the remainder of this UR, wherever there is a reference to NDT, it also includes ANDT

(ii) This UR applies to:

*   Independent NDT companies, and;
*   Internal departments of fabricators, e.g., shipyards, hull block/section fabricators performing NDT

The NDT service specified in this UR covers the service application to the following hull structure and associated items at the fabrication stage during new construction:

*   The welding of components that are integrated into the ship or offshore structure
*   The fabrication of independent fuel or cargo tanks (including those intended for low flashpoint fuels, e.g. type A, B and C independent tanks as described in IMO IGC and IGF Codes).
*   Items listed within the definition of hull structure, as defined in UR Z23 section 2.1
*   Rudders of welded construction

(iii) NDT Service Suppliers in the context of this UR are not included as part of the scope of UR Z17. The Classification Society shall verify the NDT Service Supplier in order to determine compliance with the requirements of this UR. The method of verification is to be decided by each Classification Society.

---
**Notes:**

1. This UR is to be uniformly implemented by IACS Societies on or after 1 July 2020.
2. Rev.1 of this UR is to be uniformly implemented by IACS Societies on or after 1 January 2025.

---

### 1.2 Objective

The objective of this UR is to ensure that the NDT Service Supplier is using appropriate procedures, has qualified and certified personnel and has implemented written procedures for training, experience, education, examination, certification, performance, application, control, verification and reporting of NDT. In addition, the NDT Service Supplier shall furnish appropriate equipment and facilities commensurate with providing a professional NDT Service.

### 1.3 Terms and definitions

The following terms and definitions apply for this document.

**NDT**: Non-destructive testing-the development and application of technical methods to examine materials or components in ways that do not impair their future usefulness and Serviceability, in order to measure geometrical characteristics and to detect, locate, measure and evaluate flaws. NDT is also known as non-destructive examination (NDE), non-destructive inspection (NDI) and non-destructive evaluation (NDE). Comprising, but not limited to the following methods and techniques: MT, PT, RT, VT, UT, and ET

**ANDT**: The above definition of NDT applies, however ANDT includes advanced methods such as RT-D, PAUT, TOFD and AUT.

**NDT Service Supplier**: Independent NDT company or NDT department/section that forms a part of a company providing NDT Services on the new construction of ships and offshore structures, as applicable to the bodies performing NDT on the items as listed in paragraph 1.1 (ii) of this UR.

**Society**: The Classification Society

**MT**: Magnetic Particle Testing

**PT**: Penetrant Testing

**RT**: Radiographic Testing

**RT-D**: Digital Radiography (Several techniques within the method RT, e.g., Computed Radiography or Direct Radiography).

**UT**: Ultrasonic Testing

**PAUT**: Phased Array Ultrasonic Testing (Technique within the method UT).

**TOFD**: Time of Flight Diffraction (Technique within the method UT).

**AUT**: Automated Ultrasonic Testing. A technique by which an object is tested by ultrasound using probes operating under mechanical control and where ultrasonic data is collected automatically.

**ET**: Electromagnetic Testing (i.e. Eddy Current Testing and/or Alternating Current Field Measurements [ACFM])

**VT**: Visual Testing

**Industrial sector**: Section of industry or technology where specialised NDT practices are used, requiring specific product-related knowledge, skill, equipment and/or training.

**Product sector**: A category of component that may be defined by type of manufacturing, fabrication, and/or shape, which may have unique, and/or general manufacturing/fabrication defect characteristics. Product sector examples include (but not limited to): castings, wrought products (forgings), rolled products, extruded products, and welds.

NDT personnel may hold certification in a method which is related to a product sector.

### 1.4 References

The following referenced documents are to be used for the application of this document as appropriate. For updated references, the latest edition of the referenced document (including any amendments) applies.

*   ISO 9712: 2021; Non-destructive Testing-Qualification and certification of NDT personnel
*   ISO/IEC 17020:2012; Conformity assessment - Requirements for the operation of various types of bodies performing inspection
*   ISO/IEC 17024:2012; Conformity assessment - General requirements for bodies operating certification of persons
*   ISO 9001:2015; Quality Management Systems-Requirements
*   SNT-TC-1A: 2020; Personnel Qualification and Certification in Nondestructive Testing
*   ANSI/ASNT CP-189:2020; ASNT Standard for Qualification and Certification of Nondestructive Testing Personnel

Other national adoptions of the standards listed above are accepted as compliant and hence are accepted for use together with this document.

## 2. Requirements for the NDT Service Supplier

The NDT Service Supplier shall document, as required in 2.2 to 2.9, that it has the competence and control needed to perform the specified NDT Services.

### 2.1 Requirements for document

The following documents shall be available for the Society upon request:

*   an outline of NDT Service Supplier's organisation and management structure, including any subsidiaries
*   information on the structure of the NDT Service Supplier's Quality Management System
*   quality manual and documented procedures covering the requirements given in item 2.2
*   for companies with in-house certification of personnel scheme; a written practice developed in accordance with a recognised standard or recommended practice (i.e., ASNT's SNT-TC-1A, 2020, ANSI/ASNT CP-189, 2020 or similar).
*   operational work procedures for each NDT method including selection of the NDT technique.
*   training- and follow-up programmes for NDT operators including practical training on various ship and offshore products
*   written statement issued by the employer, based upon the scope of certification, authorising the operator to carry out specified tasks
*   procedure for supervisor's authorisation of NDT operators
*   experience of the NDT Service Supplier in the specific NDT Service area,
*   for companies which obtain certification from an accredited certification body; a list of documented training and experience for NDT operators within the relevant NDT Service area, including qualifications and third party certification per ISO 9712:2021 based certification schemes.
*   description of equipment(s) used for the NDT Services performed by the NDT Service Supplier
*   a guide for NDT operators to use equipment mentioned above
*   record formats for recording results of the NDT Services referred to in item 2.9
*   information on other activities which may present a Conflict of interest, if applicable
*   record of customer claims and corrective actions, where applicable
*   any legal proceedings against the company in the past/currently in the courts of law, where applicable

### 2.2 Quality management system

The NDT Service Supplier shall have a documented quality management system, covering at least:

*   work procedures for all tasks and operations, including the various NDT methods and NDT techniques for which the NDT Service Supplier is involved.
*   preparation, issuance, maintenance and control of documents
*   maintenance and calibration of the equipment
*   training programs for the NDT operators and the supervisors
*   maintenance of records for NDT operators' and the supervisors' training, qualification and certification
*   certification of NDT operators including re-validation and recertification
*   procedure for test of operators' visual acuity
*   supervision and verification of operation to ensure compliance with the NDT procedures
*   quality management of subsidiaries
*   job preparation
*   order reference system where each engagement is traceable to when, who and where the test was carried out.
*   recording and reporting of information, including retention time of records
*   code of conduct for the NDT Service Supplier's activities; especially the NDT activities
*   periodic review of work process procedures
*   corrective and preventive action
*   feedback and continuous improvement
*   internal audits
*   the provision of accessibility to required codes, standards and procedures to assist NDT operators.

A documented quality system complying with the most current version of ISO/IEC 17020:2012 and including the above would be considered acceptable. The NDT Service Supplier should satisfy the requirements of Type A or Type B or Type C inspection body, as described in ISO/IEC 17020:2012. In all cases, production staff shall not be allowed to inspect their own work in the case of Type C inspection body.

### 2.3 Qualification and certification of NDT personnel

The NDT Service Supplier is responsible for the qualification and preferably 3rd party certification of its supervisors and operators to a recognised certification scheme based on ISO 9712: 2021.

Personnel qualification to an employer based qualification scheme as e.g. SNT-TC-1A, 2020 or ANSI/ASNT CP-189, 2020 may be accepted if the NDT Service Supplier's written practice is reviewed and found acceptable by the Society. The NDT Service Supplier's written practice shall as a minimum, except for the impartiality requirements of a certification body and/or authorised body, generally comply with the requirements of ISO 9712: 2021.

For NDT operators holding certificates issued via an employer based scheme, the employer's certification shall be deemed revoked when employment is terminated by either party.

The supervisors' and operators' certificates and competence shall comprise all industrial and product sectors and techniques being applied by the NDT Service Supplier.

Level 3 personnel shall be certified by one of the following means:

(i) obtain certification from an accredited certification body.

(ii) obtain certification from an employer based scheme via the examination method, as detailed in the written practice. It is not permissible to directly appoint a level 3 without examination if the intended certification route is from an employer based scheme.

### 2.4 Supervisor

The NDT Service Supplier shall have a supervisor or supervisors, responsible for the following:

a) validate NDT instructions and procedures established and reviewed by level 3 personnel;
b) review of NDT reporting;
c) supervise all tasks and NDT operations at all levels;
d) inspection of NDT equipment, tools and calibration;
e) re-evaluate the qualification of the operators annually on behalf of the NDT Service Supplier.

Normally, the NDT Service Supplier shall employ (on a full-time basis) a level 3 supervisor, certified to level 3 in the applicable method(s) as per the requirements of this UR.

It is recognised that an NDT Service Supplier may not directly employ a Level 3 in all the stated methods practiced. In such cases, it is permissible to employ an external Level 3 who is certified by an accredited certification body in those methods not held by the full-time Level 3(s) of the NDT Service Supplier.

Alternatively, and by agreement with the Society, the NDT Service Supplier may appoint an internal (full-time employed) supervisor of NDT activities, who does not hold level 3 certification. In this case, the supervisor shall be certified to a minimum of level 2.

For NDT Service Suppliers operating this alternative approach, the NDT Service Supplier shall comply with all other requirements of this UR and shall employ (either part time or on a contract basis) Level 3 NDT Services (to carry out functions such as procedure development, procedure approval, consultancy, review etc.) from outside the NDT Service Supplier organisation. The appointed external level 3 shall be certified by an accredited certification body in all the applicable methods appropriate to the scope of the NDT operations.

### 2.5 Operator

The operator carrying out the NDT and interpreting indications, shall as a minimum, be qualified and certified to Level 2 in the NDT method(s) concerned and as described in item 2.3.

However, operators only undertaking the gathering of data using any NDT method and not performing data interpretation or data analysis may be qualified and certified as appropriate, at level 1.

The operator shall have adequate knowledge of materials, weld, structures or components, NDT equipment and limitations that are sufficient to apply the relevant NDT method for each application appropriately.

### 2.6 Equipment

The NDT Service Supplier shall maintain records of the NDT equipment used and detail information related to maintenance, calibration and verification activities. If the NDT Service Supplier hires equipment, such equipment shall have updated calibration records, and the operators shall be familiar with the specific equipment type prior to using it. Under any circumstance, the NDT Service Supplier shall possess sufficient equipment to carry out the NDT Services being a part of the NDT scope required by the Society.

Where the equipment is of unique nature, the NDT operators shall be trained by competent personnel in the operation and use of the equipment before carrying out NDT using this equipment.

### 2.7 Work instructions and procedures

The NDT Service Supplier shall produce written procedures for the NDT being applied. These procedures are to be written, verified or approved by the NDT Service Supplier's Level 3 (either internal, or external, as described in section 2.4). Procedures shall define all relevant information relating to the inspection including defect evaluation against acceptance criteria in accordance with the Society Rules. All NDT procedures and instructions shall be properly documented in such a way that the performed testing can be easily retraced and/or repeated at a later stage. All NDT procedures are to be acceptable to the Society.

### 2.8 Sub-contractor

The NDT Service Supplier shall give information of agreements and arrangements if any part(s) of the NDT Services provided are subcontracted, included level 3 NDT Services (as described in section 2.4). The NDT Service Supplier, in the following-up of subcontracts shall give emphasis to the quality management system of the subcontractor.

Subcontractors shall meet the same requirements placed on NDT Service Suppliers for any NDT performed.

### 2.9 Reporting

All NDT shall be properly documented in such a way that the performed testing and examination can be easily retraced and/or repeated as a later stage. The reports shall identify the defects present in the tested area, and a conclusive statement as to whether the material, weld, component or structure satisfies the acceptance criteria or not.

The report shall include a reference to the applicable standard, NDT procedure and acceptance criteria applied in the applicable NDT method/technique. In general, the acceptance criteria shall comply with the Society Rules. Reports shall be signed by the personnel with the appropriate level of certification, and the appropriate signatory status as defined in the Quality Management System.


================================================================================
# FILE: UR_W/UR-W8-Rev.4-Mar-2024-CLN.md
================================================================================

# W8 Hull and machinery steel castings

**W8**
(1978)
(Rev.1 July 2002)
(Rev.2 May 2004)
(Rev.3 Mar 2022)
(Rev.4 Mar 2024)

## 1 Scope

1.1 These requirements are applicable to C, C-Mn and alloy steel castings intended for hull and machinery applications for ships and offshore units for worldwide services as specified in the relevant IACS Unified requirements and/or requirements of the Classification Society. This Unified Requirement also makes consideration for grades that are intended for fabrication by welding, as well as grades not intended for welding.

1.2 Additional requirements may be necessary, especially when the castings are intended for service at low or elevated temperatures, e.g. for ships with ice-class or for boilers. Additional requirements will typically be required for castings for offshore units depending on applicable service temperature and environment.

1.3 Similarly, C and C-Mn steel castings and alloy steel castings which comply with national or proprietary specifications may be accepted provided such specifications give reasonable equivalence to these requirements or are otherwise specially approved or required by the Classification Society.

## 2 Manufacture

2.1 Castings are to be made at a manufacturer approved by the Classification Society.

2.2 The steel is to be manufactured by a process approved by the Classification Society.

2.3 All flame cutting, scarfing or arc-air gouging to remove surplus metal is to be undertaken in accordance with recognized good practice and is to be carried out before the final heat treatment. Preheating is to be employed when necessitated by the chemical composition and/or thickness of the castings. If necessary, the affected areas are to be either machined or ground smooth.

2.4 For certain components including steel castings subjected to surface hardening process, the proposed method of manufacture may require special approval by the Classification Society.

2.5 Joining of two or more castings by welding to form a composite component:
Requirements for welding procedure qualification tests of steels for hull construction and marine structures are specified in UR W28. Welders for hull structural steel castings are to be qualified in accordance with UR W32. Requirements for other WPS and qualification thereof, for welder certification and for type approval of welding consumables are at the discretion of the Class Societies.

2.6 Temporary welds made for operations such as lifting, handling, staging, etc., are to be in accordance with approved welding procedures and qualified welders, and are to be removed, ground and inspected using suitable NDT methods.

***

**Notes:**

1. Rev.3 of this UR is to be uniformly implemented by IACS Societies for ships and offshore units contracted for construction on or after 1 July 2023.
2. Rev.4 of this UR is to be uniformly implemented by IACS Societies for ships and offshore units contracted for construction on or after 01 January 2025.
3. The "contracted for construction" date means the date on which the contract to build the vessel is signed between the prospective owner and the shipbuilder. For further details regarding the date of "contract for construction", refer to IACS Procedural Requirement (PR) No. 29.

## 3 Quality of castings

3.1 All castings are to be free from surface or internal defects, which would be prejudicial to their proper application in service. The surface finish is to be in accordance with good practice and any specific requirements of the approved plan.

## 4 Chemical composition

4.1 All castings are to be made from killed steel and the chemical composition is to be appropriate for the type of steel and the mechanical properties specified for the castings.

4.1 The chemical composition of each heat is to be determined by the manufacturer on a sample taken preferably during the pouring of the heat. When multiple heats are tapped into a common ladle, the ladle analysis shall apply.

4.2 The chemical composition is to comply with the overall limits given in Table 1 and Table 2, respectively, or, where applicable, the requirements of the approved specification.

**Table 1: Chemical composition limits for hull and machinery steel castings (%): C, C-Mn steels**

| Steel type | Applications | C (max.) | Si (max.) | Mn | S (max.) | P (max.) | Residual elements (max.) | | | | Total residuals (max.) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| | | | | | | | **Cu** | **Cr** | **Ni** | **Mo** | |
| C, C-Mn | Castings for non-welded construction | 0.40 | 0.60 | 0.50-1.60 | 0.035 | 0.035 | 0.30 | 0.30 | 0.40 | 0.15 | 0.80 |
| C, C-Mn | Castings for welded construction | 0.23 | 0.60 | 0.50-1.60 | 0.035 | 0.035 | 0.30 | 0.30 | 0.40 | 0.15 | 0.80 |

**Table 2: Chemical composition limits for hull and machinery steel castings (%): Alloy steels**

| Steel type | Applications | C (max.) | Si (max.) | Mn | S (max.) | P (max.) | Alloying elements<sup>1)</sup> (min.) | | | |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| | | | | | | | **Cu** | **Cr** | **Ni** | **Mo** |
| Alloy | Castings for non-welded construction | 0.45 | 0.60 | 0.50-1.60 | 0.030 | 0.035 | 0.30 | 0.40 | 0.40 | 0.15 |
| Alloy | Castings for welded construction | \- | \- | \- | \- | \- | \- | \- | \- | \- |

<sup>1)</sup> At least one of the elements shall comply with the minimum content.
Note: For welded construction, alloying element values to be agreed with Class Society.

4.3 Suitable grain refining elements such as aluminium may be used at the discretion of the manufacturer or as agreed with the Class Society.

## 5 Heat treatment (including straightening)

5.1 Castings are to be supplied in one of the following delivery conditions:

(a) Carbon and carbon-manganese steels:
- Fully annealed
- Normalized
- Normalized and tempered
- Quenched and tempered.

(b) Alloy steels:
- Normalized
- Normalized and tempered
- Quenched and tempered

For all types of steel the tempering temperature is to be not less than 550°C.

The delivery condition shall meet the design and application requirements. It is the manufacturers responsibility to select the appropriate heat treatment method to obtain the required mechanical properties.

5.2 Castings for components such as crankshafts and engine bedplates, where dimensional stability and freedom from internal stresses are important, are to be given a stress relief heat treatment. This is to be carried out at a temperature of not less than 550°C followed by furnace cooling to 300°C or lower.

5.3 Heat treatment is to be carried out in properly constructed furnaces which are efficiently maintained and have adequate means for control and recording of temperature. The furnace dimensions are to be such as to allow the whole casting to be uniformly heated to the necessary temperature. In the case of very large castings alternative methods for heat treatment will be specially considered by the Classification Society. Sufficient thermocouples are to be connected to the furnace charge to measure and record that its temperature is adequately uniform unless the temperature uniformity of the furnace is verified at regular intervals.

5.4 If a casting is locally reheated or any straightening operation is performed after the final heat treatment, a subsequent stress relieving heat treatment may be required in order to avoid the possibility of harmful residual stresses. The manufacturer shall have strict control of this temperature in order to avoid any detrimental effects to the final heat treatment and resultant microstructure and mechanical properties of the casting.

5.5 The foundry is to maintain records of heat treatment identifying the furnace used, furnace charge, date, temperature and time at temperature. The records are to be presented to the Surveyor on request.

## 6 Mechanical tests

6.1 Test material, sufficient for the required tests and for possible retest purposes is to be provided for each casting or batch of castings.

6.2 At least one test block is to be provided for each casting or batch of castings. Unless otherwise agreed these test blocks are to be either attached to the castings, cast integrally on the castings or cast separately.

6.3 (i) The preferred test block arrangement, where practical, is for the manufacturer to provide at least one 30mm test block by either attached to the castings or cast integrally on the castings.<sup>1</sup>

Note 1: The test results represent the material from which the castings have been poured and the subsequent heat treatment process and may not necessarily represent the properties of the castings. These properties can be affected by solidification conditions and the rate of cooling during heat treatment, which are in turn influenced by casting thickness, size, complexity and shape. The purpose of the test block is to provide a qualitative check to demonstrate the effective control of existing heat treatment processes and procedures.

6.3 (ii) For castings where it is required that the mechanical properties need to be demonstrated for specific section thicknesses and when agreed upon between the manufacturer and the purchaser, then proposals<sup>2</sup> for alternative test block arrangements (in terms of size and type) are to be submitted for approval by the Classification Society.

Note 2: The size of the test blocks for mechanical testing may be determined by the ruling section of the casting that they are representative of the casting's heat treatment and microstructure. Also see ISO 4885,2018; ISO 683-1:2016 and ISO 683-2: 2016.
Alternatively, determination of test block size and type may be supported by historical and statistical test data, production of a representative test block or a component, simulation software, or a combination of all these items.

6.4 Where the casting is of complex design or where the finished mass exceeds 10 tonnes, two cast on test blocks are to be provided, located as far as practicable from each other.

6.5 Where large castings are made from two or more casts, which are not mixed in a ladle prior to pouring, two or more test blocks are to be provided corresponding to the number of casts involved. These are to be attached to the casting or cast integrally on the castings at locations as widely separated as possible.

6.6 For castings where the method of manufacture has been specially approved by the Classification Society in accordance with 2.4, the number and position of test blocks is to be agreed with the Classification Society having regard to the method of manufacture employed.

6.7 As an alternative to 6.2, where a number of small castings of about the same size, each of which is under 1000kg in mass, are made from one cast and heat treated in the same furnace charge, a batch testing procedure may be adopted using separately cast test blocks of suitable dimensions. At least one test block is to be provided for each batch of castings.

6.8 The test blocks are not to be detached from the casting until the specified heat treatment has been completed and they have been properly identified.

6.9 One tensile test specimen and one set of impact tests are to be taken from each test block.

6.10 The preparation of test specimens and the procedures used for mechanical testing are to comply with the relevant requirements of UR W2. Unless otherwise agreed all tests are to be carried out in the presence of the Surveyors.

## 7 Mechanical properties

7.1 Table 3 and Table 4 give the minimum requirements for yield stress, elongation, reduction of area and impact test energy values corresponding to steel types and different strength levels. Where it is proposed to use a steel with a specified minimum tensile strength intermediate to those given, corresponding minimum values for the other properties may be obtained by interpolation.

7.2 Castings may be supplied to any specified minimum tensile strength selected within the general limits detailed in Table 3 and Table 4, respectively, but subject to any additional requirements of the relevant construction Rules.

7.3 The mechanical properties are to comply with the requirements<sup>3</sup> of Table 3 and Table 4, respectively, appropriate to the specified minimum tensile strength or, where applicable, the requirements of the approved specification.

Note 3: See also sections 6.3.

7.4 Re-test requirements for tensile tests are to be in accordance with UR W2.

7.5 The additional tests detailed in 7.4 are to be taken, preferably from the same, but alternatively from another, test block representative of the casting or batch of castings.

7.6 At the option of the manufacturer, when a casting or batch of castings has failed to meet the test requirements, it may be reheat treated and re-submitted for acceptance tests.

**Table 3: Mechanical properties for steel castings intended for welding**

| Steel type | Specified minimum tensile strength<sup>1)</sup> (N/mm²) | Yield stress (N/mm²) min. | Elongation on 5,65 √So (%) min. | Reduction of area (%) min. | Charpy V-notch impact test<sup>2)</sup> | |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| | | | | | **Test temperature (°C)** | **Minimum average energy (J)** |
| C, C-Mn | 400 | 200 | 25 | 40 | 0 | 27 |
| | 440 | 220 | 22 | 30 | 0 | 27 |
| | 480 | 240 | 20 | 27 | 0 | 27 |
| | 520 | 260 | 18 | 25 | 0 | 27 |
| | 560 | 300 | 15 | 20 | 0 | 27 |
| | 600 | 320 | 13 | 20 | 0 | 27 |
| Alloy | 550 | 355 | 18 | 30 | 0 | 27 |
| | 600 | 400 | 16 | 30 | 0 | 27 |
| | 650 | 450 | 14 | 30 | 0 | 27 |
| | 700 | 540 | 12 | 28 | 0 | 27 |

**NOTE**
1) A tensile strength range of 150 N/mm² may additionally be specified.
2) Special consideration may be given to alternative requirements for Charpy V-notch impact test, depending on design and application, and subject to agreement by Society.

**Table 4: Mechanical properties for machinery steel castings not intended for welding**

| Steel type | Specified minimum tensile strength<sup>1)</sup> (N/mm²) | Yield stress (N/mm²) min. | Elongation on 5,65 √So (%) min. | Reduction of area (%) min. | Charpy V-notch impact test<sup>2)</sup> | |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| | | | | | **Test temperature (°C)** | **Minimum average energy (J)** |
| C, C-Mn | 400 | 200 | 25 | 40 | AT<sup>3)</sup> | 27 |
| | 440 | 220 | 22 | 30 | AT<sup>3)</sup> | 27 |
| | 480 | 240 | 20 | 27 | AT<sup>3)</sup> | 27 |
| | 520 | 260 | 18 | 25 | AT<sup>3)</sup> | 27 |
| | 560 | 300 | 15 | 20 | AT<sup>3)</sup> | 27 |
| | 600 | 320 | 13 | 20 | AT<sup>3)</sup> | 27 |
| Alloy | 550 | 340 | 16 | 35 | AT<sup>3)</sup> | 27 |
| | 600 | 400 | 16 | 35 | AT<sup>3)</sup> | 27 |
| | 650 | 450 | 14 | 32 | AT<sup>3)</sup> | 27 |
| | 700 | 540 | 12 | 28 | AT<sup>3)</sup> | 27 |

**NOTE**
1) A tensile strength range of 150 N/mm² may additionally be specified.
2) Special consideration may be given to alternative requirements for Charpy V-notch impact test, depending on design and application, and subject to agreement by Society.
3) AT refers to Ambient Temperature (i.e. 23°C±5°C), which is specified in ISO 148-1:2016

## 8 Inspection

8.1 All castings are to be cleaned and adequately prepared for examination; suitable methods include pickling, caustic cleaning, wire brushing, local grinding, shot or sand blasting. The surfaces are not to be hammered, peened or treated in any way which may obscure defects.

8.2 Before acceptance all castings are to be presented to the Surveyors for visual examination. Where applicable, this is to include the examination of internal surfaces. Unless otherwise agreed, the verification of dimensions is the responsibility of the manufacturer.

8.3 When required by the relevant construction Rules, or by the approved procedure for welded composite components (see W8.2.6.), appropriate non-destructive testing is also to be carried out before acceptance and the results are to be reported by the manufacturer. The extent of testing and acceptance criteria are to be agreed with the Classification Society. IACS Recommendation No. 69 is regarded as an example of an acceptable standard specifying suitable minimum requirements.

8.4 When required by the relevant construction Rules castings are to be pressure tested before final acceptance. These tests are to be carried out in the presence of the Surveyor and are to be to their satisfaction.

8.5 In the event of any casting proving to be defective during subsequent machining or testing it is to be rejected notwithstanding any previous certification.

## 9 Rectification of defective castings

9.1 General

(i) Where castings are to be repaired, the manufacturer shall exercise robust controls of all repair operations regarding the repair of castings, with respect to dimensions, heat treatment, inspection and quality control.

(ii) The approval of the Classification Society is to be obtained where steel castings from which defects were removed are to be used with or without weld repair.

(iii) Defects and unacceptable indications must be repaired as indicated below:
Defective parts of material may be removed by grinding, or by chipping and grinding, or by arc air-gouging and grinding. Thermal methods of metal removal shall only be allowed before the final heat treatment. All grooves shall have a bottom radius of approximately three times the groove depth and should be smoothly blended to the surface area with a finish equal to that of the adjacent surface.

(iv) For NDT of steel castings after repair, see 8.3.

(v) Where the defective area is to be repaired by welding, the excavations are to be suitably shaped to allow good access for welding. The resulting grooves are to be subsequently ground smooth and complete elimination of the defective material is to be verified by MT or PT.

(vi) Shallow grooves or depressions resulting from the removal of defects may be accepted provided that they will cause no appreciable reduction in the strength of the casting or affect the intended use, and the depth of defect removal is not over 15mm or 10% of wall thickness, whichever is less. The resulting grooves or depressions are to be subsequently ground smooth and complete elimination of the defective material is to be verified by MT or PT. Small surface irregularities sealed by welding are to be treated as weld repairs, see 9.2.

9.2 Weld Repairs

In addition to the requirements given in 9.1, the following apply for weld repairs:

(i) For C and C-Mn steel castings weld repairs shall be suitably classified as major or minor. For alloy steel castings, repair requires approval from the Classification Society.

a. Major repairs are those where:
- the depth is greater than 25% of the wall thickness or 25mm whichever is less, or
- the total weld area on a casting exceeds 0.125m² of the casting surface noting that where a distance between two welds is less than their average width, they are to be considered as one weld.

b. Minor weld repairs: Weld repairs not classified as major are considered as minor and need to be carried out in accordance with a qualified welding procedure.

(ii) The following is required for major repairs:

a. Shall be carried out before the final delivery heat treatment condition

b. Shall comply with the requirements in (iv) below

c. Before welding is started, full details of the extent and location of the repair, the proposed welding procedure, heat treatment and subsequent inspection procedures are to be submitted for approval.

(iii) The following is required for minor repairs:

a. Shall be carried out before the final delivery heat treatment condition

b. Shall comply with the requirements in (iv) below (also with respect to records, see (iv) f) and g).

c. With the exception of alloy steels, do not require prior approval by the Classification Society, except as given in (d)

d. The Classification Society may request minor repairs in critical areas to be treated as major repairs.

(iv) The following requirements apply for all weld repairs (major and minor):

a. All castings in alloy steels and all castings for crankshafts are to be suitably pre-heated prior to welding. Castings in carbon or carbon-manganese steel may also require to be pre-heated depending on their chemical composition and the dimensions and position of the weld repairs.

b. Welding procedures are to be qualified and shall match the delivery condition of the casting. Qualification of welding procedures shall follow the Classification Society rules, or subject to agreement with the Classification Society, a recognised standard (e.g. IACS UR W28 or ISO 11970:2016).

c. Welding is to be done under cover in positions free from draughts and adverse weather conditions by qualified welders with adequate supervision. As far as possible, all welding is to be carried out in the downhand (flat) position.

d. The welding consumables used are to be of an appropriate composition, giving a weld deposit with mechanical properties similar and in no way inferior to those of the parent castings. Welding procedure tests are to be carried out by the manufacturer to demonstrate that satisfactory mechanical properties can be obtained after heat treatment as detailed in 5.1.

e. After welding has been completed the castings are to be given either a suitable heat treatment in accordance with the requirements of 5.1 or a stress relieving heat treatment at a temperature of not less than 550°C for C and C-Mn steel castings. For alloy steel castings, the heat treatment has to be agreed with the Class Society. The type of heat treatment employed will be dependent on the chemical composition of the casting and the dimensions, positions and nature of the repairs, and should not affect the properties of the casting.

Subject to the prior agreement of Classification Society, special consideration may be given to the omission of post weld heat treatment or to the acceptance of local stress-relieving heat treatment where the repaired area is small and machining of the casting has reached an advanced stage.

f. On completion of heat treatment the weld repairs and adjacent material are to be ground smooth and examined by magnetic particle or liquid penetrant testing. Supplementary examination by ultrasonics or radiography may also be required depending on the dimensions and nature of the original defect. Satisfactory results are to be obtained from all forms of non-destructive testing used.

g. The manufacturer is to maintain full records detailing the extent and location of repairs made to each casting and details of weld procedures and heat treatments applied for repairs. These records are to be available to the Surveyor and copies provided on request.

9.3 Recommendation for welding: For steels with C ≥ 0.23 or Ceq ≥ 0.45, the WPQT on which the WPS is based, should be qualified on a base material having a Ceq as follows: the Ceq of the base material should not fall below more than 0.02 of the material to be welded. (Example: WPQT for a material with actual Ceq = 0.50 may be qualified on a material with Ceq ≥ 0.48.)

## 10 Identification of castings

10.1 The manufacturer is to adopt a system of identification which will enable all finished castings to be traced to the original cast and the Surveyors are to be given full facilities for so tracing the castings when required.

10.2 Before acceptance, all castings which have been tested and inspected with satisfactory results are to be clearly marked by the manufacturer. At the discretion of individual Classification Societies any of the following particulars may be required:

(i) Steel quality.
(ii) Identification number, cast number or other marking which will enable the full history of the casting to be traced.
(iii) Manufacturer's name or trade mark.
(iv) The Classification Society's name, initials or symbol.
(v) Abbreviated name of the Classification Society's local office.
(vi) Personal stamp of Surveyors responsible for inspection.
(vii) Where applicable, test pressure.

10.3 Where small castings are manufactured in large numbers, modified arrangements for identification may be specially agreed with the Classification Society.

## 11 Certification

11.1 The manufacturer is to provide the required type of inspection certificate giving the following particulars for each casting or batch of castings which has been accepted:

(i) Purchaser's name and order number.
(ii) Description of castings and steel quality.
(iii) Identification number.
(iv) Steel making process, cast number and chemical analysis of ladle samples.
(v) Results of mechanical tests.
(vi) Results of non-destructive tests, where applicable.
(vii) Details of heat treatment, including temperatures and holding times.
(viii) Where applicable, test pressure.

***
**End of Document**


================================================================================
# FILE: UR_W/ur-w10rev2.md
================================================================================

# W10 Spheroidal or nodular graphite iron castings

(1978)
(Rev. 1 1995)
(Rev. 2 May 2004)

## W10.1 Scope
(1978)

W10.1.1 All important spheroidal or nodular graphite iron castings, as defined in the relevant construction Rules, are to be manufactured and tested in accordance with the requirements of the following paragraphs.

W10.1.2 These requirements are applicable only to castings where the design and acceptance tests are related to mechanical properties at ambient temperature. For other applications additional requirements may be necessary, especially when the castings are intended for service at low or elevated temperatures.

W10.1.3 Alternatively, castings which comply with national or proprietary specifications may be accepted provided such specifications give reasonable equivalence to these requirements or otherwise are specially approved or required by the Classification Society.

W10.1.4 Where small castings are produced in large quantities the manufacturer may adopt alternative procedures for testing and inspection subject to the approval of the Classification Society.

## W10.2 Manufacture
(1978)

W10.2.1 All important castings are to be made at foundries where the manufacturer has demonstrated to the satisfaction of the Classification Society that the necessary manufacturing and testing facilities are available and are supervised by qualified personnel. A programme of approval tests may be required in accordance with the procedures of individual Classification Societies.

W10.2.2 Suitable mechanical methods are to be employed for the removal of surplus material from castings. Thermal cutting processes are not acceptable, except as a preliminary operation to mechanical methods.

W10.2.3 Where castings of the same type are regularly produced in quantity, the manufacturer is to make any tests necessary to prove the quality of the prototype castings and is also to make periodical examinations to verify the continued efficiency of the manufacturing technique. The Surveyor is to be given the opportunity to witness these tests.

## W10.3 Quality of castings
(1978)

W10.3.1 Castings are to be free from surface or internal defects which would be prejudicial to their proper application in service. The surface finish is to be in accordance with good practice and any specific requirements of the approved plan.

## W10.4 Chemical composition
(1978)

W10.4.1 Unless otherwise specially required, the chemical composition of the iron used is left to the discretion of the manufacturer, who is to ensure that it is suitable to obtain the mechanical properties specified for the castings. When required by individual Classification Societies the chemical composition of ladle samples is to be reported.

## W10.5 Heat treatment
(Rev. 1 1995)

W10.5.1 Except as required by W10.5.2 castings may be supplied in either the as cast or heat treated condition.

W10.5.2 For some applications, such as high temperature service or where dimensional stability is important, it may be required that castings be given a suitable tempering or stress relieving heat treatment. This is to be carried out after any refining heat treatment and before machining. The special qualities with 350 N/mm² and 400 N/mm² nominal tensile strength and impact test shall undergo a ferritizing heat treatment.

W10.5.3 Where it is proposed to locally harden the surfaces of a casting full details of the proposed procedure and specification are to be submitted for approval by the Classification Society.

## W10.6 Mechanical tests
(Rev. 2 May 2004)

W10.6.1 Test material, sufficient for the required tests and for possible re-test purposes, is to be provided for each casting or batch of castings.

W10.6.2 The test samples are generally to be one of the standard types detailed in Figs. 1, 2 and 3 with a thickness of 25 mm. Test samples of other dimensions, as detailed in Figs. 1, 2 and 3 may, however, be specially required for some components.

W10.6.3 At least one test sample is to be provided for each casting and unless otherwise required may be either gated to the casting or separately cast. Alternatively test material of other suitable dimensions may be provided integral with the casting.

W10.6.4 For large castings where more than one ladle of treated metal is used, additional test samples are to be provided so as to be representative of each ladle used.

W10.6.5 As an alternative to W10.6.3, a batch testing procedure may be adopted for castings with a fettled mass of 1 tonne or less. All castings in a batch are to be of similar type and dimensions, cast from the same ladle of treated metal. One separately cast test sample is to be provided for each multiple of 2,0 tonnes of fettled castings in the batch.

![Figure 1: Type A test samples (U-type). The diagram shows a side and front view of a U-shaped test block with a 3° taper on the upper section. Dimensions u, v, x, y, and z are indicated.](fig_1_u_type_samples)

**Dimensions for Fig. 1**

| Dimensions | Standard sample | Alternative samples when specially required | | |
| :--- | :--- | :--- | :--- | :--- |
| u (mm) | 25 | 12 | 50 | 75 |
| v (mm) | 55 | 40 | 90 | 125 |
| x (mm) | 40 | 30 | 60 | 65 |
| y (mm) | 100 | 80 | 150 | 165 |
| z | To suit testing machine | | | |
| Rs | Approximately 5mm | | | |

![Figure 2: Type B test samples (double U-type). The diagram shows a test block with two U-shaped cutouts at the bottom, creating three legs. A 3° taper is shown on the upper internal section. Dimensions u, v, x, y, and z are indicated.](fig_2_double_u_type_samples)

**Dimensions for Fig. 2**

| Dimensions | Standard sample |
| :--- | :--- |
| u (mm) | 25 |
| v (mm) | 90 |
| x (mm) | 40 |
| y (mm) | 100 |
| z | To suit testing machine |
| Rs | Approximately 5mm |

![Figure 3: Type C test samples (Y-type). The diagram shows a Y-shaped test block in cross-section and side view. Dimensions u, v, x, y, and z are indicated.](fig_3_y_type_samples)

**Dimensions for Fig. 3**

| Dimensions | Standard sample | Alternative samples when specially required | | |
| :--- | :--- | :--- | :--- | :--- |
| u (mm) | 25 | 12 | 50 | 75 |
| v (mm) | 55 | 40 | 100 | 125 |
| x (mm) | 40 | 25 | 50 | 65 |
| y (mm) | 140 | 135 | 150 | 175 |
| z | To suit testing machine | | | |
| Thickness of mould surrounding test sample | 40mm min. | 40mm min. | 80mm min. | 80mm min. |

W10.6.6 Where separately cast test samples are used, they are to be cast in moulds made from the same type of material as used for the castings and are to be taken towards the end of pouring of the castings. The samples are not to be stripped from the moulds until the temperature is below 500°C.

W10.6.7 All test samples are to be suitably marked to identify them with the castings which they represent.

W10.6.8 Where castings are supplied in the heat treated condition, the test samples are to be heat treated together with the castings which they represent.

W10.6.9 One tensile test specimen is to be prepared from each test sample and is to be machined to the dimensions given in W2.

W10.6.10 All tensile tests are to be carried out using test procedures in accordance with W2. Unless otherwise agreed all tests are to be carried out in the presence of the Surveyors.

W10.6.11 Impact tests may additionally be required and in such cases a set of three test specimens of agreed type is to be prepared from each sample. Where Charpy V-notch test specimens are used, the dimensions and testing procedures are to be in accordance with W2.

## W10.7 Mechanical properties
(Rev. 2 May 2004)

W10.7.1 Table 1 gives the minimum requirements for 0,2% proof stress and elongation corresponding to different strength levels. Typical Brinell hardness values are also given in Table 1 and are intended for information purposes only.

W10.7.2 Castings may be supplied to any specified minimum tensile strength selected within the general limits detailed in Table 1 but subject to any additional requirements of the relevant construction Rules.

**Table 1 Mechanical properties**

| | Specified minimum tensile strength (N/mm²) | 0,2% proof stress (N/mm²) min. | Elongation on 5,65 √So (%) min. | Typical hardness values (Brinell) (see W10.7.1) | Impact energy | | Typical structure of matrix (see W10.9.3) |
| :--- | :--- | :--- | :--- | :--- | :---: | :---: | :--- |
| | | | | | **Test temp ºC** | **KV(2) J min** | |
| **Ordinary qualities** | 370 | 230 | 17 | 120-180 | - | - | Ferrite |
| | 400 | 250 | 12 | 140-200 | - | - | Ferrite |
| | 500 | 320 | 7 | 170-240 | - | - | Ferrite/Perlite |
| | 600 | 370 | 3 | 190-270 | - | - | Ferrite/Perlite |
| | 700 | 420 | 2 | 230-300 | - | - | Perlite |
| | 800 | 480 | 2 | 250-350 | - | - | Perlite or Tempered structure |
| **Special qualities** | 350 | 220 | 22(3) | 110-170 | +20 | 17(14) | Ferrite |
| | 400 | 250 | 18(3) | 140-200 | +20 | 14(11) | Ferrite |

**NOTE**
1. For intermediate values of specified minimum tensile strength, the minimum values for 0,2% proof and elongation may be obtained by interpolation.
2. The average value measured on 3 Charpy V-notch specimens. One result may be below the average value but not less than the minimum shown in brackets.
3. In the case of integrally cast samples, the elongation may be 2 percentage points less.

W10.7.3 Unless otherwise agreed only the tensile strength and elongation need be determined. The results of all tensile tests are to comply with the appropriate requirements of Table 1.

W10.7.4 Re-test requirements for tensile tests are to be in accordance with UR W2.

## 10.8 Inspection
(Rev. 1995)

W10.8.1 All castings are to be cleaned and adequately prepared for examination. The surfaces are not to be hammered, peened or treated in any way which may obscure defects.

W10.8.2 Before acceptance, all castings are to be visually examined including, where applicable, the examination of internal surfaces. Unless otherwise agreed the verification of dimensions is the responsibility of the manufacturer.

W10.8.3 Supplementary examination of castings by suitable nondestructive testing procedures is generally not required except in circumstances where there is reason to suspect the soundness of the casting.

W10.8.4 When required by the relevant construction Rules, castings are to be pressure tested before final acceptance.

W10.8.5 In the event of any casting proving defective during subsequent machining or testing is to be rejected notwithstanding any previous certification.

W10.8.6 Cast crankshaft are to be subjected to a magnetic particle inspection. Crack like indications are not allowed.

## W10.9 Metallographic examination
(Rev. 1995)

W10.9.1 For crankshafts the metallographic examination will be mandatory.

W10.9.2 When required, a representative sample from each ladle of treated metal is to be prepared for metallographic examination. These samples may conveniently be taken from the tensile test specimens but alternative arrangements for the provision of the samples may be adopted provided that they are taken from the ladle towards the end of the casting period.

W10.9.3 Examination of the samples is to show that at least 90% of the graphite is in a dispersed spheroidal or nodular form. Details of typical matrix structures are given in Table 1 and are intended for information purposes only.

## 10.10 Rectification of defective castings
(1978)

W10.10.1 At the discretion of the Surveyor, small surface blemishes may be removed by local grinding.

W10.10.2 Subject to the prior approval of the Surveyor, castings containing local porosity may be rectified by impregnation with a suitable plastic filler, provided that the extent of the porosity is such that it does not adversely affect the strength of the casting.

W10.10.3 Repairs by welding are generally not permitted.

## W10.11 Identification of castings
(Rev. 1995)

W10.11.1 The manufacturer is to adopt a system of identification which will enable all finished castings to be traced to the original ladle of treated metal and the Surveyor is to be given full facilities for so tracing the castings when required.

W10.11.2 Before acceptance, all castings which have been tested and inspected with satisfactory results are to be clearly marked by the manufacturer. At the discretion of individual Classification Societies any of the following particulars may be required:
(i) Quality of cast iron.
(ii) Identification number or other marking which will enable the full history of the casting to be traced.
(iii) Manufacturer's name or trade mark.
(iv) The Classification Society's name, initials or symbol.
(v) Abbreviated name of the Classification Society's local office.
(vi) Personal stamp of Surveyor responsible for inspection.
(vii) Where applicable, test pressure.
(viii) Date of final inspection.

W10.11.3 Where small castings are manufactured in large numbers, modified arrangements for identification may be specially agreed with the Classification Society.

## W10.12 Certification
(1978)

W10.12.1 The manufacturer is to provide the Surveyor with a test certificate or shipping statement giving the following particulars for each casting or batch of castings which has been accepted:
(i) Purchaser's name and order number.
(ii) Description of castings and quality of cast iron.
(iii) Identification number.
(iv) Results of mechanical tests.
(v) Where applicable, general details of heat treatment.
(vi) Where specifically required, the chemical analysis of ladle samples.
(vii) Where applicable, test pressure.


================================================================================
# FILE: UR_W/ur-w11-rev9-may-2017-cln.md
================================================================================

# W11 Normal and higher strength hull structural steels

**W11**
(1979)
(Rev. 1 1986)
(Rev. 2 1995 v.2.1)
(Rev. 3 June 2000)
(Rev. 4 May 2001)
(Rev. 5 July 2002)
(Rev. 6 May 2004)
(Rev. 7 Apr 2008)
(Corr. 1 Feb 2009)
(Rev. 8 Apr 2014)
(Rev. 9 May 2017)

## 1. Scope

**1.1** These requirements apply to weldable normal and higher strength hot-rolled steel plates, wide flats, sections and bars intended for use in hull construction.

**1.2** The requirements are primarily intended to apply to steel products with a thickness as follows:

For steel plates and wide flats:
- All Grades: Up to 100mm in thickness

For sections and bars:
- All Grades: Up to 50mm in thickness

For greater thickness certain variations in the requirements may be allowed or required in particular cases after consideration of the technical circumstances involved.

**1.3** Provision is made for four grades of normal strength steel based on the impact test requirements. For higher strength steels provision is made for three strength levels (315, 355 and 390 N/mm²) each subdivided into four grades based on the impact test temperature.

**1.4** Steels differing in chemical composition, deoxidation practice, conditions of supply and mechanical properties may be accepted, subject to the special approval of the Classification Society. Such steels are to be given a special designation.

**Note:**
1. Changes introduced in Rev.8 are to be uniformly implemented by IACS Societies on ships contracted for construction on or after 1 July 2015 and when the application for certification of steel plates is dated on or after 1 July 2015.
2. Changes introduced in Rev.9 are to be uniformly implemented by IACS Societies on ships contracted for construction on or after 1 July 2018, or when the application for certification of steel products is dated on or after 1 July 2018, or the application for certification of manufacturer approval is dated on or after 1 July 2018.
3. The “contracted for construction” date means the date on which the contract to build the vessel is signed between the prospective owner and the shipbuilder. For further details regarding the date of “contract for construction”, refer to IACS Procedural Requirement (PR) No. 29.

---

**1.5** These requirements also apply to normal and higher strength Corrosion Resistant steels when such steel is used as the alternative means of corrosion protection for cargo oil tanks as specified in the performance standard MSC.289 (87) of Regulation 3-11, Part A-1, Chapter II-1 of the SOLAS Convention (Corrosion protection of cargo oil tanks of crude oil tankers). Corrosion Resistant steels as defined within this UR, are steels whose corrosion resistance performance in the bottom or top of the internal cargo oil tank is tested and approved to satisfy the requirements in MSC.289 (87) in addition to other relevant requirements for hull structural steels, structural strength and construction. It is not intended that such steels be used for corrosion resistant applications in other areas of a vessel that are outside of those specified in the performance standard MSC.289 (87) of Regulation 3-11, Part A-1, Chapter II-1 of the SOLAS Convention. These requirements apply to plates, wide flats, sections and bars in all grades up to a maximum thickness of 50 mm.

## 2. Approval

**2.1** All materials are to be manufactured at works which have been approved by the Classification Society for the type and grade of steel which is being supplied. The suitability of each grade of steel for forming and welding is to be demonstrated during the initial approval tests at the steelworks. Approval of the steel works is to follow a scheme given in the Appendix A. For the steels intended for high heat input welding over 50kJ/cm, the approval of the manufacturer is to follow a scheme given in the Appendix B. For steels intended for a corrosion resistant designation, the approval of the manufacturer is to additionally follow the scheme given in Appendix C.

**2.2** It is the manufacturer’s responsibility to assure that effective process and production controls in operation are adhered to within the manufacturing specifications. Where control imperfection inducing possible inferior quality of product occurs, the manufacturer is to identify the cause and establish a countermeasure to prevent its recurrence. Also, the complete investigation report is to be submitted to the Surveyor.

For further use, each affected piece is to be tested to the Surveyor’s satisfaction.

The frequency of testing for subsequent products offered may be increased to gain confidence in the quality at the discretion of the Society.

**2.3** When steel is not produced at the works at which it is rolled, a certificate is to be supplied to the Surveyor at the rolling mill stating the process by which it was manufactured, the name of the manufacturer who supplied it, the number of the cast from which it was made and the ladle analysis. The Surveyor is to have access to the works at which the steel was produced.

**Note:**
1. The attention of the users must be drawn to the fact that when fatigue loading is present, the effective fatigue strength of a welded joint of higher strength steel may not be greater than that of a welded joint in normal strength steels.
2. Before subjecting steels produced by thermo-mechanical rolling to further heating for forming or stress relieving, or using high heat-input welding, special consideration must be given to the possibility of a consequent reduction in mechanical properties.

## 3. Method of Manufacture

**3.1** Steel is to be manufactured by the basic oxygen, electric furnace or open hearth processes or by other processes specially approved by the Classification Society.

**3.2** The deoxidation practice used for each grade is to comply with the appropriate requirements of Tables 1 and 2.

**3.3** The rolling practice applied for each grade is to comply with the appropriate condition of supply of Tables 4 and 5.

The definitions of applicable rolling procedures and the schematic diagrams are given as follows:

**(i) As Rolled, AR**
This procedure involves steel being cooled as it is rolled with no further heat treatment. The rolling and finishing temperatures are typically in the austenite recrystallization region and above the normalising temperature. The strength and toughness properties of steel produced by this process are generally less than steel heat treated after rolling or than steel produced by advanced processes.

**(ii) Normalising, N**
Normalising involves heating rolled steel above the critical temperature, Ac3, and in the lower end of the austenite recrystallization region for a specific period of time, followed by air cooling. The process improves the mechanical properties of as rolled steel by refining the grain size and homogenising the microstructure.

**(iii) Controlled Rolling, CR (Normalizing Rolling, NR):**
A rolling procedure in which the final deformation is carried out in the normalising temperature range, allowed to cool in air, resulting in a material condition generally equivalent to that obtained by normalising.

**(iv) Quenching and Tempering, QT**
Quenching involves a heat treatment process in which steel is heated to an appropriate temperature above the Ac3, held for a specific period of time, and then cooled with an appropriate coolant for the purpose of hardening the microstructure. Tempering subsequent to quenching is a process in which the steel is reheated to an appropriate temperature not higher than the Ac1, maintained at that temperature for a specific period of time to restore toughness properties by improving the microstructure and reduce the residual stress caused by the quenching process.

**(v) Thermo-Mechanical Rolling, TM (Thermo-Mechanical Controlled Processing, TMCP):**
This is a procedure which involves the strict control of both the steel temperature and the rolling reduction. Generally a high proportion of the rolling reduction is carried out close to the Ar3 temperature and may involve the rolling in the dual phase temperature region. Unlike controlled rolled (normalised rolling) the properties conferred by TM (TMCP) cannot be reproduced by subsequent normalising or other heat treatment.

The use of accelerated cooling on completion of TM-rolling may also be accepted subject to the special approval of the Society. The same applies for the use of tempering after completion of the TM-rolling.

**(vi) Accelerated Cooling, AcC**
Accelerated cooling is a process, which aims to improve mechanical properties by controlled cooling with rates higher than air cooling immediately after the final TM-rolling operation. Direct quenching is excluded from accelerated cooling.

The material properties conferred by TM and AcC cannot be reproduced by subsequent normalising or other heat treatment.

---

Where NR (CR) and TM with/without AcC are applied, the programmed rolling schedules are to be verified by the Classification Society at the time of the steel works approval, and are to be made available when required by the attending Surveyor. On the manufacturer’s responsibility, the programmed rolling schedules are to be adhered to during the rolling operation. Refer to the above 2.2. To this effect, the actual rolling records are to be reviewed by the manufacturer and occasionally by the Surveyor.

When deviation from the programmed rolling schedules or normalizing or quenching and tempering procedures occurs, the manufacturer shall take further measures required in the above 2.2 to the Surveyor’s satisfaction.

---

### Schematic Diagrams of Thermo-Mechanical and Conventional Processes

![Figure: Schematic Diagrams of Thermo-Mechanical and Conventional Processes](Schematic_Diagrams_of_Processes.png)
*Description: A diagram showing the temperature and reduction paths for AR, N, CR(NR), QT, and TM processes across various metallurgical structures (Recrystallized Austenite, Non-recrystallized Austenite, Austenite + Ferrite, and Ferrite + Perlite/Bainite).*

**Notes:**
- **AR:** As Rolled
- **N:** Normalizing
- **CR(NR):** Controlled Rolling (Normalizing Rolling)
- **QT:** Quenching and Tempering
- **TM:** Thermo-Mechanical Rolling (Thermo-Mechanical Controlled Process)
- **R:** Reduction
- **(\*):** Sometimes rolling in the dual-phase temperature region of austenite and ferrite
- **AcC:** Accelerated Cooling
- **♢:** Start rolling temperature
- **—:** Delays to allow cooling before finishing rolling process

## 4. Chemical Composition

**4.1** The chemical composition of samples taken from each ladle of each cast is to be determined by the manufacturer in an adequately equipped and competently staffed laboratory and is to comply with the appropriate requirements of Tables 1 and 2. For steel plates and wide flats over 50 mm thick, slight deviations in the chemical composition may be allowed as approved by the Classification Society.

**4.2** The manufacturer's declared analysis will be accepted subject to occasional checks if required by the Surveyor.

---

### Table 1 Chemical composition and deoxidation practice for normal strength steels

| Grade | A | B | D | E |
| :--- | :--- | :--- | :--- | :--- |
| **Deoxidation Practice** | For t ≤ 50 mm: Any method except rimmed steel ⁽¹⁾. For t > 50 mm: Killed | For t ≤ 50 mm: Any method except rimmed. For t > 50 mm: Killed | For t ≤ 25 mm: Killed. For t > 25 mm: Killed and fine grain treated | Killed and fine grain treated |
| **Chemical Composition %⁽⁴⁾⁽⁷⁾⁽⁸⁾ (ladle samples)** | **Carbon plus 1/6 of the manganese content is not to exceed 0.40%** | | | |
| C max. | 0.21 ⁽²⁾ | 0.21 | 0.21 | 0.18 |
| Mn min. | 2.5 x C | 0.80 ⁽³⁾ | 0.60 | 0.70 |
| Si max. | 0.50 | 0.35 | 0.35 | 0.35 |
| P max. | 0.035 | 0.035 | 0.035 | 0.035 |
| S max. | 0.035 | 0.035 | 0.035 | 0.035 |
| Al (acid soluble min) | - | - | 0.015 ⁽⁵⁾⁽⁶⁾ | 0.015 ⁽⁶⁾ |

**t = thickness**

**Notes:**
1. Grade A sections up to a thickness of 12.5 mm may be accepted in rimmed steel subject to the special approval of the Classification Society.
2. Max. 0.23% for sections.
3. When Grade B steel is impact tested the minimum manganese content may be reduced to 0.60%.
4. When any grade of steel is supplied in the thermo-mechanically rolled condition variations in the specified chemical composition may be allowed or required by the Classification Society.
5. For Grade D steel over 25 mm thick.
6. For Grade D steel over 25 mm thick and Grade E steel the total aluminium content may be determined instead of acid soluble content. In such cases the total aluminium content is to be not less than 0.020%. A maximum aluminium content may also be specified by the Classification Society. Other suitable grain refining elements may be used subject to the special approval of the Classification Society.
7. The Classification Society may limit the amount of residual elements which may have an adverse effect on the working and use of the steel, e.g. copper and tin.
8. Where additions of any other element have been made as part of the steelmaking practice, the content is to be indicated.

---

### Table 2 Chemical composition and deoxidation practice for higher strength steels

| Grade ⁽¹⁾ | A32, A36, A40 | D32, D36, D40 | E32, E36, E40 | F32, F36, F40 |
| :--- | :--- | :--- | :--- | :--- |
| **Deoxidation Practice** | | | killed and fine grain treated | |
| **Chemical Composition %⁽⁵⁾⁽⁷⁾ (ladle samples)** | | | | |
| C max. | 0.18 | | | 0.16 |
| Mn | 0.90 – 1.60 ⁽²⁾ | | | 0.90 – 1.60 |
| Si max. | 0.50 | | | 0.50 |
| P max. | 0.035 | | | 0.025 |
| S max. | 0.035 | | | 0.025 |
| Al (acid soluble min) | 0.015 ⁽³⁾⁽⁴⁾ | | | 0.015 ⁽³⁾⁽⁴⁾ |
| Nb | 0.02 – 0.05 ⁽⁴⁾ | | total: 0.12 max. | 0.02 – 0.05 ⁽⁴⁾ | total: 0.12 max. |
| V | 0.05 – 0.10 ⁽⁴⁾ | | | 0.05 – 0.10 ⁽⁴⁾ | |
| Ti max. | 0.02 | | | 0.02 | |
| Cu max. | 0.35 | | | 0.35 | |
| Cr max. | 0.20 | | | 0.20 | |
| Ni max. | 0.40 | | | 0.80 | |
| Mo max. | 0.08 | | | 0.08 | |
| N max. | - | | | 0.009 (0.012 if Al is present) | |
| Carbon Equivalent ⁽⁶⁾ | | | | | |

**Notes:**
1. The letter “H” may be added either in front or behind the grade mark e.g. HA 32 or AH 32.
2. Up to a thickness of 12.5 mm the minimum manganese content may be reduced to 0.70%.
3. The total aluminium content may be determined instead of the acid soluble content. In such cases the total aluminium content is to be not less than 0.020%.
4. The steel is to contain aluminium, niobium, vanadium or other suitable grain refining elements, either singly or in any combination. When used singly the steel is to contain the specified minimum content of the grain refining element. When used in combination, the specified minimum content of a fine graining element is not applicable.
5. When any grade of higher strength steel is supplied in the thermo-mechanically rolled condition variations in the specified chemical composition may be allowed or required by the Classification Society.
6. When required, the carbon equivalent value is to be calculated from the ladle analysis using the following formula:
   $Ceq = C + \frac{Mn}{6} + \frac{Cr + Mo + V}{5} + \frac{Ni + Cu}{15} (\%)$
   This formula is applicable only to steels which are basically of the carbon-manganese type and gives a general indication of the weldability of the steel.
7. Where additions of any other element have been made as part of the steelmaking practice, the content is to be indicated.

**4.3** For TM (TMCP) steels the following special requirements apply:
(i) The carbon equivalent value is to be calculated from the ladle analysis using the following formula and to comply with the requirements of Table 3;
$Ceq = C + \frac{Mn}{6} + \frac{Cr + Mo + V}{5} + \frac{Ni + Cu}{15} (\%)$
(ii) The following formula (cold cracking susceptibility) may be used for evaluating weldability instead of the carbon equivalent at the discretion of the Classification Society;
$Pcm = C + \frac{Si}{30} + \frac{Mn}{20} + \frac{Cu}{20} + \frac{Ni}{60} + \frac{Cr}{20} + \frac{Mo}{15} + \frac{V}{10} + 5B \%$

In such cases the cold cracking susceptibility value required may be specified by the Classification Society.

---

### Table 3 Carbon equivalent for higher strength steels up to 100 mm in thickness produced by TM

| Grade | Carbon Equivalent, max. (%) ⁽¹⁾ | |
| :--- | :--- | :--- |
| | **t ≤ 50** | **50 < t ≤ 100** |
| A32, D32, E32, F32 | 0.36 | 0.38 |
| A36, D36, E36, F36 | 0.38 | 0.40 |
| A40, D40, E40, F40 | 0.40 | 0.42 |

**t: thickness (mm)**

**Notes:**
(1) It is a matter for the manufacturer and shipbuilder to mutually agree in individual cases as to whether they wish to specify a more stringent carbon equivalent.

## 5. Condition of Supply

**5.1** All materials are to be supplied in a condition complying with the appropriate requirements of Tables 4 and 5.

### Table 4 Condition of supply for normal strength steels ⁽¹⁾

| Grades | Thickness | Condition of Supply |
| :--- | :--- | :--- |
| A | ≤ 50 mm | Any |
| | > 50 mm ≤ 100 mm | Normalized, controlled rolled or thermo-mechanically rolled ⁽²⁾ |
| B | ≤ 50 mm | Any |
| | > 50 mm ≤ 100 mm | Normalized, controlled rolled or thermo-mechanically rolled ⁽²⁾ |
| D | ≤ 35 mm | Any |
| | > 35 mm ≤ 100 mm | Normalized, controlled rolled or thermo-mechanically rolled ⁽³⁾ |
| E | ≤ 100 mm | Normalized or thermo-mechanically rolled ⁽³⁾ |

**Notes:**
(1) These conditions of supply and the impact test requirements are summarised in Table 8.
(2) Subject to the special approval of the Classification Society, Grades A and B steel plates may be supplied in the as rolled condition - see W11.14.2 (ii).
(3) Subject to the special approval of the Classification Society, sections in Grade D steel may be supplied in the as rolled condition provided satisfactory results are consistently obtained from Charpy V-notch impact tests. Similarly sections in Grade E steel may be supplied in the as rolled or controlled rolled condition. The frequency of impact tests is to be in accordance with W11.14.2 (ii) and W11.14.3 (iii) respectively.

---

### Table 5 Condition of supply for higher strength steels ⁽¹⁾

| Grades | Grain Refining Elements Used | Thickness | Condition of Supply |
| :--- | :--- | :--- | :--- |
| A32, A36 | Nb and/or V | ≤ 12.5 mm | Any |
| | | > 12.5 mm ≤ 100 mm | Normalized, controlled rolled or thermo-mechanically rolled ⁽³⁾ |
| | Al alone or with Ti | ≤ 20 mm | Any |
| | | > 20 mm ≤ 35 mm | Any, as rolled subject to special approval of the Classification Society ⁽²⁾ |
| | | > 35 mm ≤ 100 mm | Normalized, controlled rolled or thermo-mechanically rolled ⁽³⁾ |
| A40 | Any | ≤ 12.5 mm | Any |
| | | > 12.5 mm ≤ 50 mm | Normalized, controlled rolled or thermo-mechanically rolled |
| | | > 50 mm ≤ 100 mm | Normalized, thermo-mechanically rolled or quenched and tempered |
| D32, D36 | Nb and/or V | ≤ 12.5 mm | Any |
| | | > 12.5 mm ≤ 100 mm | Normalized, controlled rolled or thermo-mechanically rolled ⁽³⁾ |
| | Al alone or with Ti | ≤ 20 mm | Any |
| | | > 20 mm ≤ 25 mm | Any, as rolled subject to special approval of the Classification Society ⁽²⁾ |
| | | > 25 mm ≤ 100 mm | Normalized, controlled rolled or thermo-mechanically rolled ⁽³⁾ |
| D40 | Any | ≤ 50 mm | Normalized, controlled rolled or thermo-mechanically rolled |
| | | > 50 mm ≤ 100 mm | Normalized, thermo-mechanically rolled or quenched and tempered |
| E32, E36 | Any | ≤ 50 mm | Normalized or thermo-mechanically rolled ⁽³⁾ |
| | | > 50 mm ≤ 100 mm | Normalized, thermo-mechanically rolled |
| E40 | Any | ≤ 50 mm | Normalized, thermo-mechanically rolled or quenched and tempered |
| | | > 50 mm ≤ 100 mm | Normalized, thermo-mechanically rolled or quenched and tempered |
| F32, F36, F40 | Any | ≤ 50 mm | Normalized, thermo-mechanically rolled or quenched and tempered ⁽⁴⁾ |
| | | > 50 mm ≤ 100 mm | Normalized, thermo-mechanically rolled or quenched and tempered |

**Notes:**
(1) These conditions of supply and the requirements for impact tests are summarised in Table 9.
(2) The frequency of impact tests is to be in accordance with W11.14.2 (ii).
(3) Subject to the special approval of the Classification Society, sections in Grades A32, A36, D32 and D36 steels may be supplied in the as rolled condition provided satisfactory results are consistently obtained from Charpy V-notch impact tests. Similarly sections in Grades E32 and E36 steels maybe supplied in the as rolled or controlled rolled condition. The frequency of impact tests is to be in accordance with W11.14.2 (ii) and W11.14.2 (iii) respectively.
(4) Subject to the special approval of the Classification Society, sections in Grades F32 and F36 steels may be supplied in the controlled rolled condition. The frequency of impact tests is to be in accordance with W11.14.3 (iii).

---

## 6. Mechanical Properties

**6.1** For tensile test either the upper yield stress (ReH) or where ReH cannot be determined, the 0.2 percent proof stress (Rp 0.2) is to be determined and the material is considered to comply with the requirements if either value meets or exceeds the specified minimum value for yield strength (Re).

**6.2** The results obtained from tensile tests are to comply with the appropriate requirements of Tables 6 and 7.

### Table 6 Mechanical properties for normal strength steels

| Grade | Yield Strength ReH (N/mm²) min | Tensile Strength Rm (N/mm²) | Elongation (5.65 √S₀) A₅ (%) | Test Temp. °C | Impact Test Average Impact Energy (J) min | | | | | |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| | | | | | **t ≤ 50** | | **50 < t ≤ 70** | | **70 < t ≤ 100** | |
| | | | | | **Long⁽³⁾** | **Trans⁽³⁾** | **Long⁽³⁾** | **Trans⁽³⁾** | **Long⁽³⁾** | **Trans⁽³⁾** |
| A | 235 | 400/520 ⁽¹⁾ | 22 ⁽²⁾ | +20 | - | - | 34 ⁽⁵⁾ | 24 ⁽⁵⁾ | 41 ⁽⁵⁾ | 27 ⁽⁵⁾ |
| B | 235 | 400/520 | 22 ⁽²⁾ | 0 | 27 ⁽⁴⁾ | 20 ⁽⁴⁾ | 34 | 24 | 41 | 27 |
| D | 235 | 400/520 | 22 ⁽²⁾ | -20 | 27 | 20 | 34 | 24 | 41 | 27 |
| E | 235 | 400/520 | 22 ⁽²⁾ | -40 | 27 | 20 | 34 | 24 | 41 | 27 |

**t: thickness (mm)**

**Notes:**
(1) For all thicknesses of Grade A sections the upper limit for the specified tensile strength range may be exceeded at the discretion of the Classification Society.
(2) For full thickness flat tensile test specimens with a width of 25 mm and a gauge length of 200mm the elongation is to comply with the following minimum values:

| Thickness mm | ≤ 5 | > 5 ≤ 10 | > 10 ≤ 15 | > 15 ≤ 20 | > 20 ≤ 25 | > 25 ≤ 30 | > 30 ≤ 40 | > 40 ≤ 50 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Elongation % | 14 | 16 | 17 | 18 | 19 | 20 | 21 | 22 |

(3) See paragraph W11.6.3.
(4) Charpy V-notch impact tests are generally not required for Grade B steel with thickness of 25 mm or less.
(5) Impact tests for Grade A over 50 mm thick are not required when the material is produced using fine grain practice and furnished normalised. TM rolling may be accepted without impact testing at the discretion of the Society.

---

### Table 7 Mechanical properties for higher strength steels

| Grade | Yield Strength ReH (N/mm²) min | Tensile Strength Rm (N/mm²) | Elongation (5.65 √S₀) A₅ (%) | Test Temp. °C | Impact Test Average Impact Energy (J) min | | | | | |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| | | | | | **t ≤ 50** | | **50 < t ≤ 70** | | **70 < t ≤ 100** | |
| | | | | | **Long⁽²⁾** | **Trans⁽²⁾** | **Long⁽²⁾** | **Trans⁽²⁾** | **Long⁽²⁾** | **Trans⁽²⁾** |
| A32 | 315 | 440/570 | 22 ⁽¹⁾ | 0 | 31 ⁽³⁾ | 22 ⁽³⁾ | 38 | 26 | 46 | 31 |
| D32 | 315 | 440/570 | 22 ⁽¹⁾ | -20 | 31 | 22 | 38 | 26 | 46 | 31 |
| E32 | 315 | 440/570 | 22 ⁽¹⁾ | -40 | 31 | 22 | 38 | 26 | 46 | 31 |
| F32 | 315 | 440/570 | 22 ⁽¹⁾ | -60 | 31 | 22 | 38 | 26 | 46 | 31 |
| A36 | 355 | 490/630 | 21 ⁽¹⁾ | 0 | 34 ⁽³⁾ | 24 ⁽³⁾ | 41 | 27 | 50 | 34 |
| D36 | 355 | 490/630 | 21 ⁽¹⁾ | -20 | 34 | 24 | 41 | 27 | 50 | 34 |
| E36 | 355 | 490/630 | 21 ⁽¹⁾ | -40 | 34 | 24 | 41 | 27 | 50 | 34 |
| F36 | 355 | 490/630 | 21 ⁽¹⁾ | -60 | 34 | 24 | 41 | 27 | 50 | 34 |
| A40 | 390 | 510/660 | 20 ⁽¹⁾ | 0 | 39 | 26 | 46 | 31 | 55 | 37 |
| D40 | 390 | 510/660 | 20 ⁽¹⁾ | -20 | 39 | 26 | 46 | 31 | 55 | 37 |
| E40 | 390 | 510/660 | 20 ⁽¹⁾ | -40 | 39 | 26 | 46 | 31 | 55 | 37 |
| F40 | 390 | 510/660 | 20 ⁽¹⁾ | -60 | 39 | 26 | 46 | 31 | 55 | 37 |

**t: thickness (mm)**

**Notes:**
(1) For full thickness flat tensile test specimens with a width of 25mm and a gauge length of 200 mm the elongation is to comply with the following minimum values:

| Thickness (mm) | Grade | ≤ 5 | > 5 ≤ 10 | > 10 ≤ 15 | > 15 ≤ 20 | > 20 ≤ 25 | > 25 ≤ 30 | > 30 ≤ 40 | > 40 ≤ 50 |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Elongation % | A32, D32, E32 & F32 | 14 | 16 | 17 | 18 | 19 | 20 | 21 | 22 |
| | A36, D36, E36 & F36 | 13 | 15 | 16 | 17 | 18 | 19 | 20 | 21 |
| | A40, D40, E40 & F40 | 12 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |

(2) See paragraph W11.6.3.
(3) For Grades A32 and A36 steels a relaxation in the number of impact tests for acceptance purposes may be permitted by special agreement with the Classification Society provided that satisfactory results are obtained from occasional check tests.

**6.3** Minimum average energy values are specified for Charpy V-notch impact test specimens taken in either the longitudinal or transverse directions (see W11.13.2). Generally only longitudinal test specimens need to be prepared and tested except for special applications where transverse test specimens may be required by the purchaser or the Classification Society. Transverse test results are to be guaranteed by the supplier.

The tabulated values are for standard specimens 10 mm x 10 mm. For plate thicknesses less than 10 mm, impact test may be waived at the discretion of the Classification Society or sub-size specimens, as specified in UR W2, may be used.

**6.4** The average value obtained from one set of three impact tests is to comply with the requirements given in Tables 6 and 7. One individual value only may be below the specified average value provided it is not less than 70% of that value.

**6.5** Generally, impact tests are not required when the nominal plate thickness is less than 6 mm.

---

## 7. Surface quality

**7.1** The steel is to be free from surface defects prejudicial to the use of the material for the intended application.
The finished material is to have a surface quality in accordance with a recognized standard such as EN 10163 parts 1, 2 and 3, or an equivalent standard accepted by the Classification Society, unless otherwise specified in this section.

**7.2** The responsibility for meeting the surface finish requirements rests with the manufacturer of the material, who is to take the necessary manufacturing precautions and is to inspect the products prior to delivery. At that stage, however, rolling or heat treatment scale may conceal surface discontinuities and defects. If, during the subsequent descaling or working operations, the material is found to be defective, the Classification Society may require materials to be repaired or rejected.

**7.2.1** The surface quality inspection method shall be in accordance with recognized national or international standards agreed between purchaser and manufacturer, accepted by the Classification Society.

**7.2.2** If agreed by the manufacturer and purchaser, steel may be ordered with improved surface finish over and above these requirements.

**7.3 Acceptance Criteria**

**7.3.1 Imperfections**
Imperfections of a harmless nature, for example pitting, rolled-in scale, indentations, roll marks, scratches and grooves, regarded as being inherent of the manufacturing process, are permissible irrespective of their number, provided the maximum permissible limits of Class A of EN 10163-2 or limits specified in a recognized equivalent standard accepted by the Classification Society, are not exceeded and the remaining plate or wide flat thickness remains within the average allowable minus thickness tolerance specified in UR W13. Total affected area with imperfection not exceeding the specified limits are not to exceed 15 % of the total surface in question.

**7.3.2 Defects**
Affected areas with imperfections with a depth exceeding the limits of Class A of EN 10163-2 or the maximum permissible limits specified in a recognized equivalent standard accepted by the Classification Society, shall be repaired irrespective of their number.

Cracks, injurious surface flaws, shells (over lapping material with non-metallic inclusion), sand patches, laminations and sharp edged seams (elongated defects) visually evident on surface and/or edge of plate are considered defects, which would impair the end use of the product and which require rejection or repair, irrespective of their size and number.

**7.4 Repair**

**7.4.1 Grinding repair**
Grinding may be applied provided all the conditions below are adhered to:
(a) The nominal product thickness will not be reduced by more than 7% or 3 mm, whichever is the less.
(b) Each single ground area does not exceed 0,25 m².
(c) All ground areas do not exceed 2% of the total surface in question.
(d) Ground areas lying in a distance less than their average breadth to each other are to be regarded as one single area.
(e) Ground areas lying opposite each other on both surfaces shall not decrease the product thickness by values exceeding the limits as stated under (a).

Defects or unacceptable imperfections are to be completely removed by grinding and the remaining plate or wide flat thickness shall remain within the average allowable minus thickness tolerance specified in UR W13. The ground areas shall be a smooth transition to the surrounding surface of the product. Complete elimination of the defect is to be verified by magnetic particle or by liquid penetrant testing.

**7.4.2 Welding repair**
Weld repair procedures and the method are to be reported and be approved by the Classification Societies. Repair of defects such as unacceptable imperfections, cracks, shells or seams shall be followed by magnetic particle or liquid penetrant testing.

Local defects which cannot be repaired by grinding as stated in 7.4.1 may be repaired by welding with the agreement of the Classification Society subject to the following conditions:
(a) Any single welded area shall not exceed 0,125 m² and the sum of all areas shall not exceed 2% of the surface side in question.
(b) The distance between two welded areas shall not be less than their average width.
(c) The weld preparation shall not reduce the thickness of the product below 80% of the nominal thickness. For occasional defects with depths exceeding the 80% limit, special consideration at the Surveyor’s discretion will be necessary.
(d) If weld repair depth exceeds 3 mm, UT may be requested by the Classification Society. If required, UT shall be carried out in accordance with an approved procedure.
(e) The repair shall be carried out by qualified welders using an approved procedure for the appropriate steel grade. The electrodes shall be of low hydrogen type and shall be dried in accordance with the manufacturer’s requirements and protected against rehumidification before and during welding.

**7.5** The surface quality and condition requirement herein are not applied to products in forms of bars and tubulars, which will be subject to manufacturers’ conformance standards.

## 8. Internal soundness

**8.1** If plates and wide flats are ordered with ultrasonic inspection, this is to be made in accordance with an accepted standard at the discretion of the Classification Society.

**8.2** Verification of internal soundness is the responsibility of the manufacturer. The acceptance of internal soundness by the Classification Society’s surveyor shall not absolve the manufacturer from this responsibility.

---

## 9. Tolerances

**9.1** Unless otherwise agreed or specially required the thickness tolerances in Unified Requirement W13 "Thickness tolerances of steel plates and wide flats" are applicable.

## 10. Identification of Materials

**10.1** The steelmaker is to adopt a system for the identification of ingots, slabs and finished pieces which will enable the material to be traced to its original cast.

**10.2** The Surveyor is to be given full facilities for so tracing the material when required.

## 11. Testing and Inspection

**11.1 Facilities for Inspection**
The manufacturer is to afford the Surveyor all necessary facilities and access to all relevant parts of the works to enable him to verify that the approved process is adhered to, for the selection of test materials, and the witnessing of tests, as required by the Rules, and for verifying the accuracy of the testing equipment.

**11.2 Testing Procedures**
The prescribed tests and inspections are to be carried out at the place of manufacture before dispatch. The test specimens and procedures are to be in accordance with Unified Requirement W2 “Test Specimens and Mechanical Testing Procedures for Materials”. All the test specimens are to be selected and stamped by the Surveyor and tested in his presence, unless otherwise agreed.

**11.3 Through Thickness Tensile Tests**
If plates and wide flats with thickness of 15 mm and over are ordered with through thickness properties, the through thickness tensile test in accordance with Unified Requirement W14 “Steel Plates and Wide Flats with Specified Minimum Through Thickness Properties (“Z” quality)” is to be carried out.

**11.4 Dimensions**
Verification of dimensions are the responsibility of the steel maker. The acceptance by the Classification Society’s Surveyor shall not absolve the steel maker from this responsibility.

## 12. Test Material

**12.1 Definitions**
(a) Piece: the term "piece" is understood to mean the rolled product from a single slab, billet or ingot if this is rolled directly into plates, sections or bars.
(b) Batch: a number of similar pieces presented as a group for acceptance tests.

**12.2 Test Samples**
(a) All material in a batch presented for acceptance tests is to be of the same product form e.g. plates, flats, sections, etc. from the same cast and in the same condition of supply.
(b) The test samples are to be fully representative of the material and, where appropriate, are not to be cut from the material until heat treatment has been completed.
(c) The test specimens are not to be separately heat treated in any way.
(d) Unless otherwise agreed the test samples are to be taken from the following positions:
(i) Plates and flats with a width ≥ 600 mm. The test samples are to be taken from one end at a position approximately midway between the axis in the direction of the rolling and the edge of the rolled product (see Fig. 1). Unless otherwise agreed the tensile test specimens are to be prepared with their longitudinal axes transverse to the final direction of rolling.
(ii) Flats with a width < 600 mm, bulb flats and other sections. The test samples are to be taken from one end at a position approximately one third from the outer edge (see Figs. 2, 3 and 4) or in the case of small sections, as near as possible to this position. In the case of channels, beams or bulb angles, the test samples may alternatively be taken from a position approximately one quarter of the width from the web centre line or axis (see Fig. 3). The tensile test specimens may be prepared with their longitudinal axes either parallel or transverse to the final direction of rolling.
(iii) Bars and other similar products. The test samples are to be taken so that the longitudinal axes of the test specimens are parallel to the direction of rolling and are as near as possible to the following:
– for non-cylindrical sections, at one third of the half diagonal from the outside,
– for cylindrical sections, at one third of the radius from the outside (see Fig. 6).

---

![Figure 1, 2, 3: Test sample positions for Plates and flats, Angles, and Channels](Test_Sample_Positions_123.png)
*Description: Diagrams showing test sample positions. Fig 1 shows a plate with samples at 1/4 and 1/2 thickness and midway between axis and edge. Fig 2 shows an angle with sample at 1/3 of the flange from the edge. Fig 3 shows a channel with samples at 1/4 and 1/3 positions.*

![Figure 4, 5, 6: Test sample positions for H-sections, Bulb flats, and Bars](Test_Sample_Positions_456.png)
*Description: Diagrams showing test sample positions. Fig 4 shows an H-section. Fig 5 shows a bulb flat with sample at 1/3 from the edge. Fig 6 shows a bar with sample at 1/3 of the radius/diagonal from the outside.*

## 13. Mechanical Test specimens

**13.1 Tensile Test Specimens**
The dimensions of the tensil test specimens are to be in accordance with Unified Requirement, W2. Generally for plates, wide flats and sections flat test specimens of full product thickness are to be used. Round test specimens may be used when the product thickness exceeds 40 mm or for bards and other similar products. Alternatively for small sizes of bars, etc. test specimens may consist of a suitable length of the full cross section of the product.

**13.2 Impact Test Specimens**
The impact test specimens are to be of the Charpy V-notch type cut with their edge within 2 mm from the “as rolled” surface with their longitudinal axes either parallel (indicated “Long” in Table 6 & 7) or transverse (indicated "Trans" in Tables 6 & 7) to the final direction of rolling of the material. The notch is to be cut in a face of the test specimen which was originally perpendicular to the rolled surface. The position of the notch is not to be nearer than 25 mm to a flame cut or sheared edge (see also W11.6.3). Where the product thickness exceeds 40 mm, the impact test specimens are to be taken with their longitudinal axis at a quarter thickness position.

## 14. Number of Test Specimens

**14.1 Number of Tensile Tests**
For each batch presented, except where specially agreed by the Classification Society, one tensile test is to be made from one piece unless the weight of finished material is greater than 50 tonnes or fraction thereof. Additionally tests are to be made for every variation of 10 mm in the thickness or diameter of products from the same cast.

**14.2 Number of Impact Tests (except for Grades E, E32, E36, E40, F32, F36 and F40), see Tables 8 & 9.**
(i) Except where otherwise specified or specially agreed by the Classification Society, for each batch presented, at least one set of three Charpy V-notch test specimens is to be made from one piece unless the weight of finished material is greater than 50 tonnes, in which case one extra set of three test specimens is to be made from a different piece from each 50 tonnes or fraction thereof. When steel plates except for Grade A steel over 50 mm in thickness is supplied in the controlled rolled condition, the frequency of impact test is to be made from a different piece from each 25 tonnes or fraction thereof.
(ii) For steel plates of Grades A40 and D40 with thickness over 50 mm in normalized or TM condition, one set of impact test specimens is to be taken from each batch of 50 tonnes or fraction thereof. For those in QT condition, one set of impact test specimens is to be taken from each length as heat treated.
(iii) When, subject to the special approval of the Classification Society, material is supplied in the as rolled condition, the frequency of impact tests is to be increased to one set from each batch of 25 tonnes or fraction thereof. Similarly Grade A steel over 50 mm in thickness may be supplied in the as rolled condition. In such case one set of three Charpy V-notch test specimens is to be taken from each batch of 50 tonnes or fraction thereof.
(iv) The piece selected for the preparation of the test specimens is to be the thickest in each batch.

**14.3 Number of Impact Tests (Grades E, E32, E36, E40, F32, F36 and F40).**
(i) For steel plates supplied in the normalised or TM condition one set of impact test specimens is to be taken from each piece. For quenched and tempered steel plates one set of impact test specimens is to be taken from each length as heat treated.
(ii) For sections one set of impact tests is to be taken from each batch of 25 tonnes or fraction thereof.
(iii) When, subject to the special approval of the Classification Society, sections other than Grades E40 and F40 are supplied in the as rolled or controlled rolled condition, one set of impact tests is to be taken from each batch of 15 tonnes or fraction thereof.
(iv) For (ii) and (iii) above the piece selected for the preparation of the test specimens is to be the thickest in each batch.

## 15. Retest Procedures

**15.1** When the tensile test from the first piece selected in accordance with W11.14.1 fails to meet the requirements re-test requirements for tensile tests are to be in accordance with UR W2.

**15.2** If one or both of the additional tests referred to above are unsatisfactory, the piece is to be rejected, but the remaining material from the same batch may be accepted provided that two of the remaining pieces in the batch selected in the same way, are tested with satisfactory results. If unsatisfactory results are obtained from either of these two pieces then the batch of material is to be rejected.

**15.3** Re-test requirements for Charpy impact tests are to be in accordance with UR W2.

**15.4** When the initial piece, representing a batch, gives unsatisfactory results from the additional Charpy V-notch impact tests referred to above, this piece is to be rejected but the remaining material in the batch may be accepted provided that two of the remaining pieces in the batch are tested with satisfactory results. If unsatisfactory results are obtained from either of these two pieces then the batch of material is to be rejected. The pieces selected for these additional tests are to be the thickest remaining in the batch.

**15.5** If any test specimen fails because of faulty preparation, visible defects or (in the case of tensile test) because of fracturing outside the range permitted for the appropriate gauge length, the defective test piece may, at the Surveyors discretion, be disregarded and replayed by an additional test piece of the same type.

**15.6** At the option of the steelmaker, when a batch of material is rejected, the remaining pieces in the batch may be resubmitted individually for test and those pieces which give satisfactory results may be accepted.

**15.7** At the option of the steelmaker, rejected material may be resubmitted after heat treatment or reheat treatment, or may be resubmitted as another grade of steel and may then be accepted provided the required tests are satisfactory.

**15.8** In the event of any material proving unsatisfactory during subsequent working or fabrication, such material may be rejected, notwithstanding any previous satisfactory testing and/or certification.

## 16. Branding

**16.1** Every finished piece is to be clearly marked by the maker in at least one place with the Classification Society's brand and the following particulars:
(i) Unified identification mark for the grade steel (e.g. A, A36).
(ii) Steels which have been specially approved by the Classification Society and which differ from these requirements (see W11.1.4) are to have the letter "S" after the above identification mark (e.g. A36S, ES).
(iii) When required by the Classification Society, material supplied in the thermo-mechanically controlled process condition is to have the letters TM added after the identification mark (e.g. E36 TM).
(iv) Name or initials to identify the steelworks.
(v) Cast or other number to identify the piece.
(vi) If required by the purchaser, his order number or other identification mark.

**16.2** Steel plates that have complied with the requirements for corrosion resistant steel will be identified by adding a corrosion designation to the unified identification mark for the grade of steel.
The corrosion resistant steel is to be designated according to its area of application as follows:
- Lower surface of strength deck and surrounding structures: **RCU**
- Upper surface of inner bottom plating and surrounding structures: **RCB**
- For both strength deck and inner bottom plating: **RCW**

Example of designation: **A36 TM RCB Z35**

**16.3** The above particulars, but excluding the manufacturer's name or trade mark where this is embossed on finished products are to be encircled with paint or otherwise marked so as to be easily recognisable.

**16.4** Where a number of light materials are securely fastened together in bundles the manufacturer may, subject to the agreement of the Classification Society, brand only the top piece of each bundle, or alternatively, a firmly fastened durable label containing the brand may be attached to each bundle.

**16.5** In the event of any material bearing the Classification Society's brand failing to comply with the test requirements, the brand is to be unmistakably defaced by the manufacturer.

## 17. Documentation

**17.1** The Surveyor is to be supplied with the number of copies as required by the Classification Society, of the test certificates or shipping statements for all accepted materials. The Classification Society may require separate documents of each grade of steel. These documents are to contain, in addition to the description, dimensions, etc., of the material, at least the following particulars:
(i) Purchaser's order number and if known the hull number for which the material is intended.
(ii) Identification of the cast and piece including, where appropriate, the test specimen number.
(iii) Identification of the steelworks.
(iv) Identification of the grade of steel.
(v) Ladle analysis (for elements specified in Tables 1 & 2).
(vi) For steel with a corrosion resistant steel designation the weight percentage of each element added or intentionally controlled for improving corrosion resistance.
(vii) Condition of supply when other than as rolled i.e. normalised, controlled rolled or thermomechanically rolled.
(viii) State if rimming steel has been supplied for grade A sections, up to 12.5 mm thick.
(ix) Test Results

**17.2** Before the test certificates or shipping statements are signed by the Surveyor, the manufacturer is required to furnish him with a written declaration stating that the material has been made by an approved process and that it has been subjected to and has withstood satisfactory the required tests in the presence of the Surveyor or his authorized deputy. The name of the Classification Society is to appear on the test certificate. The following form of declaration will be accepted if stamped or printed on each test certificate or shipping statement with the name of the steelworks and initialled for the makers by an authorized official:
"We hereby certify that the material has been made by an approved process and has been satisfactorily tested in accordance with the Rules of the Classification Society."

---

### Table 8 Required condition of supply and number of impact tests for normal strength steels

| Grade | Deoxidation Practice | Products | Condition of Supply (Batch for Impact Tests)⁽¹⁾⁽²⁾ | | | | | | |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| | | | **Thickness (mm)** | | | | | | |
| | | | **10** | **12.5** | **20** | **25** | **30** | **35** | **40** | **50** | **100** |
| A | Rimmed | Sections | A (-) | | | | | | Not applicable | |
| | For t ≤ 50mm Any method except rimmed For t > 50mm Killed | Plates | A (-) | | | | | | N(-) TM(-)⁽³⁾ CR(50), AR*(50) | |
| | | Sections | A (-) | | | | | | Not applicable | |
| B | For t ≤ 50mm Any method except rimmed For t > 50mm Killed | Plates | A (-) | | | | A(50) | | N(50) TM(50) CR(25), AR*(25) | |
| | | Sections | A (-) | | | | A(50) | | Not applicable | |
| D | Killed | Plates Sections | A(50) | | | | | | Not applicable | |
| | Plates Killed and fine grain treated | Plates | A(50) | | | | | | N(50) CR(50) TM(50) | N(50) TM(50) CR(25) | |
| | | Sections | A(50) | | | | | | N(50) CR(50) TM(50) AR*(25) | Not applicable | |
| E | Killed and fine grain treated | Plates | N(Each piece) TM(Each piece) | | | | | | | | |
| | | Sections | N(25) TM(25) AR*(15), CR*(15) | | | | | | Not applicable | |

**Remarks:**
1. **Condition of Supply**
   - **A** – Any
   - **N** – Normalised Condition
   - **CR** – Controlled Rolled Condition
   - **TM** – Thermo-Mechanical rolling
   - **AR\*** – As Rolled Condition subject to special approval of the Classification Society
   - **CR\*** – Controlled Rolled Condition subject to special approval of the Classification Society
2. **Number of Impact Tests**
   One set of impact tests is to be taken from each batch of the "specified weight" in ( ) or fraction thereof.
3. See Note (5) of Table 6.

---

### Table 9 Required condition of supply and number of impact tests for higher strength steels

*(Note: Table 9 is summarized for brevity, preserving the core structure)*

| Grades | Grain Refining Elements | Products | Thickness (mm) and Condition of Supply |
| :--- | :--- | :--- | :--- |
| **A32, A36** | Nb and/or V | Plates | 10-50: A(50), CR(50), TM(50). >50: N(50), CR(50), TM(50) |
| | | Sections | 10-50: A(50). >50: N(50), CR(50), TM(50), AR*(25) |
| | Al alone or with Ti | Plates | 10-25: A(50), AR*(25). 25-50: N(50), CR(50), TM(50). >50: N(50), CR(50), TM(50) |
| | | Sections | 10-20: A(50). >20: N(50), CR(50), TM(50), AR*(25) |
| **A40** | Any | Plates | 10-50: A(50), N(50), CR(50), TM(50). >50: N(50), TM(50), QT(Each length) |
| | | Sections | 10-50: A(50), N(50), CR(50), TM(50) |
| **D32, D36** | Nb and/or V | Plates | 10-50: A(50), N(50), CR(50), TM(50). >50: N(50), CR(50), TM(50) |
| | | Sections | 10-50: A(50). >50: N(50), CR(50), TM(50), AR*(25) |
| | Al alone or with Ti | Plates | 10-25: A(50), AR*(25). 25-100: N(50), CR(50), TM(50) |
| | | Sections | 10-20: A(50). >20: N(50), CR(50), TM(50), AR*(25) |
| **D40** | Any | Plates | 10-50: N(50), CR(50), TM(50). >50: N(50), TM(50), QT(Each length) |
| | | Sections | 10-50: N(50), CR(50), TM(50) |
| **E32, E36** | Any | Plates | 10-100: N(Each piece), TM(Each piece) |
| | | Sections | 10-50: N(25), TM(25), AR*(15), CR*(15) |
| **E40** | Any | Plates | 10-100: N(Each piece), TM(Each piece), QT(Each length) |
| | | Sections | 10-50: N(25), TM(25), QT(25) |
| **F32, F36** | Any | Plates | 10-100: N(Each piece), TM(Each piece), QT(Each length) |
| | | Sections | 10-50: N(25), TM(25), QT(25), CR*(15) |
| **F40** | Any | Plates | 10-100: N(Each piece), TM(Each piece), QT(Each length) |
| | | Sections | 10-50: N(25), TM(25), QT(25) |

**Remarks:**
(1) **Condition of Supply**
    - **A** - Any
    - **N** - Normalized Condition
    - **CR** - Controlled Rolled Condition
    - **TM** - Thermo-Mechanical Rolling
    - **QT** - Quenched and Tempered Condition
    - **AR\*** - As Rolled Condition subject to special approval
    - **CR\*** - Controlled Rolled Condition subject to special approval
(2) **Number of Impact Tests**
    One set of impact tests is to be taken from each batch of the “specified weight” in ( ) or fraction thereof. For grades A32 and A36 steels a relaxation in the number of impact tests may be permitted. (See Note(3) of Table 7.)

---

## Appendix A. Manufacturing Approval Scheme of Hull Structural Steels

### A1. Manufacturing Approval Scheme of Semi Finished Products for Hull Structural Steels

**1. Scope of application**
This document specifies the scheme for the approval of the manufacturing process of semi-finished products such as ingots, slabs, blooms and billets for the structural steels.

**2. Approval application**
**2.1 Documents to be submitted**
The manufacturer has to submit request of approval, proposed approval test program and general information relevant to:
a) Name and site address of the manufacturer, location of workshops, total annual production, etc.
b) Organization and quality: organizational chart, staff, ISO 9001 certification, etc.
c) Manufacturing facilities: flow chart, storage of raw materials and finished products, etc.
d) Details of inspections and quality control facilities.
e) Type of products, types of steel, range of thickness and aim material properties.
f) Steelmaking: process, capacity, casting methods (ingot or continuous), etc.
g) Approval already granted by other Classification Societies.

**2.2 Documents to be submitted for changing the approval conditions**
...

**3. Approval tests**
**3.1 Extent of the approval tests**
...

---

### A2. Manufacturing Approval Scheme of Hull Structural Steels

**1. Scope of application**
This document specifies the scheme for the approval of the manufacturing process of normal and higher strength hull structural steels.

**2. Approval application**
**2.1 Documents to be submitted**
...
i) Programmed rolling: description of process, normalizing temperature, control standards for typical rolling parameters, etc.
j) Recommendations for working and welding.
...

**3. Approval tests**
**3.4 Selection of the test product**
For each grade of steel and for each manufacturing process, one test product with the maximum thickness and one test product of average thickness are in general to be selected.

**3.6 Tests on base material**
**3.6.1 Type of tests**
The tests to be carried out are indicated in Table 1.

---

### Table 1 Tests on base material

| Type of test | Position of the samples and direction of the test specimens ⁽¹⁾ | Remarks |
| :--- | :--- | :--- |
| Tensile test | Top and bottom transverse ⁽²⁾ | ReH, Rm, A₅(%), RA(%) are to be reported |
| Tensile test (stress relieved) only for TM steels | Top and bottom transverse ⁽²⁾ | Stress relieving at 600 °C (2 min/mm with minimum 1 hour) |
| Impact tests ⁽³⁾ on non aged specimens | Top and bottom - longitudinal / Top - transverse ⁽⁴⁾ | Testing temperature (°C) depends on grade |
| Impact test ⁽³⁾ on strain aged specimens ⁽⁵⁾ | Top - longitudinal | Testing temperature (°C) depends on grade |
| Chemical analyses ⁽⁶⁾ | Top | Complete analyses including micro alloying elements |
| Sulphur prints | Top | |
| Micro examination | Top | |
| Grain size determination | Top | only for fine grain steels |
| Drop weight test ⁽⁴⁾ | Top | only for grades E, E32, E36, E40, F32, F36, F40 |
| Through thickness tensile tests | Top and bottom | only for grades with improved through thickness properties |

**Notes for Table 1:**
1) For hot rolled strips see 3.6.2.
2) Longitudinal direction for sections and plates having width less than 600 mm.
3) One set of 3 Charpy V-notch impact specimens is required for each impact test.
4) Not required for sections and plates having width less than 600 mm.
5) Deformation 5% + 1 hour at 250°C.
6) Besides product analyses, ladle analyses are required.

---

## Appendix B. Approval scheme for manufacturer of hull structural steels intended for welding with high heat input

**1. Scope**
This document specifies the weldability confirmation scheme of normal and higher strength hull structural steels intended for welding with high heat input over 50kJ/cm.

**3. Confirmation tests**
**3.5 Examinations and tests for the test assembly**
The test assembly is to be examined and tested for:
a) Visual examination
b) Macroscopic test
c) Microscopic test
d) Hardness test
e) Transverse tensile test
f) Bend test
g) Impact test

---

## Appendix C. Procedure for Approval of Corrosion resistant steels for cargo oil tanks

**1. Scope**
This document specifies the scheme for the approval of corrosion resistant steels based upon corrosion testing.

### Table 2.1 Designations for Corrosion Resistant Steels

| Type of steel | Location where steel is effective | Corrosion Resistant Designation |
| :--- | :--- | :--- |
| Rolled steel for hull | For lower surface of strength deck and surrounding structures (ullage space) | RCU |
| | For upper surface of inner bottom plating and surrounding structures | RCB |
| | For both strength deck and inner bottom plating | RCW |

---
**End of Document**

================================================================================
# FILE: UR_W/ur-w12del.md
================================================================================

W12

# W12 Deleted

IACS Req. 1989


================================================================================
# FILE: UR_W/ur-w15del.md
================================================================================

W15

# W15 Deleted

IACS Req.


================================================================================
# FILE: UR_W/ur-w16rev3cr.md
================================================================================

# W16 High Strength Steels for Welded Structures

**W16**
(1984)
(Rev.1 1994)
(Rev.2 May 2004)
(Rev.3 Mar 2016 Complete Revision)

## 1. Scope

1.1 These requirements apply to hot-rolled, fine-grain, weldable high strength structural steels, intended for use in marine and offshore structural applications. These requirements do not apply to steels intended for hull structure of commercial ships whose requirements are specified in Unified Requirement W11.

1.2 Steels covered by the scope of these requirements are specified in yield strength levels of 420, 460, 500, 550, 620, 690, 890 and 960 N/mm². For each yield strength level grades A, D, E and F are specified, based on the impact test temperature, except for yield strength level of 890 and 960 N/mm² for which grade F is not applicable.

The full list of grades are:

| | | | |
|---|---|---|---|
| AH420 | DH420 | EH420 | FH420 |
| AH460 | DH460 | EH460 | FH460 |
| AH500 | DH500 | EH500 | FH500 |
| AH550 | DH550 | EH550 | FH550 |
| AH620 | DH620 | EH620 | FH620 |
| AH690 | DH690 | EH690 | FH690 |
| AH890 | DH890 | EH890 | |
| AH960 | DH960 | EH960 | |

1.3 Steels covered by the scope may be delivered in Normalized (N)/Normalised rolled (NR); Thermo-mechanical controlled rolled (TM) or Quenched and Tempered (QT) condition.

**Note:**
TM is a generic delivery condition that may or may not include accelerated cooling, and may or may not include direct quenching followed by tempering after TM-rolling.

1.4 Product forms include plates, wide flats, sections, bars and seamless tubulars.

**Note:**
1. This UR is to be uniformly implemented by IACS Societies in marine and offshore structures contracted for construction on or after 1 July 2017, or when the application for certification of steel products submitted by an approved manufacturer is dated on or after 1 July 2017, or the application for certification of manufacturer approval is dated on or after 1 July 2017.
2. The “contracted for construction” date means the date on which the contract to build the vessel is signed between the prospective owner and the shipbuilder. For further details regarding the date of “contract for construction”, refer to IACS Procedural Requirement (PR) No. 29.

1.5 Steels with a thickness beyond the maximum thicknesses as given in Table 3 of section 5.3 may be approved at the discretion of the Classification Society.

1.6 Steels differing in chemical composition, deoxidation practice, delivery condition and mechanical properties may be accepted, subject to the special approval of the Classification Society. Such steels are to be given a special designation.

## 2. Approval

2.1 For applications subjected to Classification, all steels are to be manufactured at steel works which have been approved by the Classification Society for the type and grade of steel which is being supplied. The procedure for approval is shown in Appendix A.

2.2 It is the steelmaker’s responsibility to assure that effective quality, process and production controls during manufacturing are adhered to within the manufacturing specification. The manufacturing specification shall be submitted to the Classification Society at the time of initial approval.

2.3 Where non-conformities arise, the manufacturer is to identify the root cause and establish countermeasures to prevent its recurrence. The non-conformities and the countermeasures are to be documented and reported to the Classification Society.

2.4 When the semi-finished products were not manufactured by the approved manufacturer of the finish rolled and heat treated products, the manufacturer of the semi-finished product shall also be subject to approval by Classification Society.

**Note 1:**
The attention of the users must be drawn to the fact that when fatigue loading is present, the effective fatigue strength of a welded joint of high strength steel may not be greater than that of a welded joint in normal strength steels.

**Note 2:**
Before subjecting steels produced by both thermo-mechanical rolling or quenched and tempered after rolling to further heating for forming or stress relieving, or using high heat-input welding, special consideration must be given to the possibility of a consequent reduction in mechanical properties.

## 3. Method of Manufacture

### 3.1 Steel making process

3.1.1 The steel is to be manufactured, by the basic oxygen, basic electric arc furnace or by processes specially approved by the Classification Society.

3.1.2 Vacuum degassing shall be used for any of the following:
a) All steels with enhanced through-thickness properties, and
b) All steels of grade H690, H890 and H960.

### 3.2 Deoxidation

3.2.1 The steel is to be fully killed.

### 3.3 Grain size

3.3.1 The steel is to be fine grain treated, and is to have a fine grain structure. The fine grain practice is to be as detailed in the manufacturing specification.

**Note:**
A fine grain structure has an equivalent index ≥ 6 determined by micrographic examination in accordance with ISO 643 or alternative test method.

### 3.4 Nitrogen control

3.4.1 The steels shall contain nitrogen binding elements as detailed in the manufacturing specification. Also see note 4 in Table 1.

## 4. Chemical Composition

4.1 The chemical composition is to be determined by the steelmaker in an adequately equipped and competently staffed laboratory. The method of sampling is to follow that carried out for the initial approval tests, either from the ladle, the tundish or the mould in the case of continuous casting. The aim analysis is to be in accordance with the manufacturing specification. All the elements listed in Table 1 are to be reported.

4.2 Elements used for alloying, nitrogen binding, and fine grain treatment, and as well as the residual elements are to be as detailed in the manufacturing specification, e.g. when boron is deliberately added for enhancement of hardenability of the steels, the maximum content of the boron content shall not be higher than 0.005%; and the analysis result shall be reported.

4.3 The carbon equivalent value is to be calculated from the ladle analysis. Maximum values are specified in Table 2.

a) For all steel grades the following formula of IIW may be used:
$$Ceq = C + \frac{Mn}{6} + \frac{Cr + Mo + V}{5} + \frac{Ni + Cu}{15} (\%)$$

b) For steel grades H460 and higher, $CET$ may be used instead of $Ceq$ at the discretion of the manufacturer, and is to be calculated according to the following formula:
$$CET = C + \frac{(Mn + Mo)}{10} + \frac{(Cr + Cu)}{20} + \frac{Ni}{40} (\%)$$

**Note:**
The CET is included in the standard EN 1011-2:2001 used as one of the parameters for pre-heating temperature determination which is necessary for avoiding cold cracking.

c) For TM and QT steels with carbon content not more than 0.12%, the cold cracking susceptibility $Pcm$ for evaluating weldability may be used instead of carbon equivalent of $Ceq$ or $CET$ at manufacturer’s discretion and is to be calculated using the following formula:
$$Pcm = C + \frac{Si}{30} + \frac{Mn}{20} + \frac{Cu}{20} + \frac{Ni}{60} + \frac{Cr}{20} + \frac{Mo}{15} + \frac{V}{10} + 5B (\%)$$

### Table 1 Chemical Composition

| Delivery condition¹⁾ | N/NR | TM | QT |
| :--- | :--- | :--- | :--- |
| **Steel grade** | **AH420, DH420, AH460, DH460** | **EH420, EH460** | **AH420, DH420, AH460, DH460, AH500, DH500, AH550, DH550, AH620, DH620, AH690, DH690, AH890** | **EH420, FH420, EH460, FH460, EH500, FH500, EH550, FH550, EH620, FH620, EH690, FH690, DH890, EH890** | **AH420, DH420, AH460, DH460, AH500, DH500, AH550, DH550, AH620, DH620, AH690, DH690, AH890, AH960** | **EH420, FH420, EH460, FH460, EH500, FH500, EH550, FH550, EH620, FH620, EH690, FH690, DH890, EH890, DH960, EH960** |
| **Chemical Composition²⁾** | | | | | | |
| Carbon % max | 0.20 | 0.18 | 0.16 | 0.14 | 0.18 | 0.18 |
| Manganese % | 1.0~1.70 | 1.0~1.70 | 1.0~1.70 | 1.0~1.70 | 1.70 | 1.70 |
| Silicon % max | 0.60 | 0.60 | 0.60 | 0.60 | 0.80 | 0.80 |
| Phosphorus % max³⁾ | 0.030 | 0.025 | 0.025 | 0.020 | 0.025 | 0.020 |
| Sulphur % max³⁾ | 0.025 | 0.020 | 0.015 | 0.010 | 0.015 | 0.010 |
| Aluminium total % min⁴⁾ | 0.02 | 0.02 | 0.02 | 0.02 | 0.018 | 0.018 |
| Niobium % max⁵⁾ | 0.05 | 0.05 | 0.05 | 0.05 | 0.06 | 0.06 |
| Vanadium % max⁵⁾ | 0.20 | 0.20 | 0.12 | 0.12 | 0.12 | 0.12 |
| Titanium % max⁵⁾ | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 |
| Nickel % max⁶⁾ | 0.80 | 0.80 | 2.00⁶⁾ | 2.00⁶⁾ | 2.00⁶⁾ | 2.00⁶⁾ |
| Copper % max | 0.55 | 0.55 | 0.55 | 0.55 | 0.50 | 0.50 |
| Chromium % max⁵⁾ | 0.30 | 0.30 | 0.50 | 0.50 | 1.50 | 1.50 |
| Molybdenum % max⁵⁾ | 0.10 | 0.10 | 0.50 | 0.50 | 0.70 | 0.70 |
| Nitrogen % max | 0.025 | 0.025 | 0.025 | 0.025 | 0.015 | 0.015 |
| Oxygen ppm max⁷⁾ | Not applicable | Not applicable | Not applicable | 50 | Not applicable | 30 |

Note 1: See section 5.1 for definition of delivery conditions.
Note 2: The chemical composition is to be determined by ladle analysis and shall meet the approved manufacturing specification at the time of approval.
Note 3: For sections the P and S content can be 0.005% higher than the value specified in the table.
Note 4: The total aluminium to nitrogen ratio shall be a minimum of 2:1. When other nitrogen binding elements are used, the minimum Al value and Al/N ratio do not apply.
Note 5: Total Nb+V+Ti ≤ 0.26% and Mo+Cr ≤ 0.65%, not applicable for QT steels.
Note 6: Higher Ni content may be approved at the discretion of the Classification Society.
Note 7: The requirement on maximum Oxygen content is only applicable to DH890; EH890; DH960 and EH960.

### Table 2 Maximum Ceq, CET and Pcm values

| Steel grade and delivery condition | Carbon Equivalent (%) | | | | | | CET all | Pcm all |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| | **Ceq** | | | | | | | |
| | **Plates** | | | **Sections** | **Bars** | **Tubulars** | | |
| | **t ≤ 50 (mm)** | **50 < t ≤ 100 (mm)** | **100 < t ≤ 250 (mm)** | **t ≤ 50 (mm)** | **t ≤ 250 or d ≤ 250 (mm)** | **t ≤ 65 (mm)** | | |
| H420N/NR | 0.46 | 0.48 | 0.52 | 0.47 | 0.53 | 0.47 | N.A | N.A |
| H420TM | 0.43 | 0.45 | 0.47 | 0.44 | N.A | N.A | N.A | N.A |
| H420QT | 0.45 | 0.47 | 0.49 | N.A | N.A | 0.46 | N.A | N.A |
| H460N/NR | 0.50 | 0.52 | 0.54 | 0.51 | 0.55 | 0.51 | 0.25 | N.A |
| H460TM | 0.45 | 0.47 | 0.48 | 0.46 | N.A | N.A | 0.30 | 0.23 |
| H460QT | 0.47 | 0.48 | 0.50 | N.A | N.A | 0.48 | 0.32 | 0.24 |
| H500TM | 0.46 | 0.48 | 0.50 | N.A | N.A | N.A | 0.32 | 0.24 |
| H500QT | 0.48 | 0.50 | 0.54 | N.A | N.A | 0.50 | 0.34 | 0.25 |
| H550TM | 0.48 | 0.50 | 0.54 | N.A | N.A | N.A | 0.34 | 0.25 |
| H550QT | 0.56 | 0.60 | 0.64 | N.A | N.A | 0.56 | 0.36 | 0.28 |
| H620TM | 0.50 | 0.52 | N.A | N.A | N.A | N.A | 0.34 | 0.26 |
| H620QT | 0.56 | 0.60 | 0.64 | N.A | N.A | 0.58 | 0.38 | 0.30 |
| H690TM | 0.56 | N.A | N.A | N.A | N.A | N.A | 0.36 | 0.30 |
| H690QT | 0.64 | 0.66 | 0.70 | N.A | N.A | 0.68 | 0.40 | 0.33 |
| H890TM | 0.60 | N.A | N.A | N.A | N.A | N.A | 0.38 | 0.28 |
| H890QT | 0.68 | 0.75 | N.A | N.A | N.A | N.A | 0.40 | N.A |
| H960QT | 0.75 | N.A | N.A | N.A | N.A | N.A | 0.40 | N.A |

Note: N.A = Not applicable

## 5. Delivery Condition - Rolling Process and Heat Treatment

5.1 Steel is to be delivered in accordance with the processes approved by the Classification Society. These processes include:
*   Normalized (N)/Normalized rolled (NR)
*   Thermo-mechanical controlled rolled (TM)/with Accelerated cooling (TM+AcC)/with direct quenching followed by tempering (TM+DQ), or
*   Quenched and Tempered condition (QT)

The definition of these delivery conditions are defined in UR W11.

**Note:**
Direct quenching after hot-rolling followed by tempering is considered equivalent to conventional quenching and tempering.

### 5.2 Rolling reduction ratio

5.2.1 The rolling reduction ratio of slab, billet, bloom or ingot should not be less than 3:1 unless agreed at the time of approval.

### 5.3 Thickness limits for approval

5.3.1 The maximum thickness of slab, billet or bloom from the continuous casting process shall be at the manufacturer’s discretion.

5.3.2 Maximum thickness of plates, sections, bars and tubulars over which a specific delivery condition is applicable are shown in Table 3.

### Table 3 Maximum thickness limits

| Delivery condition | Maximum thickness (mm) | | | |
| :--- | :--- | :--- | :--- | :--- |
| | **Plates** | **Sections** | **Bars** | **Tubulars** |
| N | 250²⁾ | 50 | 250 | 65 |
| NR | 150 | | 1) | |
| TM | 150 | 50 | Not applicable | Not applicable |
| QT | 150²⁾ | 50 | Not applicable | 50 |

Note 1: The maximum thickness limits of sections, bars and tubulars produced by NR process route are less than those manufactured by N route, and shall be at the discretion of Classification Society.
Note 2: Approval for N steels with thickness larger than 250 mm and QT steels with thickness larger than 150 mm is subject to the special consideration of the Classification Society.

## 6. Mechanical Properties

Test specimens and test procedures for mechanical properties are in accordance with UR W2 and UR W11.

### 6.1 Tensile test

6.1.1 Test specimens are to be cut with their longitudinal axes transverse to the final direction of rolling, except in the case of sections, bars, tubulars and rolled flats with a finished width of 600 mm or less, where the tensile specimens may be taken in the longitudinal direction.

6.1.2 Full thickness flat tensile specimens are to be prepared. The specimens are to be prepared in such a manner as to maintain the rolling scale at least at one side. When the capacity of the test machine is exceeded by the use of a full thickness specimen, sub-sized flat tensile specimens representing either the full thickness or half of the product thickness retaining one rolled surface are to be used. Alternatively, machined round test specimens may be used. The specimens are to be located at a position lying at a distance of t/4 from the surface and additionally at t/2 for thickness above 100 mm or as near as possible to these positions.

6.1.3 The results of the tests are to comply with the appropriate requirements of Table 4. In the case of product forms other than plates and wide flats where longitudinal tests are agreed, the elongation values are to be 2 percentage units above those transverse requirements as listed in Table 4.

### Table 4 Tensile properties at ambient temperature for all steel grades

| Mechanical properties | Minimum yield strength $ReH$¹⁾ (N/mm²) | | | Ultimate tensile strength $Rm$ (N/mm²) | | Minimum percentage elongation after fracture (%) $L_0=5.65\sqrt{S_0}$²⁾ | Charpy V-notch impact test | | |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| | **Nominal thickness (mm)⁴⁾** | | | **Nominal thickness (mm)⁴⁾** | | | **Test temp (°C)** | **Minimum (Joules)** | |
| **Steel grade and delivery condition** | **≥ 3 ≤ 50** | **> 50 ≤ 100** | **> 100 ≤ 250** | **≥ 3 ≤ 100** | **> 100 ≤ 250** | **T** | **L³⁾** | | **T** | **L** |
| H420N/NR, H420TM, H420QT | A, D, E, F | 420 | 390 | 365 | 520~680 | 470~650 | 19 | 21 | 0, -20, -40, -60 | 28 | 42 |
| H460N/NR, H460TM, H460QT | A, D, E, F | 460 | 430 | 390 | 540~720 | 500~710 | 17 | 19 | 0, -20, -40, -60 | 31 | 46 |
| H500TM, H500QT | A, D, E, F | 500 | 480 | 440 | 590~770 | 540~720 | 17 | 19 | 0, -20, -40, -60 | 33 | 50 |
| H550TM, H550QT | A, D, E, F | 550 | 530 | 490 | 640~820 | 590~770 | 16 | 18 | 0, -20, -40, -60 | 37 | 55 |
| H620TM, H620QT | A, D, E, F | 620 | 580 | 560 | 700~890 | 650~830 | 15 | 17 | 0, -20, -40, -60 | 41 | 62 |
| H690TM, H690QT | A, D, E, F | 690 | 650 | 630 | 770~940 | 710~900 | 14 | 16 | 0, -20, -40, -60 | 46 | 69 |
| H890TM, H890QT | A, D, E | 890 | 830 | Not applicable | 940~1100 | Not applicable | 11 | 13 | 0, -20, -40 | 46 | 69 |
| H960QT | A, D, E | 960 | Not applicable | Not applicable | 980~1150 | Not applicable | 10 | 12 | 0, -20, -40 | 46 | 69 |

Note 1: For tensile test either the upper yield stress ($ReH$) or where $ReH$ cannot be determined, the 0,2 percent proof stress ($Rp0.2$) is to be determined and the material is considered to comply with the requirement if either value meets or exceeds the specified minimum value of yield strength.
Note 2: For full thickness flat test specimens with a width of 25 mm and a gauge length of 200 mm the elongation is to comply with the minimum values shown in Table 5.
Note 3: In the case that the tensile specimen is parallel to the final rolling direction, the test result shall comply with the requirement of elongation for longitudinal (L) direction.
Note 4: For plates and sections for applications, such as racks in offshore platforms etc, where the design requires that tensile properties are maintained through the thickness, a decrease in the minimum specified tensile properties is not permitted with an increase in the thickness.

### Table 5 Elongation Minimum Values for a Width of 25 mm and a 200 mm Gauge Length¹⁾

| Strength level | Thickness (mm) | | | | | | |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| | **≤ 10** | **> 10 ≤ 15** | **> 15 ≤ 20** | **> 20 ≤ 25** | **> 25 ≤ 40** | **> 40 ≤ 50** | **> 50 ≤ 70** |
| H420 | 11 | 13 | 14 | 15 | 16 | 17 | 18 |
| H460 | 11 | 12 | 13 | 14 | 15 | 16 | 17 |
| H500 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
| H550 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
| H620 | 9 | 11 | 12 | 12 | 13 | 14 | 15 |
| H690 | 9²⁾ | 10²⁾ | 11²⁾ | 11 | 12 | 13 | 14 |

Note 1: The tabulated elongation minimum values are the requirements for testing specimen in transverse direction. H890 and 960 specimens and specimens which are not included in this table shall be proportional specimens with a gauge length of $L_0=5.65\sqrt{S_0}$.
Note 2: For H690 plates with thickness ≤ 20 mm, round specimen in accordance with Unified Requirement W2 may be used instead of the flat tensile specimen. The minimum elongation for testing specimen in transverse direction is 14%.

### 6.2 Impact test

6.2.1 The Charpy V-notch impact test specimens for plates and wide flats over 600 mm in width are to be taken with their axes transverse to the final rolling direction and the results should comply with the appropriate requirements for transverse direction of Table 4. For other product forms, the impact tests are to be in the longitudinal direction, the results of the tests are to comply with the appropriate requirements for longitudinal direction of Table 4.

6.2.2 Sub-surface test specimens will be taken in such a way that one side is not further away than 2 mm from a rolled surface, however, for material with a thickness in excess of 50 mm, impact tests shall be taken at the quarter thickness (t/4) location and mid-thickness (t/2).

6.2.3 Impact test for a nominal thickness less than 6 mm are normally not required.

### 6.3 Test frequency

6.3.1 Tensile test sample is to be randomly selected from each batch, as defined in IACS UR W11, that is to be less than or equal to 25 tonnes, and to be from the same cast, in the same delivery condition and of the same thickness.

6.3.2 Impact test
a) For steels plates in N/NR or TM condition test sample is to be taken from each piece.
b) For steels in QT condition test sample is to be taken from each individually heat treated part thereof.
c) For sections, bars and tubulars, test sample is to be taken from each batch of 25 tonnes or fraction thereof.

**Note 1:**
If the mass of the finished material is greater than 25 tonnes, one set of tests from each 25 tonnes and/or fraction thereof is required. (e.g. for consignment of 60 tonnes would require 3 plates to be tested).

**Note 2:**
For continuous heat treated product special consideration may be given to the number and location of test specimens required by the manufacturer to be agreed by the Classification Society.

### 6.4 Traceability

Traceability of test material, specimen sampling and test procedures including test equipment with respect to mechanical properties testing, is to be in accordance with UR W11.

### 6.5 Re-test procedures

Re-test procedures for tensile tests and Charpy impact tests are to be in accordance with UR W2.

### 6.6 Through thickness tensile test

6.6.1 For steels designated with improved through thickness properties, through thickness tensile tests are to be performed in accordance with Unified Requirement W14, “Steel plates and wide flats with specified minimum through thickness properties (“Z” quality)”.

6.6.2 Subject to the discretion of Classification Society, through thickness tensile strength may be required to be not less than 80% of the specified minimum tensile strength.

## 7. Tolerances

Unless otherwise agreed or specially required, the thickness tolerances in Unified Requirement W13, “Allowable under thickness tolerances of steel plates and wide flats” are applicable.

## 8. Surface Quality

8.1 All materials are to be free from cracks, injurious surface flaws, injurious laminations and similar defects.

8.2 The surface quality inspection method shall be in accordance with recognised national or international standards agreed between purchaser and manufacturer.
a) Welding repair procedures and the method for reporting repairs are to be approved by the individual Classification Societies.
b) Where repair by grinding is carried out then the remaining plate thickness below the ground area must be within the allowable under thickness tolerance.

8.3 Surface finish requirement shall be in accordance with the relevant requirements in Unified Requirement W11.

8.4 Surface inspection is the responsibility of the manufacturer. The acceptance by the Classification Society’s Surveyor of material later found to be defective shall not absolve the manufacturer of this responsibility.

## 9. Internal Soundness

9.1 Verification of internal soundness is the responsibility of the manufacturer. The acceptance by the Classification Society’s Surveyor shall not absolve the manufacturer of this responsibility.

9.2 Ultrasonic examination
9.2.1 If required by the Classification Society, ultrasonic examination should be carried out in accordance with UR W11 for the requirement of internal soundness, and is to be performed in accordance with an approved standard.

## 10. Stress relieving heat treatment and other heat treatments

10.1 Steels approved by the procedures given in Appendix A with respect to Heat Treatment are suitable for stress relieving heat treatment such as post-weld heat treatment and stress relieving heat treatment after cold forming for the purpose of reducing the risk of brittle fracture, increasing the fatigue lifetime and dimensional stability for machining.

**Note:**
Products can be susceptible to deterioration in mechanical strength and toughness if they are subjected to incorrect post-weld heat treatment procedures or other processes involving heating such as flame straightening, rerolling, etc. where the heating temperature and the holding time exceed the limits given by the manufacturer.

## 11. Facilities for Inspection

11.1 Testing is to be carried out under the witness of the Surveyor, or an authorised deputy, in order to verify whether the test results meet the specified requirements.

11.2 The manufacturer is to afford the Surveyor all necessary facilities and access to all relevant parts of the steel works to enable him to verify the approved process is adhered to, for the selection of test materials, and the witnessing of tests, as required by this UR. Also for verifying the accuracy of the testing, calibration of inspection equipment and traceability of materials.

## 12. Identification of Materials

12.1 The manufacturer is to adopt a system for the identification of ingots, slabs, billet or bloom and finished products, which will enable the material to be traced to its original cast. The Surveyor is to be given full facilities for so tracing the material when required.

## 13. Branding

13.1 Each finished piece is to be clearly marked by the manufacturer with the following particulars:
a) Classification Society’s brand mark
b) Unified identification mark for the grade of steel (e.g. EH620)
c) Name or initials to identify the steelworks
d) Cast number/Heat number, plate number or equivalent identification mark
e) Delivery condition (N/NR, TM/TM+AcC/TM+DQ or Q&T)

The entire markings are to be encircled with paint or otherwise marked so as to be easily recognised. Steels which have been specially approved by the Classification Society and which differ from these requirements (see W16.1.6) are to have the letter “S” after the identification mark (e.g. EH620S)

## 14. Documentation of Inspection Tests

14.1 The Surveyor is to be supplied with two copies, of the test certificates or shipping statements for all accepted materials. In addition to the description, dimensions, etc., of the material, the following particulars are to be included:
a) Purchaser's order number
b) Identification of the cast and piece
c) Manufacturer’s identification
d) Identification of the grade of steel
e) Chemical analysis, Ceq, CET or Pcm value
f) Delivery condition with heat treatment temperatures
g) Mechanical properties test results, including traceable test identification
h) Surface quality and inspection results
i) UT result, where applicable

14.2 Before the test certificates are signed by the Surveyor, the steelmaker is required to provide a written declaration stating that the material has been made by an approved process, and that it has been subjected to and has withstood satisfactorily the required tests in the presence of the Surveyor, or an authorised deputy. The following form of declaration will be accepted if stamped or printed on each test certificate with the name of the steelworks and signed by an authorised representative of the manufacturer:

“We hereby certify that the material has been made by an approved process and has been satisfactorily tested in accordance with the Rules of the Classification Society”.

---

## Appendix A. Manufacturing Approval Scheme of High Strength Steels for Welded Structures

### 1. Scope of application

This appendix specifies the procedure for the approval of the manufacturing process of high strength steels for welded structures.

All materials are to be manufactured at works which have been approved by the Classification Society for the type, delivery condition, grade and thickness of steel which is being supplied. The suitability of each grade of steel for forming and welding is to be demonstrated during the initial approval tests at the steelworks.

The manufacturing approval scheme is valid for verifying the manufacturer’s capability to provide satisfactory products stably under effective process and production controls in operation including programmed rolling, which is required in W16.2.2.

### 2. Approval application

#### 2.1 Documents to be submitted

The manufacturer is to submit to the Society, a request for approval, a proposed approval test program (see A3.1) and general information relevant to:

a) Name and site address of the manufacturer, location of the workshops, general indications relevant to the background, dimension of the works, estimated total annual production of finished products, as deemed useful.
b) Organisation and quality
*   organisational chart
*   number of staff employed
*   staff employed and organisation of the quality control department
*   qualification of the personnel involved in activities related to the quality of the products
*   certification of compliance of the quality system with IS0 9001 or 9002, if any
*   approval certificates already granted by other Classification Societies, if any
c) Manufacturing facilities
*   flow chart of the manufacturing process
*   origin and storage of raw materials
*   storage of finished products
*   equipment for systematic control during manufacturing
d) Details of inspections and quality control facilities
*   details of system used for identification of materials at the different stages of manufacturing
*   equipment for mechanical tests, chemical analyses and metallography and relevant calibration procedures
*   equipment for non-destructive examinations (NDE)
*   list of quality control procedures

#### 2.2 Manufacturing specification

a) Material to be approved, including type of products (plates, sections, bars and tubular), delivery condition, grades of steel, range of thickness and aim material properties as follows:
*   range of chemical composition, aim analyses and associated control limits, including grain refining, nitrogen binding, micro alloying and residual elements, for the various grades of steel; if the range of chemical composition depends on thickness and delivery condition, the different ranges are to be specified, as appropriate.
*   in addition, where zirconium, calcium and rare earth metals have been used during steelmaking for grain refinement and, or inclusion modification, the contents of these elements shall be specified in the manufacturing specification.
*   aim carbon equivalent Ceq according to IIW formula or CET formula and/or aim Pcm content and associated control limits.
*   production statistics of the chemical composition and mechanical properties ($ReH, Rm, A\%$ and $CVN$). The statistics are intended to demonstrate the capability to manufacture the steel products.

b) Steelmaking (if applicable)
*   steel making process and capacity of furnace/s or converter/s
*   raw material used
*   deoxidation, grain refining, nitrogen binding and alloying practice
*   desulphurisation, dehydrogenation, sulphide treatment, ladle refining and vacuum degassing installations, if any
*   casting methods: ingot or continuous casting. In the case of continuous casting, information relevant to type of casting machine, teeming practice, methods to prevent re-oxidation, inclusions and segregation control, presence of electromagnetic stirring, soft reduction, etc., is to be provided as appropriate
*   casting/solidification cooling rate control
*   ingot or slab size and weight
*   ingot or slab treatment: scarfing and discarding procedures

c) Reheating and rolling
*   type of furnace and treatment parameters
*   rolling: reduction ratio of ingot/slab/bloom/billet to finished product, rolling and finishing temperatures for each grade/thickness combination
*   descaling treatment during rolling
*   capacity of the rolling stands

d) Heat treatment
*   type of furnaces, heat treatment parameters for products to be approved
*   accuracy and calibration of temperature control devices
*   the methods used to determine austenitizing temperature, re-crystallization temperature and Ar3 temperature
*   description of quenching and tempering process, if applicable

e) Programmed rolling
For products delivered in the Normalised rolling (NR) or thermo-mechanical rolling (TM) condition, the following additional information on the programmed rolling schedules is to be given:
*   description of the rolling process
*   the methods used to determine austenitizing temperature, re-crystallization temperature and Ar3 temperature
*   control standards for typical rolling parameters used for the different thickness and grades of steel (temperature and thickness at the beginning and at the end of the passes, interval between passes, reduction ratio, temperature range and cooling speed of accelerated cooling, if any) and relevant method of control
*   calibration of the control equipment

f) Recommendations for fabrication and welding in particular for products delivered in the NR or TM condition:
*   cold and hot working recommendations if needed in addition to the normal practice used in the shipyards and workshops
*   minimum and maximum heat input and recommended pre-heat/interpass temperature

g) Where any part of the manufacturing process is assigned to other companies or other manufacturing plants, additional information required by the Society is to be included.

h) Approval already granted by other Classification Societies and documentation of approval tests performed.

#### 2.3 Documents to be submitted for changing the approval conditions

The manufacturer has to submit to the Society the documents required in 2.1 together with the request of changing the approval conditions, in the case of the following a) through e) as applicable:
a) Change of the manufacturing process (steel making, casting, rolling and heat treatment).
b) Change of the maximum thickness (dimension).
c) Change of the chemical composition, added element, etc.
d) Subcontracting the rolling, heat treatment, etc.
e) Use of the ingots, slabs, blooms and billets manufactured by companies other than the ones verified in the approval tests.

However, where the documents are duplicated by the ones at the previous approval for the same type of product, part or all of the documents may be omitted except the approval test program (see 3.1).

### 3. Approval tests

#### 3.1 Extent of the approval tests

The extent of the test program is specified in 3.6 and 3.7; it may be modified on the basis of the preliminary information submitted by the manufacturer.

In particular a reduction of the indicated number of casts, steel plate thicknesses and grades to be tested or complete suppression of the approval tests may be accepted by the Society taking into account:
a) Approval already granted by other Classification Societies and documentation of approval tests performed.
b) Grades of steel to be approved and where available the long term statistical results of chemical and mechanical properties.

An increase of the number of casts and thicknesses to be tested may be required in the case of newly developed types of steel or manufacturing processes.

In case of multi-source slabs or changing of slab manufacturer, the rolled steel manufacturer is required to obtain the approval of the manufacturing process of rolled steels using the slabs from each slab manufacturer and to conduct approval tests in accordance with 3.6 and 3.7. A reduction or complete suppression of the approval tests may be considered by the Society taking into account previous approval as follows:
*   the rolled steel manufacturer has already been approved for the rolling process and heat treatment using approved other semi finished products characterized by the same thickness range, steel grade, grain refining and micro-alloying elements, steel making(deoxidation) and casting process.
*   the semi finished products have been approved for the complete manufacturing process with the same conditions (steelmaking, casting, rolling and heat treatment) for the same steel types.

#### 3.2 Approval test program

Where the number of tests differs from those shown in 3.6 and 3.7, the program is to be confirmed by the Society before the tests are carried out.

#### 3.3 Approval survey

The approval tests are to be witnessed by the Surveyor at the manufacturer’s plant and the execution of the plant inspection in operation may be required by the Surveyor during the visit for the approval.

If the testing facilities are not available at the works, the tests are to be carried out at accredited laboratories.

#### 3.4 Selection of the test product

For each grade of steel and for each manufacturing process (e.g. steel making, casting, rolling and condition of supply), one test product with the maximum thickness (dimension) to be approved is in general to be selected for each kind of product.

In addition, for initial approval, the Society will require selection of one test product of representative thickness.

The selection of the casts for the test product is to be based on the typical chemical composition, with particular regard to the aimed Ceq, CET or Pcm values and grain refining micro-alloying additions.

#### 3.5 Position of the test samples and specimens

The test samples are to be taken, unless otherwise agreed, from the product (plate, flat, section, bar and tubular) corresponding to the top and bottom of the ingot as indicated in Table A1, or, in the case of continuous casting, a random sample.

The position of the samples to be taken in the length of the rolled product, “piece” defined in W11, (top and bottom of the piece) and the direction of the test specimens with respect to the final rolling direction of the material are indicated in Table A1.

The position of the samples in the width of the product is to be in accordance with W11.

The position of the tensile and Charpy impact test samples with respect to the plate thickness is to be in accordance with Appendix 2 section 3.6.2 of W11.

#### 3.6 Tests on base material

##### 3.6.1 Type of tests

The tests to be carried out are indicated in the following Table A1.

### Table A1 Tests on base material

| Type of Test | Position and direction of test specimens | Remarks |
| :--- | :--- | :--- |
| 1. Chemical analysis (ladle and product¹⁾) | Top | a) Contents of C, Mn, Si, P, S, Ni, Cr, Mo, Al, N, Nb, V, Ti, B, Zr, Cu, As, Sn, Bi, Pb, Ca, Sb, O, H are to be reported.<br>b) Carbon equivalent calculation, and/or<br>c) Pcm calculation, as applicable. |
| 2. Segregation examination | Top | Sulphur prints²⁾ are to be taken from plate edges which are perpendicular to the axis of the ingot or slab. These sulphur prints are to be approximately 600 mm long taken from the centre of the edge selected, i.e. on the ingot centreline, and are to include the full plate thickness. |
| 3. Micrographic examination³⁾ | Top | a) Grain size determination. Ferrite and/or prior austenite grain size should be determined.<br>b) All photomicrographs are to be taken at x 100 and 500 magnification.<br>c) Non-metallic inclusion contents/Cleanliness<br>The level of non-metallic inclusions and impurities in term of amount, size, shape and distribution shall be controlled by the manufacturer. The standards of the micrographic examination methods ISO 4967 or equivalent standards are applicable. Alternative methods for demonstrating the non-metallic inclusions and impurities may be used by the manufacturer. |
| 4. Tensile test | Top and bottom - longitudinal and transverse direction | Yield strength ($ReH$), Tensile strength ($Rm$), Elongation ($A5$), Reduction in Area ($RA$) and Y/T ratio are to be reported. |
| 5a. Charpy Impact tests on unstrained specimens for grades⁴⁾ | Top and bottom | Testing temperature (°C) |
| | | **AH**: +20, 0, -20<br>**DH**: 0, -20, -40<br>**EH**: 0, -20, -40, -60<br>**FH**: -20, -40, -60, -80 |
| 5b. Charpy Impact tests on strain aged specimens for grades⁴⁾⁵⁾ | Top | Deformation of 5% + 1 hour at 250°C |
| | | Testing temperature (°C)<br>**AH**: +20, 0, -20<br>**DH**: 0, -20, -40<br>**EH**: 0, -20, -40, -60<br>**FH**: -20, -40, -60, -80 |
| 6. Drop weight test | Top | The test is to be performed only on plates in accordance with ASTM E208. The NDTT is to be determined and photographs of the tested specimens are to be taken and enclosed with the test report. |
| 7. Through thickness tensile tests | Top and bottom | Optional for grades with improved through thickness properties, testing in accordance with UR W14. |
| 8. Weldability test⁶⁾ | | |
| a) Butt Weld Assembly as-welded | Top | Cross weld tensile, Charpy impact test on WM, FL, FL+2, FL+5, FL+20 Macro examination and hardness survey, CTOD at -10°C on Grain-coarsened HAZ. |
| b) Butt Weld Assembly (PWHT), if applicable | Top | Cross weld tensile, Charpy impact test on WM, FL, FL+2, FL+5, FL+20 Macro examination and hardness survey, CTOD at -10°C on Grain-coarsened HAZ. |
| c) Y-shape weld crack test (Hydrogen crack test) | Top | |

Note 1: The product analyses should be taken from the tensile specimen. The deviation of the product analysis from the ladle analysis shall be permissible in accordance with the limits given in the manufacturing specification.
Note 2: Other tests than Sulphur prints for segregation examination may be applied and subject to acceptance by the Classification Society.
Note 3: The micrographs are to be representative of the full thickness. For thick products in general at least three examinations are to be made at surface, 1/4t and 1/2t of the product.
Note 4: In addition to the determination of the absorbed energy value, also the lateral expansion and the percentage crystallinity are to be reported.
Note 5: Strain ageing test is to be carried out on the thickest plate.
Note 6: Weldability test is to be carried out on the thickest plate.

##### 3.6.2 Test specimens and testing procedure

The test specimens and testing procedures are to be in accordance with W2, where applicable.

##### 3.6.3 Other tests

Additional tests such as CTOD test on parent plate, large scale brittle fracture tests (Double Tension test, ESSO test, Deep Notch test, etc.) or other tests may be required in the case of newly developed type of steel, outside the scope of W16, or when deemed necessary by the Society.

#### 3.7 Weldability tests - Butt weld test

3.7.1 For H420 to H500 grade steels: Weldability tests are to be carried out on samples of the thickest plate. Testing on higher grades can cover the lower strength and toughness grades.
a) 1x butt weld test assembly welded with a heat input 15±2 kJ/cm is to be tested as-welded.
b) 1x butt weld test assembly welded with a heat input 50±5 kJ/cm for N/NR and TM and 35±3.5 kJ/cm for QT steels is to be tested as-welded.
c) 1x butt weld test assembly welded with the same heat input as given in b) is to be post-weld heat treated (PWHT) prior to testing.

Option: Steels intended to be designated as steels for high heat input welding are to be tested with 1x butt weld test assembly in the as-welded condition and 1x test assembly in the PWHT condition, both welded with the maximum heat input being approved.

3.7.2 For H550 to H960 grade steels:
In general, the thickest plate with the highest toughness grade for each strength grade is to be tested. Provided the chemical composition of the higher grade is representative to the lower grade, testing requirements on the lower grades may be reduced at the discretion of the Classification Society.
a) 1x butt weld test assembly welded with a heat input 10±2 kJ/cm is to be tested as-welded.
b) 1x butt weld test assembly welded with a maximum heat input as proposed by the manufacturer is to be tested as-welded. The approved maximum heat input shall be stated on the manufacturer approval certificate.

Option: If the manufacturer requests to include the approval for Post Weld Heat Treated (PWHT) condition, 1x additional butt weld test assembly welded with a maximum heat input proposed by the manufacturer for the approval same as test assembly b) is to be post-weld heat treated (PWHT) prior to testing.

3.7.3 Butt weld test assembly
The butt weld test assemblies of N/NR plates are to be prepared with the weld seam transverse to the final plate rolling direction.
The butt weld test assemblies of TM/TM+AcC/TM+DQ and QT plates are to be prepared with the weld seam parallel to the final plate rolling direction. The butt weld test assemblies of long products, sections and seamless tubular in any delivery condition are to be prepared with the weld seam transverse to the rolling direction.

3.7.4 Bevel preparation
The bevel preparation should be preferably 1/2V or K related to thickness.
The welding procedure should be as far as possible in accordance with the normal welding practice used for the type of steel in question.
The welding procedure and welding record are to be submitted to the Classification Society for review.

3.7.5 Post-weld heat treatment procedure
a) Steels delivered in N/NR or TM/TM+AcC/TM+DQ condition shall be heat treated for a minimum time of 1 hour per 25 mm thickness (but not less than 30 minutes and needs not be more than 150 minutes) at a maximum holding temperature of 580°C, unless otherwise approved at the time of approval.
b) Steels delivered in QT condition shall be heat treated for a minimum time of 1 hour per 25 mm thickness (but not less than 30 minutes and needs not be more than 150 minutes) at a maximum holding temperature of 550°C with the maximum holding temperature of at least 30°C below the previous tempering temperature, unless otherwise approved at the time of approval.
c) Heating and cooling above 300°C shall be carried out in a controlled manner in order to heat/cool the material uniformly. The cooling rate from the max. holding temperature to 300°C shall not be slower than 55°C/hr.

3.7.6 Type of tests
From the test assemblies the following test specimens are to be taken:
a) 1 cross weld tensile test - 1 full thickness test sample or sub-sized samples cover the full thickness cross section.
b) 1 set of 3 Charpy V-notch impact specimens transverse to the weld seam and 1-2 mm below the surface with the notch located at the fusion line and at a distance 2, 5 and 20 mm from the straight fusion line. An additional set of 3 Charpy test specimens at root is required for each aforementioned position for plate thickness t ≥ 50 mm. The fusion boundary is to be identified by etching the specimens with a suitable reagent. The test temperature is to be the one prescribed for the testing of the steel grade.
c) Hardness tests HV10 across the weldment. The indentations are to be made along a 1-2 mm transverse line beneath the plate surface on both the face side and the root side of the weld as follows:
*   fusion line
*   HAZ: at each 0.7 mm from fusion line into unaffected base material (6 to 7 minimum measurements for each HAZ)

The maximum hardness value should not be higher than 350HV for grade steels H420 to H460; not be higher than 420HV for H500 to H690; and not be higher than 450HV for H890 and H960.

A sketch of the weld joint depicting groove dimensions, number of passes, hardness indentations should be attached to the test report together with photomacrographs of the weld cross section.

d) CTOD test
CTOD test specimens are to be taken from butt weld test assembly specified in 3.7.1 b) or 3.7.2 b) in Appendix A of this UR. CTOD test is to be carried out in accordance with EN ISO 15653 or equivalent.
*   the specimen geometry (B = W) is permitted for plate thickness up to 50 mm. For plate thicker than 50 mm, subsidiary specimen geometry (50x50 mm) is permitted, which is to be taken 50 mm in depth through thickness from the subsurface and 50 mm in width. See Figure A1 a) and b) for more details.
*   the specimens shall be notched in through thickness direction.
*   grain-coarsened HAZ (GCHAZ) shall be targeted for the sampling position of the crack tip.
*   the test specimens shall be in as-welded and post-weld heat treated, if applicable.
*   three tests shall be performed at -10°C on each butt weld test assembly.

For grades H690 and above, dehydrogenation of as-welded test pieces may be carried out by a low temperature heat treatment, prior to CTOD testing. Heat treatment conditions of 200°C for 4 h are recommended, and the exact parameters shall be notified with the CTOD test results.

![Figure A1 a): CTOD test specimen for plate thickness t ≤ 50 mm, sampled in full thickness. It shows the notch location at the GCHAZ.](image_description)

![Figure A1 b): CTOD test specimen for plate thickness t > 50 mm, subsidiary test specimen with a thickness of maximum 50 mm in subsurface area is to be sampled.](image_description)

3.7.7 Crack susceptibility weld test (Hydrogen crack test)
Testing in accordance with national and international recognised standards such as GB/T4675.1 and JIS Z 3158 for Y-groove weld crack test. Minimum preheat temperature is to be determined and the relationship of minimum preheat temperature with thickness is to be derived.

3.7.8 Other tests
Additional tests may be required in the case of newly developed types of steel, outside the scope of W16, or when deemed necessary by the Society.

### 4. Results

All the results are to comply with the requirements of the scheme of initial approval.
The subject manufacturer shall submit all the test results together with the manufacturing specification containing all the information required under Appendix A, Section 2, and manufacturing records relevant to steel making, casting, rolling and heat treatment, applicable to the product submitted to the tests.

### 5. Certification

#### 5.1 Approval
Upon satisfactory completion of the survey, approval is granted by the Society.

#### 5.2 List of approved manufacturers
The approved manufacturers are entered in a list containing the types of steel and the main conditions of approval.

### 6. Renewal of approval

The validity of the approval is to be a maximum of five years.
Renewal can be granted by a periodic inspection and evaluation of the result of the inspection to the surveyor’s satisfaction during the period.*

Where for operational reasons, the renewal audit falls outside the period of approval, the manufacturer will still be considered as approved if agreement to this audit date is made within the original period of approval, in this instance if successful, the extension of approval will be back dated to the original renewal date.

Manufacturers who have not produced the approved grades and products during the period between renewals may be required to either carry out approval tests or, on the basis of the statistical data of results of production of similar grades of products, at the discretion of the Society, be reapproved.

### 7. Removal of the approval

During the period of validity the approval may be reconsidered in the following cases:
a) In service failures, traceable to product quality.
b) Non conformity of the product revealed during fabrication and construction.
c) Discovered failure of the Manufacturer’s quality system.
d) Changes brought by the Manufacturer, without preliminary agreement of the Society, to the extent of invalidating the approval.
e) Evidence of major non conformities during testing of the products.

\* The provision for renewal of approval is also to be applied to all grades and products which were approved by the Society prior to an implementation of revision 3 of this UR W16 regardless of the validity of certificate in existing approvals. Such renewal is to be completed within five years after the revision 3 becomes effective.

**End of Document**

================================================================================
# FILE: UR_W/ur-w19del.md
================================================================================

W19-W21

# W19 Deleted

***

# W20 Deleted

***

# W21 Deleted

***

IACS Req. 1995

================================================================================
# FILE: UR_W/ur-w20del.md
================================================================================

W19-W21

# W19 Deleted

***

# W20 Deleted

***

# W21 Deleted

***

IACS Req. 1995

================================================================================
# FILE: UR_W/ur-w21del.md
================================================================================

W19-W21

# W19 Deleted

# W20 Deleted

# W21 Deleted

---
IACS Req. 1995

================================================================================
# FILE: UR_W/ur-w22rev6.md
================================================================================

# W22 Offshore Mooring Chain

(1993)
(Rev.1 1997)
(Rev.2 July 1999)
(Rev.3 May 2004)
(Rev.4 Sept 2006)
(Rev.5 Dec 2009)
(Corr.1 June 2011)
(Rev.6 June 2016)

## 1 GENERAL REQUIREMENTS

### 1.1 Scope

1.1.1 These requirements apply to the materials, design, manufacture and testing of offshore mooring chain and accessories intended to be used for applications such as: mooring of mobile offshore units, mooring of floating production units, mooring of offshore loading systems and mooring of gravity based structures during fabrication.

1.1.2 Mooring equipment covered are common stud and studless links, connecting common links (splice links), enlarged links, end links, detachable connecting links (shackles), end shackles, subsea connectors, swivels and swivel shackles.

1.1.3 Studless link chain is normally deployed only once, being intended for long-term permanent mooring systems with pre-determined design life.

1.1.4 Requirements for chafing chain for single point mooring arrangements are given in Appendix A.

### 1.2 Chain grades

1.2.1 Depending on the nominal tensile strength of the steels used for manufacture, chains are to be subdivided into five grades, i.e.: R3, R3S, R4, R4S and R5.

1.2.2 Manufacturers propriety specifications for R4S and R5 may vary subject to design conditions and the acceptance of the Classification Society.

1.2.3 Each Grade is to be individually approved. Approval for a higher grade does not constitute approval of a lower grade. If it is demonstrated to the satisfaction of the Classification Society that the higher and lower grades are produced to the same manufacturing procedure using the same chemistry and heat treatment, consideration will be given to qualification of a lower grade by a higher. The parameters applied during qualification are not to be modified during production.

---

**Note:**

1. This UR is to be uniformly implemented by IACS Societies on offshore units and single point moorings contracted for construction on or after 1 July 2011 and when the application for certification of mooring chains and accessories is dated on or after 1 July 2011.
2. Rev.6 of this UR is to be uniformly implemented by IACS Societies on offshore units and single point moorings contracted for construction on or after 1 July 2017 and when the application for certification of mooring chains and accessories is dated on or after 1 July 2017.
3. The “contracted for construction” date means the date on which the contract to build the vessel is signed between the prospective owner and the shipbuilder. For further details regarding the date of “contract for construction”, refer to IACS Procedural Requirement (PR) No. 29.

### 1.3 Approval of chain manufacturers

1.3.1 Offshore mooring chains are to be manufactured only by works approved by the Classification Society. For this purpose approval tests are to be carried out, the scope of which is to include proof and breaking load tests, measurements and mechanical tests including fracture mechanics tests.

1.3.2 Manufacturers are to submit for review and approval the sequence of operations from receiving inspection to shipment and details of the following manufacturing processes:

a) Bar heating and bending including method, temperatures, temperature control and recording,
b) Flash welding including current, force, time and dimensional variables as well as control and recording of parameters, maintenance procedure and programme for welding machine,
c) Flash removal including method and inspection,
d) Stud insertion method, for stud link chain,
e) Heat treatment including furnace types, means of specifying, controlling and recording of temperature and chain speed and allowable limits, quenching bath and agitation, cooling method after exit,
f) Proof and break loading including method/machine, means of horizontal support (if applicable), method of measurement and recording,
g) Non-destructive examination procedures,
h) The manufacturer’s surface quality requirement of mooring components is to be submitted.
i) The manufacturer’s procedure for removing and replacing defective links without heat treatment of the entire chain.

1.3.3 For initial approval CTOD tests are to be carried out on the particular IACS mooring grade of material. CTOD tests are to be tested in accordance with a recognized standard such as BS 7448 Part 1 & BS EN ISO 15653:2010. The CTOD test piece is to be a standard 2 x 1 single edge notched bend piece, test location as shown in Figure 1. The notch of the CTOD specimen is to be located as close to the surface as practicable. The minimum cross section of the test piece shall be 50 x 25mm for chain diameters less than 120mm, and 80 x 40mm for diameters 120mm and above. CTOD specimens are to be taken from both the side of the link containing the weld and from the opposite side. Three links are to be selected for testing, a total of six CTOD specimens. The tests are to be taken at minus 20º C and the lowest CTOD of each set of 3 specimens shall meet the minimum values indicated below in table 1:

**Table 1: Minimum CTOD test values for chain type**

| Chain Type | R3 in mm (BM) | R3 in mm (WM) | R3S in mm (BM) | R3S in mm (WM) | R4 in mm (BM) | R4 in mm (WM) | R4S & R5 in mm (BM) | R4S & R5 in mm (WM) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Stud link | 0.20 | 0.10 | 0.22 | 0.11 | 0.24 | 0.12 | 0.26 | 0.13 |
| Studless | 0.20 | 0.14 | 0.22 | 0.15 | 0.24 | 0.16 | 0.26 | 0.17 |

1.3.4 Calibration of furnaces shall be verified by measurement and recording of a calibration test piece with dimensions equivalent to the maximum size of link manufactured. The manufacturer shall submit a procedure for furnace temperature surveys which shall include the following requirements: The temperature uniformity of furnaces is to be surveyed whenever approval of manufacturer is requested and at least annually during normal operating conditions. Furnaces are to be checked by conveying a monitoring link instrumented with two thermocouples through the furnaces at representative travel speed. One thermocouple shall be attached to the surface of the straight part and one thermocouple shall be imbedded in a drilled hole located at the mid thickness position of the straight part of the calibration block. The time-temperature curves shall show that the temperatures throughout the cross section and the soaking times are within specified limits as given in the heat treatment procedure.

1.3.5 For R4S and R5 chain and accessories, prior to approval, the manufacturer is to have undertaken experimental tests or have relevant supporting data to develop the chain and accessory material. The tests and data may include: fatigue tests, hot ductility tests (no internal flaws are to develop whilst bending in the link forming temperature range), welding parameter research, heat treatment study, strain age resistance, temper embrittlement study, stress corrosion cracking (SCC) data and hydrogen embrittlement (HE) study, using slow strain test pieces in hydrated environments. Reports indicating the results of experimental tests are to be submitted.

![Figure 1: Location of CTOD test specimens for chain showing the weld side and non-weld side of a link with notch locations](image_description)

### 1.4 Approval of quality system at chain and accessory manufacturers

1.4.1 Chain and accessory manufacturers are to have a documented and effective quality system approved by the Classification Society. The provision of such a quality system is required in addition to, and not in lieu of, the witnessing of tests by a Surveyor as specified in Sections 2 to 5 of this Unified Requirement.

### 1.5 Approval of steel mills; Rolled Bar

1.5.1 Bar materials intended for chain and accessories are to be manufactured only by works approved by the Classification Society. The approval is limited to a nominated supplier of bar material. If a chain manufacturer wishes to use material from a number of suppliers, separate approval tests must be carried out for each supplier.

1.5.2 Approval will be given only after successful testing of the completed chain. Each Grade is to be individually approved. Approval for a higher grade does not constitute approval of a lower grade. If it is demonstrated to the satisfaction of the Classification Society that the higher and lower grades are produced to the same manufacturing procedure using the same chemistry and heat treatment, consideration will be given to qualification of a lower grade by a higher. The parameters applied during qualification are not to be modified during production. The approval will normally be limited up to the maximum diameter equal to that of the chain diameter tested. The rolling reduction ratio is to be recorded and is to be at least 5:1 for R3, R3S, R4, R4S and R5. The rolling reduction ratio used in production can be higher, but should not be lower than that qualified.

1.5.3 The steelmaker is to submit a specification of the chemical composition of the bar material, which must be approved by the Classification Society and by the chain manufacturer. The steel maker is to confirm by analysis and testing that the specification is met. For Grade R4, R4S and R5 chain the steel shall contain a minimum of 0.20 per cent molybdenum.

1.5.4 A heat treatment sensitivity study simulating chain production conditions shall be applied in order to verify mechanical properties and establish limits for temperature and time combinations. All test details and results are to be submitted to the Classification Society.

1.5.5 The bar manufacturer is to provide evidence that the manufacturing process produces material that is resistant to strain ageing, temper embrittlement and for R3S, R4, R4S and R5, hydrogen embrittlement. All test details and results are to be submitted to the Classification Society.

### 1.6 Approval of forges and foundries; Accessories

1.6.1 Forges and foundries intending to supply finished or semi-finished accessories are to be approved by the Classification Society. A description of manufacturing processes and process controls is to be submitted to the Classification Society. The scope of approval is to be agreed with the Classification Society. The approval is to be limited to a nominated supplier of forged or cast material. If an accessory manufacturer wishes to use material from a number of suppliers, a separate approval must be carried out for each supplier.

1.6.2 Approval will be given only after successful testing of the completed accessory. Approval for a higher grade does not constitute approval of a lower grade. If it is demonstrated to the satisfaction of the Classification Society that the higher and lower grades are produced to the same manufacturing procedure using the same steel specification, supplier and heat treatment, consideration will be given to qualification of a lower grade by a higher. The approval will normally be limited to the type of accessory and the IACS designated mooring grade of material up to the maximum diameter or thickness equal to that of the completed accessory used for qualification unless otherwise agreed by the Classification Society. However for the different accessories that have the same geometry, the tests for initial approval are to be carried out on the one having the lowest reduction ratio. Qualification of accessory pins to maximum diameters is also required. Individual accessories of complex geometries will be subject to the Classification Society requirements.

1.6.3 For forgings – Forgings are to have wrought microstructure and the minimum reduction ratio is to be 3 to 1. The forging reduction ratio, used in the qualification tests, from cast ingot/slab to forged component is to be recorded. The forging reduction ratio used in production can be higher, but should not be lower than that qualified. The degree of upsetting during qualification is to be recorded and maintained during production. Heat cycling during forging and reheating is to be monitored by the manufacturer and recorded in the forging documentation. The manufacturer is to have a maintenance procedure and schedule for dies and tooling which shall be submitted to the Classification Society.

1.6.4 The forge or foundry is to submit a specification of the chemical composition of the forged or cast material, which must be approved by the Classification Society. For Grade R4, R4S and R5 chain the steel should contain a minimum of 0.20 per cent molybdenum.

1.6.5 Forges and foundries are to provide evidence that the manufacturing process produces material that is resistant to strain ageing, temper embrittlement and for R4S and R5 grades, hydrogen embrittlement. A heat treatment sensitivity study simulating accessory production conditions shall be applied in order to verify mechanical properties and establish limits for temperature and time combinations. (Cooling after tempering shall be appropriate to avoid temper embrittlement). All test details and results are to be submitted to the Classification Society.

1.6.6 For initial approval CTOD tests are to be carried out on the particular IACS mooring grade of material. Three CTOD tests are to be tested in accordance with a recognized standard such as BS 7448 Part 1 & BS EN ISO 15653:2010. For rectangular accessories, the CTOD test piece is to be a standard 2 x 1 single edge notched bend specimen of thickness equal to full thickness of material to be tested. Subsized specimens can be used subject to approval of the Classification Society. For circular geometries, the minimum cross section of the test piece shall be 50 x 25mm for accessory diameters less than 120mm, and 80 x 40mm for diameters 120mm and above. The notch of the CTOD specimen is to be located as close to the surface as practicable. The tests are to be taken at minus 20º C and the results submitted for review. The minimum values of each set of three specimens are to at least meet the requirements as indicated in table 2 (same as that of the studless chain material shown in table 1).

**Table 2: Minimum CTOD test values for accessories**

| Grade of Accessory | R3 in mm | R3S in mm | R4 in mm | R4S & R5 in mm |
| :--- | :--- | :--- | :--- | :--- |
| CTOD | 0.20 | 0.22 | 0.24 | 0.26 |

The geometry of accessories can vary. Figure 2 shows the CTOD location for circular and rectangular cross sections such as those of the D-shackle and accessories fabricated from rectangular sections. The orientation of the specimen shall consider the direction of the grain flow. Figure 2(b) shows two possible sampling positions for CTOD test specimens with notch orientation for rectangular type accessories.

![Figure 2: Location of CTOD test specimens: a) Circular type accessory (e.g. D-Type Shackle) and b) rectangular type accessory, B corresponds to the thickness of material, the grain flow is considered in the longitudinal direction X](image_description)

1.6.7 Calibration of furnaces shall be verified by measurement and recording of a calibration test piece with dimensions equivalent to the maximum size of link manufactured. Thermocouples are to be placed both on the surface and in a drilled hole located at the mid thickness position of the calibration block. The furnace dimensions shall be such as to allow the whole furnace charge to be uniformly heated to the necessary temperature. Temperature uniformity surveys of heat treatment furnaces for forged and cast components shall be carried out according to API Spec 6A/ISO 10423 Annex M or ASTM A991. The initial survey shall be carried out with maximum charge (load) in the furnace. Subsequent surveys shall be carried out annually and may be carried out with no furnace charge.

The quench bath maximum temperature and the maximum heat treatment transfer times from furnace to quench are to be established and documented. During production the established quenching parameters are to be followed and records are to be maintained of bath temperatures and transfer times.

1.6.8 For R4S and R5 refer to additional requirements in 1.3.5.

### 1.7 Approval of quality system at accessory manufacturers

1.7.1 Refer to 1.4.

## 2 MATERIALS

### 2.1 Scope

2.1.1 These requirements apply to rolled steels, forgings and castings used for the manufacture of offshore mooring chain and accessories.

### 2.2 Rolled steel bars

#### 2.2.1 Steel manufacture

2.2.1.1 The steels are to be manufactured by basic oxygen, electric furnace or such other process as may be specially approved. All steels are to be killed and fine grain treated. The austenitic grain size for R3, R3S and R4 is to be 6 or finer in accordance with ASTM E112 or equivalent grain size index in accordance to ISO 643. Measurements for circular sections are to be taken at 1/3 radius.

2.2.1.2 Steel for bars intended for R4S and R5 chain is to be vacuum degassed. The austenitic grain size is to be 6 or finer in accordance with ASTM E112 or equivalent grain size index in accordance to ISO 643. Measurements for circular sections are to be taken at 1/3 radius.

2.2.1.3 For R4S and R5 the following information is to be supplied by the bar manufacturer to the mooring chain manufacturer and the results included in the chain documentation:

a) Each heat is to be examined for non-metallic inclusions. The level of micro inclusions is to be quantified and assessed in accordance to the national/international standards; to be sure inclusion levels are acceptable for the final product.
b) A sample from each heat is to be macro etched according to ASTM E381 or equivalent, to be sure there is no injurious segregation or porosity.
c) Hardenability data, according to ASTM A255, or equivalent, is to be supplied with each heat.

#### 2.2.2 Chemical composition

2.2.2.1 For acceptance tests, the chemical composition of ladle samples of each heat is to be determined by the steel maker and is to comply with the approved specification.

#### 2.2.3 Mechanical tests

2.2.3.1 Bars of the same nominal diameter are to be presented for test in batches of 50 tonnes or fraction thereof from the same heat. Test specimens are to be taken from material heat treated in the same manner as intended for the finished chain.

2.2.3.2 Each heat of Grade R3S, R4, R4S and R5 is to be tested for hydrogen embrittlement. In case of continuous casting, test samples representing both the beginning and the end of the charge shall be taken. In case of ingot casting, test samples representing two different ingots shall be taken.

2.2.3.2.1 Two (2) tensile test specimens shall be taken from the central region of bar material which has been subjected to the heat treatment cycle intended to be used in production. A specimen with a diameter of 20 mm is preferred (consideration will be given to a diameter of 14 mm).

2.2.3.2.2 One of the specimens is to be tested within a maximum of 3 hours after machining (for a 14 mm diameter specimen, the time limit is 1½ hours). Where this is not possible, the specimen is to be immediately cooled to -60°C after machining and kept at that temperature for a maximum period of 5 days.

2.2.3.2.3 The second specimen is to be tested after baking at 250°C for 4 hours, alternatively 2 hours for 14 mm diameter specimen.

2.2.3.2.4 A slow strain rate < 0,0003 s⁻¹ must be used during the entire test, until fracture occurs (This is approximately 10 minutes for the 20 mm diameter specimen). Tensile strength, elongation and reduction of area are to be reported.

2.2.3.2.5 The acceptance requirement for the test is:
$Z_1 / Z_2 \ge 0.85$

where:
$Z_1$ = Reduction of area without baking
$Z_2$ = Reduction of area after baking

If the requirement $Z_1/Z_2 \ge 0.85$ is not achieved, the bar material may be subjected to a hydrogen degassing treatment after agreement with the Classification Society. New tests shall be performed after degassing.

2.2.3.3 For all grades, one tensile and three Charpy V-notch specimens are to be taken from each sample selected. The test specimens are to be taken at approx. one-third radius below the surface, as shown in Figure 3 and prepared in accordance with UR W2. The results of all tests are to be in accordance with the appropriate requirements of Table 3.

2.2.3.4 Re-test requirements for tensile and Charpy impact tests are detailed in UR W2.

2.2.3.5 Failure to meet the requirements will result in rejection of the batch represented unless it can be clearly attributable to improper simulated heat treatment.

**Table 3: Mechanical properties of offshore mooring chain and accessories**

| Grade | Yield stress N/mm² minimum (1) | Tensile strength N/mm² minimum (1) | Elongation % minimum | Reduction (3) of area % minimum | Charpy V-notch impact tests: Test temp °C (2) | Charpy V-notch impact tests: Avg energy J minimum | Avg energy flash weld J minimum |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **R3** | 410 | 690 | 17 | 50 | 0 / -20 | 60 / 40 | 50 / 30 |
| **R3S** | 490 | 770 | 15 | 50 | 0 / -20 | 65 / 45 | 53 / 33 |
| **R4** | 580 | 860 | 12 | 50 | -20 | 50 | 36 |
| **R4S(4)** | 700 | 960 | 12 | 50 | -20 | 56 | 40 |
| **R5(4)** | 760 | 1000 | 12 | 50 | -20 | 58 | 42 |

**NOTES**
1. Aim value of yield to tensile ratio: 0.92 max.
2. At the option of the Classification Society the impact test of Grade R3 and R3S may be carried out at either 0°C or minus 20°C (See Table 3).
3. Reduction of area of cast steel is to be for Grades R3 and R3S: min. 40 %, for R4, R4S and R5: min. 35 %, cf. item 2.4.4.
4. Aim maximum hardness for R4S is HB330 and R5 HB340.

![Figure 3: Sampling of steel bars, forgings and castings showing the locations for tensile and impact test specimens at r/3](image_description)

#### 2.2.4 Dimensional tolerances

2.2.4.1 The diameter and roundness shall be within the tolerances specified in Table 4, unless otherwise agreed.

**Table 4: Dimensional tolerance of bar stock**

| Nominal diameter mm | Tolerance on diameter mm | Tolerance on roundness (dmax - dmin) mm |
| :--- | :--- | :--- |
| less than 25 | -0 + 1.0 | 0.6 |
| 25 - 35 | -0 + 1.2 | 0.8 |
| 36 - 50 | -0 + 1.6 | 1.1 |
| 51 - 80 | -0 + 2.0 | 1.5 |
| 81 - 100 | -0 + 2.6 | 1.95 |
| 101 - 120 | -0 + 3.0 | 2.25 |
| 121 - 160 | -0 + 4.0 | 3.00 |
| 161 - 222 | -0 + 5.0 | 4.00 |

#### 2.2.5 Non-destructive examination and repair

2.2.5.1 Non-destructive examination is to be performed in accordance with recognized Standards such as those indicated below or equivalent. Non-destructive examination procedures, together with rejection/acceptance criteria are to be submitted to the Classification Society.

Magnetic particle testing (MT) of bars:
- ASTM E1444 and ISO 9934

Magnetic Leakage Flux Testing (MLFT)-JIS Z2319

Eddy current testing (ET) of bars:
- ISO 15549

2.2.5.2 Manufacturers shall prepare written procedures for NDE. NDE personnel shall be qualified and certified according to ISO 9712, ACCP or equivalent. Personnel qualification to an employer or responsible agency based qualification scheme as SNT-TC-1A may be accepted if the employer's written practice is reviewed and found acceptable and the Level III is ASNT Level III, ISO 9712 Level III or ACCP Professional Level III and certified in the applicable method. NDE operators shall be qualified to at least level II.

2.2.5.3 The manufacturer shall ensure that 100 percent of bar material intended for either chain or fittings is subjected to ultrasonic examination at an appropriate stage of the manufacture to procedures approved by the Classification Society and to the acceptance criteria required. The bars shall be free of pipe, cracks and flakes. If the end length of the delivered bars is not subjected to UT then it must be agreed between the bar supplier and the chain manufacturer of what length of bar is to be removed from the ends. The details are to be documented in the approval of each bar supplier. Phased array UT procedures may be applied, subject to approval by the Classification Society.

2.2.5.4 100 percent of the bar material is to be examined by magnetic particle (MT) or eddy current (ET) or Magnetic Leakage Flux Testing (MLFT) methods. The bars shall be free of injurious surface imperfections such as seams, laps and rolled-in mill scale. Provided that their depth is not greater than 1% of the bar diameter, longitudinal discontinuities may be removed by grinding and blending to a smooth contour.

All bars supplied in a machined (peeled) condition shall be 100% visually inspected. The Classification Society may also require: 10% inspected with magnetic particle testing (MT) or eddy current testing (ET) or Magnetic Leakage Flux Testing (MLFT), for longitudinal imperfections. The maximum depth of peeling is to be agreed and documented in the approval of each supplier.

2.2.5.5 The frequency of NDE may be reduced at the discretion of the Classification Society provided it is verified by statistical means that the required quality is consistently achieved.

2.2.5.6 Weld repair of bar is not permitted.

#### 2.2.6 Marking

2.2.6.1 Each bar is to be stamped with the steel grade designation and the charge number (or a code indicating the charge number) on one of the end surfaces. Other marking methods may be accepted subject to agreement.

### 2.3 Forged steel

#### 2.3.1 Manufacture

2.3.1.1 Forged steels used for the manufacture of accessories must be in compliance with approved specifications and the submitted test reports approved by the Classification Society. Steel is to be manufactured by basic oxygen, electric furnace or such other process as may be specially approved. All steel is to be killed and fine grain treated. The austenitic grain size for R3, R3S and R4 is to be 6 or finer in accordance with ASTM E112 or equivalent grain size index in accordance to ISO 643. Measurements for circular sections are to be taken at 1/3 radius. Measurements for non-circular sections are to be taken at 1/4t.

2.3.1.2 Steel for forgings intended for R4S and R5 chain is to be vacuum degassed. The austenitic grain size is to be 6 or finer in accordance with ASTM E112 or equivalent grain size index in accordance to ISO 643. Measurements for circular sections are to be taken at 1/3 radius. Measurements for non-circular sections are to be taken at 1/4t.

2.3.1.3 For steel intended for R4S and R5 accessories the following information is to be supplied by the steel manufacturer to the mooring accessory manufacturer and the results included in the accessory documentation:

a) Each heat is to be examined for non-metallic inclusions. The level of micro inclusions is to be quantified and assessed in accordance with the national/international standards; to be sure inclusion levels are acceptable for the final product.
b) A sample from each heat is to be macro-etched according to ASTM E381 or equivalent, to be sure there is no injurious segregation or porosity.
c) Hardenability data, according to ASTM A255, or equivalent, is to be supplied with each heat.

#### 2.3.2 Chemical composition (See 2.2.2)

#### 2.3.3 Heat treatment

2.3.3.1 Finished forgings are to be properly heat treated in compliance with specifications submitted and approved.

#### 2.3.4 Mechanical properties

2.3.4.1 The forgings must comply with the mechanical properties given in Table 3, when properly heat treated.

#### 2.3.5 Mechanical tests

2.3.5.1 For test sampling, forgings of similar dimensions (diameters do not differ by more than 25mm) originating from the same heat treatment charge and the same heat of steel are to be combined into one test unit. From each test unit one tensile and three impact test specimens are to be taken and tested in accordance with UR W2. For the location of the test specimens see Figure 3.

2.3.5.2 Each heat of Grade R3S, R4, R4S and R5 is to be tested for hydrogen embrittlement. In case of continuous casting, test samples representing both the beginning and the end of the charge shall be taken. In case of ingot casting, test samples representing two different ingots shall be taken.

2.3.5.2.1 Two (2) tensile test specimens shall be taken from the central region of forged material which has been subjected to the heat treatment cycle intended to be used in production. A specimen with a diameter of 20 mm is preferred (consideration will be given to a diameter of 14 mm).

2.3.5.2.2 One of the specimens is to be tested within a maximum of 3 hours after machining (for a 14 mm diameter specimen, the time limit is 1½ hours). Where this is not possible, the specimen is to be immediately cooled to -60°C after machining and kept at that temperature for a maximum period of 5 days.

2.3.5.2.3 The second specimen is to be tested after baking at 250°C for 4 hours, alternatively 2 hours for 14 mm diameter specimen.

2.3.5.2.4 A slow strain rate < 0,0003 s⁻¹ must be used during the entire test, until fracture occurs (This is approximately 10 minutes for the 20 mm diameter specimen). Tensile strength, elongation and reduction of area are to be reported.

2.3.5.2.5 The acceptance requirement for the test is:
$Z_1 / Z_2 \ge 0.85$

where:
$Z_1$ = Reduction of area without baking
$Z_2$ = Reduction of area after baking

If the requirement $Z_1/Z_2 \ge 0.85$ is not achieved, the bar material may be subjected to a hydrogen degassing treatment after agreement with the Classification Society. New tests shall be performed after degassing.

#### 2.3.6 Non-destructive examination and repair

2.3.6.1 Non-destructive examination is to be performed in accordance with recognized Standards, such as those indicated below, or equivalent. The non-destructive examination procedures, together with rejection/acceptance criteria are to be submitted to the Classification Society.

Magnetic particle testing (MT) of forgings:
- EN 10228-1, ASTM A275, using wet continuous magnetization technique

Ultrasonic testing (UT) of forgings:
- EN 10228-3, ASTM A388, ISO 13588

2.3.6.2 Manufacturers shall prepare written procedures for NDE. NDE personnel shall be qualified and certified according to ISO 9712, ACCP or equivalent. Personnel qualification to an employer or responsible agency based qualification scheme as SNT-TC-1A may be accepted if the employer's written practice is reviewed and found acceptable and the Level III is ASNT Level III, ISO 9712 Level III or ACCP Professional Level III and certified in the applicable method. NDE operators shall be qualified to at least level II.

2.3.6.3 The forgings are to be subjected to one hundred percent ultrasonic examination at an appropriate stage of manufacture and in compliance with the standard submitted and approved.

2.3.6.4 Defects on non-machined surfaces may be removed by grinding to a depth of 5% of the nominal diameter. Grinding is not permitted on machined surfaces, except for slight inspection grinding on plane surfaces to a maximum depth of 0.8 mm in order to investigate spurious indications. Welding repairs are not permitted.

#### 2.3.7 Marking

2.3.7.1 Marking is to be similar to that specified in 2.2.6.

### 2.4 Cast steel

#### 2.4.1 Manufacture

2.4.1.1 Cast steel used for the manufacture of accessories must be in compliance with approved specifications and the submitted test reports approved by the Classification Society. Steel is to be manufactured by basic oxygen, electric furnace or such other process as may be specially approved. All steel is to be killed and fine grain treated. The austenitic grain size for R3, R3S and R4 is to be 6 or finer in accordance with ASTM E112 or equivalent grain size index in accordance to ISO 643. Measurements for circular sections are to be taken at 1/3 radius. Measurements for non-circular sections are to be taken at 1/4t.

2.4.1.2 Steel for castings intended for R4S and R5 accessories is to be vacuum degassed. The austenitic grain size is to be 6 or finer in accordance with ASTM E112 or equivalent grain size index in accordance to ISO 643. Measurements for circular sections are to be taken at 1/3 radius. Measurements for non-circular sections are to be taken at 1/4t.

2.4.1.3 For steel intended for R4S and R5 accessories the following information is to be obtained and the results included in the accessory documentation:

a) Each heat is to be examined for non-metallic inclusions. The level of micro inclusions is to be quantified and assessed in accordance to the national/international standards; to be sure inclusion levels are acceptable for the final product.
b) A sample from each heat is to be macro etched according to ASTM E381 or equivalent, to be sure there is no injurious segregation or porosity.
c) Hardenability data, according to ASTM A255, or equivalent, is to be supplied with each heat.

#### 2.4.2 Chemical composition (See 2.2.2)

#### 2.4.3 Heat treatment

2.4.3.1 All castings are to be properly heat treated in compliance with specifications submitted and approved.

#### 2.4.4 Mechanical properties

2.4.4.1 The castings must comply with the mechanical properties given in Table 3. The acceptance requirement for reduction of area is, however, reduced to 40 percent for grades R3 and R3S and 35 percent for grades R4, R4S and R5.

#### 2.4.5 Mechanical tests

2.4.5.1 For test sampling, castings of similar dimensions originating from the same heat treatment charge and the same heat of steel are to be combined into one test unit. From each test unit one tensile and three impact test specimens are to be taken and tested. For the location of the test specimens see Figure 3.

#### 2.4.6 Non-destructive examination and repair

2.4.6.1 Non-destructive examination is to be performed in accordance with recognized standards, such as those indicated below, or equivalent. The non-destructive examination procedures, together with rejection/acceptance criteria are to be submitted to the Classification Society.

Magnetic particle testing (MT) of castings:
- ASTM E709, using wet continuous magnetisation technique

Ultrasonic testing (UT) of castings:
- ASTM A609, ISO 13588

2.4.6.2 Manufacturers shall prepare written procedures for NDE. NDE personnel shall be qualified and certified according to ISO 9712, ACCP or equivalent. Personnel qualification to an employer or responsible agency based qualification scheme as SNT-TC-1A may be accepted if the employer's written practice is reviewed and found acceptable and the Level III is ASNT Level III, ISO 9712 Level III or ACCP Professional Level III and certified in the applicable method. NDE operators shall be qualified to at least level II.

2.4.6.3 The castings are to be subjected to one hundred percent ultrasonic examination in compliance with the standard submitted and approved.

2.4.6.4 Defects on non-machined surfaces may be removed by grinding to a depth of 5% of the nominal diameter. Grinding is not permitted on machined surfaces, except for slight inspection grinding on plane surfaces to a maximum depth of 0.8 mm in order to investigate spurious indications.

2.4.6.5 Where the repair entails removal of more than 5% of the diameter or thickness, the defective area shall be repaired by welding. The excavations shall be suitably shaped to allow good access for welding. The resulting grooves shall be subsequently ground smooth and complete elimination of the defective material shall be verified by NDE.

2.4.6.6 Weld repairs are classified as major or minor. A weld repair is considered major when the depth of the groove prepared for welding exceeds 25% of the diameter/thickness or 25 mm, whichever is smaller. All other weld repairs are considered minor.

2.4.6.7 Major weld repairs require approval before the repair is commenced. Proposals for major repairs shall be accompanied by sketches or photographs showing the extent and positions of the repairs. A grain refining heat treatment shall be given to the whole casting prior to major repairs. A post weld heat treatment or repeat of original heat treatment of castings shall be carried out.

2.4.6.8 Minor and major weld repairs must be recorded on sketches or photographs showing the extent and positions of the repairs.

2.4.6.9 All weld repairs shall be done by qualified welders using qualified procedures. Welders shall be qualified according to ISO 9606, ASME IX, ASTM A488 or equivalent. Procedures shall be qualified according to ISO 15614, ASME IX, ASTM A488 or equivalent with the following additional requirements: Charpy V notch impact tests with notch locations in weld metal, fusion line and heat affected zone + 2 mm and + 5 mm from fusion line, respectively. Test results shall meet the requirements specified for the parent metal.

#### 2.4.7 Marking (See 2.3.7)

### 2.5 Materials for studs

2.5.1 Studs intended for stud link chain cable are to be made of steel corresponding to that of the chain or in compliance with specifications submitted and approved. In general, the carbon content should not exceed 0.25 percent if the studs are to be welded in place.

## 3 DESIGN AND MANUFACTURE

### 3.1 Design

3.1.1 Drawings accompanied by design calculations, giving detailed design of chain and accessories made by or supplied through the chain manufacturer are to be submitted for approval. Typical designs are given in ISO 1704. For studless chain the shape and proportions are to comply with the requirements of this UR. Other studless proportions are to be specially approved. It should be considered that new or non-Standard designs of chain, shackles or fittings, may require a fatigue analysis and possible performance, fatigue or corrosion fatigue testing.

3.1.2 In addition, for stud link chain, drawings showing the detailed design of the stud shall be submitted for information. The stud shall give an impression in the chain link which is sufficiently deep to secure the position of the stud, but the combined effect of shape and depth of the impression shall not cause any harmful notch effect or stress concentration in the chain link.

3.1.3 Machining of Kenter shackles shall result in fillet radius min. 3 percent of nominal diameter.

### 3.2 Chain cable manufacturing process

#### 3.2.1 General

3.2.1.1 Offshore mooring chains shall be manufactured in continuous lengths by flash butt welding and are to be heat treated in a continuous furnace; batch heat treatment is not permitted, except in special circumstances where short lengths of chain are delivered, such as chafing chain. Ref. Appendix A.

3.2.1.2 The use of joining shackles to replace defective links is subject to the written approval of the end purchaser in terms of the number and type permitted. The use of connecting common links is restricted to 3 links in each 100m of chain.

#### 3.2.2 Chain cable manufacturing process records

3.2.2.1 Records of bar heating, flash welding and heat treatment shall be made available for inspection by the Surveyor.

#### 3.2.3 Bar heating

3.2.3.1 Bars for links shall be heated by electric resistance, induction or in a furnace.

3.2.3.2 For electric resistance heating or induction heating, the heating phase shall be controlled by an optical heat sensor. The controller shall be checked at least once every 8 hours and records made.

3.2.3.3 For furnace heating, the heat shall be controlled and the temperature continuously recorded using thermocouples in close proximity to the bars. The controls shall be checked at least once every 8 hours and records made.

#### 3.2.4 Flash welding of chain cable

3.2.4.1 The following welding parameters shall be controlled during welding of each link:
a) Platen motion
b) Current as a function of time
c) Hydraulic pressure

3.2.4.2 The controls shall be checked at least every 4 hours and records made.

#### 3.2.5 Heat treatment of chain cable

3.2.5.1 Chain shall be austenitized, above the upper transformation temperature, at a combination of temperature and time within the limits established.

3.2.5.2 When applicable, chain shall be tempered at a combination of temperature and time within the limits established. Cooling after tempering shall be appropriate to avoid temper embrittlement.

3.2.5.3 Temperature and time or temperature and chain speed shall be controlled and continuously recorded.

3.2.5.4 Grain determination shall be made for the final product. The austenitic grain size for R3, R3S, R4, R4S and R5 is to be 6 or finer in accordance with ASTM E112 or equivalent grain size index in accordance to ISO 643. Measurements for circular sections are to be taken at surface, 1/3 radius and centre for the base material, HAZ and weld.

#### 3.2.6 Mechanical properties

3.2.6.1 The mechanical properties of finished chain and accessories are to be in accordance with Table 3. For the location of test specimens see Figures 3 and 4.

#### 3.2.7 Proof and breaking test loads

3.2.7.1 Chains and accessories are to withstand the proof and break test loads given in Table 5.

#### 3.2.8 Freedom from defects

3.2.8.1 All chains are to have a workmanlike finish consistent with the method of manufacture and be free from defects. Each link is to be examined in accordance with section 4.5 using approved procedures.

![Figure 4: Sampling of chain links showing the orientation and location of tensile and impact test specimens in the link and weld zone](image_description)

**Table 5: Formulas for proof and break test loads, weight and length over 5 links**

| Test Load, in kN | Grade R3 Stud Link | Grade R3S Stud Link | Grade R4 Stud Link | Grade R4S Stud Link | Grade R5 Stud Link |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Proof** | 0.0148 d² (44 – 0.08d) | 0.0180 d² (44 – 0.08d) | 0.0216 d² (44 – 0.08d) | 0.0240 d² (44 – 0.08d) | 0.0251 d² (44 – 0.08d) |
| **Break** | 0.0223 d² (44 – 0.08d) | 0.0249 d² (44 – 0.08d) | 0.0274 d² (44 – 0.08d) | 0.0304 d² (44 – 0.08d) | 0.0320 d² (44 – 0.08d) |

| Test Load, in kN | Grade R3 Studless | Grade R3S Studless | Grade R4 Studless | Grade R4S Studless | Grade R5 Studless |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Proof** | 0.0148 d² (44 – 0.08d) | 0.0174 d² (44 – 0.08d) | 0.0192 d² (44 – 0.08d) | 0.0213 d² (44 – 0.08d) | 0.0223 d² (44 – 0.08d) |
| **Break** | 0.0223 d² (44 – 0.08d) | 0.0249 d² (44 – 0.08d) | 0.0274 d² (44 – 0.08d) | 0.0304 d² (44 – 0.08d) | 0.0320 d² (44 – 0.08d) |

| Chain Weight, in kg/m | Stud link = 0.0219d² |
| :--- | :--- |
| **Chain Weight, in kg/m** | Studless chain: Weight calculations for each design are to be submitted. |
| **Pitch Length** | Five Link Measure |
| **Minimum** | 22d |
| **Maximum** | 22.55d |

#### 3.2.9 Dimensions and dimensional tolerances

3.2.9.1 The shape and proportion of links and accessories must conform to ISO 1704 or the designs specially approved.

3.2.9.2 The following tolerances are applicable to links:

a) The negative tolerance on the nominal diameter measured at the crown:
- up to 40 mm nominal diameter : - 1 mm
- over 40 up to 84 mm nominal diameter : - 2 mm
- over 84 up to 122 mm nominal diameter : - 3 mm
- over 122 up to 152 mm nominal diameter : - 4 mm
- over 152 up to 184 mm nominal diameter : - 6 mm
- over 184 up to 222 mm nominal diameter : - 7.5 mm

**Note 1:** The cross sectional area at the crown must have no negative tolerance. For diameters of 20 mm or greater, the plus tolerance may be up to 5 percent of the nominal diameter. For diameters less than 20 mm the plus tolerance is to be agreed with the Classification Society at the time of approval.

**Note 2:** The cross sectional area at the crown is to be calculated using the average of the diameters with negative tolerance and plus tolerance, measurements are to be taken from at least 2 locations approximately 90 degrees apart.

b) Diameter measured at locations other than the crown: The diameter is to have no negative tolerance. The plus tolerance may be up to 5 percent of the nominal diameter except at the butt weld where it is to be in accordance to manufacturer’s specification, which is to be agreed with the Classification Society. For diameters less than 20 mm, the plus tolerance is to be agreed with the Classification Society at the time of approval.

c) The allowable manufacturing tolerance on a length of five links is + 2.5 percent, but may not be negative.

d) All other dimensions are subject to a manufacturing tolerance of ± 2.5 percent, provided always that all parts fit together properly.

e) The tolerances for stud link and studless common links are to be measured in accordance with Figure 5.

f) For stud link chains studs must be located in the links centrally and at right angles to the sides of the link. The following tolerances in Figure 5 are acceptable provided that the stud fits snugly and its ends lie flush against the inside of the link:

**(a) Stud link - The internal link radii (R) and external radii should be uniform**

![Figure: Diagram of a stud link showing dimensions a, b, c, R and the crown](image_description)

**Table for Stud link dimensions**

| Designation (1) | Description | Nominal Dimension of the Link | Minus Tolerance | Plus Tolerance |
| :--- | :--- | :--- | :--- | :--- |
| **a** | Link Length | 6d | 0.15d | 0.15d |
| **b** | Link Half Length | a*/2 | 0.1d | 0.1d |
| **c** | Link Width | 3.6d | 0.09d | 0.09d |
| **e** | Stud Angular Misalignment | 0 degrees | 4 degrees | 4 degrees |
| **R** | Inner Radius | 0.65d | 0 | ----- |

**Note 1:** Dimension designation is shown in above figure. d = Nominal diameter of chain, a* = Actual link length

**(b) Studless - The internal link radii (R) and external radii should be uniform.**

![Figure: Diagram of a studless link showing dimensions a, b and R](image_description)

**Table for Studless link dimensions**

| Designation (1) | Description | Nominal Dimension of the Link | Minus Tolerance | Plus Tolerance |
| :--- | :--- | :--- | :--- | :--- |
| **a** | Link Length | 6d | 0.15d | 0.15d |
| **b** | Link Width | 3.35d | 0.09d | 0.09d |
| **R** | Inner Radius | 0.60d | 0 | ----- |

**Notes:** 
1. Dimension designation is shown in above figure. d = Nominal diameter of chain
2. Other dimension ratios are subject to special approval.

**Figure 5 (a) Stud link and (b) studless common link, proportions dimensions and tolerances**

#### 3.2.10 Stud link chain - welding of studs

3.2.10.1 A welded stud may be accepted for grade R3 and R3S chains. Welding of studs in grades R4, R4S and R5 chain is not permitted unless specially approved.

3.2.10.2 Where studs are welded into the links this is to be completed before the chain is heat treated.

3.2.10.3 The stud ends must be a good fit inside the link and the weld is to be confined to the stud end opposite to the flash butt weld. The full periphery of the stud end is to be welded unless otherwise approved.

3.2.10.4 Welding of studs both ends is not permitted unless specially approved.

3.2.10.5 The welds are to be made by qualified welders using an approved procedure and low-hydrogen approved consumables.

3.2.10.6 The size of the fillet weld shall as a minimum be as per API Specification 2F.

3.2.10.7 The welds are to be of good quality and free from defects such as cracks, lack of fusion, gross porosity and undercuts exceeding 1 mm.

3.2.10.8 All stud welds shall be visually examined. At least 10 per cent of all stud welds within each length of chain shall be examined by dye penetrant or magnetic particles after proof testing. If cracks or lack of fusion are found, all stud welds in that length are to be examined.

#### 3.2.11 Connecting common links (splice links)

3.2.11.1 Single links to substitute for test links or defective links without the necessity for re-heat treatment of the whole length are to be made in accordance with an approved procedure. Separate approvals are required for each grade of chain and the tests are to be made on the maximum size of chain for which approval is sought.

3.2.11.2 Manufacture and heat treatment of connecting common link is not to affect the properties of the adjoining links. The temperature reached by these links is nowhere to exceed 250°C.

3.2.11.3 Each link is to be subjected to the appropriate proof load and non-destructive examination as detailed in Table 5 and Section 4.5. A second link shall be made identical to the connecting common link; the link shall be tested and inspected per Section 4.4 and 4.5.

3.2.11.4 Each connecting common link is to be marked either; on the stud for stud link chain or, on the outer straight length on the side opposite the flash butt weld for studless chain. This marking is to be in accordance with Section 4.7 plus a unique number for the link. The adjoining links are also to be marked on the studs or straight length as above.

## 4 TESTING AND INSPECTION OF FINISHED CHAIN

### 4.1 General

4.1.1 This section applies to but is not limited to finished chain cable such as common stud and studless links, end links, enlarged end links and connecting common links (splice links).

4.1.2 All chain is to be subjected to proof load tests, sample break load tests and sample mechanical tests after final heat treatment in the presence of a Surveyor. Where the manufacturer has a procedure to record proof loads and the Surveyor is satisfied with the adequacy of the recording system, he need not witness all proof load tests. The Surveyor is to satisfy himself that the testing machines are calibrated and maintained in a satisfactory condition. Prior to inspection the chain is to be free from scale, paint or other coating and is to have a suitably prepared surface as per the applied NDE testing standard. The chain shall be sand or shot blast to meet this requirement.

### 4.2 Proof and break load tests

4.2.1 The entire length of chain shall withstand the proof load specified in Table 5 without fracture and shall not crack in the flash weld. The load applied shall not exceed the proof load by more than 10% when stretching the chain. Where plastic straining is used to set studs, the applied load is not to be greater than that qualified in approval tests.

4.2.2 A break-test specimen consisting of at least 3 links is to be either taken from the chain or produced at the same time and in the same manner as the chain. The test frequency is to be based on tests at sampling intervals according to Table 6 provided that every cast is represented. Each specimen shall be capable of withstanding the break load specified without fracture and shall not crack in the flash weld. It shall be considered acceptable if the specimen is loaded to the specified value and maintained at that load for 30 seconds.

4.2.3 For chain diameters over 100mm, alternative break-test proposals to the above break test will be considered whereby a one link specimen is used. Alternatives are to be approved by the Classification Society, every heat is to be represented, the test frequency is to be in accordance with Table 6, and it is to be demonstrated and proven that the alternative test represents an equivalent load application to the three link test.

4.2.4 If the loading capacity of the testing machine is insufficient, an alternative load testing machine is to be used that does have sufficient capacity (e.g. two loading machines in parallel) provided the testing and calibration procedure are agreed with the Classification Society.

**Table 6: Frequency of break and mechanical tests**

| Nominal chain diameter (mm) | Maximum sampling interval (m) |
| :--- | :--- |
| Min - 48 | 91 |
| 49 - 60 | 110 |
| 61 - 73 | 131 |
| 74 - 85 | 152 |
| 86 - 98 | 175 |
| 99 - 111 | 198 |
| 112 - 124 | 222 |
| 125 - 137 | 250 |
| 138 - 149 | 274 |
| 150 - 162 | 297 |
| 163 - 175 | 322 |
| 176 – 186 | 346 |
| 187 - 198 | 370 |
| 199 - 210 | 395 |
| 211 - 222 | 420 |

### 4.3 Dimensions and dimensional tolerances

4.3.1 After proof load testing measurements are to be taken on at least 5 per cent of the links in accordance with Section 3.2.9.

4.3.2 The entire chain is to be checked for the length, five links at a time. By the five link check the first five links shall be measured. From the next set of five links, at least two links from the previous five links set shall be included. This procedure is to be followed for the entire chain length. The measurements are to be taken preferably while the chain is loaded to 5 - 10 % of the minimum proof load. The tolerances for the 5 link measurements are indicated in Table 5, any deviations from the 5 link tolerances are to be agreed by the client and Classification Society. The links held in the end blocks may be excluded from this measurement.

4.3.3 Chain dimensions are to be recorded and the information retained on file.

### 4.4 Mechanical tests

4.4.1 Links of samples detached from finished, heat treated chain shall be sectioned for determination of mechanical properties. A test unit shall consist of one tensile and nine impact specimens. The tensile specimen shall be taken in the side opposite the flash weld. Three impact specimens shall be taken across the flash weld with the notch centred in the middle. Three impact specimens shall be taken across the unwelded side and three impact specimens shall be taken from the bend region.

4.4.2 The test frequency is to be based on tests at sampling intervals according to Table 6 provided that every cast is represented. Mechanical properties shall be as specified in Table 3.

4.4.3 The frequency of impact testing in the bend may be reduced at the discretion of the Classification Society provided it is verified by statistical means that the required toughness is consistently achieved.

4.4.4 Hardness tests are to be carried out on finished chain. The frequency and locations are to be agreed with the Classification Society. The recorded values are for information only and used as an additional check to verify that the heat treatment process has been stable during the chain production.

### 4.5 Non-destructive examination after proof load testing

4.5.1 All surfaces of every link shall be visually examined. Burrs, irregularities and rough edges shall be contour ground. Links shall be free from mill defects, surface cracks, dents and cuts, especially in the vicinity where gripped by clamping dies during flash welding. Studs shall be securely fastened. Chain is to be positioned in order to have good access to all surfaces. In order to allow optimal access to the surface area it is recommended that chain be hung in the vertical position, however access to inspect the interlink area may only be possible with the chain in the horizontal position.

4.5.2 Testing is to be performed in accordance with a recognized Standard and the procedures, together with acceptance/rejection criteria are to be submitted to the Classification Society for review. Manufacturers shall prepare written procedures for NDE. NDE personnel shall be qualified and certified according to ISO 9712, ACCP or equivalent. Personnel qualification to an employer or responsible agency based qualification scheme as SNT-TC-1A may be accepted if the employer's written practice is reviewed and found acceptable and the Level III is ASNT Level III, ISO 9712 Level III or ACCP Professional Level III and certified in the applicable method. NDE operators shall be qualified to at least level II.

4.5.3 Magnetic particles shall be employed to examine the flash welded area including the area gripped by the clamping dies. Procedures are to be submitted to the Classification Society for approval. Procedures and equipment in accordance with those approved shall be used. Frequency of examination shall be every link. Additionally, 10% of links are to be tested on all accessible surfaces. Link surfaces and the surface at the flash weld shall be free from cracks, lack of fusion and gross porosity. Testing shall be performed in accordance with ASTM E709 or another recognized standard (e.g. ISO 9934) using wet continuous fluorescent magnetization technique. Non fluorescent techniques can be accepted in special cases where the standard inspection procedures are impractical.

Links shall be free from:
- relevant linear indications exceeding 1.6 mm in transverse direction
- relevant linear indications exceeding 3.2 mm in longitudinal direction
- relevant non-linear indications exceeding 4.8 mm.

4.5.4 Ultrasonics shall be employed to examine the flash weld fusion. Procedures are to be submitted to the Classification Society for approval. Procedures and equipment in accordance with those approved shall be used. On-site calibration standards for chain configurations shall be approved. Frequency of examination shall be every link. The flash weld shall be free from defects causing ultrasonic back reflections equal to or greater than the calibration standard. The flash butt welds shall be ultrasonic tested (UT) in accordance with ASTM E587 or another recognized standard using single probe, angle-beam shear waves in the range from 45 to 70°.

Single probe technique has limitations as far as testing of the central region is concerned and the flash weld imperfections such as flat spots may have poor reflectivity. Where it is deemed necessary, detectability of imperfections may need to be carried out by using a tandem technique, TOFD or phased array.

4.5.5 Stud welds, if used, shall be visually inspected. The toes of the fillets shall have a smooth transition to the link with no undercuts exceeding 1.0 mm. Additionally, at least 10% of the stud welds distributed through the length shall be dye penetrant tested according to ASTM E1417 or magnetic particle tested according to ASTM E1444 or equivalent. Cracks, lack of fusion or gross porosity are not acceptable. If defects are found, testing shall be extended to all stud welds in that length.

### 4.6 Retest, rejection and repair criteria

4.6.1 If the length over 5 links is short, the chain may be stretched by loading above the proof test load specified provided that the applied load is not greater than that approved and that only random lengths of the chain need stretching. If the length exceeds the specified tolerance, the over length chain links shall be cut out and 4.6.2 shall apply.

4.6.2 If single links are found to be defective or do not meet other applicable requirements, defective links may be cut out and a connecting common link inserted in their place. The individual heat treatment and inspection procedure of connecting common links is subject to the Classification Society's approval. Other methods for repair are subject to the written approval of the Classification Society and the end purchaser. Weld repair of chain is not permitted.

4.6.3 If a crack, cut or defect in the flash weld is found by visual or magnetic particle examination, it shall be ground down no more than 5% of the link diameter in depth and streamlined to provide no sharp contours. The final dimensions must still conform to the agreed standard.

4.6.4 If indications of interior of flash weld defects, in reference to the accepted calibration standards are detected during ultrasonic examination, 4.6.2 shall apply.

4.6.5 If link diameter, length, width and stud alignment do not conform to the required dimensions, these shall be compared to the dimensions of 40 more links; 20 on each side of the affected link. If a single particular dimension fails to meet the required dimensional tolerance in more than 2 of the sample links, all links shall be examined. Sec. 4.6.2 shall apply.

4.6.6 If a break load test fails, a thorough examination with the Surveyor informed in a timely manner is to be carried out to identify the cause of failure. Two additional break test specimens representing the same sampling length of chain are to be subjected to the break load test. Based upon satisfactory results of the additional tests and the results of the failure investigation, it will be decided what lengths of chain can be accepted. Failure of either or both additional tests will result in rejection of the sampling length of chain represented and 4.6.2 shall apply.

4.6.7 If a link fails during proof load testing, a thorough examination with the Surveyor informed in a timely manner is to be carried out to identify the probable cause of failure of the proof test. In the event that two or more links in the proof loaded length fail, that section of proof loaded length is to be rejected. The above failure investigation is to be carried out especially with regard to the presence in other lengths of factors or conditions thought to be causal to failure.

4.6.8 In addition to the above failure investigation, a break test specimen is to be taken from each side of the one failed link, and subjected to the breaking test. Where multiple chains are produced simultaneously it is recognised that the preceding flash butt welded link and subsequent flash butt welded link will be on an alternative chain length or the other end of the chain length. In such cases the Classification Society may require that two additional break tests are to be taken from the lengths of chain that include the preceding and subsequent welded links. Based upon satisfactory results of both break tests and the results of the failure investigation, it will be decided what length of chain can be considered for acceptance. Failure of either or both breaking tests will result in rejection of the same proof loaded length. Replacement of defective links is to be in accordance with 4.6.2.

If the investigation identifies defects in the flash butt weld or a lower strength flash weld “a glue-weld” is found, additional NDT such as phased array UT is to be carried out to identify if other links are affected. A full assessment of the flash butt welding machine is to be carried out, together with assessment of the condition of the bar ends prior to welding.

4.6.9 Re-test requirements for tensile tests are to be in accordance with UR W2. Failure to meet the specified requirements of either or both additional tests will result in rejection of the sampling length of chain represented and 4.6.2 shall apply.

4.6.10 Re-test requirements for Charpy impact tests are to be in accordance with UR W2. Failure to meet the requirements will result in rejection of the sampling length represented and 4.6.2 shall apply.

### 4.7 Marking

4.7.1 The chain shall be marked at the following places:
- At each end.
- At intervals not exceeding 100 m.
- On connecting common links.
- On links next to shackles or connecting common links.

4.7.2 All marked links shall be stated on the certificate, and the marking shall make it possible to recognize leading and tail end of the chain. In addition to the above required marking, the first and last common link of each individual charge used in the continuous length shall be traceable and adequately marked.

The marking shall be permanent and legible throughout the expected lifetime of the chain.

4.7.3 The chain shall be marked on the studs as follows:
- Chain grade
- Certificate No.
- Classification Society's stamp

4.7.4 The Certificate number may be exchanged against an abbreviation or equivalent. If so, this shall be stated in the certificate.

4.7.5 The chain certificate shall contain information on number and location of connecting common links. The certificate number and replacement link number may be exchanged against an abbreviation or equivalent. If so, this shall be stated in the certificate.

### 4.8 Documentation

4.8.1 A complete Chain Inspection and Testing Report in booklet form shall be provided by the chain manufacturer for each continuous chain length. This booklet shall include all dimensional checks, test and inspection reports, NDT reports, process records, photographs as well as any nonconformity, corrective action and repair work.

4.8.2 Individual certificates are to be issued for each continuous single length of chain.

4.8.3 All accompanying documents, appendices and reports shall carry reference to the original certificate number.

4.8.4 The manufacturer will be responsible for storing, in a safe and retrievable manner, all documentation produced for a period of at least 10 years.

## 5 TESTING AND INSPECTION OF ACCESSORIES

### 5.1 General

5.1.1 This section applies to but is not limited to mooring equipment accessories such as detachable connecting links (shackles), detachable connecting plates (triplates), end shackles, swivels and swivel shackles, and subsea connectors.

5.1.2 All accessories are to be subjected to proof load tests, sample break load tests and sample mechanical tests after final heat treatment in the presence of a Surveyor. Where the manufacturer has a procedure to record proof loads and the Surveyor is satisfied with the adequacy of the recording system, he need not witness all proof load tests. The Surveyor is to satisfy himself that the testing machines are calibrated and maintained in a satisfactory condition. Prior to testing and inspection the chain accessories are to be free from scale, paint or other coating.

5.1.3 For accessory production a Manufacturing Procedure Specification (MPS) is to be submitted to the Classification Society that details all critical aspects of accessory production, casting, forging, heat treating (including arrangement and spacing of components in the heat treatment furnaces), quenching, mechanical testing, proof and break loading and NDE.

### 5.2 Proof and break load tests

5.2.1 All accessories are to be subjected to the proof load specified for the corresponding stud link chain.

5.2.2 Chain accessories are to be tested at the break load prescribed for the grade and size of chain for which they are intended. At least one accessory out of every batch or every 25 accessories, whichever is less, is to be tested.

5.2.2.1 For individually produced, individually heat treated, accessories or accessories produced in small batches (less than 5), alternative testing will be subject to special consideration. Alternative testing is to be approved by the Classification Society and the following additional conditions may apply.

(a) Alternative testing is described in a written procedure and manufacturing procedure specification (MPS).
(b) A finite element analysis is provided at the break load and demonstrates that the accessory has a safety margin over and above the break load of the chain.
(c) Strain age testing (as per approved procedure by the Classification Society) is carried out on the material grade produced to the same parameters at the time of qualification.
(d) If an accessory is of a large size that will make heat treating in batches unfeasible or has a unique design, strain gauges are to be applied during the proof and break load tests during initial qualification and during production. The strain gauge results from production are to be comparable with the results from qualification.

5.2.3 A batch is defined as accessories that originate from the same heat treatment charge and the same heat of steel. Reference sections 2.3 and 2.4.

5.2.4 The accessories which have been subjected to the break load test are to be destroyed and not used as part of an outfit, with the exceptions given in 5.2.5.

5.2.5 Where the accessories are of increased dimension or alternatively a material with higher strength characteristics is used, they may be included in the outfit at the discretion of the Classification Society, provided that;

(a) the accessories are successfully tested at the prescribed breaking load appropriate to the chain for which they are intended, and
(b) it is verified by procedure tests that such accessories are so designed that the breaking strength is not less than 1.4 times the prescribed breaking load of the chain for which they are intended.
(c) strain age properties have been carried out on the material grade produced to the same parameters.
(d) strain gauges are to be applied during the break load test in the high stress locations to monitor that the strains stay within allowable limits.

### 5.3 Dimensions and dimensional tolerances

5.3.1 At least one accessory (of the same type, size and nominal strength) out of 25 is to be checked for dimensions after proof load testing. The manufacturer is to provide a statement indicating compliance with the purchaser's requirements.

5.3.2 The following tolerances are applicable to accessories:
a) Nominal diameter: + 5 percent, - 0 percent
b) Other dimensions: ± 2½ percent

These tolerances do not apply to machined surfaces.

### 5.4 Mechanical tests

5.4.1 Accessories are to be subjected to mechanical testing as described in Section 2.3 and 2.4. Mechanical tests are to be taken from proof loaded full size accessories that have been heat treated with the production accessories they represent. At least one accessory out of every batch or every 25 accessories, whichever is less, is to be tested. Hardness tests are to be carried out on finished accessories. The frequency and locations are to be agreed with the Classification Society. The recorded values are for information only and used as an additional check to verify that the heat treatment process has been stable during the accessory production.

The use of separate representative coupons is not permitted except as indicated in 5.4.5 below.

5.4.2 Test location of forged shackles. Forged shackle bodies and forged Kenter shackles are to have a set of three impact tests and a tensile test taken from the crown of the shackle. Tensile tests on smaller diameter shackles can be taken from the straight part of the shackle, where the geometry does not permit a tensile specimen from the crown. The tensile properties and impact values are to meet the requirements of Table 3 in the locations specified in Figure 3, with the Charpy pieces on the outside radius.

5.4.3 The locations of mechanical tests of cast shackles and cast Kenter shackles can be taken from the straight part of the accessory. The tensile properties and impact values are to meet the requirements of Table 3 in the locations specified in Figure 3.

5.4.4 The locations of mechanical tests of other accessories with complex geometries are to be agreed with the Classification Society.

For non-circular sections, 1/4t (thickness) from the surface is considered appropriate.

Rolled plates are to be tested to the Standard to which they are produced.

5.4.5 For individually produced (heat treated) accessories or accessories produced in small batches, (less than 5), alternative testing can be proposed to the Classification Society. Each proposal for alternative testing is to be detailed by the manufacturer in a written procedure and submitted to the Classification Society, and the following additional conditions may apply:

(a) If separately forged or cast coupons are used, they are to have a cross-section and, for forged coupon, a reduction ratio similar to that of the accessories represented, and are to be heat treated in the same furnace and quenched in the same tank at the same time, as the actual forgings or castings. Thermocouples are to be attached to the coupon and to the accessories.
(b) If separately forged or cast coupons are agreed, it is to be verified by procedure test that coupon properties are representative of accessory properties.

5.4.6 A batch is defined as accessories that originate from the same heat treatment charge and the same heat of steel. Reference sections 2.3 and 2.4.

5.4.7 Mechanical tests of pins are to be taken as per Figure 3 from the mid length of a sacrificial pin of the same diameter as the final pin. For oval pins the diameter taken is to represent the smaller dimension. Mechanical tests may be taken from an extended pin of the same diameter as the final pin that incorporates a test prolongation and a heat treatment buffer prolongation, where equivalence with mid length test values have been established. The length of the buffer is to be at least equal to 1 pin diameter dimension which is removed after the heat treatment cycle is finished. The test coupon can then be removed from the pin. The buffer and test are to come from the same end of the pin as per Figure 6.

![Figure 6: Buffer and test piece location showing the Pin, Test section, and Buffer section](image_description)

### 5.5 Non-destructive examination after proof load testing

5.5.1 All chain accessories are to be subjected to a close visual examination. Special attention is to be paid to machined surfaces and high stress regions. Prior to inspection, chain accessories are to have a suitably prepared surface as per the applied NDE testing standard. All non-machined surfaces are to be sand or shot blast to permit a thorough examination. Where applicable, accessories shall be dismantled for inspection of internal surfaces. All accessories are to be checked by magnetic particles or dye penetrant. UT of accessories may be required by the Classification Society. The acceptance /rejection criteria of UT established for the design is to be met.

5.5.2 Testing is to be performed in accordance with a recognized Standard, such as those indicated below, or equivalent. The procedures, together with acceptance/rejection criteria are to be submitted to the Classification Society for review. Manufacturers shall prepare written procedures for NDE. NDE personnel shall be qualified and certified according to ISO 9712, ACCP or equivalent. Personnel qualification to an employer or responsible agency based qualification scheme as SNT-TC-1A may be accepted if the employer's written practice is reviewed and found acceptable and the Level III is ASNT Level III, ISO 9712 Level III or ACCP Professional Level III and certified in the applicable method. NDE operators shall be qualified to at least level II.

Magnetic particle testing (MT) of forgings:
- EN 10228-1, ASTM A275, using wet continuous magnetization technique or equivalent standards such as ISO 4986, IACS Rec 69

Ultrasonic testing (UT) of forgings:
- EN 10228-3, ASTM A388, ISO 13588

Magnetic particle testing (MT) of castings:
- ASTM E709, using wet continuous magnetization technique

Ultrasonic testing (UT) of castings:
- ASTM A609, ISO 13588

All surfaces shall be magnetic particle tested (MT). Testing shall be performed in accordance with standards referenced using the fluorescent technique. As a minimum surfaces shall be free from:
- relevant linear indications exceeding 1.6 mm in transverse direction
- relevant linear indications exceeding 3.2 mm in longitudinal direction
- relevant non-linear indications exceeding 4.8 mm.

When required by the Classification Society, ultrasonic testing is to be carried out on 100% of cast or forged accessories. The acceptance/rejection criteria established for the design is to be met.

5.5.3 The manufacturer is to provide a statement that non destructive examination has been carried out with satisfactory results. This statement should include a brief reference to the techniques and to the operator's qualification.

5.5.4 Weld repairs of finished accessories are not permitted.

### 5.6 Test failures

5.6.1 In the event of a failure of any test the entire batch represented is to be rejected unless the cause of failure has been determined and it can be demonstrated to the Surveyor's satisfaction that the condition causing the failure is not present in any of the remaining accessories.

### 5.7 Marking

5.7.1 Each accessory is to be marked as follows:
- Chain grade

5.7.2 The Certificate number may be exchanged against an abbreviation or equivalent. If so, this shall be stated in the certificate.

### 5.8 Documentation

5.8.1 A complete Inspection and Testing Report in booklet form shall be provided by the manufacturer for each order. This booklet shall include all dimensional checks, test and inspection reports, NDT reports, process records and example photographs of components positioned in furnaces, as well as any nonconformity, corrective action and repair work.

5.8.2 Each type of accessory shall be covered by separate certificates.

5.8.3 All accompanying documents, appendices and reports shall carry reference to the original certificate number.

5.8.4 The manufacturer will be responsible for storing, in a safe and retrievable manner, all documentation produced for a period of at least 10 years.

## Appendix A - Chafing Chain for Single Point Mooring arrangements

### A.1. Scope

These requirements apply to short lengths (approximately 8m) of 76mm diameter chain to be connected to hawsers for the tethering of oil carriers to single point moorings, FPSO’s and similar uses.

### A.2. Approval of Manufacturing

A.2.1 The chafing chain is to be manufactured by works approved by the Classification Society according to W22.1.3.

### A.3. Materials

A.3.1 The materials used for the manufacture of the chafing chain are to satisfy the requirements of W22.2.

### A.4. Design, manufacturing, testing and certification

A.4.1 The chafing chain is to be designed, manufactured, tested and certified in accordance with W22.3, W22.4 and W22.5, except that batch heat treatment is permitted.

A.4.2 The arrangement of the end connections is to be of an approved type.

A.4.3 The common link is to be of the stud link type – Grade R3 or R4.

A.4.4 The chafing chain is to be capable of withstanding the breaking test loads of 4884kN (Grade R3) and 6001kN (Grade R4). See Note 1.

A.4.5 The chain lengths shall be proof load tested in accordance with W22.4.2. The test load for Grade R3 is 3242kN and for Grade R4 is 4731kN.

**Note 1:** Documented evidence of satisfactory testing of similar diameter mooring chain in the prior 6 month period may be used in lieu of break testing subject to agreement with the Classification Society.

**Note 2:** The requirements herein are also applicable to other diameter chafing chains, such as 84 mm and 96 mm, subject to compliance with the proof and break load requirements specified for the chain grade and diameters in Section 3 Table 5.

**End of Document**

================================================================================
# FILE: UR_W/ur-w23corr1.md
================================================================================

# W23 Approval of Welding Consumables for High Strength Steels for Welded Structures

(1995)
(Rev.1 1997)
(Rev.2 Apr 2018)
(Corr.1 June 2019)

## 1. General

### 1.1 Scope

1.1.1 These requirements supplement the UR W17 and give the conditions of approval and inspection of welding consumables used for high strength steels for welded structures according to UR W16 with yield strength levels from 420 N/mm² up to 960 N/mm², and impact grades A, D, E and F, except that impact grade F is not applicable for 890 N/mm² and 960 N/mm² yield strength levels.

Where no special requirements are given, those of UR W17 apply in analogous manner.

1.1.2 The welding consumables preferably to be used for the steels concerned are divided into several categories as follows:

- covered electrodes for manual welding,
- wire-flux combinations for multi-run* submerged arc welding,
- solid wire-gas combinations for arc welding (including rods for gas tungsten arc welding),
- flux cored wire with or without gas for arc welding.

### 1.2 Grading, Designation

1.2.1 Based on the yield strength of the weld metal, the welding consumables concerned are divided into eight (yield) strength groups:

- Y42 - for welding steels with minimum yield strength 420 N/mm²
- Y46 - for welding steels with minimum yield strength 460 N/mm²
- Y50 - for welding steels with minimum yield strength 500 N/mm²
- Y55 - for welding steels with minimum yield strength 550 N/mm²
- Y62 - for welding steels with minimum yield strength 620 N/mm²
- Y69 - for welding steels with minimum yield strength 690 N/mm²
- Y89 - for welding steels with minimum yield strength 890 N/mm²
- Y96 - for welding steels with minimum yield strength 960 N/mm²

1.2.2 Each of the eight (yield) strength groups is further divided into three main grades in respect of Charpy V-notch impact test requirements (test temperatures):

- Grade 3, test temperature -20°C
- Grade 4, test temperature -40°C
- Grade 5, test temperature -60°C

1.2.3 Analogously to the designation scheme used in UR W17 the welding consumables for high strength steels are subject to classification designation and approval as follows:

- According to 1.2.2 with the quality grades **3, 4 or 5**
- With the added symbol, **Y** and an appended code number designating the minimum yield strength of the weld metal corresponding 1.2.1: Y42, Y46, Y50, Y55, Y62, Y69, Y89 and Y96.
- With the added symbol **H10** or **H5** for controlled hydrogen content of the weld metal,
- With the added symbol, **S** (= semi-automatic) for semi-mechanised welding,
- With the added symbol, **M** designating multi-run technique* (and is applicable only to welding consumables for fully mechanised welding).

1.2.4 Each higher quality grade includes the one (or those) below Grade A... and D... steels acc. to UR W16 are to be welded using welding consumables of at least quality grade 3, grade E... steels using at least quality grade 4 and grade F... steels using at least quality grade 5., see the following table:

| Consumable Grade | Steel Grades covered |
| :--- | :--- |
| 3Y.. | D.. and A.. |
| 4Y.. | E.., D.. and A.. |
| 5Y.. | F.., E.., D.. and A.. |

Welding consumables approved with grades ..Y42, ..Y46 and ..Y50 are also considered suitable for welding steels in the two strength levels below that for which they have been approved. Welding consumables approved with grades ..Y55, ..Y62 and ..Y69 are also considered suitable for welding steels in the one strength level below that for which they have been approved.

Welding consumables with grade Y89 are considered suitable for welding steels in the same strength level only. Welding consumables with grade Y96 are also considered suitable for welding steels in the one strength level below that for which they have been approved.

For grades Y89 and Y96, where the design requirements permit undermatching weld joint, then welding consumables within the scope of this UR can be considered subject to Society discretion and Manufacturer's recommendations.

The Society may, in individual cases, restrict the range of application in (up to) such a way, that approval for any one strength level does not justify approval for any other strength level.

### 1.3 Manufacture, testing and approval procedure

1.3.1 Manufacturer's plant, production methods and quality control measures shall be such as to ensure reasonable uniformity in manufacture, see also UR W17.

1.3.2 Testing and approval procedure shall be in accordance with UR W17, sections 2 and 3 and as required in UR W17 for the individual categories (types) of welding consumables mentioned in 1.1.2 above.

---

## 2. Testing of the weld metal

2.1 For testing the deposited weld metal, test pieces analogous to those called for in UR W17, sections 4.2, 5.2, 6.2 or 6.3 respectively shall be prepared, depending on the type of the welding consumables (and according to the welding process). The base metal used shall be a fine-grained structural steel compatible with the properties of the weld metal, or the side walls of the weld shall be buttered with a weld metal of the same composition.

2.2 The chemical composition of the deposited weld metal shall be determined and certified in a manner analogous to that prescribed in UR W17, section 4.2.2. The results of the analysis shall not exceed the limit values specified in the standards or by the manufacturer, the narrower tolerances being applicable in each case.

2.3 Depending on the type of the welding consumables (and according to the welding process), the test specimens prescribed in UR W17, sections 3.1 and 4.2, 5.2, 6.2 or 6.3 respectively shall be taken from the weld metal test pieces in a similar manner.

2.4 The mechanical properties must meet the requirements stated in Tables 1 and 2. The provisions of UR W17 apply in analogous manner to the performance of the tests, including in particular the maintenance of the test temperature in the notched bar impact test and the carrying out of results.

### Table 1 Required toughness properties of the weld metal

| Quality grade | Test temperature [°C] | Minimum notch impact energy [J]¹⁾ |
| :--- | :---: | :--- |
| 3 | -20 | Y42: ≥ 47 |
| 4 | -40 | Y46: ≥ 47<br>Y50: ≥ 50 |
| 5 | -60 | Y55: ≥ 55<br>Y62: ≥ 62<br>Y69: ≥ 69<br>Y89: ≥ 69²⁾<br>Y96: ≥ 69²⁾ |

¹⁾ Charpy V-notch impact test specimen, mean value of three specimens; for requirements regarding minimum individual values and retests, see UR W17, section 3.3.2.
²⁾ Quality grade 5 is not applicable for Y89 and Y96 grade consumables.

### Table 2 Required strength properties of the weld metal

| Symbols added to quality grade | Minimum yield strength or 0.2% proof stress [N/mm²] | Tensile Strength [N/mm²] | Minimum elongation [%] |
| :---: | :---: | :---: | :---: |
| Y42 | 420 | 520-680 | 20 |
| Y46 | 460 | 540-720 | 20 |
| Y50 | 500 | 590-770 | 18 |
| Y55 | 550 | 640-820 | 18 |
| Y62 | 620 | 700-890 | 18 |
| Y69 | 690 | 770-940 | 17 |
| Y89 | 890 | 940-1100 | 14 |
| Y96 | 960 | 980-1150 | 13 |

---

## 3. Testing on welded joints

3.1 Depending on the type of the welding consumables (and according to the welding process), the testing on the welded joints shall be performed on butt-weld test pieces in analogous manner to UR W17, sections 4.3, 5.2, 6.2, 6.3, or 6.4 respectively.

3.2 Depending on the type of the welding consumables (and according to the welding process), the butt-weld test pieces called for in para. 3.1 shall be welded in a manner analogous to that prescribed in UR W17. The base metal used shall be a high-strength fine-grained structural steel with a minimum yield strength and tensile strength matching the consumable grade being approved and compatible with the added symbol for which application is made.

3.3 Depending on the type of the welding consumables (and according to the welding process), the test specimens described in UR W17 shall be taken from the butt-weld test pieces.

3.4 The mechanical properties must meet the requirements stated in Table 3. The provisions of UR W17 apply in analogous manner to the performance of the tests, including in particular the maintenance of the test temperatures in the notched bar impact test and the requirements regarding the retest specimens.

### Table 3 Required properties of welded joints

| Quality grade | Added symbol | Minimum tensile strength [N/mm²] | Minimum notch impact energy, test temperature | Minimum bending angle¹⁾ | Bend ratio D/t²⁾ |
| :--- | :---: | :---: | :--- | :---: | :---: |
| 3 to 5 accordance with Table 1 | Y42 | 520 | Depending on the quality grade & yield strength in accordance Table 1 | 120° | 4 |
| | Y46 | 540 | | | 4 |
| | Y50 | 590 | | | 4 |
| | Y55 | 640 | | | 5 |
| | Y62 | 700 | | | 5 |
| | Y69 | 770 | | | 5 |
| | Y89 | 940 | | | 6 |
| | Y96 | 980 | | | 7 |

¹⁾ Bending angle attained before the first incipient crack, minor pore exposures up to a maximum length of 3mm allowed.
²⁾ D = Mandrel diameter, t = specimen thickness

3.5 Where the bending angle required in Table 3 is not achieved, the specimen may be considered as fulfilling the requirements, if the bending elongation on a gauge length Lo fulfills the minimum elongation requirements stated in Table 2. The gauge length Lo = Ls + t (Ls = width of weld, t = specimen thickness), see sketch below.

![Figure 1: Sketch showing the measurement of the gauge length Lo for a welded joint bend test. Lo is defined as the sum of the weld width Ls and the specimen thickness t (Lo = Ls + t).](image_description)

---

## 4. Hydrogen test

4.1 The welding consumables, other than solid wire-gas combinations, shall be subjected to a hydrogen test in accordance with the mercury method to ISO 3600, or any other method such as the gas chromatographic method which correlates with that method, in respect of cooling rate and delay times during preparation of the weld samples, and the hydrogen volume determinations.

4.2 The diffusible hydrogen content of the weld metal determined in accordance with the provisions of UR W17, section 4.5 shall not exceed the limits given in table 4.

### Table 4 Allowable diffusible hydrogen content

| Yield strength group | Hydrogen symbol | Maximum hydrogen content [cm³/100 g deposited weld metal] |
| :--- | :---: | :---: |
| Y42 | | |
| Y46 | H 10 | 10 |
| Y50 | | |
| Y55 | | |
| Y62 | H 5 | 5 |
| Y69 | | |
| Y89 | | |
| Y96 | H5 | 5 |

## 5. Annual repeat test

The annual repeat tests specified in UR W17 shall entail the preparation and testing of weld metal test pieces as prescribed under 2. For grades Y69 to Y96 annual hydrogen test is required. In special cases, the Society may require more extensive repeat tests.

---

*Note: Rev.2 of this UR is to be uniformly implemented by IACS Societies when an application for approval is dated on or after 1 July 2019.*

*Wire-flux combinations for single or two-run technique are subject to special consideration of the Classification Society.


================================================================================
# FILE: UR_W/ur-w28rev2.md
================================================================================

# W28 Welding procedure qualification tests of steels for hull construction and marine structures

(June 2005)
(Rev.1 Nov 2006)
(Rev.2 Mar 2012)

## 1. Scope

1.1 This document gives requirements for qualification tests of welding procedures intended for the use of weldable steels as specified in UR W7, UR W8, UR W11 and UR W16 for hull construction and marine structures.

1.2 This document specifically excludes the welding procedure specified in UR W1.

1.3 All new welding procedure qualification tests are to be carried out in accordance with this document from 1 July 2007.

1.4 This document does not invalidate welding procedure qualification tests made and accepted by the Classification Society before 1 July 2007 provided the welding procedure qualification tests are considered by the Classification Society to meet the technical intent of this UR or have been qualified in accordance with the recognized standards such as ISO, EN, AWS, JIS or ASME.

## 2. General

2.1 Welding procedure qualification tests are intended to verify that a manufacturer is adequately qualified to perform welding operations using a particular procedure.

2.2 In general welding procedure tests are to reflect fabrication conditions in respect to welding equipment, inside or outside fabrication, weld preparation, preheating and any post-weld heat treatment. It is to be the manufacturer's responsibility to establish and document whether a procedure is suitable for the particular application.

2.3 For the welding procedure approval the welding procedure qualification test is to be carried out with satisfactory results. Welding procedure specifications are to refer to the test results achieved during welding procedure qualification testing.

2.4 Welding procedures qualified at a manufacturer are valid for welding in workshops under the same technical and quality management.

**Note:**

1. This UR is to be uniformly implemented by IACS Societies on ships contracted for construction from 1 January 2007 as well as the manufacturing of which is commenced on or after 1 January 2007.
2. The "contracted for construction" date means the date on which the contract to build the vessel is signed between the prospective owner and the shipbuilder. For further details regarding the date of "contract for construction", refer to IACS Procedural Requirement (PR) No. 29.
3. Rev.2 of this UR is to be uniformly implemented by IACS Societies on ships contracted for construction on or after 1 January 2013.

---

## 3. Welding procedure specification

### 3.1 Preliminary welding procedure specification and welding procedure specification

3.1.1 A welding procedure specification (WPS) is to be prepared by the shipyard or manufacturer which intends to perform the welding procedure qualification test. This document is also referred to as a preliminary welding procedure specification (pWPS). The pWPS can be modified and amended during procedure tests as deemed necessary however it is to define all relevant variables as mentioned in the WPS (refer to ISO 15614 or other recognized standards).

3.1.2 The shipyard or manufacturer is to submit to the Society a pWPS for review prior to the tests. In case that the test pieces welded according to the pWPS show unacceptable results the pWPS is to be adjusted by the shipyard or manufacturer. The new pWPS is to be prepared and the test pieces welded in accordance with the new pWPS.

3.1.3 The WPS is to be used as a basis for the production welds, and upon satisfactory completion of the tests based on the pWPS, the Society may approve it as a WPS. In case that a WPS is approved by the Society the approval range is to be in compliance with section 5.

## 4. Qualification of welding procedures

### 4.1 General

4.1.1 Preparation and welding of test pieces are to be carried out in accordance with the pWPS and under the general condition of production welding which it represents.

4.1.2 Welding of the test assemblies and testing of test specimens are to be witnessed by the Surveyor.

4.1.3 If tack welds and/or start and stop points are a condition of the weld process they are to be fused into the joint and are to be included in the test assemblies.

### 4.2 Butt weld

#### 4.2.1 Assembly of test pieces

The test assembly is to be of a size sufficient to ensure a reasonable heat distribution and according to Fig. 1 with the minimum dimensions:

- **manual or semi-automatic welding:**
  - width = 2a, a = 3 x t, min 150 mm
  - length b = 6 x t, min 350 mm

- **automatic welding:**
  - width = 2a, a = 4 x t, min 200 mm
  - length b = 1000 mm

---

![Figure 1: Test assembly for butt weld](Diagram showing a butt weld test assembly. Two plates of width 'a' are joined with a weld of length 'b'. The rolling direction of the plates is indicated. For CVN-L plates, the weld is perpendicular to the rolling direction. For CVN-T plates, it is parallel. 50mm discard zones are shown at both ends of the weld.)

**Fig.1 Test assembly for butt weld**

For hull structural steel plates impact tested in the longitudinal direction (CVN-L) in UR W11, the butt weld of the test piece is perpendicular to the rolling direction of the two plates.

For high strength quenched and tempered steel plates impact tested in the transverse direction (CVN-T) in UR W16, the butt weld of the test piece is parallel to the rolling direction of the two plates.

#### 4.2.2 Examinations and tests

Test assemblies are to be examined non-destructively and destructively in accordance with the following and Fig 2:

- Visual testing: 100 %
- Surface crack detection: 100 % (dye penetrant testing or magnetic particle testing)
- Radiographic or Ultrasonic testing: 100 %
- Transverse tensile test: two specimens as per 4.2.2.2
- Longitudinal tensile test: required as per 4.2.2.3
- Transverse bend test: four specimens as per 4.2.2.4
- Charpy V-notch impact test: required as per 4.2.2.5
- Macro examination: one specimen as per 4.2.2.6
- Hardness test: required as per 4.2.2.7

---

![Figure 2: Test sampling](Diagram of a butt weld test assembly showing the locations for specimen extraction. From top to bottom: Discard zone (50mm), Transverse tensile test (T1), Face bend test (P1), Root bend test (P2), Longitudinal tensile test, Macro examination & Hardness test (M), Charpy V-notch impact tests (notches in weld metal, fusion line, and HAZ), Face bend test (P3), Root bend test (P4), Transverse tensile test (T2), and Discard zone (50mm).)

**Fig.2 Test sampling**

---

##### 4.2.2.1 Non-destructive testing

Test assemblies are to be examined by visual and by non-destructive testing prior to the cutting of test specimen. In case that any post-weld heat treatment is required or specified, non-destructive testing is to be performed after heat treatment. For steels according to UR W16 with specified minimum yield strength of 420 N/mm² and above the non-destructive testing is to be delayed for a minimum of 48 hrs, unless heat treatment has been carried out. NDT procedures are to be agreed with the Society.

Imperfections detected by visual or non-destructive testing are to be assessed in accordance with ISO 5817, class B, except for excess weld metal and excess of penetration for which the level C applies.

##### 4.2.2.2 Transverse tensile test

The testing is to be carried out in accordance with UR W2.4. The tensile strength recorded for each specimen is not to be less than the minimum required for the base metal.

When butt welds are made between plates of different grades, the tensile strength to be obtained on the welded assembly is to be in accordance with the requirements relating to the steel grade having lower strength.

##### 4.2.2.3 Longitudinal tensile test

Longitudinal tensile test of deposited weld metal taken lengthways from the weld is required for cases where the welding consumable is not approved by the Society.

The testing is to be carried out in accordance with UR W2.4. The tensile properties recorded for each specimen are not to be less than the minimum required for the approval of the appropriate grade of consumable.

Where more than one welding process or type of consumable has been used to make the test weld, test specimens are to be taken from the area of the weld where each was used with the exception of those processes or consumables used to make the first weld run or root deposit.

##### 4.2.2.4 Bend test

Transverse bend tests for butt joints are to be in accordance with UR W2.6.

The mandrel diameter to thickness ratio (i.e. D/t) is to be that specified for the welding consumable (UR W17, UR W23) approvals + 1.

The bending angle is to be 180°. After testing, the test specimens are not to reveal any open defects in any direction greater than 3 mm. Defects appearing at the corners of a test specimen during testing are to be investigated case by case.

Two root and two face bend specimens are to be tested. For thickness 12 mm and over, four side bend specimens may alternatively be tested.

For butt joints in heterogeneous steel plates, face and root longitudinal bend test specimens may be used instead of the transverse bend test specimens.

---

##### 4.2.2.5 Impact test

a) Normal and higher strength hull structural steels according to UR W11

The positions of specimens are to be in accordance with these requirements. Dimensions and testing are to be in accordance with the requirements of UR W2.7.

Test specimen with Charpy-V-notch are to be used and sampled from 1 to 2 mm below the surface of the base metal, transverse to the weld and on the side containing the last weld run.

V-notch specimens are located in the butt-welded joint as indicated in Fig. 1 and 2 of Annex A and the V-notch is to be cut perpendicular to the surface of the weld.

Test temperature and absorbed energy are to be in accordance with Table 1.

**Table 1 Impact test requirements for butt joints (t ≤ 50 mm)<sup>(1),(2)</sup>**

| Grade of steel | Testing Temperature (C°) | Value of minimum average absorbed energy (J) | |
| :--- | :---: | :---: | :---: |
| | | **For manually or semi-automatically welded joints** | **For automatically welded joints** |
| | | **Downhand, Horizontal, Overhead** | **Vertical upward, Vertical downward** | |
| A<sup>(3)</sup> | 20 | | | |
| B<sup>(3)</sup>, D | 0 | | | |
| E | -20 | 47 | 34 | 34 |
| A32, A36 | 20 | | | |
| D32, D36 | 0 | | | |
| E32, E36 | -20 | | | |
| F32, F36 | -40 | | | |
| A40 | 20 | | 39 | 39 |
| D40 | 0 | | | |
| E40 | -20 | | | |
| F40 | -40 | | | |

**Note:**
(1) For thickness above 50 mm impact test requirements are to be agreed by the Society.
(2) These requirements are to apply to test piece of which butt weld is perpendicular to the rolling direction of the plates.
(3) For Grade A and B steels average absorbed energy on fusion line and in heat affected zone is to be minimum 27 J.

When butt welds are made between different steel grades/types, the test specimens are to be taken from the side of the joint with lower toughness of steel. Temperature and absorbed energy results are to be in accordance with the requirements for the lower toughness steel.

Where more than one welding process or consumable has been used to make the test weld, impact test specimens are to be taken from the respective areas where each was employed. This is not to apply to the process or consumables used solely to make the first weld run or root deposit.

---

The testing of sub - size specimen is to be in accordance with UR W2.7.2

b) High strength quenched and tempered steels according to UR W16

Impact test is to be performed as described in the above a).

V-notch specimens are located in the butt welded joint as indicated in Fig. 1 and 2 of Annex A and the V-notch is to be cut perpendicular to the surface of the weld.

Test temperature and absorbed energy are to be in accordance with the requirements of base metal as specified in UR W16.

c) Weldable C and C-Mn hull steel castings and forgings according to UR W7 and UR W8

For base metal with specified impact values test temperature and absorbed energy are to be in accordance with the requirements of the base metal to be welded.

##### 4.2.2.6 Macro examination

The test specimens are to be prepared and etched on one side to clearly reveal the weld metal, the fusion line and the heat affected zone.

Macro examination is to include about 10 mm unaffected base metal.

The examination is to reveal a regular weld profile, through fusion between adjacent layers of weld and base metal and the absence of defects such as cracks, lack of fusion etc.

##### 4.2.2.7 Hardness test

Hardness test is required for steels with specified minimum yield strength of R<sub>eH</sub> ≥ 355 N/mm². The Vickers method HV 10 is normally to be used. The indentations are to be made in the weld metal, the heat affected zone and the base metal measuring and recording the hardness values. At least two rows of indentations are to be carried out in accordance with Fig. 1 and 2 of Annex B.

For each row of indentations there is to be a minimum of 3 individual indentations in the weld metal, the heat affected zones (both sides) and the base metal (both sides). A typical example is shown in Annex B.

The results from the hardness test are not to exceed the following:
- Steel with a specified minimum yield strength R<sub>eH</sub> ≤ 420 N/mm² ; 350 HV10
- Steel with a specified minimum yield strength 420 N/mm² < R<sub>eH</sub> ≤ 690 N/mm² ; 420 HV10

### 4.3 Fillet welds

#### 4.3.1 Assembly of test pieces

The test assembly is to be of a size sufficient to ensure a reasonable heat distribution and according to Fig. 3 with the minimum dimensions:

- **manual and semi-automatic welding:**
  - width a = 3 x t, min. 150 mm
  - length b = 6 x t, min. 350 mm

---

- **automatic welding:**
  - width a = 3 x t, min. 150 mm
  - length b = 1000 mm

![Figure 3: Test assembly for fillet weld](Diagram showing a T-joint fillet weld test assembly. Plate thicknesses t1 and t2 are indicated. The vertical plate is joined to the horizontal plate with a fillet weld. Dimensions 'a' (width) and 'b' (length) are shown.)

**Fig.3 Test assembly for fillet weld**

#### 4.3.2 Welding of test pieces

The test assembly is welded on one side only. For single run manual and semi-automatic welding, a stop/restart is to be included in the test length and its position is to be clearly marked for subsequent examination.

#### 4.3.3 Examinations and tests

Test assemblies are to be examined non-destructively and destructively in accordance with the following:

- Visual testing: 100 %
- Surface crack detection: 100 % (dye penetrant testing or magnetic particle testing)
- Macro examination: two specimen as per 4.3.3.2
- Hardness test: required as per 4.3.3.3
- Fracture test: required as per 4.3.3.4

---

##### 4.3.3.1 Non-destructive testing

Test assemblies are to be examined by visual and by non-destructive testing prior to the cutting of test specimen. In case that any post-weld heat treatment is required or specified, non-destructive testing is to be performed after heat treatment. For steels according to UR W16 with specified minimum yield strength of 420 N/mm² and above the non-destructive testing is to be delayed for a minimum of 48 hrs, unless heat treatment has been carried out. NDT procedures are to be agreed with the Society.

Imperfections detected by visual or non-destructive testing are to be assessed in accordance with ISO 5817, class B except for excess convexity and excess throat thickness for which the level C applies.

##### 4.3.3.2 Macro examination

The test specimens are to be prepared and etched on one side to clearly reveal the weld metal, fusion line, root penetration and the heat affected zone.

Macro examination is to include about 10 mm unaffected base metal.

The examination is to reveal a regular weld profile, through fusion between adjacent layers of weld and base metal, sufficient root penetration and the absence of defects such as cracks, lack of fusion etc.

##### 4.3.3.3 Hardness test

Hardness test is required for steels with specified minimum yield strength of R<sub>eH</sub> ≥ 355 N/mm². The Vickers method HV 10 is normally to be used. The indentations are to be made in the weld metal, the heat affected zone and the base metal measuring and recording the hardness values. At least two rows of indentations are to be carried out in accordance with Fig. 3, 4a and 4b of Annex B.

For each row of indentations there is to be a minimum of 3 individual indentations in the weld metal, the heat affected zone (both sides) and the base metal (both sides). A typical example is shown in Annex B.

The results from the hardness test are not to exceed the following:
- Steel with a specified minimum yield strength R<sub>eH</sub> ≤ 420 N/mm² ; 350 HV10
- Steel with a specified minimum yield strength 420 N/mm² < R<sub>eH</sub> ≤ 690 N/mm² ; 420 HV10

##### 4.3.3.4 Fracture test

The fracture test is to be performed by folding the upright plate onto the through plate. Evaluation is to concentrate on cracks, porosity and pores, inclusions, lack of fusion and incomplete penetration. Imperfection that are detected is to be assessed in accordance with ISO 5817, class B.

### 4.4 Re-testing

4.4.1 If the test piece fails to comply with any of the requirements for visual or non-destructive testing one further test piece is to be welded and subjected to the same examination. If this additional test piece does not comply with the relevant requirements, the pWPS is to be regarded as not capable of complying with the requirements without modification.

---

4.4.2 If any test specimens fail to comply with the relevant requirements for destructive testing due to weld imperfections only, two further test specimens are to be obtained for each one that failed. These specimens can be taken from the same test piece if there is sufficient material available or from a new test piece, and are to be subjected to the same test. If either of these additional test specimens does not comply with the relevant requirements, the pWPS is to be regarded as not capable of complying with the requirements without modification.

4.4.3 If a tensile test specimen fails to meet the requirements, the re-testing is to be in accordance with UR W 2.4.3.

4.4.4 If there is a single hardness value above the maximum values allowed, additional hardness tests are to be carried out (on the reverse of the specimen or after sufficient grinding of the tested surface). None of the additional hardness values is to exceed the maximum hardness values required.

4.4.5 The re-testing of Charpy impact specimens are to be carried out in accordance with UR W 2.7.4.

4.4.6 Where there is insufficient welded assembly remaining to provide additional test specimens, a further assembly is to be welded using the same procedure to provide the additional specimens.

### 4.5 Test record

4.5.1 Welding conditions for test assemblies and test results are to be recorded in welding procedure test record. Forms of welding procedure test records can be taken from the Society's rules or from relevant standards.

4.5.2 A statement of the results of assessing each test piece, including repeat tests, is to be made for each welding procedure test. The relevant items listed for the WPS of these requirements are to be included.

4.5.3 A statement that the test piece was made according to the particular welding procedure is to be signed by the Surveyor witnessing the test and is to include the Society´s identification.

## 5. Range of approval

### 5.1 General

5.1.1 All the conditions of validity stated below are to be met independently of each other.

5.1.2 Changes outside of the ranges specified are to require a new welding procedure test.

5.1.3 Shop primers may have an influence on the quality of fillet welds and is to be considered. Welding procedure qualification with shop primer will qualify those without but not vice versa.

### 5.2 Base metal

5.2.1 Normal and higher strength hull structural steels according to UR W11

a) For each strength level, welding procedures are considered applicable to the same and lower toughness grades as that tested.

---

b) For each toughness grade, welding procedures are considered applicable to the same and two lower strength levels as that tested.

c) For applying the above a) and b) to high heat input processes above 50kJ/cm, e.g. the two-run technique with either submerged arc or gas shielded metal arc welding, electro slag and electro gas welding, welding procedure is applicable to that toughness grade tested and one strength level below.

Where steels used for construction are supplied from different delivery conditions from those tested the Society may require additional tests.

5.2.2 High strength quenched and tempered steels according to UR W16

a) For each strength level, welding procedures are considered applicable to the same and lower toughness grades as that tested.

b) For each toughness grade, welding procedures are considered applicable to the same and one lower strength level as that tested.

c) The approval of quenched and tempered steels does not quality thermo-mechanically rolled steels (TMCP steels) and vice versa.

5.2.3 Weldable C and C-Mn hull steel forgings according to UR W7

a) Welding procedures are considered applicable to the same and lower strength level as that tested.

b) The approval of quenched and tempered hull steel forgings does not quality other delivery conditions and vice versa.

5.2.4 Weldable C and C-Mn hull steel castings according to UR W8

a) Welding procedures are considered applicable to the same and lower strength level as that tested.

b) The approval of quenched and tempered hull steel castings does not quality other delivery conditions and vice versa.

### 5.3 Thickness

5.3.1 The qualification of a WPS carried out on a test assembly of thickness t is valid for the thickness range given in Table 2.

**Table 2 Approval range of thickness for butt and T-joint welds and fillet welds**

| Thickness of test piece T<sup>(1)</sup> (mm) | Range of approval | |
| :--- | :--- | :--- |
| | **Butt and T-joint welds with single run or single run from both sides** | **Butt and T-joint welds with multi-run and fillet welds<sup>(2)</sup>** |
| 3 < t ≤ 12 | 0.7 x t to 1.1 x t | 3 to 2 x t |
| 12 < t ≤ 100 | 0.7 x t to 1.1 x t<sup>(3)</sup> | 0.5 x t to 2 x t (Max. 150) |

---

**Note:**

(1) For multi process procedures, the recorded thickness contribution of each process is to be used as a basis for the range of approval for the individual welding process.

(2) For fillet welds, the range of approval is to be applied to both base metals.

(3) For high heat input processes over 50kJ/cm, the upper limit of range of approval is to be 1.0 x t.

5.3.2 In addition to the requirements of Table 2, the range of approval of throat thickness "a" for fillet welds is to be as follows:

- Single run ; "0.75 x a" to "1.5 x a"
- Multi-run ; as for butt welds with multi-run (i.e. a=t)

5.3.3 For the vertical-down welding, the test piece thickness "t" is always taken as the upper limit of the range of application.

5.3.4 For unequal plate thickness of butt welds the lesser thickness is ruling dimension.

5.3.5 Notwithstanding the above, the approval of maximum thickness of base metal for any technique is to be restricted to the thickness of test assembly if three of the hardness values in the heat affected zone are found to be within 25 HV of the maximum permitted, as stated 4.2.2.7 and 4.3.3.3.

### 5.4 Welding position

Approval for a test made in any position is restricted to that position (see Annex C). To qualify a range of positions, test assemblies are to be welded for highest heat input position and lowest heat input position and all applicable tests are to be made on those assemblies.

### 5.5 Welding process

5.5.1 The approval is only valid for the welding process(es) used in the welding procedure test. It is not permitted to change from a multi-run to a single run.

5.5.2 For multi-process procedures the welding procedure approval may be carried out with separate welding procedure tests for each welding process. It is also possible to make the welding procedure test as a multi-process procedure test. The approval of such a test is only valid for the process sequence carried out during the multi-process procedure test.

### 5.6 Welding consumable

Except high heat input processes over 50kJ/cm, welding consumables cover other approved welding consumables having the same grade mark including all suffixes specified in UR W17 and UR W23 with the welding consumable tested.

### 5.7 Heat input

5.7.1 The upper limit of heat input approved is 25% greater than that used in welding the test piece or 55kJ/cm whichever is smaller, except that the upper limit is 10% greater than that for high heat input processes over 50kJ/cm.

---

5.7.2 The lower limit of heat input approved is 25% lower than that used in welding the test piece.

### 5.8 Preheating and interpass temperature

5.8.1 The minimum preheating temperature is not to be less than that used in the qualification test.

5.8.2 The maximum interpass temperature is not to be higher than that used in the qualification test.

### 5.9 Post-weld heat treatment

The heat treatment used in the qualification test is to be maintained during manufacture. Holding time may be adjusted as a function of thickness.

### 5.10 Type of joint

5.10.1 Range of approval depending on type of welded joints for test assembly is to be specified in Table 3.

5.10.2 A qualification test performed on a butt weld will also qualify for fillet welding within the thickness ranges specified for fillet welds specified in 5.3 above.

**Table 3 Range of approval for type of welded joint**

| Type of welded joint for test assembly | | Range of approval |
| :--- | :--- | :--- |
| Butt welding | One side | With backing (A) | A, C |
| | | Without backing (B) | A, B, C, D |
| | Both side | With gouging (C) | C |
| | | Without gouging (D) | C, D |

### 5.11 Other variables

The range of approval relating to other variables may be taken according to the Society requirements.

---

## Annex A: Location of Charpy V-notch impact test

---

![Figure 1 (Annex A): Locations of V-notch for butt weld of normal heat input](Diagram showing notch locations for butt welds with heat input ≤ 50 kJ/cm. Case a) t ≤ 50mm shows single-V and double-V preparations with notch locations 'a' (center of weld), 'b' (fusion line), and 'c' (HAZ, 2mm from fusion line). Case b) t > 50mm shows similar locations with added root-side notch for one-side welding.)

**Fig. 1 Locations of V-notch for butt weld of normal heat input (heat input ≤ 50 kJ/cm)**

**a) t≤50mm<sup>(1)</sup>**

**Note:**
(1) For one side single run welding over 20mm notch location "a" is to be added on root side.

**b) t>50mm**

**Notch locations:**
a : center of weld "WM"
b : on fusion line "FL"
c : in HAZ, 2mm from fusion line

---

![Figure 2 (Annex A): Locations of V-notch for butt weld of high heat input](Diagram showing notch locations for butt welds with heat input > 50 kJ/cm. Case a) t ≤ 50mm and Case b) t > 50mm. Notch locations 'a' (center of weld), 'b' (fusion line), 'c' (HAZ, 2mm from fusion line), 'd' (HAZ, 5mm from fusion line), and 'e' (HAZ, 10mm from fusion line for heat input > 200 kJ/cm) are indicated.)

**Fig. 2 Locations of V-notch for butt weld of high heat input (heat input > 50kJ/cm)**

**a) t≤50mm<sup>(1)</sup>**

**Note:**
(1) For one side welding with thickness over 20mm notch locations "a", "b" and "c" are to be added on root side.

**b) t>50mm**

**Notch locations:**
a : center of weld "WM"
b : on fusion line "FL"
c : in HAZ, 2mm from fusion line
d : in HAZ, 5mm from fusion line
e : in HAZ, 10mm from fusion line in case of heat input > 200kJ/cm

---

## Annex B: Hardness test

(Typical examples of hardness test)

---

![Figure 1 (Annex B): Examples of hardness test with rows of indentations (R) in butt welds](Diagram showing the placement of two rows of hardness indentations in single-V and double-V butt welds. Rows are placed 2mm max from the top and bottom surfaces.)

**Fig. 1 Examples of hardness test with rows of indentations (R) in butt welds**

**Table 1 Recommended distances l between indentations for hardness test in the heat affected zone**

| Vickers hardness Symbol | Distance between indentations l (mm) |
| :---: | :---: |
| HV 10 | 1 |

The distance of any indentation from the previous indentation is not to be less than the value allowed for the previous indentation by ISO 6507/1.

---

![Figure 2 (Annex B): Position of indentations in a butt weld](Detailed diagram showing a single row of indentations across the weld metal, fusion line, and heat affected zone of a butt weld. Indentations are spaced 'l' apart. The first indentation in the HAZ is ≤ 0.5mm from the fusion line.)

**Fig. 2 Example showing the position of the indentations for hardness test in the weld metal, the heat affected zone and the base metal of a butt weld (dimensions in mm)**

---

![Figure 3 (Annex B): Hardness test rows in fillet and T-joint welds](Diagram showing the placement of two rows of hardness indentations in fillet welds and T-joint welds. Rows are placed 2mm max from the surfaces and across the fusion lines.)

**Fig. 3 Examples of hardness test with row indentation (R) in fillet welds and in T-joint welds**

![Figure 4a (Annex B): Position of indentations in a fillet weld](Detailed diagram showing indentations in a fillet weld. Rows of indentations cross the fusion line into the HAZ and base metal. Distances 'h' from the fusion line and spacing 'l' are indicated.)

**Fig. 4a Example showing the position of the indentations for hardness test in the weld metal, the heat affected zone and the base metal of a fillet weld (dimensions in mm)**

---

![Figure 4b (Annex B): Position of indentations in a T-joint weld](Detailed diagram showing indentations in a T-joint weld. Similar to 4a, showing rows of indentations across the weld metal, fusion zones, and HAZ.)

**Fig. 4b Example showing the position of the indentations for hardness test on the weld metal, the heat affect zone and the base metal of a T-joint weld (dimensions in mm)**

---

## Annex C: Welding positions

---

### Annex C.1: Welding positions according to ISO Standard

![Figure: ISO Welding Positions](Diagram showing various welding positions according to ISO: a) Butt welds for plates (PA Flat, PC Horizontal Vertical, PG Vertical downwards, PF Vertical upwards, PO Overhand) and b) Fillet welds for plates (PA Flat, PC Horizontal Vertical, PG Vertical downwards, PF Vertical upwards, PO Overhand).)

---

### Annex C.2: Welding positions according to AWS-Code

**a) Butt weld for plates**

![Figure: AWS Butt Weld Positions](Diagram showing AWS butt weld positions: (A) TEST POSITION 1G (Flat), (B) TEST POSITION 2G (Horizontal), (C) TEST POSITION 3G (Vertical), (D) TEST POSITION 4G (Overhead).)

---

**b) Fillet welds for plates**

![Figure: AWS Fillet Weld Positions](Diagram showing AWS fillet weld positions: (A) FLAT POSITION 1F, (B) HORIZONTAL POSITION 2F, (C) VERTICAL POSITION 3F, (D) OVERHEAD POSITION 4F. Notes indicate plate orientation requirements.)

**End of Document**


================================================================================
# FILE: UR_W/ur-w29.md
================================================================================

# W29 Requirements for manufacture of anchors

(June 2005)

## 1. General requirements

### 1.1 Scope

These Rules apply to the materials, manufacture and testing, and certification of anchors, shanks and anchor shackles produced from cast or forged steel, or fabricated by welded rolled steel plate and bars. Frequent reference is made to UR A1.

With regard to holding power tests at sea for high holding power (HHP) and super high holding power (SHHP) anchors, refer to UR A1.

### 1.2 Types of anchor

The types of anchor covered include:

a) Ordinary anchors. Refer to UR A1.4.1.1
   i) Stockless anchors
   ii) Stocked anchors
b) HHP anchors. Refer to UR A1.4.1.2
c) SHHP anchors, not exceeding 1500kg in mass. Refer to UR A1.4.1.3

Any changes to the design made during manufacture are to have prior written agreement from the Classification Society.

## 2. Materials

### 2.1 Materials for anchors

All anchors are to be manufactured from materials meeting the requirements of the UR Ws as indicated below:

a) Cast steel anchor flukes, shanks, swivels and shackles are to be manufactured and tested in accordance with the requirements of UR W8 and comply with the requirements for castings for welded construction. The steel is to be fine grain treated with Aluminium. If test programme B is selected in Section 4.2 then Charpy V notch (CVN) impact testing of cast material is required. Special consideration is to be given to the use of other grades of steels for the manufacture of swivels.

b) Forged steel anchor pins, shanks, swivels and shackles are to be manufactured and tested in accordance with the requirements of UR W7. Shanks, swivels and shackles are to comply with the requirements for carbon and carbon-manganese steels for welded construction. Special consideration is to be given to the use of other grades of steels for the manufacture of swivels.

c) Rolled billets, plate and bar for fabricated steel anchors are to be manufactured and tested in accordance with the requirements of UR W11.

d) Rolled bar intended for pins, swivels and shackles are to be manufactured and tested in accordance with the requirements of UR W7 or UR W11.

### 2.2 Materials for SHHP anchors

In addition to the requirements of 2.1 above, SHHP anchors are to be produced in accordance with the material toughness requirements of UR A1.4.4.

## 3. Manufacture of anchors

### 3.1 Tolerance

If not otherwise specified on standards or on drawings demonstrated to be appropriate, the following assembly and fitting tolerance are to be applied.

The clearance either side of the shank within the shackle jaws is to be no more than 3mm for small anchors up to 3 tonnes weight, 4mm for anchors up to 5 tonnes weight, 6mm for anchors up to 7 tonnes weight and is not to exceed 12 mm for larger anchors.

The shackle pin is to be a push fit in the eyes of the shackle, which are to be chamfered on the outside to ensure a good tightness when the pin is clenched over on fitting. The shackle pin to hole tolerance is to be no more than 0.5mm for pins up to 57mm and 1.0mm for pins of larger diameter.

The trunnion pin is to be a snug fit within the chamber and be long enough to prevent horizontal movement. The gap is to be no more than 1% of the chamber length.

The lateral movement of the shank is not to exceed 3 degrees, see Figure 1.

![Figure 1: Allowable lateral movement of shank](The diagram shows a cross-section of an anchor head assembly where the shank is pivoted. A vertical dashed center line is shown, and a second dashed line represents the maximum tilt of the shank. The angle between these two lines is marked as 3°, indicating the maximum allowable lateral movement.)

### 3.2 Welding of anchors

Welded construction of fabricated anchors is to be done in accordance with procedures approved by the Classification Society. Welding is to be carried out by qualified welders, following the approved welding procedures qualified in accordance with UR W28, using consumables manufactured in accordance with the requirements of UR W17. NDE is to be carried in accordance with the requirements of 4.2 Product tests.

### 3.3 Heat treatment

Components for cast or forged anchors are to properly heat treated; fully annealed; normalised or normalised and tempered in accordance with UR W7 and UR W8.

Fabricated anchors may require stress relief after welding depending upon weld thickness. Stress relief is to be carried out as indicated in the approved welding procedure. Stress relief temperatures are not to exceed the tempering temperature of the base material.

### 3.4 Freedom from defects

All parts are to have a clean surface consistent with the method of manufacture and be free from cracks, notches, inclusions and other defects that would impair the performance of the product.

### 3.5 Repairs

Any necessary repairs to forged and cast anchors are to be agreed by the Surveyor and carried out in accordance with the repair criteria indicated in UR W7 and UR W8. Repairs to fabricated anchors are to be agreed by the Surveyor and carried out in accordance with qualified weld procedures, by qualified welders, following the parameters of the welding procedures used in construction.

### 3.6 Anchor assembly

Assembly and fitting are to be done in accordance with the design details.

Securing of the anchor pin, shackle pin or swivel nut by welding is to be done in accordance with an approved procedure.

## 4. Testing and certification

### 4.1 Proof load test

Proof load tests are to be carried out by an approved testing facility.

Proof load testing for Ordinary, HHP and SHHP anchors is to be carried out in accordance with the pertinent requirements of UR A1.4.3.

### 4.2 Product tests

#### 4.2.1 Product Test Programmes

The Classification Society can request that either programme A or programme B be applied.

**Table 1: Applicable programmes for each product form**

| Product test | Cast components | Forged components | Fabricated/Welded components |
| :--- | :--- | :--- | :--- |
| Programme A | Applicable | Not applicable | Not applicable |
| Programme B | Applicable (1) | Applicable | Applicable |

Notes : (1) CVN impact tests are to be carried out to demonstrate at least 27 joules average at 0ºC. Refer to 2.1 a).

**Table 2: Product test requirements for programme A and B**

| Programme A | Programme B |
| :--- | :--- |
| Drop test | － |
| Hammering test | － |
| Visual inspection | Visual inspection |
| General NDE | General NDE |
| － | Extended NDE |

#### 4.2.2 Drop test

Each anchor fluke and shank is individually raised to a height of 4m and dropped on to a steel slab without fracturing. The steel slab is to be suitable to resist the impact of the dropped component.

#### 4.2.3 Hammering test

After the drop test, hammering tests are carried out on each anchor fluke and shank, which is slung clear of the ground, using a non-metallic sling, and hammered to check the soundness of the component. A hammer of at least 3kg mass is to be used.

#### 4.2.4 Visual inspection

After proof loading visual inspection of all accessible surfaces is to be carried out.

#### 4.2.5 General non-destructive examination

After proof loading general NDE is to be carried out as indicated in the following Tables 3 and 4.

**Table 3: General NDE for Ordinary and HHP anchors**

| Location | Method of NDE |
| :--- | :--- |
| Feeders of castings | PT or MT |
| Risers of castings | PT or MT |
| Weld repairs | PT or MT |
| Forged components | Not required |
| Fabrication welds | PT or MT |

**Table 4: General NDE for SHHP anchors**

| Location | Method of NDE |
| :--- | :--- |
| Feeders of castings | PT or MT and UT |
| Risers of castings | PT or MT and UT |
| All surfaces of castings | PT or MT |
| Weld repairs | PT or MT |
| Forged components | Not required |
| Fabrication welds | PT or MT |

IACS Recommendation No. 69 "Guidelines for non-destructive examination of marine steel castings" is regarded as an example of an acceptable standard for surface and volumetric examination.

#### 4.2.6 Extended non-destructive examination

After proof loading general NDE is to be carried out as indicated in the following Table 5.

**Table 5: Extended NDE for Ordinary, HHP and SHHP anchors**

| Location | Method of NDE |
| :--- | :--- |
| Feeders of castings | PT or MT and UT |
| Risers of castings | PT or MT and UT |
| All surfaces of castings | PT or MT |
| Random areas of castings | UT |
| Weld repairs | PT or MT |
| Forged components | Not required |
| Fabrication welds | PT or MT |

IACS Recommendation No. 69 "Guidelines for non-destructive examination of marine steel castings" is regarded as an example of an acceptable standard for surface and volumetric examination.

#### 4.2.7 Repair criteria

If defects are detected by NDE, repairs are to be carried out in accordance with 3.5. For fracture and unsoundness detected in a drop test or hammering test, repairs are not permitted and the component is to be rejected.

### 4.3 Mass and dimensional inspection

Unless otherwise agreed, the verification of mass and dimensions is the responsibility of the manufacturer. The Surveyor is only required to monitor this inspection. The mass of the anchor is to exclude the mass of the swivel, unless this is an integral component.

### 4.4 Retests

Mechanical retest are permitted in accordance with the requirements of UR W2.

### 4.5 Marking

Anchors which meet the requirements are to be stamped on the shank and the fluke. The markings on the shank are to be approximately level with the fluke tips. On the fluke, these markings are to be approximately at a distance of two thirds from the tip of the bill to the center line of the crown on the right hand fluke looking from the crown towards the shank. The markings are to include:

- Mass of anchor
- Identification, e.g. test No. or certificate No.
- Society's stamp
- Manufacturer's mark

Additionally the unique cast identification is to be cast on the shank and the fluke.

### 4.6 Certification

Anchors which meet the requirements are to be certified by the Society at least with the following items:

- Manufacturer's name
- Type
- Mass
- Fluke and Shank identification numbers
- Grade of materials
- Proof test loads
- Heat treatment
- Marking applied to anchor

### 4.7 Painting

All types of anchor are not to be painted until all tests and inspections have been completed.

**END**


================================================================================
# FILE: UR_W/ur-w30del.md
================================================================================

# W30 Normal and higher strength corrosion resistant steels for cargo oil tanks

(Feb 2013)

Deleted 1 July 2015, replaced by UR W11.

***

**Page 1 of 1**
**IACS Req. 2013**

**End of Document**

================================================================================
# FILE: UR_W/ur-w31rev3.md
================================================================================

# W31 YP47 Steels and Brittle Crack Arrest Steels

**W31**
(Jan 2013)
(Rev.1 Sept 2015)
(Rev.2 Dec 2019 Complete Revision)
(Rev.3 Mar 2023)

## 1. Scope

### 1.1 General

1.1.1 This UR defines the requirements on YP47 steels and brittle crack arrest steels as required by UR S33.

1.1.2 Unless otherwise specified in this UR, UR W11 is to be followed.

### 1.2 YP47 steels

1.2.1 Steels designated as YP47 refer to steels with a specified minimum yield point of 460 N/mm².

1.2.2 The YP47 steels can be applied to longitudinal structural members in the upper deck region of container carriers (such as hatch side coaming, hatch coaming top and the attached longitudinals, etc.). Special consideration is to be given to the application of YP47 steels for other hull structures.

1.2.3 This UR gives the requirements for YP47 steels in thickness greater than 50mm and not greater than 100mm intended for the upper deck region of container carriers. For YP47 steels outside scope of the said thickness range, special consideration is to be given by the Classification Society.

**Notes:**

1. This UR is to be applied by IACS Societies on ships contracted for construction on or after 1 January 2014.
2. Revision 1 of this UR is to be applied by IACS Societies to ships contracted for construction on or after 1 January 2017.
3. The “contracted for construction” date means the date on which the contract to build the vessel is signed between the prospective owner and the shipbuilder. For further details regarding the date of “contract for construction”, refer to IACS Procedural Requirement (PR) No. 29.
4. Revision 2 of this UR is to be uniformly implemented by IACS Societies on ships contracted for construction on or after 01 January 2021.
5. Revision 3 of this UR is to be uniformly implemented by IACS Societies when the application for certification of manufacturer approval is dated on or after 01 July 2024.

---

### 1.3 Brittle crack arrest steels

1.3.1 The brittle crack designation can be assigned to YP36 and YP40 steels specified in UR W11 and YP47 steels specified in this UR, which meet the additional brittle crack arrest requirements and properties defined in this UR.

1.3.2 The application of brittle crack arrest steels is to comply with UR S33, which covers longitudinal structural members in the upper deck region of container carriers (such as hatch side coaming, upper deck, hatch coaming top and the attached longitudinals, etc.).

1.3.3 The thickness range of brittle crack arrest steels is over 50mm and not greater than 100mm as specified in Table 3 of this UR.

## 2 Material specifications

### 2.1 YP47 steels

Material specifications for YP47 steels are specified in Table 1 and Table 2.

**Table 1: Chemical composition and deoxidation practice for YP47 steels without specified brittle crack arrest properties**

| Grade | EH47 |
| :--- | :--- |
| **Deoxidation Practice** | Killed and fine grain treated |
| **Chemical Composition % (ladle samples)<sup>(6)(7)</sup>** | |
| C max. | 0.18 |
| Mn | 0.90 – 2.00 |
| Si max. | 0.55 |
| P max. | 0.020 |
| S max. | 0.020 |
| Al (acid soluble min) | 0.015<sup>(1)(2)</sup> |
| Nb | 0.02 – 0.05<sup>(2)(3)</sup> |
| V | 0.05 – 0.10<sup>(2)(3)</sup> |
| Ti max. | 0.02<sup>(3)</sup> |
| Cu max. | 0.35 |
| Cr max. | 0.25 |
| Ni max. | 1.0 |
| Mo max. | 0.08 |
| Ceq max.<sup>(4)</sup> | 0.49 |
| Pcm max.<sup>(5)</sup> | 0.22 |

**Notes:**

1. The total aluminium content may be determined instead of the acid soluble content. In such cases the total aluminium content is to be not less than 0.020%.
2. The steel is to contain aluminium, niobium, vanadium or other suitable grain refining elements, either singly or in any combination. When used singly the steel is to contain the specified minimum content of the grain refining element. When used in combination, the specified minimum content of a fine graining element is not applicable.
3. The total niobium, vanadium and titanium content is not to exceed 0.12%.
4. The carbon equivalent $C_{eq}$ value is to be calculated from the ladle analysis using the following formula:
   $C_{eq} = C + \frac{Mn}{6} + \frac{Cr + Mo + V}{5} + \frac{Ni + Cu}{15}$ (%)
5. Cold cracking susceptibility $P_{cm}$ value is to be calculated using the following formula:
   $P_{cm} = C + \frac{Si}{30} + \frac{Mn}{20} + \frac{Cu}{20} + \frac{Ni}{60} + \frac{Cr}{20} + \frac{Mo}{15} + \frac{V}{10} + 5B$ (%)
6. Where additions of any other element have been made as part of the steelmaking practice subject to approval by the Classification Society, the content is to be indicated on product inspection certificate.
7. Variations in the specified chemical composition may be allowed subject to approval of Classification Society.

---

**Table 2: Conditions of supply, grade and mechanical properties for YP47 steels without specified brittle crack arrest properties<sup>(1)</sup>**

| Supply condition | Grade | Yield Strength (N/mm²) min. | Tensile Strength (N/mm²) | Elongation (%) min. | Test Temp. (°C) | Average Impact Energy (J) min. | | |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| | | | | | | **50 < t ≤ 70** | **70 < t ≤ 85** | **85 < t ≤ 100** |
| | | | | | | Longitudinal | Longitudinal | Longitudinal |
| TMCP<sup>(2)</sup> | EH47 | 460 | 570 - 720 | 17 | -40 | 53 | 64 | 75 |

**t: thickness (mm)**

**Notes:**

1. The additional requirements for YP47 steel with brittle crack arrest properties is specified in 2.2 of this UR.
2. Other conditions of supply are to be in accordance with the Classification Society’s procedures.

---

### 2.2 Brittle crack arrest steels

2.2.1 Brittle crack arrest steels are defined as steel plate with the specified brittle crack arrest properties measured by either the brittle crack arrest toughness $K_{ca}$ or Crack Arrest Temperature (CAT).

2.2.2 In addition to the required mechanical properties of UR W11 for YP36 and YP40 and Table 2 of this UR for YP47, brittle crack arrest steels are to comply with the requirements specified in Table 3 and Table 4 of this UR.

2.2.3 The brittle crack arrest properties specified in Table 3 are to be evaluated for the products in accordance with the procedure approved by the Classification Society. Test specimens are to be taken from each piece (means “the rolled product from a single slab or ingot if this is rolled directly into plates” as defined in UR W11), unless otherwise agreed by the Classification Society.

**Table 3: Requirement of brittle crack arrest properties for brittle crack arrest steels**

| Suffix to the steel grade<sup>(1)</sup> | Thickness range (mm) | Brittle crack arrest properties<sup>(2)(6)</sup> | |
| :--- | :--- | :--- | :--- |
| | | **Brittle Crack Arrest Toughness $K_{ca}$ at -10 °C (N/mm³/²)<sup>(3)</sup>** | **Crack Arrest Temperature CAT (°C)<sup>(4)</sup>** |
| BCA1 | 50 < t ≤ 100 | 6,000 min. | -10 or below |
| BCA2 | 80 < t ≤ 100<sup>(7)</sup> | 8,000 min. | (5) |

**t: thickness (mm)**

**Notes:**

1. Suffix “BCA1” or “BCA2” is to be affixed to the steel grade designation (e.g. EH40-BCA1, EH47-BCA1, EH47-BCA2, etc.).
2. Brittle crack arrest properties for brittle crack arrest steels are to be verified by either the brittle crack arrest toughness $K_{ca}$ or Crack Arrest Temperature (CAT).
3. $K_{ca}$ value is to be obtained by the brittle crack arrest test specified in Annex 3 of this UR.
4. CAT is to be obtained by the test method specified in Annex 4 of this UR.
5. Criterion of CAT for brittle crack arrest steels corresponding to $K_{ca}=8,000$ N/mm³/² is to be approved by the Classification Society.
6. Where small-scale tests are used for product testing (batch release testing), these test methods are to be approved by the Classification Society in accordance with Annex 5 of this UR.
7. Lower thicknesses may be approved at the discretion of the Classification Society.

---

**Table 4: Chemical composition and deoxidation practice for brittle crack arrest steels**

| Grade | EH36-BCA | EH40-BCA | EH47-BCA |
| :--- | :--- | :--- | :--- |
| **Deoxidation Practice** | | Killed and fine grain treated | |
| **Chemical Composition %<sup>(1)(7)(8)</sup> (ladle samples)** | | | |
| C max. | 0.18 | 0.18 | |
| Mn | 0.90 – 2.00 | 0.90 – 2.00 | |
| Si max. | 0.50 | 0.55 | |
| P max. | 0.020 | 0.020 | |
| S max. | 0.020 | 0.020 | |
| Al (acid soluble min) | 0.015<sup>(2)(3)</sup> | 0.015<sup>(2)(3)</sup> | |
| Nb | 0.02 – 0.05<sup>(3)(4)</sup> | 0.02 – 0.05<sup>(3)(4)</sup> | |
| V | 0.05 – 0.10<sup>(3)(4)</sup> | 0.05 – 0.10<sup>(3)(4)</sup> | |
| Ti max. | 0.02<sup>(4)</sup> | 0.02<sup>(4)</sup> | |
| Cu max. | 0.50 | 0.50 | |
| Cr max. | 0.25 | 0.50 | |
| Ni max. | 2.0 | 2.0 | |
| Mo max. | 0.08 | 0.08 | |
| Ceq max.<sup>(5)</sup> | 0.47 | 0.49 | 0.55 |
| Pcm max.<sup>(6)</sup> | - | - | 0.24 |

**Notes:**

1. Chemical composition of brittle crack arrest steels shall comply with Table 4 of this UR, regardless of chemical composition specified in UR W11 and Table 1 of this UR.
2. The total aluminium content may be determined instead of the acid soluble content. In such cases the total aluminium content is to be not less than 0.020%.
3. The steel is to contain aluminium, niobium, vanadium or other suitable grain refining elements, either singly or in any combination. When used singly the steel is to contain the specified minimum content of the grain refining element. When used in combination, the specified minimum content of a fine graining element is not applicable.
4. The total niobium, vanadium and titanium content is not to exceed 0.12%.
5. The carbon equivalent $C_{eq}$ value is to be calculated from the ladle analysis using the following formula:
   $C_{eq} = C + \frac{Mn}{6} + \frac{Cr + Mo + V}{5} + \frac{Ni + Cu}{15}$ (%)
6. Cold cracking susceptibility $P_{cm}$ value is to be calculated using the following formula:
   $P_{cm} = C + \frac{Si}{30} + \frac{Mn}{20} + \frac{Cu}{20} + \frac{Ni}{60} + \frac{Cr}{20} + \frac{Mo}{15} + \frac{V}{10} + 5B$ (%)
7. Where additions of any other element have been made as part of the steelmaking practice subject to approval by the Classification Society, the content is to be indicated on product inspection certificate.
8. Variations in the specified chemical composition may be allowed subject to approval of Classification Society.

---

## 3 Manufacturing approval scheme

### 3.1 YP47 steels

Manufacturing approval scheme for YP47 steels is to be in accordance with Annex 1 of this UR.

### 3.2 Brittle crack arrest steels

Manufacturing approval scheme for brittle crack arrest steels is to be in accordance with Annex 2 of this UR.

## 4 Welding procedure qualification test

### 4.1 YP47 steels

4.1.1 General
Approval test items, test methods and acceptance criteria not specified in this UR are to be in accordance with the Classification Society’s procedures.

4.1.2 Approval range
UR W28 is to be followed for approval range.

4.1.3 Impact test
UR W28 is to be followed for impact test. 64J at -20°C is to be satisfied.

4.1.4 Hardness
HV10, as defined in UR W28, is to be not more than 350. Measurement points are to include mid-thickness position in addition to the points required by UR W28.

4.1.5 Tensile test
Tensile strength in transverse tensile test is to be not less than 570N/mm².

4.1.6 Brittle fracture initiation test
Deep notch test or CTOD test may be required. Test method and acceptance criteria are to be considered appropriate by the Classification Society.

### 4.2 Brittle crack arrest steels

4.2.1 General
Where Welding Procedure Specification (WPS) for the non-BCA steels has been approved by the Classification Society, the said WPS is applicable to the same welding procedure applied to the same grade with suffix “BCA1” or “BCA2” specified in Table 3 of this UR except high heat input processes over 50kJ/cm.

---

The requirements for welding procedure qualification test for brittle crack arrest steels is to be in accordance with the relevant requirements for each steel grade excluding suffix “BCA1” or “BCA2” specified in Table 3 of this UR, except for 4.2.2 below.

4.2.2 Hardness
For YP47 steels with brittle crack arrest properties, HV10, as defined in UR W28, is to be not more than 380, and measurement points are to include mid-thickness position in addition to the points required by UR W28.

## 5 Production welding

### 5.1 YP47 steels

5.1.1 Welder
Welders engaged in YP47 welding work are to possess welder’s qualifications specified in UR W32.

5.1.2 Short bead
Short bead length for tack and repairs of welds by welding are not to be less than 50mm.
In the case where $P_{cm}$ is less than or equal to 0.19, 25mm of short bead length may be adopted with approval of the Classification Society.

5.1.3 Preheating
Preheating is to be 50°C or over when air temperature is 5°C or below.
In the case where $P_{cm}$ is less than or equal to 0.19 and the air temperature is below 5°C but above 0°C, alternative preheating requirements may be adopted with approval of the Classification Society.

5.1.4 Welding consumables
Approval procedure, approval test items, test methods and acceptance criteria not specified in this UR are to be in accordance with UR W17.
Specifications of welding consumables for YP47 steel plates are to be in accordance with Table 5.

**Table 5: Mechanical properties for deposited metal tests for welding consumables**

| Mechanical Properties | | | Impact test | |
| :--- | :--- | :--- | :--- | :--- |
| **Yield Strength (N/mm²) min.** | **Tensile Strength (N/mm²)** | **Elongation (%) min.** | **Test Temp. (°C)** | **Average Impact Energy (J) min.** |
| 460 | 570 - 720 | 19 | -20 | 64 |

---

Consumables tests for butt weld assemblies are to be in accordance with Table 6.

**Table 6: Mechanical properties for butt weld tests for welding consumables**

| Tensile strength (N/mm²) | Bend test ratio: D/t | Charpy V-notch impact tests | |
| :--- | :--- | :--- | :--- |
| | | **Test temperature (°C)** | **Average absorbed energy (J) min.** |
| 570 - 720 | 4 | - 20 | 64 |

5.1.5 Others
Special care is to be paid to the final welding so that harmful defects do not remain.
Jig mountings are to be completely removed with no defects in general, otherwise the treatment of the mounting is to be accepted by the Classification Society.

### 5.2 Brittle crack arrest steels

Welding work (such as relevant welder’s qualification, short bead, preheating, selection of welding consumables, etc.) for brittle crack arrest steels is to be in accordance with the relevant requirements for each steel grade excluding suffix “BCA1” or “BCA2” specified in Table 3 of this UR.

---

## Annex 1 Manufacturing Approval Scheme for YP47 Steels

### A1.1. Scope

A1.1.1 This Annex specifies, as given in 3.1 of this UR, the manufacturing approval scheme for YP47 steels of grade EH47.

A1.1.2 Unless otherwise specified in this Annex, Appendix A2 of UR W11 is to be followed.

### A1.2. Approval tests

#### A1.2.1 Extent of the approval tests

A1.2.1.1 3.1 (c) and (d), Appendix A2 of UR W11 are not applied to manufacturing approval of YP47 steels.

A1.2.1.2 The products for testing are to represent the maximum thickness for approval. If the target chemical composition changes with the thickness, the maximum thickness for each specified chemical composition specification shall be tested.

#### A1.2.2 Type of tests

A1.2.2.1 Brittle fracture initiation test
Deep notch test or Crack Tip Opening Displacement (CTOD) test is to be carried out. Test method is to be in accordance with the Classification Society’s practice.

A1.2.2.2 Weldability test
(a) Y-groove weld cracking test (Hydrogen crack test)
The test method is to be in accordance with recognized national standards such as ISO 17642-2:2005. Acceptance criteria are to be in accordance with the Classification Society’s practice.

(b) Brittle fracture initiation test
Deep notch test or CTOD test is to be carried out. Test method and results are to be considered appropriate by the Classification Society.

A1.2.2.3 Other tests
In addition to the requirement specified in A1.2.2.1 and A1.2.2.2 above, the approval tests required for steels specified in Appendix A2 of UR W11 are to be carried out. Additional tests may be required when deemed necessary by the Classification Society.

---

## Annex 2 Manufacturing Approval Scheme for Brittle Crack Arrest Steels

### A2.1. Scope

A2.1.1 This Annex specifies, as given in 3.2 of this UR, the manufacturing approval scheme for brittle crack arrest steels.

A2.1.2 Unless otherwise specified in this Annex, Appendix A2 of UR W11 and/or Annex 1 of this UR are to be followed.

### A2.2. Approval Application

#### A2.2.1 Documents to be submitted

The manufacturer is to submit to the Classification Society the following documents together with those required in 2.1, Appendix A2 of UR W11:
a) In-house test reports of the brittle crack arrest properties of the steels intended for approval
b) Approval test program for the brittle crack arrest properties (see A2.3.1 below)
c) Production test procedure for the brittle crack arrest properties.

### A2.3. Approval tests

#### A2.3.1 Extent of the approval tests

A2.3.1.1 The extent of the test program is specified in A2.3.2, A2.3.3 and A2.3.4 of this Annex. If the manufacturing process and mechanism to ensure the brittle crack arrest properties for the steels intended for approval are same, 3.1, Appendix A2 of UR W11 is to be followed for the extent of the approval tests. For YP47 steels with brittle crack arrest properties, 3.1 (c) and (d), Appendix A2 of UR W11 are not applied.

A2.3.1.2 The products for testing are to represent the maximum thickness for approval. If the target chemical composition changes with the thickness, the maximum thickness for each specified chemical composition specification shall be tested.

A2.3.1.3 The number of test samples and test specimens may be increased when deemed necessary by the Classification Society, based on the in-house test reports of the brittle crack arrest properties of the steels intended for approval specified in A2.2.1 a).

#### A2.3.2 Type of tests

A2.3.2.1 Brittle crack arrest tests are to be carried out in accordance with A2.3.3 of this Annex in addition to the approval tests specified in Appendix A2 of UR W11 and/or Annex 1 of this UR.

A2.3.2.2 In the case of applying for addition of the specified brittle crack arrest properties for YP36, YP40 and YP47 steels of which, manufacturing process has been approved by the Classification Society (i.e. The aim analyses and method of manufacture are similar and the steelmaking process, deoxidation and fine grain practice, casting method and condition of supply are the same), brittle crack arrest tests, chemical analyses, tensile test and Charpy V-notch impact test are to be carried out in accordance with Annex 2 of this UR and Appendix A2 of UR W11.

---

#### A2.3.3 Test specimens and testing procedure of brittle crack arrest tests

A2.3.3.1 The test specimens of the brittle crack arrest tests are to be taken with their longitudinal axis parallel to the final rolling direction of the test plates.

A2.3.3.2 The loading direction of brittle crack tests is to be parallel to the final rolling direction of the test plates.

A2.3.3.3 The thickness of the test specimens of the brittle crack arrest tests is to be the full thickness of the test plates.

A2.3.3.4 The test specimens and repeat test specimens are to be taken from the same steel plate. Where the brittle crack arrest properties are evaluated by $K_{ca}$, and the brittle crack arrest test result fails to meet the requirement, further brittle crack arrest tests may be carried out. In this case, the judgment of acceptance is to be made on the arrest toughness value $K_{ca}$ of all test specimens (results of the initial test, failed tests and additional tests shall be included in the testing report.).

A2.3.3.5 The thickness of the test specimen is to be the maximum thickness of the steel plate requested for approval.

A2.3.3.6 In the case where the brittle crack arrest properties are evaluated by $K_{ca}$, the brittle crack arrest test method is to be in accordance with Annex 3 of this UR. In the case where the brittle crack arrest properties are evaluated by CAT, the test method is to be in accordance with Annex 4 of this UR.

#### A2.3.4 Other tests

Additional tests may be required when deemed necessary by the Classification Society in addition to the tests specified in A2.3.3.

### A2.4. Results

Appendix A2 of UR W11 is to be followed for the results. Additionally, results of test items and the procedures shall comply with the test program approved by the Classification Society. In the case where the brittle crack arrest properties are evaluated by $K_{ca}$ or CAT, the manufacturer also is to submit to the Classification Society the brittle crack arrest test reports in accordance with Annex 3 for $K_{ca}$ and Annex 4 for CAT of this UR.

### A2.5. Approval and Certification

Upon satisfactory completion of the survey and tests, approval is granted by the Classification Society with the grade designation having the suffix “BCA1” or “BCA2” (e.g. EH40-BCA1, EH47-BCA1, EH47-BCA2, etc.).

### A2.6. Renewal of approval

The manufacturer is also to submit to the Classification Society actual manufacturing records of the approved brittle crack arrest steels within the term of validity of the manufacturing approval certificate.

**Note:** Chemical composition, mechanical properties, brittle crack arrest properties (e.g. brittle crack arrest test results or small-scale test results) and nominal thickness are to be described in the form of histogram or statistics.

---

## Annex 3 Test Method for Brittle Crack Arrest Toughness, Kca

### A3.1. Scope

ISO 20064: 2019 provides a test method for the determination of brittle crack arrest toughness of steel by using wide plates with a temperature gradient.
This Annex 3 specifies the test procedures for brittle crack arrest toughness (i.e. $K_{ca}$) of steel using fracture mechanics parameter and determination method of $K_{ca}$ at a specific temperature which are specified in ISO 20064:2019. Additionally, this Annex 3 specifies the evaluation method of $K_{ca}$ of test plate. This Annex 3 is applicable to hull structural steels with the thickness over 50mm and not greater than 100mm specified in UR W11 or this UR.

### A3.2. Test Procedures

The test procedures including testing equipment, test specimens, test methods, determination of arrest toughness, reporting of test results, etc. are to be in accordance with ISO 20064: 2019.
As a method for initiating a brittle crack, a secondary loading mechanism can be used in accordance with Annex D of ISO 20064: 2019, except that the first sentence in Annex B.2.4 of ISO 20064: 2019 is revised to “Obtain the value {$K_{ca}$ /[$K_0$ *exp(−c/$T_{caK}$)]} for each data point”.

### A3.3. Determination of Kca at a specific temperature and the evaluation

#### A3.3.1 Method

The method for conducting multiple tests to obtain $K_{ca}$ value at a specific temperature is to be in accordance with Annex B of ISO 20064: 2019.

#### A3.3.2 Evaluation

The straight-line approximation of Arrhenius plot for valid $K_{ca}$ data by interpolation method are to comply with either the following (1) or (2):

(1) The evaluation temperature of $K_{ca}$ (i.e. - 10 degree C) is located between the upper and lower limits of the arrest temperature, with the $K_{ca}$ corresponding to the evaluation temperature not lower than the required $K_{ca}$ (e.g. 6,000 N/mm³/² or 8,000 N/mm³/²), as shown in Fig. A3-1.

![Fig. A3-1 Example for evaluation of Kca at - 10 degree C](Arrhenius_plot_Kca_evaluation_at_-10C)

---

(2) The temperature corresponding to the required $K_{ca}$ (e.g. 6,000 N/mm³/² or 8,000 N/mm³/²) is located between the upper and lower limits of the arrest temperature, with the temperature corresponding to the required $K_{ca}$ not higher than the evaluation temperature (i.e. -10 degree C), as shown in Fig. A3-2.

![Fig. A3-2 Example for evaluation of temperature corresponding to the required Kca](Arrhenius_plot_temperature_evaluation_for_required_Kca)

If both of (1) and (2) above are not satisfied, conduct additional tests to satisfy this condition.

---

## Annex 4 Outline of requirements for undertaking isothermal Crack Arrest Temperature (CAT) test

### A4.1 Scope of application

A4.1.1 Annex 4 is to be applied according to the scope defined in UR W31.

A4.1.2 Annex 4 specifies the requirements for test procedures and test conditions when using the isothermal crack arrest test to determine a valid test result under isothermal conditions and in order to establish the crack arrest temperature (CAT). Annex 4 is applicable to steels with thickness over 50mm and not greater than 100mm.

A4.1.3 This method uses an isothermal temperature in the test specimen being evaluated. Unless otherwise specified in this Annex 4, the other test parameters are to be in accordance with ISO 20064: 2019.

A4.1.4 Table 3 of UR W31 gives the relevant requirements for the brittle crack arrest property described by the crack arrest temperature (CAT).

A4.1.5 The manufacturer is to submit the test procedure to the Classification Society for review prior to testing.

### A4.2 Symbols and their significance

A4.2.1 Table A4-1 supplements Table 1 in ISO 20064: 2019 with specific symbols for the isothermal test.

---

**Table A4-1 Nomenclature supplementary to Table 1 in ISO 20064: 2019**

| Symbol | Unit | Significance |
| :--- | :--- | :--- |
| $t$ | mm | Test specimen thickness |
| $L$ | mm | Test specimen length |
| $W$ | mm | Test specimen width |
| $a_{MN}$ | mm | Machined notch length on specimen edge |
| $L_{SG}$ | mm | Side groove length on side surface from the specimen edge. $L_{SG}$ is defined as a groove length with constant depth except a curved section in depth at side groove end. |
| $d_{SG}$ | mm | Side groove depth in section with constant depth |
| $L_{EB - min}$ | mm | Minimum length between specimen edge and electron beam re-melting zone front |
| $L_{EB-s1, -s2}$ | mm | Length between specimen edge and electron beam re-melting zone front appeared on both specimen side surfaces |
| $L_{LTG}$ | mm | Local temperature gradient zone length for brittle crack runway |
| $a_{arrest}$ | mm | Arrested crack length |
| $T_{target}$ | °C | Target test temperature |
| $T_{test}$ | °C | Defined test temperature |
| $T_{arrest}$ | °C | Target test temperature at which valid brittle crack arrest behaviour is observed |
| $\sigma$ | N/mm² | Applied test stress at cross section of $W \times t$ |
| SMYS | N/mm² | Specified minimum yield strength of the tested steel grade to be approved |
| CAT | °C | Crack arrest temperature, the lowest temperature, $T_{arrest}$, at which running brittle crack is arrested |

### A4.3 Testing equipment

A4.3.1 The test equipment to be used is to be of the hydraulic type of sufficient capacity to provide a tensile load equivalent to ⅔ of SMYS of the steel grade to be approved.

A4.3.2 The temperature control system is to be equipped to maintain the temperature in the specified region of the specimen within ±2°C from $T_{target}$.

A4.3.3 Methods for initiating the brittle crack may be of drop weight type, air gun type or double tension tab plate type.

A4.3.4 The detailed requirements for testing equipment are to be in accordance with ISO 20064: 2019.

### A4.4 Test specimens

#### A4.4.1 Impact type crack initiation

A4.4.1.1 Test specimens are to be in accordance with ISO 20064: 2019, unless otherwise specified in this Annex.

A4.4.1.2 Specimen dimensions are shown in Figure A4-1. The test specimen width, $W$ shall be 500mm. The test specimen length, $L$ shall be equal to or greater than 500mm.

---

A4.4.1.3 V-shape notch for brittle crack initiation is machined on the specimen edge of the impact side. The whole machined notch length shall be equal to 29mm with a tolerance range of ±1mm.

A4.4.1.4 Requirements for side grooves are described in A4.4.4.

![Figure A4-1 Test specimen dimensions for an impact type specimen](Technical_drawing_specimen_dimensions_W500_L500_notch_detail)

**NOTE:** Saw cut notch radius may be machined in the range 0.1mmR and 1mmR in order to control a brittle crack initiation at test.

#### A4.4.2 Double tension type crack initiation

A4.4.2.1 Reference shall be made to Annex D in ISO 20064: 2019 for the shape and sizes in secondary loading tab and secondary loading method for brittle crack initiation.

A4.4.2.2 In a double tension type test, the secondary loading tab plate may be subject to further cooling to enhance an easy brittle crack initiation.

#### A4.4.3 Embrittled zone setting

A4.4.3.1 An embrittled zone shall be applied to ensure the initiation of a running brittle crack. Either Electron Beam Welding (EBW) or Local Temperature Gradient (LTG) may be adopted to facilitate the embrittled zone.

A4.4.3.2 In EBW embrittlement, electron beam welding is applied along the expected initial crack propagation path, which is the centre line of the specimen in front of the machined V-notch.

A4.4.3.3 The complete penetration through the specimen thickness is required along the embrittled zone. One side EBW penetration is preferable, but dual sides EB penetration may be also adopted when the EBW power is not enough to achieve the complete penetration by one side EBW.

A4.4.3.4 The EBW embrittlement is recommended to be prepared before specimen contour machining.

---

A4.4.3.5 In EBW embrittlement, zone shall be of an appropriate quality.

**Note:** EBW occasionally behaves in an un-stable manner at start and end points. EBW line is recommended to start from the embrittled zone tip side to the specimen edge with an increasing power control or go/return manner at start point to keep the stable EBW.

A4.4.3.6 In LTG system, the specified local temperature gradient between machined notch tip and isothermal test region is regulated after isothermal temperature control. LTG temperature control is to be achieved just before brittle crack initiation, nevertheless the steady temperature gradient through the thickness shall be ensured.

#### A4.4.4 Side grooves

A4.4.4.1 Side grooves on side surface can be machined along the embrittled zone to keep brittle crack propagation straight. Side grooves shall be machined in the specified cases as specified in this section.

A4.4.4.2 In EBW embrittlement, side grooves are not necessarily mandatory. Use of EBW avoids the shear lips. However, when shear lips are evident on the fractured specimen, e.g. shear lips over 1mm in thickness in either side then side grooves should be machined to suppress the shear lips.

A4.4.4.3 In LTG embrittlement, side grooves are mandatory. Side grooves with the same shape and size shall be machined on both side surfaces.

A4.4.4.4 The length of side groove, $L_{SG}$ shall be no shorter than the sum of the required embrittled zone length.

A4.4.4.5 When side grooves would be introduced, the side groove depth, the tip radius and the open angle are not regulated, but are adequately selected in order to avoid any shear lips over 1mm thickness in either side. An example of side groove dimensions are shown in Figure A4-2.

A4.4.4.6 Side groove end shall be machined to make a groove depth gradually shallow with a curvature larger than or equal to groove depth, $d_{SG}$. Side groove length, $L_{SG}$ is defined as a groove length with constant depth except a curved section in depth at side groove end.

![Figure A4-2 Side groove configuration and dimensions](Technical_drawing_side_groove_AA_section_details)

---

#### A4.4.5 Nominal length of embrittled zone

A4.4.5.1 The length of embrittled zone shall be at least 150mm.

![Figure A4-3 Definition of EBW length](Schematic_diagram_EBW_length_definition_no_side_groove_vs_with_side_groove)

A4.4.5.2 EBW zone length is regulated by three measurements on the fracture surface after test as shown in Figure A4-3, $L_{EB-min}$ between specimen edge and EBW front line, and $L_{EB-s1}$ and $L_{EB-s2}$.

A4.4.5.3 The minimum length between specimen edge and EBW front line, $L_{EB-min}$ should be no smaller than 150mm. However, it can be acceptable even if $L_{EB-min}$ is no smaller than 150mm-0.2t, where t is specimen thickness. When $L_{EB-min}$ is smaller than 150mm, a temperature safety margin shall be considered into $T_{test}$ (See A4.8.1.2).

A4.4.5.4 Another two are the lengths between specimen edge and EBW front appeared on both side surfaces, as denoted with $L_{EB-s1}$ and $L_{EB-s2}$. Both of $L_{EB-s1}$ and $L_{EB-s2}$ shall be no smaller than 150mm.

A4.4.5.5 In LTG system, $L_{LTG}$ is set as 150mm.

#### A4.4.6 Tab plate / pin chuck details and welding of test specimen to tab plates

A4.4.6.1 The configuration and size of tab plates and pin chucks shall be referred to ISO 20064: 2019. The welding distortion in the integrated specimen, which is welded with specimen, tab plates and pin chucks, shall be also within the requirement in ISO 20064: 2019.

---

### A4.5 Test method

#### A4.5.1 Preloading

A4.5.1.1 Preloading at room temperature can be applied to avoid unexpected brittle crack initiation at test. The applied load value shall be no greater than the test stress. Preloading can be applied at higher temperature than ambient temperature when brittle crack initiation is expected at preloading process. However, the specimen shall not be subjected to temperature higher than 100°C.

#### A4.5.2 Temperature measurement and control

A4.5.2.1 Temperature control plan showing the number and position of thermocouples is to be in accordance with this section.

A4.5.2.2 Thermocouples are to be attached to both sides of the test specimen at a maximum interval of 50mm in the whole width and in the longitudinal direction at the test specimen centre position (0.5 $W$) within the range of ±100mm from the centreline in the longitudinal direction, refer to Figure A4-4.

![Figure A4-4 Locations of temperature measurement](Technical_drawing_thermocouple_locations_on_specimen_FaceA_FaceB)

A4.5.2.3 For EBW embrittlement

A4.5.2.3.1 The temperatures of the thermocouples across the range of 0.3W~0.7W in both width and longitudinal directions are to be controlled within ± 2°C of the target test temperature, $T_{target}$.

A4.5.2.3.2 When all measured temperatures across the range of 0.3W~0.7W have reached $T_{target}$, steady temperature control shall be kept at least for 10 + 0.1 x t [mm] minutes to ensure a uniform temperature distribution into mid-thickness prior to applying test load.

A4.5.2.3.3 The machined notch tip can be locally cooled to easily initiate brittle crack. Nevertheless, the local cooling shall not disturb the steady temperature control across the range of 0.3W~0.7W.

A4.5.2.4 For LTG embrittlement:

A4.5.2.4.1 In LTG system, in addition to the temperature measurements shown in Figure A4-4, the additional temperature measurement at the machine notch tip, $A_0$ and $B_0$ is required. Thermocouples positions within LTG zone are shown in Figure A4-5.

---

![Figure A4-5 Detail of LTG zone and additional thermocouple A0](Technical_drawing_LTG_zone_thermocouple_A0_A1_A2_A3_positions)

A4.5.2.4.2 The temperatures of the thermocouples across the range of 0.3W~0.7W in both width and longitudinal directions are to be controlled within ± 2°C of the target test temperature, $T_{target}$. However, the temperature measurement at 0.3W (location of $A_3$ and $B_3$) shall be in accordance with A4.5.2.4.6 below.

A4.5.2.4.3 Once the all measured temperatures across the range of 0.3W~0.7W have reached $T_{target}$, steady temperature control shall be kept at least for 10 + 0.1 x t [mm] minutes to ensure a uniform temperature distribution into mid-thickness, then the test load is applied.

A4.5.2.4.4 LTG is controlled by local cooling around the machined notch tip. LTG profile shall be recorded by the temperature measurements from $A_0$ to $A_3$ shown in Figure A4-6.

A4.5.2.4.5 LTG zone is established by temperature gradients in three zones, Zone I, Zone II and Zone III. The acceptable range for each temperature gradient is listed Table A4-2.

A4.5.2.4.6 Temperature measurements at $A_2, B_2$ and $A_3, B_3$ shall be satisfied the following requirements:
* $T$ at $A_3, T$ at $B_3 < T_{target} – 2°C$
* $T$ at $A_2 < T$ at $A_3 – 5°C$
* $T$ at $B_2 < T$ at $B_3 – 5°C$

A4.5.2.4.7 No requirements for $T$ at $A_0$ and $T$ at $A_1$ temperatures when $T$ at $A_3$ and $T$ at $A_2$ satisfy the requirements above. Face B is the same.

A4.5.2.4.8 The temperatures from $A_0, B_0$ to $A_3, B_3$ should be decided at test planning stage refer to Table A4-2 which gives the recommended temperature gradients in three zones, Zone I, Zone II and Zone III in LTG zone.

---

![Figure A4-6 Schematic temperature gradient profile in LTG zone](Graph_temperature_gradient_profile_LTG_zone_Distance_from_impact_edge)

**Table A4-2 Acceptable LTG range**

| Zone | Location from edge | Acceptable range of temperature gradient |
| :--- | :--- | :--- |
| Zone I | 29mm – 50mm | 2.00 °C/mm – 2.30 °C/mm |
| Zone II | 50mm – 100mm | 0.25 °C/mm – 0.60 °C/mm |
| Zone III<sup>1)</sup> | 100mm – 150mm | 0.10 °C/mm – 0.20 °C/mm |

**Note 1: The Zone III arrangement is mandatory**

A4.5.2.4.9 The temperature profile in LTG zone mentioned above shall be ensured after holding time at least for 10 + 0.1 x t [mm] minutes to ensure a uniform temperature distribution into mid-thickness before brittle crack initiation.

A4.5.2.4.10 The acceptance of LTG in the test shall be decided from Table A4-2 based on the measured temperatures from $A_0$ to $A_3$.

A4.5.2.5 For double tension type crack initiation specimen:

A4.5.2.5.1 Temperature control and holding time at steady state shall be the same as the case of EBW embrittlement specified in 5.2.3 or the case of LTG embrittlement specified in Section A4.5.2.4.

#### A4.5.3 Loading and brittle crack initiation

A4.5.3.1 Prior to testing, a target test temperature ($T_{target}$) shall be selected.

A4.5.3.2 Test procedures are to be in accordance with ISO 20064: 2019 except that the applied stress is to be ⅔ of SMYS of the steel grade tested.

A4.5.3.3 The test load shall be held at the test target load or higher for a minimum of 30 seconds prior to crack initiation.

A4.5.3.4 Brittle crack can be initiated by impact or secondary tab plate tension after all of the temperature measurements and the applied force are recorded.

---

### A4.6 Measurements after test and test validation judgement

#### A4.6.1 Brittle crack initiation and validation

A4.6.1.1 If brittle crack spontaneously initiates before the test force is achieved or the specified hold time at the test force is not achieved, the test shall be invalid.

A4.6.1.2 If brittle crack spontaneously initiates without impact or secondary tab tension but after the specified time at the test force is achieved, the test is considered as a valid initiation. The following validation judgments of crack path and fracture appearance shall be examined.

#### A4.6.2 Crack path examination and validation

A4.6.2.1 When brittle crack path in embrittled zone deviates from EBW line or side groove in LTG system due to crack deflection and/or crack branching, the test shall be considered as invalid.

A4.6.2.2 All of the crack path from embrittled zone end shall be within the range shown in Figure A4-7. If not, the test shall be considered as invalid.

![Figure A4-7 Allowable range of main crack propagation path](Schematic_diagram_crack_propagation_path_validation_limits)

#### A4.6.3 Fracture surface examination, crack length measurement and their validation

A4.6.3.1 Fracture surface shall be observed and examined. The crack “initiation” and “propagation” are to be checked for validity and judgements recorded. The crack “arrest” positions are to be measured and recorded.

A.4.6.3.2 When crack initiation trigger point is clearly detected at side groove root, other than the V-notch tip, the test shall be invalid.

A4.6.3.3 In EBW embrittlement setting, EBW zone length is quantified by three measurements of $L_{EB-s1}, L_{EB-s2}$ and $L_{EB-min}$, which are defined in A4.4.5. When either or both of $L_{EB-s1}$ and $L_{EB-s2}$ are smaller than 150mm, the test shall be invalid. When $L_{EB-min}$ is smaller than 150mm-0.2t, the test shall be invalid.

A4.6.3.4 When the shear lip with thickness over 1mm in either side near side surfaces of embrittled zone are visibly observed independent of the specimens with or without side grooves, the test shall be invalid.

---

A4.6.3.5 In EBW embrittlement setting, the penetration of brittle crack beyond the EBW front line shall be visually examined. When any brittle fracture appearance area continued from the EB front line is not detected, the test shall be invalid.

A4.6.3.6 The weld defects in EBW embrittled zone shall be visually examined. If detected, it shall be quantified. A projecting length of defect on the thickness line through EB weld region along brittle crack path shall be measured, and the total occupation ratio of the projected defect part to the total thickness is defined as defect line fraction (See Figure A4-8). When the defects line fraction is larger than 10 %, the test shall be invalid.

![Fig. A4-8 Counting procedure of defect line fraction](Schematic_drawing_EBW_defects_counting_procedure)

A4.6.3.7 In EBW embrittlement by dual sides’ penetration, a gap on embrittled zone fracture surface which is induced by miss meeting of dual fusion lines is visibly detected at an overlapped line of dual side penetration, the test shall be invalid.

### A4.7 Judgement of “arrest” or “propagate”

A4.7.1 The final test judgment of “arrest”, “propagate” or “invalid” is decided by the following requirements of A4.7.2 through A4.7.6.

A4.7.2 If initiated brittle crack is arrested and the tested specimen is not broken into two pieces, the fracture surfaces should be exposed with the procedures specified in ISO 20064: 2019.

A4.7.3 When the specimen was not broken into two pieces during testing, the arrested crack length, $a_{arrest}$ shall be measured on the fractured surfaces. The length from the specimen edge of impact side to the arrested crack tip (the longest position) is defined as $a_{arrest}$.

A4.7.4 For LTG and EBW, $a_{arrest}$ shall be greater than $L_{LTG}$ and $L_{EB-s1}, L_{EB-s2}$ or $L_{EB-min}$. If not, the test shall be considered as invalid.

A4.7.5 Even when the specimen was broken into two pieces during testing, it can be considered as “arrest” when brittle crack re-initiation is clearly evident. Even in the fracture

---

surface all occupied by brittle fracture, when a part of brittle crack surface from embrittled zone is continuously surrounded by thin ductile tear line, the test can be judged as re-initiation behaviour. If so, the maximum crack length of the part surrounded tear line can be measured as $a_{arrest}$. If re-initiation is not visibly evident, the test is judged as “propagate”.

A4.7.6 The test is judged as “arrest” when the value of $a_{arrest}$ is no greater than 0.7 $W$. If not, the test is judged as “propagate”.

### A4.8 Ttest, Tarrest and CAT determination

#### A4.8.1 Ttest determination

A4.8.1.1 It shall be ensured on the thermocouple measured record that all temperature measurements across the range of 0.3W ~ 0.7W in both width and longitudinal direction are in the range of $T_{target} ±2°C$ at brittle crack initiation. If not, the test shall be invalid. However, the temperature measurement at 0.3W (location of $A_3$ and $B_3$) in LTG system shall be exempted from this requirement.

A4.8.1.2 If $L_{EB-min}$ in EBW embrittlement is no smaller than 150mm, $T_{test}$ can be defined to equal with $T_{target}$. If not, $T_{test}$ shall be equaled with $T_{target} + 5°C$.

A4.8.1.3 In LTG embrittlement, $T_{test}$ can be equaled with $T_{target}$.

A4.8.1.4 The final arrest judgment at $T_{test}$ is concluded by at least two tests at the same test condition which are judged as “arrest”.

#### A4.8.2 Tarrest determination

A4.8.2.1 When at least repeated two “arrest” tests appear at the same $T_{target}$, brittle crack arrest behaviour at $T_{target}$ will be decided ($T_{arrest} = T_{target}$).When a “propagate” test result is included in the multiple test results at the same $T_{target}$, the $T_{target}$ cannot to be decided as $T_{arrest}$.

#### A4.8.3 CAT determination

A4.8.3.1 When CAT is determined, one “propagate” test is needed in addition to two “arrest” tests. The target test temperature, $T_{target}$ for “propagate” test is recommended to select 5°C lower than $T_{arrest}$. The minimum temperature of $T_{arrest}$ is determined as CAT.

A4.8.3.2 With only the “arrest” tests, without “propagation” test, it is decided only that CAT is lower than $T_{test}$ in the two “arrest” tests, i.e. not deterministic CAT.

### A4.9 Reporting

The following items are to be reported:
(i) Test material: grade and thickness
(ii) Test machine capacity
(iii) Test specimen dimensions: thickness $t$; width $W$ and length $L$; notch details and length $a_{MN}$, side groove details if machined;
(iv) Embrittled zone type: EBW or LTG embrittlement

---

(v) Integrated specimen dimensions: Tab plate thickness, tab plate width, integrated specimen unit length including the tab plates, and distance between the loading pins, angular distortion and linear misalignment
(vi) Brittle crack trigger information: impact type or double tension. If impact type, drop weight type or air gun type, and applied impact energy.
(vii) Test conditions; Applied load; preload stress, test stress
- Judgements for preload stress limit, hold time requirement under steady test stress.
(viii) Test temperature: complete temperature records with thermocouple positions for measured temperatures (figure and/or table) and target test temperature.
- Judgements for temperature scatter limit in isothermal region.
- Judgement for local temperature gradient requirements and holding time requirement after steady local temperature gradient before brittle crack trigger, if LTG system is used.
(ix) Crack path and fracture surface: tested specimen photos showing fracture surfaces on both sides and crack path side view; Mark at “embrittled zone tip” and “arrest” positions.
- Judgment for crack path requirement.
- Judgment for cleavage trigger location (whether side groove edge or V-notch edge).
(x) Embrittled zone information:
When EBW is used: $L_{EB-s1}, L_{EB-s2}$ and $L_{EB-min}$
- Judgement for shear lip thickness requirement
- Judgment whether brittle fracture appearance area continues from the EBW front line
- Judgement for EBW defects requirement
- Judgement for EBW lengths, $L_{EB-s1}, L_{EB-s2}$ and $L_{EB-min}$ requirements
When LTG is used: $L_{LTG}$
- Judgment for shear lip thickness requirement
Test results:
When the specimen did not break into two pieces after brittle crack trigger, arrested crack length $a_{arrest}$
When the specimen broke into two pieces after brittle crack trigger,
- judgement whether brittle crack re-initiation or not.

---

If so, arrested crack length $a_{arrest}$:
- Judgement for $a_{arrest}$ in the valid range (0.3 $W < a_{arrest} ≤ 0.7 W$)
- Final judgement either “arrest”, “propagate” or “invalid”
(xi) Dynamic measurement results: History of crack propagation velocity, and strain change at pin chucks, if needed

### A4.10 Use of test for material qualification testing

Where required, the method can also be used for determining the lowest temperature at which a steel can arrest a running brittle crack (the determined CAT) as the material property characteristic in accordance with A4.8.3.

---

## Annex 5 Approval Scheme of Small-scale Test Methods for Brittle Crack Arrest Steels

### A5.1. Scope

A5.1.1 This Annex specifies the approval scheme of small-scale test methods which are used for product testing (batch release testing) of brittle crack arrest steels specified as Table 3 of this UR.

A5.1.2 Unless otherwise specified in this Annex, Annex 1 of this UR and/or Annex 2 of this UR are to be followed.

### A5.2. Approval Application

A5.2.1 The manufacturer is to submit to the Classification Society the following documents:
a) Application for approval of small-scale test procedure specification
b) Small-scale test procedure specification including the following items at least:
* Applicable material grades, thickness range, deoxidation practice, heat treatment, etc.
* Types and methods of small-scale tests
* Sampling positions in plate thickness direction and final rolling direction of test specimens
* Size and dimension of test specimens
* Number of test specimens
* Test conditions, such as test temperature
* Acceptance criterion
* Example of format of test report
* Example of product inspection certificate including small-scale test results
* Handling of the products when small-scale test results do not satisfy the criterion
c) Mechanism of achieving the brittle crack arrest properties of brittle crack arrest steels
d) Technical background for enabling the evaluation of brittle crack arrest properties by small-scale test methods considering the mechanism specified in above c).
e) Procedure of the evaluation for the brittle crack arrest properties of brittle crack arrest steels by small-scale test results.
f) Data records which validate the correlation between small-scale test results and the large brittle crack arrest test results of brittle crack arrest steels whose number can satisfy the requirement for minimum data number given in A5.3.3
g) Proposed test plan for approval

A5.2.2 Small-scale test procedure specification is to be prepared in accordance with A5.3 of this Annex.

A5.2.3 Where the manufacturer proposes to change any part of the approved small-scale test procedure specification, then the manufacturer is to submit to the Classification Society the documents which can cover all items specified in Annex A5.2.1 of this UR.

A5.2.4 The documents confirming the reason for the change shall be submitted to identify the impact of those changes on the existing procedure, and the proposed actions to address any such impacts.

---

### A5.3. Establishment of Procedure Specification for Small-scale Testing

#### A5.3.1 General

A5.3.1.1 Small-scale test methods are to be determined based on the manufacturer’s own technical philosophy with regard to achieving the brittle crack arrest properties of brittle crack arrest steels. Furthermore, description of an appropriate correlation between large scale brittle crack arrest properties and small-scale test results is to be required, and the acceptance criterion of the small-scale test are to be determined, based on the followings:
* Mechanism of achieving the suitable brittle crack arrest properties
* Sampling position and direction
* Frequency of sampling
* Small-scale test methodology
* Demonstrated correlation between brittle crack arrest test results and small-scale test results
* Derivation of small scale testing acceptance criterion based on the statistical analysis

A5.3.1.2 The manufacturer shall prepare the small-scale test procedure specification in accordance with the following A5.3.2 through A5.3.5.

#### A5.3.2 Types and Methods of Testing

A5.3.2.1 Types, methods, dimension and positions as well as direction of test specimens, etc. of small-scale tests are to be specified by the manufacturer, and approved in accordance with this UR.

A5.3.2.2 In general, the test method should reproduce the crack initiation, propagation and arrest feature by such as the following test method.
* Combination of test methods, e.g. NRL drop weight test and V-notch Charpy impact test
* One test method, e.g. press-notch Charpy impact test or side-section drop weight test

A5.3.2.3 In general, brittle crack arrest properties of brittle crack arrest steels are to be predicted using a regression equation on the relationship between small scale test result (e.g. transition temperature obtained by small scale tests) and large scale brittle crack arrest test result (e.g. $K_{ca}$ or temperature corresponding to the specific brittle crack arrest properties).
Other approaches can be used subject to the approval of the Classification Society.

**NOTE:** Table A5-1, Table A5-2 and Table A5-3 give the examples of small scale test methods.

A5.3.2.4 For determination of test methods, the manufacturer should confirm the applicability of these test methods to their brittle crack arrest steels theoretically taking into account the methodology of test methods, their own mechanism of achieving the brittle crack arrest properties, and sampling positions of test specimens (See A5.3.1.1). Then, the manufacturer should also submit the technical background for determination of small-scale test methods to the Classification Society as given in A5.2.1.

---

#### A5.3.3 Testing Data

A5.3.3.1 Selection of test plates

A5.3.3.1.1 Brittle crack arrest tests and small-scale tests are to be conducted for each material grade (including all suffixes) of brittle crack arrest steels in accordance with A5.3.3 of this Annex.

A5.3.3.1.2 Brittle crack arrest tests and small-scale tests are to be carried out on at least 12 test plates, in accordance with A5.3.3.1.3, by which these test results can reliably estimate brittle crack arrest properties of brittle crack arrest steels.

**NOTE:** “One test plate” means “the rolled product from a single slab or ingot if this is rolled directly into plates” as defined in URW11.

A5.3.3.1.3 In order to ensure appropriate correlation between small-scale test results and brittle crack arrest properties with various manufacturing conditions of steel plates, the steel plates should be representative for each combination of thickness range and heat sample to include:
* The intended maximum and minimum plate thickness;
* Different heats are to be chosen for each thickness.

Furthermore, the above test plates are to include a fixed number of steel plate(s) whose brittle crack arrest properties (i.e. brittle crack arrest test results) do not comply with the requirements specified in Table 3 of this UR. Such a number should be at least one, but not exceeding one quarter of all test plates. Manufacturing process of these test plates can be different (or intentionally altered from the approved manufacturing process) from that of the brittle crack arrest steels to which the small-scale test method is applied. It is recommended that the strength grade of these test plates (non-compliant with the relevant requirements of brittle crack arrest properties) are similar to that of the brittle crack arrest steels.

Where the manufacturer has requested approval for only a single thickness, the thickness of test plates can be only a single thickness. In this case, at least four steel plates for each combination of thickness (single thickness) and heats (three different heats) should be used, and the applicable thickness of the small scale test is only that single thickness condition.

A5.3.3.1.4 Brittle crack arrest steels used for the approval test of manufacturing process of these steels (and its approval test results) can also be used as the test plates specified in A5.3.3.1.3

A5.3.3.1.5 Brittle crack arrest test specimens and small-scale test specimens are to be taken from the same test plate.

A5.3.3.1.6 A decrease of the total of the indicated number of test plates may be accepted by the Classification Society in the following (a) or (b) cases:
(a) When the manufacturer applies a small-scale test procedure specification to multiple material grades, and the manufacturing process and mechanism to ensure the brittle crack arrest properties of these different material grades are the same.
(b) When a small-scale test procedure specification is already approved by the Classification Society for one or some material grades, and the manufacturer applies similar small-scale test procedure specification to the other material grade(s), and the manufacturing process and mechanism to ensure the brittle crack arrest properties of these different material grades are same.

---

#### A5.3.3.2 Brittle crack arrest tests

A5.3.3.2.1 Brittle crack arrest tests are to be carried out for each test plate in accordance with A2.3.3, Annex 2 of this UR.

A5.3.3.2.2 Where brittle crack arrest tests are carried out for evaluation of $K_{ca}, K_{ca}$ at a specific temperature is to be obtained in accordance with A3.3 of Annex 3.

A5.3.3.2.3 Where brittle crack arrest tests are carried out for evaluation of CAT, deterministic (actual) CAT is to be obtained in accordance with A4.8.3 of Annex 4.

#### A5.3.3.3 Small-scale tests

A5.3.3.3.1 Small-scale tests are to be carried out in accordance with small-scale test procedure specification to be approved for each test plate.

A5.3.3.3.2 In general, the test specimens of small-scale tests are to be taken with their longitudinal axis parallel to the final rolling direction of the test plates.

A5.3.3.3.3 The test specimens of small-scale tests are to be taken from the specified positions in plate thickness direction of the test plates, as given in A5.3.2.3.

#### A5.3.4 Validation of Correlation

A5.3.4.1 A regression equation on the relationship between brittle crack arrest property obtained from brittle crack arrest test and single or multiple small-scale test results is to be established. For brittle crack arrest properties, a specific temperature (e.g. $T_{Kca6000}$ in BCA1, $T_{Kca8000}$ in BCA2 or CAT) or the $K_{ca}$ value at -10°C may be used.

A5.3.4.2 The validity of the regression equation shall be examined to predict brittle crack arrest properties with enough accuracy. The correlation in brittle crack arrest properties between the calculated values from small scale tests and the brittle crack arrest test results shall be assured by using the value of twice the standard deviation (2σ). When using temperature for brittle crack arrest property, 2σ shall not be greater than 20°C. In other cases (e.g. $K_{ca}$ value at -10°C), an upper limit of 2σ shall be established with the agreement of the Classification Society.

**NOTE:**
Calculation procedure of the standard deviation (σ) is given as follows:
$\sigma = \sqrt{\frac{1}{(n-1)}\sum_{i=1}^n(y_i - x_i)^2}$
n: number of test plates
$y_i$: brittle crack arrest property obtained from brittle crack arrest test for one test plate
$x_i$: brittle crack arrest property estimated from small scale tests for one test plate

#### A5.3.5 Acceptance Criterion

A5.3.5.1 Acceptance criterion of brittle crack arrest steels by the small-scale tests is to be proposed by the manufacturer based on the regression equation which is assured in the correlation with brittle crack arrest properties in A5.3.4 above. The criterion is to be determined so that regression equation can predict brittle crack arrest properties on safety side, considering the scatter of brittle crack arrest properties from the predicted value by the regression equation.

---

A5.3.5.2 Unless otherwise agreed by the Classification Society, an acceptance criterion of small-scale tests is to be determined by following procedures:

(a) For correlation by means of temperature
(i) The required temperature (see Fig A5-1) is obtained by subtracting 2σ (°C) from the brittle crack arrest steel specification in Table 3 of this UR, that is -10-2σ (°C), where 2σ is given in A5.3.4.2.
$T_{Kca6000}$ and $T_{Kca8000}$ in Fig. A5-1 are the temperatures at which the $K_{ca}$ value of steel plates equals 6,000N/mm³/² and 8,000N/mm³/², respectively.
(ii) The temperature predicted from the small-scale test results through the regression equation shall be no higher than the value of -10-2σ(°C).

![Fig. A5-1 Example for determination of acceptance criterion of small-scale test for correlation by means of temperature](Plot_temperature_correlation_small_scale_vs_large_scale)

**Note: This is only a schematic and may not represent the actual data obtained**

(b) For correlation by means of brittle crack arrest toughness ($K_{ca}$):
(i) The required $K_{ca}$ (see Fig. A5-2) is obtained by adding 2σ (N/mm³/²) to the brittle crack arrest steel specification in Table 3 of this UR, that is either 6,000+2σ(N/mm³/²) in BCA1 or 8,000+2σ(N/mm³/²) in BCA2, where 2σ is given in A5.3.4.2.
(ii) The $K_{ca}$ value predicted from the small-scale test results through the regression equation shall be no smaller than the value of 6000+2σ(N/mm³/²) for BCA1, or 8000+2σ(N/mm³/²) for BCA2.

---

![Fig. A5-2 Example for determination of acceptance criteria of small-scale test for correlation by means of brittle crack arrest toughness (Kca)](Plot_Kca_correlation_small_scale_vs_large_scale)

**Note: This is only a schematic and may not represent the actual data obtained**

### A5.4. Approval Tests

#### A5.4.1 General

A5.4.1.1 In order to confirm the validity of the submitted technical documents specified in A5.2.1, approval tests are to be carried out.

A5.4.1.2 Approval test plan is to be approved by the Classification Society prior to testing.

A5.4.1.3 Considering the contents of the submitted technical documents specified in A5.2.1, the Classification Society may require additional tests in the following cases:
a) When the Classification Society determines that the number of brittle crack arrest tests or small-scale tests is too few to adequately confirm the validity of the acceptance criterion of small-scale tests (See A5.3.3.1);
b) When the Classification Society determines that the testing data obtained for setting the acceptance criterion of small-scale tests varies too widely (See A5.3.4.2), or that the data is clustered producing a biased correlation curve;
c) When the Classification Society determines that the validity of brittle crack arrest test results or small-scale test results for setting the acceptance criterion of small-scale tests is insufficient, or has some flaws during tests and/or for test results (See A5.3.3.2 and A5.3.3.3); and
d) Others as deemed necessary by the Classification Society.

#### A5.4.2 Extent of the approval tests

A5.4.2.1 Extent of the approval tests is to be in accordance with 2.1, Annex 1 and 3.1, Annex 2 of this UR.

---

#### A5.4.3 Type of tests

A5.4.3.1 Brittle crack arrest tests

A5.4.3.1.1 Brittle crack arrest tests are to be carried out in accordance with A2.3.3, Annex 2 of this UR.

A5.4.3.1.2 Where brittle crack arrest tests are carried out for evaluation of $K_{ca}, K_{ca}$ at a specific temperature ($T_{Kca6000}$ or $T_{Kca8000}$) is to be obtained in accordance with A3.3 of Annex 3.

A5.4.3.1.3 Where brittle crack arrest tests are carried out for evaluation of CAT, deterministic CAT is to be obtained in accordance with A4.8.3 of Annex 4.

A5.4.3.2 Small-scale tests

A5.4.3.2.1 Small-scale tests are to be carried out in accordance with A5.3.3.3.

### A5.5. Results

A5.5.1 Results of test items and the procedures shall comply with the test program approved by the Classification Society.

A5.5.2 For the brittle crack arrest test results, the manufacturer is to submit to the Classification Society the brittle crack arrest test reports in accordance with Annex 3 of this UR for $K_{ca}$ and Annex 4 of this UR for CAT.

A5.5.3 For small-scale test results, the manufacturer is to submit to the Classification Society the small-scale test reports in accordance with the example of format of test reports submitted as specified in A5.2.1 b) of this Annex.

### A5.6. Approval

Upon satisfactory completion of the survey and tests, and satisfactory confirmation of the submitted technical documents, the approval for small scale test procedure specification is granted by the Classification Society.

---

**Table A5-1 Example of small-scale test method using NRL drop weight test and V-notch Charpy impact test (Informative)**

| | |
| :--- | :--- |
| **Test type:** | NRL drop weight test and V-notch Charpy impact test |
| **Standard:** | ASTM E208:2020 and ISO 148-1:2016 |
| **Sampling positions of test specimens:** | NRL drop weight test: at surface V-notch charpy impact test: 1/4 of thickness |
| **Length direction of test specimen:** | Parallel to the final rolling direction of test plate |
| **Regression equation:** | $T_{Kca} = \alpha \cdot (NDTT + 10) + \beta \cdot vTrs + 153(t - 5)^{1/13} - 170.5$ |
| | $T_{Kca}$: Temperature at $K_{ca}$ of 6,000N/mm³/² or $K_{ca}$ of 8,000N/mm³/², (°C) |
| | $NDTT$: Nil-ductility transition temperature (°C) |
| | $vTrs$: Transition temperature of the absorbed energy (°C) |
| | $t$: thickness |
| | $\alpha, \beta^{(1)}$: constant |
| **Notes:** | (1) $\alpha$ and $\beta$ are determined by comparing small-scale test results with brittle crack arrest test results. |

**Table A5-2 Example of small-scale test method using pressed-notch Charpy impact test (Informative)**

| | |
| :--- | :--- |
| **Test type:** | Pressed-notch Charpy impact test |
| **Standard:** | Dimension, shape, introducing method of notch: Manufacturer’s proposal Others: ISO148-1:2016 |
| **Sampling position of test specimen:** | 1/2 of thickness |
| **Length direction of test specimen:** | Parallel to the final rolling direction of test plate |
| **Regression equation:** | $T_{Kca} = \alpha \cdot _pT_{E\gamma J} + \beta$ |
| | $T_{Kca}$: Temperature at $K_{ca}$ of 6,000N/mm³/² or $K_{ca}$ of 8,000N/mm³/², (°C) |
| | $_pT_{E\gamma J}$: Test temperature at absorbed energy of $\gamma$ (J), (°C) |
| | $\alpha$ and $\beta$: Constant |
| | $\gamma$: Absorbed energy at brittle fracture surface ratio of $\delta$ (%),(J) |
| **Notes:** | (1) $\alpha, \beta, \gamma$ and $\delta$ are determined by comparing small-scale test results with brittle crack arrest test results. |

---

**Table A5-3 Example of small-scale test method using Side-section drop weight test (Informative)**

| | |
| :--- | :--- |
| **Test type:** | Side-section drop weight test |
| **Standard:** | Dimension: P-2 type of ASTM E 208 2020 |
| **Sampling positions of test specimens:** | 1/2 of thickness and side-section |
| | ![Table A5-3 Diagram](Technical_drawing_side_section_drop_weight_test_sampling) |
| **Length direction of test specimen:** | Parallel to the final rolling direction of test plate |
| **Regression equation:** | $T_{Kca} = \alpha + \beta \cdot T_{NDT}^{side} + \gamma \cdot t^{1.5}$ |
| | $T_{Kca}$: Temperature at $K_{ca}$ of 6,000N/mm³/² or $K_{ca}$ of 8,000N/mm³/², (°C) |
| | $T_{NDT}^{side}$: Nil-ductility transition temperature obtained by side-section drop weight test, (°C) |
| | $t$: thickness |
| | $\alpha, \beta, \gamma^{(1)}$: constant |
| **Notes:** | (1) $\alpha, \beta$ and $\gamma$ are to be determined by comparing small-scale test results with brittle crack arrest test results. |

**End of Document**

================================================================================
# FILE: UR_W/ur-w32-rev1-sep-2020-cln.md
================================================================================

# W32 Qualification scheme for welders of hull structural steels

**W32**
(Sep 2016)
(Rev.1 Sep 2020)

### 1. Scope

1.1 This document gives requirements for a qualification scheme for welders intended to be engaged in the fusion welding of steels as specified in UR W7, W8, W11 and W31 for hull structures.

1.2 This qualification scheme does not cover welders engaged in oxy-acetylene welding.

1.3 This qualification scheme does not cover welding of pipes and pressure vessels.

1.4 Alternative welding Standards or Codes are to be applied in full, however, cross-mixing requirements of Standards and Codes is not permitted.

**Note:**

1. This UR is to be applied by IACS Societies to applications for welder or welding operator qualification (initial or renewal) dated on or after 1 January 2018.

2. This document does not invalidate welder's qualifications issued and accepted by the Classification Society before 1 January 2018 provided the welder's qualifications are considered by the Classification Society to meet the technical intent of this UR. These qualifications are to be renewed in accordance with this UR latest by 31 December 2020.

3. Certificates that expire after 1 January 2018 are to be renewed in accordance with this UR.

4. The welder's or welding operator's qualifications which have not been required by the Society's Rules before 1 January 2018, are to be initially issued in accordance with this UR by the 31 December 2020 at the latest.

5. Revision 1 of this UR is to be applied by IACS Societies to applications for welder or welding operator initial qualification dated on or after 1 January 2022.

5.1 Existing qualifications are to be renewed in accordance with Rev.1 of this UR when they become due.

***

### 2. General

2.1 Those welders intended to be engaged in welding of hull structures in shipyards and manufacturers shall be tested and qualified in accordance with this scheme and issued with a qualification certificate endorsed by the Society.

2.2 The welding operator responsible for setting up and/or adjustment of fully mechanized and automatic equipment, such as submerged arc welding, gravity welding, electro-gas welding and MAG welding with auto-carriage, etc., must be qualified whether he operates the equipment or not. However a welding operator, who solely operates the equipment without responsibility for setting up and/or adjustment, does not need qualification provided that he has experience of the specific welding work concerned and the production welds made by the operators are of the required quality.

The qualification test and approval range of the welding operator are left to the discretion of the Society with reference to ISO 14732:2013.

2.3 This document is applicable to welding of hull structures both during new construction and the repair of ships.

2.4 The training of welders, control of their qualification and maintenance of their skills are the responsibility of shipyards and manufacturers. The Society Surveyor is to verify and be satisfied that the welders are appropriately qualified.

2.5 Equivalence of national or international standards to this UR

2.5.1 Welders or welding operators qualified in accordance with national or international welder qualification standards may also be engaged in welding of hull structures at the discretion of the Society provided that standard is considered equivalent to this UR from technical perspective covering examination, testing and range approval.

2.5.2. Even if the requirements stipulated in the standards are applied, the requirement for revalidation of welders' qualification shall be in accordance with 6.2.1.

### 3. Range of qualification of welders

3.1 A welder is to be qualified in relation to the following variables of welding:
a) base metal
b) welding consumables type
c) welding process
d) type of welded joint
e) plate thickness
f) welding position

3.2 Base metals for qualification of welders or welding operators are combined into one group with a specified minimum yield strength $R_{eH} \le 460$ N/mm². The welding of any one metal in this group covers qualification of the welder or welding operator for the welding of all other metals within this group.

3.3 For manual metal arc welding, qualification tests are required using basic, acid or rutile covered electrodes. The type of covered electrodes (basic, acid or rutile) included in the range of approval is left at the discretion of the Society.

Welding with filler material qualifies for welding without filler material, but not vice versa.

3.4 The welding processes for welder's qualification are to be classified in Table 1 as,

M - Manual welding
S - Semi-automatic welding/Partly mechanized welding
T - TIG welding

Each testing normally qualifies only for one welding process. A change of welding process requires a new qualification test.

**Table 1 - Welding processes for welder's qualification**

| Symbol | Welding process in actual welding works | ISO 4063:2009 |
| :--- | :--- | :--- |
| **M** | Manual welding | Manual metal arc welding (metal arc welding with covered electrode) | 111 |
| **S** | Partly mechanized welding | Metal inert gas (MIG) welding | 131 |
| | | Metal active gas (MAG) welding Flux cored arc (FCA) welding | 135, 138¹ 136² |
| **T** | TIG welding | Tungsten inert gas (TIG) welding | 141 |

Note:
The Society may require separate qualification for solid wires, metal-cored wires and flux-cored wires as follows:
¹ A change from MAG welding with solid wires (135) to that with metal cored wires (138), or vice versa is permitted.
² A change from a solid or metal cored wire (135/138) to a flux cored wire (136) or vice versa requires a new welder qualification test.

3.5 The types of welded joint for welder's qualification are to be classified as shown in Table 2 in accordance with the qualification test.

**Table 2 - Types of welded joint for welder's qualification**

| Type of welded joint used in the test assembly for the qualification test | | | Type of welded joint qualified |
| :--- | :--- | :--- | :--- |
| Butt weld | Single sided weld | With backing | A | A, C, F |
| | | Without backing | B | A, B, C, D, F |
| | Double sided weld | With gouging | C | A, C, F |
| | | Without gouging | D | A, C, D, F |
| Fillet weld | ---- | ---- | F | F |

Welders engaged in full/partial penetration T welds shall be qualified for butt welds for the welding process and the position corresponding to the joints to be welded.

3.6 For fillet welding, welders who passed the qualification tests for multi-layer technique welding can be deemed as qualified for single layer technique, but not vice versa.

3.7 The qualified plate thickness range arising from the welder qualification test plate thickness is shown in Table 3.

**Table 3 - Plate thicknesses for welder's qualification**

| Thickness of test assembly T (mm) | Qualified plate thickness range t (mm) |
| :--- | :--- |
| T < 3 | T ≤ t ≤ 2T |
| 3 ≤ T < 12 | 3 ≤ t ≤ 2T |
| 12 ≤ T | 3 ≤ t |

3.8 The welding positions qualified as a result of the actual welding position used in a satisfactory welder's qualification test, are shown in Table 4 and Table 5. Diagrams showing the definitions of weld position used in Table 4 and Table 5 are shown in Figure 1.

**Table 4 - Qualified welding positions when testing with butt welding**

| Qualification Test Position with butt weld | Qualified welding positions in actual welding works | |
| :--- | :--- | :--- |
| | **Butt welds** | **Fillet welds** |
| PA | PA | PA, PB |
| PC | PA, PC | PA, PB, PC |
| PE | PA, PC, PE | PA, PB, PC, PD, PE |
| PF | PA, PF | PA, PB, PF |
| PG | PG | PG |

**Table 5 - Qualified welding positions when testing with fillet welding**

| Qualification Test Position with fillet weld | Qualified welding positions in actual welding works |
| :--- | :--- |
| | **Fillet welds** |
| PA | PA |
| PB | PA, PB |
| PC | PA, PB, PC |
| PD | PA, PB, PC, PD, PE |
| PE | PA, PB, PC, PD, PE |
| PF | PA, PB, PF |
| PG | PG |

The Society may require a qualification test with fillet welding for welders who are employed to perform fillet welding only. Welders engaged in welding of T joints with partial or full penetration are to be qualified for butt welding.

3.9 A welder qualified for butt or fillet welding can be engaged in tack welding for the welding process and position corresponding to those permitted in his certificate.

Alternatively, welders engaged in tack welding only can be qualified on the test assemblies shown in Figure 5 or Figure 6.

***

![Figure 1: Welding positions](Seven diagrams showing different welding positions: a) PA: flat position (butt and fillet); b) PB: horizontal vertical position (fillet); c) PC: horizontal position (butt); d) PD: horizontal overhead position (fillet); e) PE: overhead position (butt); f) PF: vertical up position (butt and fillet); g) PG: vertical down position (butt and fillet). The letter 'p' indicates the welding position.)

***

### 4. Qualification test

4.1 General

4.1.1 Welding of the test assemblies and testing of test specimens shall be witnessed by the Surveyor.

4.2 Test assemblies

4.2.1 Test assemblies for butt welds and for fillet welds are to be prepared as shown in Figure 2, Figure 3 and Figure 4 in each qualification test.

4.2.2 Test assemblies for butt tack welds and for fillet tack welds are to be prepared as shown in Figure 5 and Figure 6.

![Figure 2: Dimensions and types of test assembly for butt welds (T < 12mm)](Diagram showing a rectangular plate with a central butt weld. Dimensions: Width Min. 200mm, Total Height Min. 200mm. It is divided into sections: Discard (about 25mm), Face bend test specimen (30mm), Discard, Root bend test specimen (30mm), Discard, Face bend test specimen (30mm), Discard, Root bend test specimen (30mm), Discard (about 25mm). Thickness is T < 12mm.)

![Figure 3: Dimensions and types of test assembly for butt welds (T ≥ 12mm)](Diagram showing a rectangular plate with a central butt weld. Dimensions: Width Min. 200mm, Total Height Min. 200mm. It is divided into sections: Discard (about 25mm), Side bend test specimen (10mm), Discard, Side bend test specimen (10mm), Discard, Side bend test specimen (10mm), Discard, Side bend test specimen (10mm), Discard (about 25mm). Thickness is T ≥ 12mm.)

![Figure 4: Dimensions and types of test assembly for fillet welds](Diagram showing a T-joint test assembly. Vertical plate: Min. 150mm length, Min. 100mm height. Horizontal plate: Min. 200mm length, Min. 100mm width. Shows a fracture test specimen section. A detail 'Z' shows the weld throat 'a' and leg length 'z=a√2'. For T ≥ 6mm, 0.5T ≤ a ≤ 0.5T + 3mm. For T < 6mm, 0.5T ≤ a ≤ T.)

![Figure 5: Dimensions and types of test assembly for tack butt welds](Diagram of a butt weld tack test. Plate size about 200mm x 200mm. Three tacks are placed along the joint: central one is about 100mm long, top and bottom ones are about 30mm long with 20mm discards. Groove angle is 60°, gap 3-6mm, backing plate width 25mm, thickness 4-6mm.)

![Figure 6: Dimensions and types of test assembly for tack fillet welds](Diagram of a fillet weld tack test. Vertical plate on a horizontal base. Dimensions 100mm x 100mm on vertical, 200mm length on base. Three tack welds are shown: central one about 100mm, others about 30mm with 20mm/10mm spacing.)

***

4.2.3 Testing materials and welding consumables shall conform to one of the following requirements or to be of equivalent grade approved by the Society.

a) Testing materials
- Hull structural steels specified in UR W11
- Hull structural forged steels specified in UR W7
- Hull structural cast steels specified in UR W8
- Hull structural steels with specified minimum yield point 460 N/mm² specified in UR W31

b) Welding consumables
- Consumables for hull structural steels specified in UR W17
- Consumables for YP47 steels specified in UR W31

4.2.4 The welder qualification test assembly is to be welded according to a welding procedure specification (WPS or pWPS) simulating the conditions in production, as far as practicable.

4.2.5 Root run and capping run need each to have a minimum of one stop and restart. The welders are allowed to remove minor imperfections only in the stop by grinding before restart welding.

4.3 Examination and test

4.3.1 The test assemblies specified in 4.2 shall be examined and tested as follows:

a) For butt welds
- Visual examination
- Bend test
Note: Radiographic test or fracture test may be carried out in lieu of bend test except the gas-shielded welding processes with solid wire or metal cored wire.

b) For fillet welds
- Visual examination
- Fracture test
Note: Two macro sections may be taken in lieu of the fracture test.

c) For tack welds
- Visual examination
- Fracture test

Additional tests may be required, at the discretion of the Society.

4.3.2 Visual examination

The welds shall be visually examined prior to the cutting of the test specimen for the bend test and fracture test. The result of the examination is to show the absence of cracks or other serious imperfections.

Imperfections detected are to be assessed in accordance with quality level B in ISO 5817:2014, except for the following imperfection types for which level C applies;
- Excess weld metal
- Excess penetration
- Excessive convexity
- Excessive throat thickness

4.3.3 Bend test

Transverse bend test specimens are to be in accordance with UR W2.

The mandrel diameter to thickness ratio (i.e. D/T) is to be that specified for welding consumable (UR W17 and W31) approvals +1.

Two face bend test and two root bend test specimens are to be tested for initial qualification test, and one face and one root bend test specimens for extension of approval. For thickness 12mm and over, four side specimens (two side specimens for extension of approval) with 10 mm in thickness may be tested as an alternative.

At least one bend test specimen shall include one stop and restart in the bending part, for root run or for cap run.

The test specimens are to be bent through 180 degrees. After the test, the test specimens shall not reveal any open defects in any direction greater than 3mm. Defects appearing at the corners of a test specimen during testing should be investigated case by case.

4.3.4 Radiographic test

When radiographic testing is used for butt welds, imperfections detected shall be assessed in accordance with ISO 5817:2014, level B.

4.3.5 Fracture test (Butt welds)

When fracture test is used for butt welds, full test specimen in length is to be tested in accordance with ISO 9017:2017. Imperfections detected shall be assessed in accordance with ISO 5817:2014, level B.

4.3.6 Fracture test (Fillet welds)

The fracture test is to be performed by folding the upright plate onto the through plate. Evaluation shall concentrate on cracks, porosity and pores, inclusions, lack of fusion and incomplete penetration. Imperfections that are detected shall be assessed in accordance with ISO 5817:2014, level B.

4.3.7 Macro examination

When macro examination is used for fillet welds, two test specimens are to be prepared from different cutting positions; at least one macro examination specimen shall be cut at the position of one stop and restart in either root run or cap run. These specimens are to be etched on one side to clearly reveal the weld metal, fusion line, root penetration and the heat affected zone.

Macro sections shall include at least 10mm of unaffected base metal.

The examination is to reveal a regular weld profile, through fusion between adjacent layers of weld and base metal, sufficient root penetration and the absence of defects such as cracks, lack of fusion etc.

4.4 Retest

4.4.1 When a welder fails a qualification test, the following shall apply.

a) In cases where the welder fails to meet the requirements in part of the tests, a retest may be welded immediately, consisting of another test assembly of each type of welded joint and position that the welder failed. In this case, the test is to be done for duplicate test specimens of each failed test.
All retest specimens shall meet all of the specified requirements.

b) In cases where the welder fails to meet the requirements in all parts of the required tests or in the retest prescribed in 4.4.1 a), the welder shall undertake further training and practice.

c) When there is specific reason to question the welder's ability or the period of effectiveness has lapsed, the welder shall be re-qualified in accordance with the tests specified in 4.2 and 4.3.

4.4.2 Where any test specimen does not comply with dimensional specifications due to poor machining, a replacement test assembly shall be welded and tested.

### 5. Certification

5.1 Qualification certificates are normally issued when the welder has passed the qualification test in accordance with the Society's Rules. Each Shipyard and Manufacturer shall be responsible for the control of the validity of the certificate and the range of the approval.

5.2 The following items shall be specified in the certificate:
a) Range of qualification for base metal, welding processes, filler metal type, types of welded joint, plate thicknesses and welding positions.
b) Expiry date of the validity of the qualification.
c) Name, date of birth, identification and the photograph of the welder.
d) Name of shipbuilder / manufacturer.

5.3 When a certificate is issued, the relative documents such as test reports and/or re-validation records shall be archived as annexes to the copy of certificate according to the rules of the Society.

5.4 The status of approvals of each individual qualification is to be demonstrated to the Classification Society when requested.

### 6. Period of Validity

6.1 Initial approval

6.1.1 Normally the validity of the welder's approval begins from the issue date of qualification certificate when all the required tests are satisfactorily completed.

6.1.2 The certificate is to be signed at six-month intervals by the shipyards/manufacturers personnel who is responsible for production weld quality provided that all the following conditions are fulfilled:

a) The welder shall be engaged with reasonable continuity on welding work within the current range of approval. An interruption for a period no longer than six months is permitted.
b) The welder's work shall in general be in accordance with the technical conditions under which the approval test is carried out.
c) There shall be no specific reason to question the welder's skill and knowledge.

6.1.3 If any of these conditions are not fulfilled, the Society is to be informed and the certificate is to be cancelled.

6.1.4 The validity of the certificate may be maintained in agreement with the Society as specified in 6.2. The chosen maintenance option of qualification in accordance with 6.2.1 a) or b) or c) shall be stated on the certificate at the time of issue.

6.2 Maintenance of the approval

6.2.1 Revalidation shall be carried out by the Society. The skill of the welder shall be periodically verified by one of the following options:

a) The welder shall be re-tested every 3 years.

b) Every 2 years, two welds made during the last 6 months of the 2 years validity period shall be tested by radiographic or ultrasonic testing or destructive testing and shall be recorded. The weld tested shall reproduce the initial test conditions except for the thickness. These tests revalidate the welder's qualifications for an additional 2 years.

c) A welder's qualification for any certificate shall be valid as long as it is signed according to 6.1.2 subject that all the following conditions are fulfilled. In this option, the fulfilment of all the conditions is to be verified by the Society. The frequency of verification by the Society is to be no longer than 3 years and is to be agreed between the Society and the shipyards/manufacturers.

I. The welder is working for the same shipyard/manufacturer which is responsible for production weld quality as indicated on his or her qualification certificate.

II. Society shall verify that the welder quality management system of the shipyard/manufacturer includes as minimum:
- A designated person responsible for the coordination of the welder quality management system.
- List of welders and welding supervisors in shipyard/manufacturer
- If applicable, list of subcontracted welders
- Qualification certificate of welders and description of the associated management system
- Training requirements for welder qualification programme
- Identification system for welders and WPS used on welds
- Procedure describing the system in place to monitor each welder performance based on results of welds examination records (e.g. repair rate, etc.) including the criteria permitting the maintenance of the welder qualification without retesting.

III. The shipyards/manufacturers have to document at least once a year that the welder has produced acceptable welds in accordance with construction quality standards and Classification Society's requirements in the welding positions, type of welds and backing conditions covered by its certificate. Which documents are required and how to document the evidences should be in agreement between the Society and the shipyards/manufacturers.

6.2.2 The Society has to verify compliance with the above conditions and sign the maintenance of the welder's qualification certificate.

***

### Annex: Example of Welder's qualification certificate

**WELDER'S QUALIFICATION CERTIFICATE**

| | | |
| :--- | :--- | :--- |
| Welder's name: | Date of birth: | **Photograph** |
| Cert. No: | Sex: | |
| Identification No. | | |
| Employer's name and address | | |
| WPS/pWPS No. | | |
| Date of initial approval | | |

This is to certify that the welder has passed the qualification test [/and re-validation record audit] according to the rules of [the Society], and is qualified to undertake welding operation specified in range of qualification of this certificate.

| Items | Test piece | Range of qualification |
| :--- | :--- | :--- |
| Welding process | | |
| Base metal | | |
| Filler metal type | | |
| Plate thickness | | |
| Type of welded joint | | |
| Welding position | | |
| Revalidation method | In accordance with 6.2.1 a) $\square$ b) $\square$ c) $\square$ | |
| Other details | | |

This certificate is issued at [place], and valid until [DD/MM/YYYY].
Signature/seal of examiner: Issued on [DD/MM/YYYY].

| | Report No. to be reviewed | Date of report | Signature of Employee | Date of signature |
| :--- | :--- | :--- | :--- | :--- |
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |
| 6 | | | | |

***

### TEST RECORD

| Type of test | Performed and accepted | Not required |
| :--- | :--- | :--- |
| Visual examination | | |
| Radiographic examination | | |
| Surface examination | | |
| Macro examination | | |
| Fracture test | | |
| Bend test | | |
| Additional tests | | |

* At the discretion of the Society, this page can be as the back page of a certificate, and also can be as a separate file.

**End of Document**


================================================================================
# FILE: UR_W/ur-w33rev1corr1.md
================================================================================

# W33 Non-destructive testing of ship hull steel welds

**(Dec 2019)**
**(Rev.1 May 2020)**
**(Corr.1 Aug 2021)**

## 1 General

1.1 This document gives minimum requirements on the methods and quality levels that are to be adopted for the non-destructive testing (NDT) of ship hull structure steel welds during new building ("hull structure" as defined in UR Z23).

1.2 The quality levels given in this document refer to production quality and not to fitness-for-purpose of the welds examined.

1.3 The NDT is normally to be performed by the Shipbuilder or its subcontractors in accordance with these requirements. The Classification Surveyor may require witnessing of the testing.

1.4 It is the Shipbuilder's responsibility to assure that testing specifications and procedures are adhered to during the construction and the reports are made available to the Classification Society on the findings made by the NDT.

1.5 The extent of testing and the number of checkpoints are to be agreed between the Shipbuilder and the Classification Society. For criticality of structure reference is to be made to IACS UR S6 Tables of Structural Member Categories and IACS CSR for Bulk Carriers and Oil Tankers.

1.6 This UR covers conventional NDT methods. Advanced non-destructive testing (ANDT) methods such as phased array ultrasonic testing (PAUT), time of flight diffraction (TOFD), digital radiography (RT-D), radioscopic testing (RT-S), and computed radiography (RT-CR) are covered by UR W34.

**Note:**
1. This UR is to be uniformly implemented by IACS Societies to ships contracted for construction on or after 1 July 2021.
2. The "contracted for construction" date means the date on which the contract to build the vessel is signed between the prospective owner and the Shipbuilder. For further details regarding the date of "contract for construction", refer to IACS Procedural Requirement (PR) No. 29.
3. Rev.1 of this Unified Requirement is to be uniformly implemented by IACS Societies to ships contracted for construction on or after 1 July 2021.

1.7 **Terms and definitions**
The following terms and definitions apply for this document.

*   **NDT** Non-Destructive Testing - the development and application of technical methods to examine materials or components in ways that do not impair their future usefulness and serviceability, in order to measure geometrical characteristics and to detect, locate, measure and evaluate flaws. NDT is also known as non-destructive examination (NDE), non-destructive inspection (NDI) and non-destructive evaluation (NDE).
*   **RT** Radiographic Testing
*   **UT** Ultrasonic Testing
*   **MT** Magnetic Particle Testing
*   **PT** Dye or Liquid Penetrant Testing
*   **PWHT** Post Weld Heat Treatment
*   **VT** Visual Testing

## 2 Application

### 2.1 Base Metals
2.1.1 This document applies to fusion welds made in normal and higher strength hull structural steels in accordance with UR W11, and UR W31, high strength steels for welded structures in accordance with UR W16 and connections welds with hull steel forgings in accordance with UR W7 and hull steel castings in accordance with UR W8. Base metal other than the above may be applied by each Classification Society.

### 2.2 Welding processes
2.2.1 This document applies to fusion welds made using manual metal arc welding (shielded metal arc welding, 111), gas-shielded metal arc welding (gas metal arc welding, including flux cored arc welding, 13x), gas-shielded arc welding with non-consumable tungsten electrode (gas tungsten arc welding, 14x), submerged arc welding (12x), electro-slag welding (72x) and electro-gas welding processes (73). Terms and numbers according to ISO 4063:2009 ("x" indicates that relevant subgroups are included). This document may also be applied to welding processes other than the above at the discretion of each Classification Society.

### 2.3 Weld joints
2.3.1 This document applies to butt welds with full penetration, tee, corner and cruciform joints with or without full penetration, and fillet welds.

### 2.4 Timing of NDT
2.4.1 NDT shall be conducted after welds have cooled to ambient temperature and after post weld heat treatment where applicable.

2.4.2 For high strength steels for welded structure with specified minimum yield stress in the range of 420 N/mm² to 690 N/mm², NDT shall not be carried out before 48 hours after completion of welding. For steel with specified minimum yield greater than 690 N/mm² NDT shall not be carried out before 72 hours after completion of welding. Regardless of yield strength consideration is to be given to requiring a delayed inspection where evidence of delayed cracking has been observed in production welds.

At the discretion of the surveyor, a longer interval and/or additional random inspection at a later period may be required, (for example in case of high thickness welds).

At the discretion of the surveyor, the 72 hour interval may be reduced to 48 hours for RT or UT inspection, provided there is no indication of delayed cracking, and a complete visual and random MT or PT inspection to the satisfaction of the surveyor is conducted 72 hours after welds have been completed and cooled to ambient temperature.

Where PWHT is carried out the requirement for testing after a delay period may be relaxed, at the discretion of the surveyor.

### 2.5 Applicable methods for testing of weld joints
2.5.1 The methods mentioned in this document for detection of surface imperfections are VT, PT and MT. The methods mentioned in this document for detection of internal imperfections are UT and RT.

2.5.2 Applicable methods for testing of the different types of weld joints are given in Table 1.

**Table 1: Applicable methods for testing of weld joints**

| WELD JOINT | PARENT MATERIAL THICKNESS | APPLICABLE TEST METHODS |
| :--- | :--- | :--- |
| Butt welds with full penetration | thickness < 8mm¹ | VT, PT, MT, RT |
| | thickness ≥ 8mm | VT, PT, MT, UT, RT |
| Tee joints, corner joints and cruciform joints with full penetration | thickness < 8mm¹ | VT, PT, MT, RT³ |
| | thickness ≥ 8mm | VT, PT, MT, UT, RT³ |
| Tee joints, corner joints and cruciform joints without full penetration and fillet welds | All | VT, PT, MT, UT², RT³ |

**Notes:**
1) In cases of thickness below 8mm the Classification Society may consider application of an appropriate advanced UT method.
2) UT may be used to check the extent of penetration in tee, corner and cruciform joints. This requirement is to be agreed with the Classification Society.
3) RT may be applied however there will be limitations.

## 3 Qualification of personnel involved in NDT

3.1 The Shipbuilder or its subcontractors is responsible for the qualification and preferably 3rd party certification of its supervisors and operators to a recognised certification scheme based on ISO 9712:2012.

Personnel qualification to an employer based qualification scheme as e.g. SNT-TC-1A, 2016 or ANSI/ASNT CP-189, 2016 may be accepted if the Shipbuilder or its subcontractors written practice is reviewed and found acceptable by the Society. The Shipbuilder or its subcontractors written practice shall as a minimum, except for the impartiality requirements of a certification body and/or authorised body, comply with ISO 9712:2012.

The supervisors' and operators' certificates and competence shall comprise all industrial sectors and techniques being applied by the Shipbuilder or its subcontractors. Level 3 personnel shall be certified by an accredited certification body.

3.2 The Shipbuilder or its subcontractors shall have a supervisor or supervisors, responsible for the appropriate execution of NDT operations and for the professional standard of the operators and their equipment, including the professional administration of the working procedures. The Shipbuilder or its subcontractors shall employ, on a full-time basis, at least one supervisor independently certified to Level 3 in the method(s) concerned as per the requirements of item 3.1. It is not permissible to appoint Level 3 personnel; they must be certified by an accredited certification body. It is recognised that a Shipbuilder or its subcontractors may not directly employ a Level 3 in all the stated methods practiced. In such cases, it is permissible to employ an external, independently certified, Level 3 in those methods not held by the full-time Level 3(s) of the Shipbuilder or its subcontractors.

The supervisor shall be directly involved in review and acceptance of NDT Procedures, NDT reports, calibration of NDT equipment and tools. The supervisor shall on behalf of the Shipbuilder or its subcontractors re-evaluate the qualification of the operators annually.

3.3 The operator carrying out the NDT and interpreting indications, shall as a minimum, be qualified and certified to Level 2 in the NDT method(s) concerned and as described in item 3.1.

However, operators only undertaking the gathering of data using any NDT method and not performing data interpretation or data analysis may be qualified and certified as appropriate, at level 1.

The operator shall have adequate knowledge of materials, welding, structures or components, NDT equipment and limitations that are sufficient to apply the relevant NDT method for each application appropriately.

## 4 Surface condition

4.1 Areas to be examined shall be free from scale, slag, loose rust, weld spatter, oil, grease, dirt or paint that might affect the sensitivity of the testing method.

Preparation and cleaning of welds for subsequent NDT are to be in accordance with the accepted NDT procedures, and are to be to the satisfaction of the surveyor. Surface conditions that prevent proper interpretation may be cause for rejection of the weld area of interest.

## 5 General plan of testing: NDT method selection

5.1 The extent of testing and the associated quality levels are to be planned by the Shipbuilder according to the ship design, ship type and welding processes used. For new construction survey reference is to be made to the NDT requirements of IACS UR Z23 and the applicable parts of the UR Z23 enclosures Table 1 and Appendices.

5.2 For each construction, the Shipbuilder shall submit a plan for approval by the Classification Society, specifying the areas to be examined and the extent of testing and the quality levels, with reference to the NDT procedures to be used. Particular attention is to be paid to inspecting welds in highly stressed areas and welds in primary and special structure indicated in IACS UR S6. The NDT procedure(s) shall meet the requirement stated in section 6 of this UR and the specific requirements of the Classification Society. The plan shall only be released to the personnel in charge of the NDT and its supervision.

In selecting checkpoints, emphasis shall be given to the following inspection locations:
*   Welds in high stressed areas
*   Fatigue sensitive areas
*   Other important structural elements
*   Welds which are inaccessible or very difficult to inspect in service
*   Field erected welds
*   Suspected problem areas

Block construction welds performed in the yards, or at subcontracted yards/facilities, are to be considered in selecting checkpoints.

For other marine and offshore structures the extent is to be agreed by the Classification Society.

If an unacceptable level of indications are found the NDT extent is to be increased.

5.3 The identification system shall identify the exact locations of the lengths of weld examined.

5.4 All welds over their full length are to be subject to VT by personnel designated by the Shipbuilder, who may be exempted from the qualification requirements defined in section 3 of the UR.

5.5 As far as practicable, PT or MT shall be used when investigating the outer surface of welds, checking the intermediate weld passes and back-gouged joints prior to subsequent passes deposition. MT shall be performed in ferromagnetic materials welds unless otherwise agreed with the Classification Society. Surface inspection of important tee or corner joints, using an approved MT or PT method, shall be conducted to the satisfaction of the surveyor.

5.6 Welded connections of large cast or forged components (e.g. stern frame, stern boss, rudder parts, shaft brackets...) are to be tested over their full length using MT (MT is the preferred method) or PT, (PT is to be applied for non-ferrous metals) and at agreed locations using RT or UT.

5.7 As given in Table 1, UT or RT or a combination of UT and RT may be used for testing of butt welds with full penetration of 8mm or greater. Methods to be used shall be agreed with the Classification Society. The method used shall be suited for the detection of particular types and orientations of discontinuities. RT and UT are used for detection of internal discontinuities, and in essence they supplement and complement each other. RT is generally most effective in detecting volumetric discontinuities (e.g. porosity and slag) whilst UT is more effective for detecting planar discontinuities (e.g. laminations, lack of fusion and cracks). Although one method may not be directly relatable to the other, either one would indicate conditions of inadequate control of the welding process.

5.8 In general start/stop points in welds made using automatic or fully mechanized welding processes are to be examined using RT or UT, except for internal members where the extent of testing is to be agreed with the attending surveyor.

5.9 Where the surveyor becomes aware that an NDT location has been repaired without a record of the original defect, the shipyard is to carry out additional examinations on adjacent areas to the repaired area to the satisfaction of the attending surveyor. Reference is to be made to UR Z23.

5.10 Welds in thick steels (>50mm) used in container carrier, deck and hatch coaming areas are to be inspected in accordance with the additional requirements in IACS UR S33.

## 6 Testing

### 6.1 General
6.1.1 The testing method, equipment and conditions shall comply with recognized National or International standards, or other documents to the satisfaction of the Classification Society.

6.1.2 Sufficient details shall be given in a written procedure for each NDT technique submitted to the Classification Society for acceptance.

6.1.3 The testing volume shall be the zone which include the weld and parent material for at least 10mm each side of the weld, or the width of the heat affected zone (HAZ), whichever is greater. In all cases inspection shall cover the whole testing volume.

6.1.4 Provision is to be made for the surveyor to verify the inspection, reports and records (e.g. radiographs) on request.

### 6.2 Visual testing (VT)
6.2.1 The personnel in charge of VT is to confirm that the surface condition is acceptable prior to carrying out the inspection. VT shall be carried out in accordance with standards agreed between the Shipbuilder and the Classification Society.

### 6.3 Liquid penetrant testing (PT)
6.3.1 PT shall be carried out in accordance to ISO 3452-1:2013 or a recognized accepted standard and the specific requirement of each Classification Society.

6.3.2 The extent of PT shall be in accordance to the plans agreed with the attending surveyor and to the satisfaction of the surveyor.

6.3.3 The surface to be examined shall be clean and free from scale, oil, grease, dirt or paint so there are not contaminants and entrapped material that may impede penetration of the inspection media.

6.3.4 The temperature of parts examined shall be typically between 5°C and 50°C, outside this temperature range special low/high temperature penetrant and reference comparator blocks shall be used.

### 6.4 Magnetic particle testing (MT)
6.4.1 MT shall be carried out in accordance to ISO 17638:2016 or a recognized accepted standard and the specific requirement of each Classification Society.

6.4.2 The extent of MT shall be in accordance to the plans agreed with the attending surveyor and to the satisfaction of the surveyor.

6.4.3 The surface to be examined shall be free from scale, weld spatter, oil, grease, dirt or paint and shall be clean and dry. In general, the inside and outside of the welds to be inspected need to be sufficiently free from irregularities that may mask or interfere with interpretation.

### 6.5 Radiographic testing (RT)
6.5.1 RT shall be carried out in accordance to ISO 17636-1:2013 or an accepted recognized standard and any specific requirement of Classification Society.

6.5.2 The minimum inspected weld length for each checkpoint is to be specified in the approved NDT plan (see 5.2) and shall follow the requirements of each Classification Society.

For hull welds the minimum length inspected by RT is typically 300mm. The extent of RT shall be in accordance to the approved plans and to the satisfaction of the surveyor.

Consideration may be given for reduction of inspection frequency for automated or fully mechanized welds where quality assurance techniques indicate consistent satisfactory quality. The number of checkpoints is to be increased if the proportion of non-conforming indications is abnormally high.

6.5.3 The inside and outside surfaces of the welds to be radiographed are to be sufficiently free from irregularities that may mask or interfere with interpretation. Surface conditions that prevent proper interpretation of radiographs may be cause for rejection of the weld area of interest.

### 6.6 Ultrasonic testing (UT)
6.6.1 UT shall be carried out according to procedure based on ISO 17640:2018 (testing procedure), ISO 23279:2017 (characterization) and ISO 11666:2018 (acceptance levels) or accepted standards and the specific requirements of the Classification Society.

6.6.2 The minimum inspected weld length for each checkpoint is to be specified in the approved NDT plan (see 5.2) and shall follow the requirements of each Classification Society.

The extent of UT shall be in accordance to the approved plans and to the satisfaction of the surveyor.

A checkpoint shall consist of the entire weld length or a length agreed with the Classification Society.

## 7 Acceptance Levels (criteria)

### 7.1 General
7.1.1 This section details the acceptance levels (criteria) followed for the assessment of the NDT results. Techniques include but are not limited to: VT, MT, PT, RT and UT.

7.1.2 As far as necessary, testing techniques shall be combined to facilitate the assessment of indications against the acceptance criteria.

7.1.3 The assessment of indications not covered by this document shall be made in accordance with a standard agreed with the Classification Society. Alternative acceptance criteria can be agreed with the Classification Society, provided equivalency is established.

The general accepted methods for testing of welds are provided in Table 2 and Table 3 for surface and embedded discontinuities respectively. Refer to ISO 17635:2016.

**Table 2. Method for detection of surface discontinuities (All type of welds including fillet welds)**

| Materials | Testing Methods |
| :--- | :--- |
| Ferritic Steel | VT |
| | VT, MT |
| | VT, PT |

**Table 3. NDT for detection of embedded discontinuities (for butt and T joints with full penetration)**

| Materials and type of joint | Nominal thickness (t) of the parent material to be welded (mm) | | |
| :--- | :--- | :--- | :--- |
| | **t < 8** | **8 ≤ t ≤ 40** | **t > 40** |
| Ferritic butt-joints | RT or UT¹ | RT or UT | UT or RT² |
| Ferritic T-joints | UT¹ or RT² | UT or RT² | UT or RT² |

**Notes:**
1) Below 8mm the Classification Society may consider application of an appropriate advanced UT method.
2) RT may be applied however there will be limitations.

### 7.2 Quality Levels.
Testing requirements follows the designation of a particular quality level of imperfections in fusion-welded joints in accordance with ISO 5817:2014. Three quality levels (B, C and D) are specified.

In general Quality level C is to be applied for hull structure.

Quality level B corresponds to the highest requirement on the finished weld, and may be applied on critical welds.

This standard applies to steel materials with thickness above 0.5 mm. ISO 5817:2014 Table 1 provides the requirements on the limits of imperfections for each quality level. ISO 5817:2014 Annex A also provides examples for the determination of percentage of imperfections (number of pores in surface percent).

All levels (B, C and D) refer to production quality and not to the fitness for purpose (ability of product, process or service to serve a defined purpose under specific conditions). The correlation between the quality levels defined in ISO 5817:2014, testing levels/ techniques and acceptance levels (for each NDT technique) will serve to define the purpose under specific conditions. The acceptance level required for examination shall be agreed with the Classification Society. This will determine the quality level required in accordance with the non-destructive technique selected. Refer to tables 4 to 9.

### 7.3 Testing Levels.
7.3.1 The testing coverage and thus the probability of detection increases from testing level A to testing level C. The testing level shall be agreed with the Classification Society. Testing level D is intended for special applications, this can only be used when defined by specification. ISO 17640:2018 Annex A tables A.1 to A.7 provide guidance on the selection of testing levels for all type of joints in relation to the thickness of parent material and inspection requirements.

7.3.2 The testing technique used for the assessment of indications shall also be specified.

### 7.4 Acceptance Levels.
7.4.1 The acceptance levels are specified for each testing technique used for performing the inspection. The criteria applied is to comply with each standard identified in tables 4 to 9 (or any recognized acceptable standard agreed with the Classification Society).

7.4.2 Probability of detection (POD) indicates the probability that a testing technique will detect a given flaw.

### 7.5 Visual testing (VT)
7.5.1 The acceptance levels and required quality levels for VT are provided in IACS Rec 47 and Table 4 below.

**Table 4. Visual testing**

| Quality Levels (ISO 5817:2014 applies)ᵃ | Testing Techniques/ levels (ISO 17637:2016 applies)ᵃ | Acceptance levelsᵇ |
| :--- | :--- | :--- |
| B | Level not specified | B |
| C | | C |
| D | | D |

ᵃ Or any recognized standard agreed with Classification Society and demonstrated to be acceptable
ᵇ The acceptance levels for VT are the same to the quality levels requirements of ISO 5817:2014

### 7.6 Penetrant testing (PT)
7.6.1 The acceptance levels and required quality levels for PT are provided in Table 5 below:

**Table 5. Penetrant Testing**

| Quality Levels (ISO 5817:2014 applies)ᵃ | Testing Techniques/ levels (ISO 3452-1:2013 applies)ᵃ | Acceptance levels (ISO 23277:2015 applies)ᵃ |
| :--- | :--- | :--- |
| B | Level not specified | 2X |
| C | | 2X |
| D | | 3X |

ᵃ Or any recognized standard agreed with Classification Society and demonstrated to be acceptable

### 7.7 Magnetic Particle testing (MT)
7.7.1 The acceptance levels and required quality levels for MT is provided in Table 6 below:

**Table 6. Magnetic Particle Testing**

| Quality Levels (ISO 5817:2014 applies)ᵃ | Testing Techniques/ levels (ISO 17638:2016 applies)ᵃ | Acceptance levels (ISO 23278:2015 applies)ᵃ |
| :--- | :--- | :--- |
| B | Level not specified | 2X |
| C | | 2X |
| D | | 3X |

ᵃ Or any recognized standard agreed with Classification Society and demonstrated to be acceptable

### 7.8 Radiographic testing (RT)
7.8.1 The acceptance levels and required quality levels for RT are provided in Table 7 below. Reference radiographs for the assessment of weld imperfections shall be provided in accordance to ISO 5817:2014 or acceptable recognized standard agreed with the Classification Society.

**Table 7. Radiographic Testing**

| Quality Levels (ISO 5817:2014 applies)ᵃ | Testing Techniques/ levels (ISO 17636-1:2013 applies)ᵃ | Acceptance levels (ISO 10675-1:2016 applies)ᵃ |
| :--- | :--- | :--- |
| B | B (class) | 1 |
| C | Bᵇ (class) | 2 |
| D | At least A (class) | 3 |

ᵃ Or any recognized standard agreed with Classification Society and demonstrated to be acceptable
ᵇ For circumferential weld testing, the minimum number of exposures may correspond to the requirements of ISO 17636-1:2013, class A

### 7.9 Ultrasonic testing (UT)
7.9.1 The acceptance levels and required quality levels for UT are provided in Tables 8 and 9 below:

**Table 8. Ultrasonic Testing**

| Quality Levels (ISO 5817:2014 applies) ᵃ, ᵇ | Testing Techniques/Levels (ISO 17640:2018 applies) ᵃ, ᵇ | Acceptance Levels (ISO 11666:2018 applies)ᵃ, ᵇ |
| :--- | :--- | :--- |
| B | at least B | 2 |
| C | at least A | 3 |
| D | at least A | 3ᶜ |

ᵃ Or any recognized standard agreed with Classification Society and demonstrated to be acceptable
ᵇ When characterization of indications is required, ISO 23279:2017 is to be applied
ᶜ UT is not recommended but can be defined in a specification with same requirement as Quality Level C

**Table 9. Recommended Testing and Quality Levels (ISO 17640)**

| Testing Levelᵃ,b,c (ISO 17640:2018 applies) | Quality Level (ISO 5817:2014 applies) |
| :--- | :--- |
| A | C, D |
| B | B |
| C | By agreement |
| D | Special application |

ᵃ POD increases from testing level A to C as testing coverage increases
ᵇ Testing Level D for special application shall be agreed with Classification Society
ᶜ Specific requirements for testing levels A to C, are provided for various types of joints in ISO 17640:2018 Annex A

7.9.2 UT Acceptance Levels apply to the examination of full penetration ferritic steel welds, with thickness from 8 mm to 100mm. The nominal frequency of probes used shall be between 2MHz and 5MHz. Examination procedures for other type of welds, material, thicknesses above 100 mm and examination conditions shall be submitted to the consideration of the Classification Society.

7.9.3 The acceptance levels for UT of welds are to be defined in accordance to ISO 11666:2018 requirements or any recognized acceptable standard agreed with the Classification Society. The standard specifies acceptance level 2 and 3 for full penetration welded joints in ferritic steels, corresponding to quality levels B and C (Refer to table 8).

7.9.4 Sensitivity settings and levels. The sensitivity levels are set by the following techniques:
*   Technique 1: based on 3mm diameter side- drilled holes
*   Technique 2: based on distance gain size (DGS) curves for flat bottom holes (disk shaped reflectors)
*   Technique 3: using a distance-amplitude-corrected (DAC) curve of a rectangular notch of 1mm depth and 1mm width
*   Technique 4: using the tandem technique with reference to a 6mm diameter flat bottom hole (disk shaped reflector)

The evaluation levels (reference, evaluative, recording and acceptance) are specified in ISO 11666:2018 Annex A.

## 8 Reporting

8.1 Reports of NDT required shall be prepared by the Shipbuilder and shall be made available to the Classification Society.

8.2 Reports of NDT shall include the following generic items:
*   Date of testing
*   Hull number, location and length of weld inspected
*   Names, qualification level and signature of personnel that have performed the testing
*   Identification of the component examined
*   Identification of the welds examined
*   Steel grade, type of joint, thickness of parent material, welding process
*   Acceptance criteria
*   Testing standards used
*   Testing equipment and arrangement used
*   Any test limitations, viewing conditions and temperature
*   Results of testing with reference to acceptance criteria, location and size of reportable indications
*   Statement of acceptance / non-acceptance, evaluation date, name and signature of evaluator
*   Number of repairs if specific area repaired more than twice

8.3 In addition to generic items, reports of PT shall include the following specific items:
*   Type of penetrant, cleaner and developer used
*   Penetration time and development time

8.4 In addition to generic items, reports of MT shall include the following specific items:
*   Type of magnetization
*   Magnetic field strength
*   Detection media
*   Viewing conditions
*   Demagnetization, if required

8.5 In addition to generic items, reports of RT shall include the following specific items:
*   Type and size of radiation source (width of radiation source), X-ray voltage
*   Type of film/designation and number of film in each film holder/cassette
*   Number of radiographs (exposures)
*   Type of intensifying screens
*   Exposure technique, time of exposure and source-to-film distance as per below:
*   Distance from radiation source to weld
*   Distance from source side of the weld to radiographic film
*   Angle of radiation beam through the weld (from normal)
*   Sensitivity, type and position of IQI (source side or film side)
*   Density
*   Geometric un-sharpness
*   Specific acceptance class criteria for RT

Examinations used for acceptance or rejection of welds shall be recorded in an acceptable medium. A written record providing following information: identification and description of welds, procedures and equipment used, location within recorded medium and results shall be included. The control of documentation unprocessed original images and digitally processes images is to be to the satisfaction of the surveyor.

8.6 In addition to generic items, reports of UT shall include the following specific items:
*   Type and identification of ultrasonic equipment used (instrument maker, model, series number), probes (instrument maker, serial number), transducer type (angle, serial number and frequency) and type of couplant (brand).
*   Sensitivity levels calibrated and applied for each probe
*   Transfer loss correction applied Type of reference blocks
*   Signal response used for defect detection
*   Reflections interpreted as failing to meet acceptance criteria

The method for review and evaluation of UT reports is required for adequate quality control and is to be to the satisfaction of the surveyor.

8.7 The shipyard is to keep the inspection records specified in 8.2 to 8.6 of this document for at least 5 years.

## 9 Unacceptable indications and repairs

9.1 Unacceptable indications shall be eliminated and repaired where necessary. The repair welds are to be examined on their full length using appropriate NDT method at the discretion of the Surveyor.

9.2 When unacceptable indications are found, additional areas of the same weld length shall be examined unless it is agreed with the surveyor and fabricator that the indication is isolated without any doubt. In case of automatic or fully mechanized welded joints, additional NDT shall be extended to all areas of the same weld length.

All radiographs exhibiting non-conforming indications are to be brought to the attention of the surveyor. Such welds are to be repaired and inspected as required by the surveyor. When non-conforming indications are observed at the end of a radiograph, additional RT is generally required to determine their extent. As an alternative, the extent of non-conforming welds may be ascertained by excavation, when approved by the surveyor.

9.3 The extent of testing can be extended at the surveyor's discretion when repeated non-acceptable discontinuities are found.

9.4 The inspection records specified in section 8 are to include the records of repaired welds.

9.5 The Shipbuilder shall take appropriate actions to monitor and improve the quality of welds to the required level. The repair rate is to be recorded by the shipyard and any necessary corrective actions are to be identified in the builder's QA system.

**End of Document**


================================================================================
# FILE: UR_W/ur-w34.md
================================================================================

# W34 Advanced non-destructive testing of materials and welds

**(Dec 2019)**

## 1. General

1.1 This document gives minimum requirements on the methods and quality levels that are to be adopted for the advanced non-destructive testing (ANDT) of materials and welds during new building of ships. The advanced methods intended for use under this UR are listed in Section 2.

1.2 The ANDT is to be performed by the shipbuilder, manufacturer or its subcontractors in accordance with these requirements. The Classification Society's surveyor may require witnessing testing.

1.3 It is the shipbuilder's or manufacturer's responsibility to ensure that testing specifications and procedures are adhered to during the construction, and the report is to be made available to the Classification Society on the findings made by the ANDT.

1.4 The extent and method of testing, and the number of checkpoints are normally agreed between the shipyard and the Classification Society.

1.5 Terms and definitions

The following terms and definitions apply for this document.

| Term | Definition |
| :--- | :--- |
| **ANDT** | Advanced non-destructive testing |
| **RT-D** | Digital Radiography |
| **RT-S** | Radioscopic testing with digital image acquisition (dynamic ≥ 12 bit) |
| **RT-CR** | Testing with computed radiography using storage phosphor imaging plates |
| **PAUT** | Phased Array Ultrasonic Testing |
| **TOFD** | Time of Flight Diffraction |
| **AUT** | Automated Ultrasonic Examinations. A technique of ultrasonic examination performed with equipment and search units that are mechanically mounted and guided, remotely operated, and motor-controlled (driven) without adjustments by the technician. The equipment used to perform the examinations is capable of recording the ultrasonic response data, including the scanning positions, by means of integral encoding devices such that imaging of the acquired data can be performed. |
| **SAUT** | Semi-Automated Ultrasonic Examinations. A technique of ultrasonic examination performed with equipment and search units that are mechanically mounted and guided, manually assisted (driven), and which may be manually adjusted by the technician. The equipment used to perform the examinations is capable of recording the ultrasonic response data, including the scanning positions, by means of integral encoding devices such that imaging of the acquired data can be performed. |

**Note:**
1. This UR is to be uniformly implemented by IACS Societies to ships contracted for construction on or after 1 July 2021.
2. The "contracted for construction" date means the date on which the contract to build the vessel is signed between the prospective owner and the shipbuilder. For further details regarding the date of "contract for construction", refer to IACS Procedural Requirement (PR) No. 29.

## 2. Applicability

### 2.1 Materials

2.1.1 This document applies to the following materials and manufactured products:
- Material and welding for gas tankers in accordance with UR W1
- Normal and higher strength hull structural steels in accordance with UR W11
- High strength steels for welded structures in accordance with UR W16
- Hull steel forgings in accordance with UR W7
- Hull and machinery steel castings in accordance with UR W8
- Extremely Thick Steel Plates in Container Ships in accordance with UR S33
- Cast Copper Alloy propellers in accordance with UR W24
- Aluminium alloys for hull construction in accordance with UR W25
- Cast Steel Propellers in accordance with UR W27
- YP47 Steels and Brittle Crack Arrest Steels in accordance with UR W31
- Hull and machinery steel forgings in accordance with REC68
- Marine steel castings in accordance with REC69

### 2.2 Welding processes

2.2.1 This document applies to welding processes specified in Table 1. ANDT of welding process unspecified in Table 1 is to be to the satisfaction of the Classification Society.

**Table 1: Applicable welding process**

| Welding process | ISO 4063:2009 |
| :--- | :--- |
| **Manual welding** | Shield Metal Arc Welding (SMAW) | 111 |
| **Resistance welding** | Flash welding (FW) | 24 |
| **Semi-automatic welding** | (1) Metal Inert Gas welding (MIG)<br>(2) Metal Active Gas welding (MAG)<br>(3) Flux Cored Arc Welding (FCAW) | 131<br>135, 138<br>136 |
| **TIG welding** | Gas Tungsten Arc Welding (GTAW) | 141 |
| **Automatic welding** | (1) Submerged Arc Welding (SAW)<br>(2) Electro-gas Welding (EGW)<br>(3) Electro-slag Welding (ESW) | 12<br>73<br>72 |

### 2.3 Weld joints

2.3.1 This document applies to butt welds with full penetration. Variations of joint design, for example, tee, corner and cruciform joints (with or without full penetration) can be tested using PAUT. The constraints of joint design with respect to testing are to be recognized, documented, and agreed with the Society before application.

### 2.4 Timing of ANDT

2.4.1 ANDT are to be conducted after welds have cooled to ambient temperature and after post weld heat treatment where applicable.

2.4.2 Timing of ANDT on ship hull welds on steels with specified minimum yield stress in the range of 420 N/mm² to 690 N/mm² shall be in accordance with 2.4.2 of UR W33 Non-destructive testing of ship hull steel welds.

### 2.5 Testing methods

2.5.1 The methods mentioned in this document for detection of imperfections are PAUT (only automated / semi-automated PAUT), TOFD, RT-D.

2.5.2 Applicable methods for testing of the different types of materials and weld joints are given in Table 2.

**Table 2: Applicable methods for testing of materials and weld joints**

| MATERIALS AND WELD JOINTS | PARENT MATERIAL THICKNESS | APPLICABLE METHODS |
| :--- | :--- | :--- |
| Ferritic butt welds with full penetration | thickness < 6mm | RT-D |
| | 6 mm ≤ thickness ≤ 40 mm | PAUT, TOFD, RT-D |
| | thickness > 40mm | PAUT, TOFD, RT-D* |
| Ferritic tee joints and corner joints with full penetration | thickness ≥ 6mm | PAUT, RT-D* |
| Ferritic cruciform joints with full penetration | thickness ≥ 6mm | PAUT* |
| Austenitic stainless steel butt welds with full penetration¹ | thickness < 6mm | RT-D |
| | 6 mm ≤ thickness ≤ 40 mm | RT-D, PAUT* |
| | thickness > 40mm | PAUT*, RT-D* |
| Austenitic stainless steel tee joints, corner joints with full penetration¹ | thickness ≥ 6mm | PAUT*, RT-D* |
| Aluminum tee joints and corner joints with full penetration | thickness ≥ 6mm | PAUT*, RT-D* |
| Aluminum cruciform joints with full penetration | thickness ≥ 6mm | PAUT* |
| Aluminum butt welds with full penetration | thickness < 6mm | RT-D |
| | 6 mm ≤ thickness ≤ 40 mm | RT-D, TOFD, PAUT |
| | thickness > 40mm | TOFD, PAUT, RT-D* |
| Cast Copper Alloy | All | PAUT, RT-D* |
| Steel forgings | All | PAUT, RT-D* |
| Steel castings | All | PAUT, RT-D* |
| Base materials/Rolled steels, Wrought Aluminum Alloys | thickness < 6mm | RT-D |
| | 6 mm ≤ thickness ≤ 40 mm | PAUT, TOFD, RT-D |
| | thickness > 40mm | PAUT, TOFD, RT-D* |

\* Only applicable with limitations, need special qualification subject to acceptance by Classification Society.

**Note:** 1) The ultrasonic testing of anisotropic material using advanced methods will require specific procedures and techniques. Additionally, the use of complementary techniques and equipment may also be required, e.g. using angle compression waves, and/or creep wave probes for detecting defects close to the surface.

## 3. Qualification of personnel involved in ANDT

3.1 The Shipbuilder, manufacturer or its subcontractors is responsible for the qualification and preferably 3rd party certification of its supervisors and operators to a recognised certification scheme based on ISO 9712:2012.

Personnel qualification to an employer based qualification scheme as e.g. SNT-TC-1A, 2016 or ANSI/ASNT CP-189, 2016 may be accepted if the Shipbuilder, manufacturer or its subcontractors written practice is reviewed and found acceptable by the Society. The Shipbuilder, manufacturer or its subcontractors written practice shall as a minimum, except for the impartiality requirements of a certification body and/or authorised body, comply with ISO 9712:2012.

The supervisors' and operators' certificates and competence shall comprise all industrial sectors and techniques being applied by the Shipbuilder or its subcontractors. Level 3 personnel shall be certified by an accredited certification body.

3.2 The Shipbuilder, manufacturer or its subcontractors shall have a supervisor or supervisors, responsible for the appropriate execution of NDT operations and for the professional standard of the operators and their equipment, including the professional administration of the working procedures. The Shipbuilder, manufacturer or its subcontractors shall employ, on a full-time basis, at least one supervisor independently certified to Level 3 in the method(s) concerned as per the requirements of item 3.1. It is not permissible to appoint Level 3 personnel; they must be certified by an accredited certification body. It is recognised that a Shipbuilder, manufacturer or its subcontractors may not directly employ a Level 3 in all the stated methods practiced. In such cases, it is permissible to employ an external, independently certified, Level 3 in those methods not held by the full-time Level 3(s) of the Shipbuilder, manufacturer or its subcontractors.

The supervisor shall be directly involved in review and acceptance of NDT Procedures, NDT reports, calibration of NDT equipment and tools. The supervisor shall on behalf of the Shipbuilder, manufacturer or its subcontractors re-evaluate the qualification of the operators annually.

3.3 The operator carrying out the NDT and interpreting indications, shall as a minimum, be qualified and certified to Level 2 in the NDT method(s) concerned and as described in item 3.1.

However, operators only undertaking the gathering of data using any NDT method and not performing data interpretation or data analysis may be qualified and certified as appropriate, at level 1.

The operator shall have adequate knowledge of materials, weld, structures or components, NDT equipment and limitations that are sufficient to apply the relevant NDT method for each application appropriately.

## 4. Technique and procedure qualification

### 4.1 General

The shipbuilder or manufacturer has to submit to the Classification Society the following documentation for review:
- The technical documentation of the ANDT.
- The operating methodology and procedure of the ANDT according to section 7.
- Result of software simulation, when applicable.

### 4.2 Software simulation

Software simulation may be required by the Classification Society, when applicable for PAUT or TOFD techniques. The simulation may include initial test set-up, scan plan, volume coverage, result image of artificial flaw etc.. In some circumstances, artificial defect modeling/simulation may be needed or required by the project.

### 4.3 Procedure qualification test

The procedure qualification for ANDT system shall include the following steps:
- Review of available performance data for the inspection system (detection abilities and defect sizing accuracy).
- Identification and evaluation of significant parameters and their variability.
- Planning and execution of a repeatability and reliability test programme¹ which including onsite demonstration.
- Documentation of results from the repeatability and reliability test programs.

**Note:** 1) The data from the repeatability and reliability test program is to be analyzed with respect to comparative qualification block test report and onsite demonstration. The qualification block shall be in accordance with ASME V Article 14 MANDATORY APPENDIX II UT PERFORMANCE DEMONSTRATION CRITERIA or agreed by the Classification Society, and at least the intermediate level qualification blocks shall be used. The high level qualification blocks shall be used when sizing error distributions and an accurate POD need to be evaluated. The demonstration process onsite shall be witnessed by the Classification Society's surveyor.

### 4.4 Procedure approval

The testing procedure is to be evaluated based upon the qualification results, if satisfactory the procedure can be considered approved.

### 4.5 Onsite review

For the test welds, supplementary NDT shall be performed on an agreed proportion of welds to be cross checked with other methods. Alternatively, other documented reference techniques may be applied to compare with ANDT results.

Data analyses shall be performed in accordance with the above activities. Probability of Detection (PoD) and sizing accuracy shall be established when applicable.

When the result of inspection review does not conform to the approved procedure, the inspection shall be suspended immediately. Additional procedure review qualification and demonstration shall be undertaken to account for any nonconformity.

When a significant nonconformity is found, the Classification Society has the right to reject the results of such activities.

## 5. Surface condition

5.1 Area to be examined shall be free from scale, loose rust, weld spatter, oil, grease, dirt or paint that might affect the sensitivity of the testing method.

5.2 Where there is a requirement to carry out PAUT or TOFD through paint, the suitability and sensitivity of the test shall be confirmed through an appropriate transfer correction method defined in the procedure. In all cases, if transfer losses exceed 12 dB, the reason shall be considered and further preparation of the scanning surfaces shall be carried out, if applicable. If testing is done through paint, then the procedure shall be qualified on a painted surface.

5.3 The requirement for acceptable test surface finish is to ensure accurate and reliable detection of defects. For the testing of welds, where the test surface is irregular or has other features likely to interfere with the interpretation of NDT results, the weld is to be ground or machined.

## 6. General plan of testing: NDT method selection

6.1 The extent of testing shall be planned by the shipbuilder or manufacturer according to the ship design, ship or equipment type and welding processes used. Particular attention shall be paid to highly stressed areas. The extent of testing shall be in accordance with UR or REC applicable with material of weld examined.

## 7. Testing requirements

### 7.1 General

7.1.1 The shipyard or manufacturer is to ensure that personnel carrying out NDT or interpreting the results of NDT are qualified to the appropriate level as detailed in section 3.

7.1.2 Procedures
(1) All NDT are to be carried out to a procedure that is representative of the item under inspection.
(2) Procedures are to identify the component to be examined, the NDT method, equipment to be used and the full extent of the examinations including any test restrictions.
(3) Procedures are to include the requirement for components to be positively identified and for a datum system or marking system to be applied to ensure repeatability of inspections.
(4) Procedures are to include the method and requirements for equipment calibrations and functional checks, together with specific technique sheets / scan plans, for the component under test.
(5) Procedures are to be approved by personnel qualified to Level III in the appropriate technique in accordance with a recognised standard.
(6) Procedures are to be reviewed by the Classification Society's Surveyor.

7.1.3 The methods considered within the application of this UR are defined in section 2.5.1

7.1.4 PAUT techniques shall conform as a minimum to section 7.2 of this UR. Depending on the complexity of the item under test and the access to surfaces, there may be a requirement for additional scans and/or complementary NDT techniques to ensure that full coverage of the item is achieved.

7.1.4.1 PAUT of welds shall include a linear scan of the fusion face, together with other scans as defined in the specific test technique. Refer to linear scan requirements in section 7.2.2.4

7.1.5 TOFD techniques shall conform as a minimum to section 7.3 of this UR. Depending on the complexity of the item under test and the access to surfaces, there may be a requirement for additional scans and/or complementary NDT techniques to ensure that full coverage of the item is achieved.

7.1.6 RT-D techniques shall conform as a minimum to section 7.4 of this UR. For the purpose of this UR, RT-D comprises of two main RT methods; RT-S and RT-CR. Other methods may be included (e.g. radioscopy systems), however, then must conform to this UR as applicable, and any specific requirements shall demonstrate equivalence to these requirements.

7.1.6.1 In all RT-D methods, in addition to specific requirements, detector output quality control methods shall be described within the procedure.

7.1.6.2 The procedure shall define the level of magnification, post-processing tools, image/data security and storage, for final evaluation and reporting.

### 7.2 Phased array ultrasonic testing

PAUT shall be carried out according to procedures based on ISO 13588:2019, ISO 18563-1:2015, ISO 18563-2:2017, ISO 18563-3:2015 and ISO 19285:2017 or recognized standards and the specific requirements of the Classification Society.

#### 7.2.1 Information required prior to testing

A procedure shall be written and include the following information as in minimum shown in table 3. When an essential variable in Table 3 is to change from the specified value, or range of values, the written procedure shall require requalification. When a nonessential variable is to change from the specified value, or range of values, requalification of the written procedure is not required. All changes of essential or nonessential variables from the value, or range of values, specified by the written procedure shall require revision of, or an addendum to, the written procedure.

**Table 3: Requirements of a PAUT Procedure**

| Requirement | Essential Variable | Nonessential Variable |
| :--- | :---: | :---: |
| Material types or weld configurations to be examined, including thickness dimensions and material product form (castings, forgings, pipe, plate, etc.) | X | ... |
| The surfaces from which the examination shall be performed | X | ... |
| Technique(s) (straight beam, angle beam, contact, and/or immersion) | X | ... |
| Angle(s) and mode(s) of wave propagation in the material | X | ... |
| Search unit type, frequency, element size and number, pitch and gap dimensions, and shape | X | ... |
| Focal range (identify plane, depth, or sound path) | X | ... |
| Virtual aperture size (i.e., number of elements, effective height¹, and element width) | X | ... |
| Focal laws for E-scan and S-scan (i.e., range of element numbers used, angular range used, element or angle increment change) | X | ... |
| Special search units, wedges, shoes, or saddles, when used | X | ... |
| Ultrasonic instrument(s) | X | ... |
| Calibration [calibration block(s) and technique(s)] | X | ... |
| Directions and extent of scanning | X | ... |
| Scanning (manual vs. automatic) | X | ... |
| Method for sizing indications and discriminating geometric from flaw indications | X | ... |
| Computer enhanced data acquisition, when used | X | ... |
| Scan overlap (decrease only) | X | ... |
| Personnel performance requirements, when required | X | ... |
| testing levels, acceptance levels and/or recording levels | X | ... |
| Personnel qualification requirements | ... | X |
| Surface condition (examination surface, calibration block) | ... | X |
| Couplant (brand name or type) | ... | X |
| Post-examination cleaning technique | ... | X |
| Automatic alarm and/or recording equipment, when applicable | ... | X |
| Records, including minimum calibration data to be recorded (e.g., instrument settings) | ... | X |
| Environmental and safety issues | ... | X |

**Note:** 1) Effective height is the distance from the outside edge of the first to last element used in the focal law.

#### 7.2.2 Testing

**7.2.2.1 Testing levels**
The testing levels specified in the testing procedure shall be in accordance with recognized standards accepted by the Classification Society. Four testing levels are specified in ISO 13588:2019, each corresponding to a different probability of detection of imperfections.

**7.2.2.2 Weld Examinations**
The weld examinations shall in accordance with ISO 13588:2019 and the additional special requirements of this UR.

**7.2.2.3 Material Examinations**
Material examinations shall conform to section 2.1 as a minimum.

**7.2.2.4 Volume to be inspected**
The purpose of the testing shall be defined by the testing procedure. Based on this, the volume to be inspected shall be determined.

A scan plan shall be provided. The scan plan shall show the beam coverage, the weld thickness and the weld geometry.

If the evaluation of the indications is based on amplitude only, it is a requirement that an 'E' scan (or linear scan) shall be utilized to scan the fusion faces of welds, so that the sound beam is perpendicular to the fusion face +/- 5 degrees. This requirement may be omitted if an 'S' (or sectorial) scan can be demonstrated to verify that discontinuities at the fusion face can be detected and sized, using the stated procedure (note, this demonstration shall utilize reference blocks containing suitable reflectors in location of fusion zone).

**7.2.2.5 Reference blocks**
Depending on the testing level, a reference block shall be used to determine the adequacy of the testing (e.g. coverage, sensitivity setting). The design and manufacture of reference blocks shall be in accordance with ISO 13588:2019 or recognized equivalent standards and the specific requirements of the Classification Society.

**7.2.2.6 Indication assessment**
Indications detected when applying testing procedure shall be evaluated either by length and height or by length and maximum amplitude. Indication assessment shall be in accordance with ISO 19285:2017 or recognized standards and the specific requirements of the Classification Society. The sizing techniques include reference levels, Time Corrected Gain (TCG), Distance Gain Size (DGS) and 6 dB drop. 6 dB drop method shall only be used for measuring the indications larger than the beam width.

### 7.3 Time of flight diffraction

TOFD shall be carried out according to procedure based on ISO 10863:2011, and ISO 15626:2018 or recognized standards and the specific requirements of the Classification Society.

#### 7.3.1 Information required prior to testing

A procedure shall be written and include the following information as shown in table 4. When an essential variable in Table 4 is to change from the specified value, or range of values, the written procedure shall require requalification. When a nonessential variable is to change from the specified value, or range of values, requalification of the written procedure is not required. All changes of essential or nonessential variables from the value, or range of values, specified by the written procedure shall require revision of, or an addendum to, the written procedure.

**Table 4: Requirements of a TOFD Procedure**

| Requirement | Essential Variable | Nonessential Variable |
| :--- | :---: | :---: |
| Weld configurations to be examined, including thickness dimensions and material product form (castings, forgings, pipe, plate, etc.) | X | ... |
| The surfaces from which the examination shall be performed | X | ... |
| Angle(s) of wave propagation in the material | X | ... |
| Search unit type(s), frequency(ies), and element size(s)/shape(s) | X | ... |
| Special search units, wedges, shoes, or saddles, when used | X | ... |
| Ultrasonic instrument(s) and software(s) | X | ... |
| Calibration [calibration block(s) and technique(s)] | X | ... |
| Directions and extent of scanning | X | ... |
| Scanning (manual vs. automatic) | X | ... |
| Data sampling spacing (increase only) | X | ... |
| Method for sizing indications and discriminating geometric from flaw indications | X | ... |
| Computer enhanced data acquisition, when used | X | ... |
| Scan overlap (decrease only) | X | ... |
| Personnel performance requirements, when required | X | ... |
| testing levels, acceptance levels and/or recording levels | X | ... |
| Personnel qualification requirements | ... | X |
| Surface condition (examination surface, calibration block) | ... | X |
| Couplant (brand name or type) | ... | X |
| Post-examination cleaning technique | ... | X |
| Automatic alarm and/or recording equipment, when applicable | ... | X |
| Records, including minimum calibration data to be recorded (e.g., instrument settings) | ... | X |
| environmental and safety issues | ... | X |

#### 7.3.2 Testing

**7.3.2.1 Testing levels**
The testing levels specified in the testing procedure shall be in accordance with recognized standards accepted by the Classification Society. Four testing levels are specified in ISO 10863:2011, each corresponding to a different probability of detection of imperfections.

**7.3.2.2 Volume to be inspected**
The purpose of the testing shall be defined by the testing procedure. Based on this, the volume to be inspected shall be determined.

A scan plan shall be provided. The scan plan shall show the locations of the probes, beam coverage, the weld thickness and the weld geometry.

**7.3.2.3** Due to the nature of the TOFD method, there is a possibility that the scan plan may reveal weld volume zones that will not receive full TOFD coverage (commonly known as dead zones, either in the lateral wave, back wall, or both). If the scan plan reveals that these dead zones are not adequately inspected, then further TOFD scans and/or complementary NDT methods shall be applied to ensure full inspection coverage.

### 7.4 Digital radiography

Digital radiography shall be performed per procedure(s) based on ISO 17636-2:2013 and standards referenced therein, or recognized standards and additional specific requirements of the Classification Society.

Any variation to applying the standard (e.g. IQI placement) shall be agreed with Classification Society.

A procedure shall be written and include the following information as shown in table 5.

**Table 5: Requirements of a Digital radiography Procedure**

| Requirement |
| :--- |
| Material types or weld configurations to be examined, including thickness dimensions and material product form (castings, forgings, pipe, plate, etc.) |
| **Digitizing System Description:** |
| Manufacturer and model no. of digitizing system |
| Physical size of the usable area of the image monitor |
| Film size capacity of the scanning device |
| Spot size(s) of the film scanning system |
| Image display pixel size as defined by the vertical/horizontal resolution limit of the monitor |
| Illuminance of the video display |
| Data storage medium |
| **Digitizing Technique:** |
| Digitizer spot size (in microns) to be used |
| Loss-less data compression technique, if used |
| Method of image capture verification |
| Image processing operations |
| Time period for system verification |
| **Spatial resolution used:** |