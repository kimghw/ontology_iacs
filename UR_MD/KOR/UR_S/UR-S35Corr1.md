Gemini response:
# S35 Buckling Strength Assessment of Ship Structural Elements

(Feb 2023)
(Corr.1 Sep 2024)

## TABLE OF CONTENTS

### SECTION 1 APPLICATION AND DEFINITIONS
1. **Application**
   1.1 General
   1.2 Application of this UR
2. **Terminology and Assumptions**
   2.1 Buckling
   2.2 Net Scantling Approach
   2.3 Structural Idealisation
   2.4 Sign Convention
3. **Assessment Methods and Acceptance Criteria**
   3.1 Assessment Methods
   3.2 Buckling Utilisation Factor
   3.3 Allowable Buckling Utilisation Factor
   3.4 Buckling Acceptance Criteria

### SECTION 2 SLENDERNESS REQUIREMENTS
1. **General**
   1.1 Introduction
2. **Stiffeners**
   2.1 Proportions of Stiffeners
3. **Primary Supporting Members**
   3.1 Proportions and Stiffness

### SECTION 3 BUCKLING REQUIREMENTS FOR HULL GIRDER PRESCRIPTIVE ANALYSIS
1. **General**
   1.1 Introduction
   1.2 Definitions
   1.3 Assumptions for Equivalent Plate Panels
2. **Buckling Criteria**
   2.1 Overall Stiffened Panel
   2.2 Plates
   2.3 Stiffeners
   2.4 Vertically Corrugated Longitudinal Bulkheads
   2.5 Horizontally Corrugated Longitudinal Bulkheads

### SECTION 4 BUCKLING REQUIREMENTS FOR DIRECT STRENGTH ANALYSIS OF HATCH COVERS
1. **General**
   1.1 Introduction
2. **Stiffened and Unstiffened Panels**
   2.1 General
   2.2 Stiffened Panels
   2.3 Unstiffened Panels
   2.4 Reference Stress
   2.5 Lateral Pressure
   2.6 Buckling Criteria

### SECTION 5 BUCKLING CAPACITY
1. **General**
   1.1 Introduction
2. **Buckling Capacity of Plate Panels**
   2.1 Overall Stiffened Panels
   2.2 Plates
   2.3 Stiffeners
   2.4 Primary Supporting Members
   2.5 Stiffened Panels with U-type Stiffeners
3. **Buckling Capacity of Column Structures**
   3.1 Column Buckling of Corrugations

### APPENDIX 1 STRESS BASED REFERENCE STRESSES
1. **Stress Based Method**
   1.1 Introduction
   1.2 Stress Application
2. **Reference Stresses**
   2.1 Regular Panel
   2.2 Irregular Panel and Curved Panel

---

**Note:**
1. This UR is to be applied by IACS Societies to ships according to the application dates, on or after 1 July 2024, of the individual IACS Unified Requirements requiring compliance with this UR S35.
2. The “contracted for construction” date means the date on which the contract to build the vessel is signed between the prospective owner and the shipbuilder. For further details regarding the date of “contract for construction”, refer to IACS Procedural Requirement (PR) No. 29.

---

## SECTION 1 APPLICATION AND DEFINITIONS

### Abbreviations
*   **EPP**: Elementary Plate Panel, as defined in [2.3.1].
*   **PSM**: Primary Supporting Member.
*   **SP**: Stiffened Panel, as defined in [2.3.3].
*   **UP**: Unstiffened Panel, as defined in [2.3.3].
*   **UR-S**: IACS Unified Requirements concerning Strength of Ships.

### 1. Application

#### 1.1 General

##### 1.1.1 Relevant Unified Requirements concerning Strength of Ships
This Unified Requirement (UR) establishes a general buckling assessment procedure as illustrated in Figure 1 and is to be applied in conjunction with UR S21 for hatch cover structures. UR S21 is referred to as Relevant UR-S hereafter in this UR.

![Figure 1: Overview of applying this UR in conjunction with Relevant UR-S](A flowchart showing the relationship between Relevant UR-S and UR S35. It illustrates how working stresses, pressures, and net scantlings flow from the Relevant UR-S into UR S35's stress-based and slenderness requirements. The assessment paths include HG (Hull Girder) prescriptive analysis, direct strength analysis for HC (Hatch Covers), and slenderness checks for stiffeners, leading to buckling check criteria like BUFs (Buckling Utilisation Factors).)

*Note: BUF stands for Buckling Utilisation Factor, HC stands for Hatch Cover, and HG stands for Hull Girder.*

#### 1.2 Application of this UR

##### 1.2.1 Sections of this UR
The buckling checks are to be performed according to:
- Sec 1 for general definitions regarding buckling capacity, allowable buckling utilisation factors and buckling check criteria.
- Sec 2 for the slenderness requirements of longitudinal and transverse stiffeners.
- Sec 3 for the prescriptive buckling requirements of plates, longitudinal and transverse stiffeners, primary supporting members and other structures subject to hull girder stresses.
- Sec 4 for direct strength analysis (usually by finite element method) buckling requirements of hatch cover structural members including plates, stiffeners and primary supporting members.
- Sec 5 for the determination of buckling capacities of plate panels, stiffeners, primary supporting members and column structures.

##### 1.2.2 Buckling assessment with this UR
For the buckling assessment of a ship hull girder, a hatch cover or some structural component, the slenderness requirements as defined in Sec 2 and the buckling requirements as defined in Sec 3 or Sec 4 are to be checked as per the requirements of the applicable Relevant UR-S.

##### 1.2.3 Alternative methods
This UR contains the general methods for the determination of buckling capacities of plate panels, stiffeners, primary supporting members, and columns. For special cases not covered in this UR, such as a whole plate structure with stiffeners in two directions (i.e., a stiffened panel with both primary and secondary stiffeners), other more advanced methods, such as finite element analysis methods, can be used as deemed appropriate by the Society.

### 2. Terminology and Assumptions

#### 2.1 Buckling

##### 2.1.1 Buckling strength
Buckling strength or capacity refers to the strength of a structure under in-plane compressions and/or shear and lateral load. Buckling strength with consideration of the buckling behaviour in [2.1.2] gives a lower bound estimate of ultimate capacity, or the maximum load a structural member can carry without suffering major permanent set.
For each structural member, its buckling strength is to be taken as corresponding to the most unfavourable or critical buckling mode.

##### 2.1.2 Buckling behaviour
Buckling strength assessment takes into account both elastic buckling and post-buckling behaviours. Post-buckling can consider the internal redistribution of loads depending on the load situation, slenderness and type of structure. Such as for the buckling assessment of plates, generally its positive elastic post-buckling effect can be utilized.

As such, for slender structures, the calculated buckling strength is typically higher than the ideal elastic buckling stress (minimum eigenvalue). Accepting elastic buckling of slender plate panels implies that large elastic deflections and reduced in-plane stiffness may occur at higher buckling utilisation levels.

#### 2.2 Net Scantling Approach

##### 2.2.1 General
Unless otherwise specified, all the scantling requirements, including slenderness requirements, in this UR are based on net scantlings obtained by removing full corrosion addition $t_c$ from the gross offered thicknesses.

##### 2.2.2 Corrosion addition
Corrosion addition $t_c$ referred to in this UR is defined in the Relevant UR-S.

##### 2.2.3 Stress calculation models
The structural models used for the calculation of stresses to be applied for buckling assessment, which are usually based on net scantlings, are defined in the Relevant UR-S.

#### 2.3 Structural Idealisation

##### 2.3.1 Elementary plate panel
An elementary plate panel (EPP) is the unstiffened part of the plating between stiffeners and/or primary supporting members. The plate panel length, $a$, and breadth, $b$, of the EPP are defined respectively as the longest and shortest plate edges, as shown in Figure 2.

![Figure 2: Elementary plate panel (EPP) definition](Diagrams illustrating EPP definitions for longitudinal/horizontal framing and transverse/vertical framing. $a$ is the longer dimension, $b$ is the shorter dimension. It shows strake considered, PSM or stiffener locations, and the framing direction.)

##### 2.3.2 Standard types of stiffeners
Definitions of the cross-sectional dimensions of typical stiffener types are shown in Figure 3, which are flat bars, bulb flats, angles, L2 and T bars. If applicable, other types of stiffeners can be idealized to one of the typical types in Figure 3 for buckling check. For the U-type stiffener which is usually fitted in some hatch covers, the definition of its cross-sectional dimensions is shown in Figure 4.

Unless otherwise specified, the full span or full length $l$, in mm, of a stiffener is to be used for buckling check, which equals to the spacing between primary supporting members.

Symbolic dimensions of the cross-sections are as below:
*   $b_1$: Width of the attached plate enclosed by the U-type stiffener, in mm, as shown in Figure 4.
*   $b_2$: Width of the attached plate between adjacent U-type stiffeners, in mm, as shown in Figure 4.
*   $b_f$: Width of the flange or face plate of the stiffener, in mm as shown in Figure 3 and Figure 4.
*   $b_{f-out}$: Maximum distance, in mm, from mid thickness of the web to the flange edge, in mm, as shown in Figure 3.
*   $d_f$: Breadth of the extended part of the flange for L2 profiles, in mm, as shown in Figure 3.
*   $e_f$: Distance from attached plating to centre of flange, in mm, as shown in Figure 3. For its detailed definition, refer to Sec 5, Symbols.
*   $h_w$: Depth of stiffener web, in mm, as shown in Figure 3 and Figure 4.
*   $t_f$: Net flange thickness, in mm.
*   $t_p$: Net thickness of plate, in mm.
*   $t_w$: Net web thickness, in mm.

![Figure 3: Dimensions of typical stiffener cross sections](Sectional diagrams for Flat, Bulb, Angle, T, and L2 stiffeners showing $h_w, t_w, b_f, t_f, d_f, e_f, b_{f-out}, t_p$ and the connection point C.)

![Figure 4: Dimensions of a U-type stiffener cross section](Sectional diagram of a U-type stiffener showing $b_1, b_2, h_w, t_w, t_f, b_f$ and plate thickness $t_p$.)

##### 2.3.3 Stiffened panel (SP) and Unstiffened panel (UP)
For a panel with relatively strong interactive effect between the stiffener and its attached plate, each stiffener with its attached plate as a whole is to be modelled as a stiffened panel (SP), so as to be able to consider both of its local and global buckling modes.

However, for an EPP, if its buckling strength can be checked without considering its interactive effect with stiffeners fitted along its edges, it’s to be modelled as an unstiffened panel (UP).

#### 2.4 Sign Convention

##### 2.4.1 Stresses
In this UR, compressive and shear stresses are to be taken as positive, tension stresses are to be taken as negative.

### 3. Assessment Methods and Acceptance Criteria

#### 3.1 Assessment Methods

##### 3.1.1 Method A and Method B
The buckling assessment is to be carried out according to one of the following two methods taking into account different boundary condition types:
- **Method A**: All the edges of the EPP are forced to remain straight (but free to move in the in-plane directions) due to the surrounding structure/neighbouring plates.
- **Method B**: The edges of the EPP are not forced to remain straight due to low in-plane stiffness at the edges and/or no surrounding structure/neighbouring plates.

##### 3.1.2 SP-A, SP-B, UP-A and UP-B models
For the buckling assessment of the stiffened panel (SP) and unstiffened panel (UP) structural models defined in [2.3.3], with application of either Method A or Method B for the plate buckling assessment, the following four buckling assessment models are established:
- **SP-A**: a stiffened panel with application of Method A.
- **SP-B**: a stiffened panel with application of Method B.
- **UP-A**: an unstiffened panel with application of Method A.
- **UP-B**: an unstiffened panel with application of Method B.

#### 3.2 Buckling Utilisation Factor

##### 3.2.1
The utilisation factor, $\eta$, is defined as the ratio between the applied loads and the corresponding buckling capacity.

##### 3.2.2
For combined loads, the utilisation factor, $\eta_{act}$, is to be defined as the ratio of the applied equivalent stress and the corresponding buckling capacity, as shown in Figure 5, and is to be taken as:
$$\eta_{act} = \frac{W_{act}}{W_U} = \frac{1}{\gamma_c}$$

where:
*   $W_{act}$: Equivalent applied stress. The actual applied stresses are given in Sec 3 and Sec 4 respectively for buckling assessment by prescriptive and direct strength analysis.
*   $W_U$: Equivalent buckling capacity. For plates and stiffeners, their respective buckling or ultimate capacities are given in Sec 5.
*   $\gamma_c$: Stress multiplier factor at failure.

For each typical failure mode, the corresponding buckling capacity of the panel is calculated by applying the actual stress combination and then increasing or decreasing the stresses proportionally until collapse occurs, i.e., when the increased or decreased stresses are on a buckling strength interaction curve or surface.

![Figure 5: Illustration of buckling capacity and buckling utilisation factor](A graph showing a 'Buckling capacity interaction curve' on a plot of $\sigma_y$ vs $\sigma_x$. A vector from the origin passes through point $W_{act}$ to point $W_u$ on the curve, representing the scaling of actual stress to capacity.)

#### 3.3 Allowable Buckling Utilisation Factor

##### 3.3.1
The allowable buckling utilisation factor $\eta_{all}$ is to be taken according to the Relevant UR-S.

#### 3.4 Buckling Acceptance Criteria

##### 3.4.1
A structural member is considered to have an acceptable buckling strength if it satisfies the following criterion:
$$\eta_{act} \le \eta_{all}$$

where:
*   $\eta_{act}$: Buckling utilisation factor based on the applied stress, defined in [3.2.2].
*   $\eta_{all}$: Allowable buckling utilisation factor as defined in [3.3.1].

---

## SECTION 2 SLENDERNESS REQUIREMENTS

### Symbols
For symbols not defined in this section, refer to Sec 1, [2.3.2].
*   $R_{eH}$: Specified minimum yield stress of the structural member being considered, in N/mm².

### 1. General

#### 1.1 Introduction

##### 1.1.1
The stiffener elements except for U-type stiffeners are to comply with the applicable slenderness and proportion requirements given in [2].

### 2. Stiffeners

#### 2.1 Proportions of Stiffeners

##### 2.1.1 Net thickness of all stiffener types
The net thickness of stiffeners is to satisfy the following criteria:

a) Stiffener web plate:
$$t_w \ge \frac{h_w}{C_w} \sqrt{\frac{R_{eH}}{235}}$$

b) Flange:
$$t_f \ge \frac{b_{f-out}}{C_f} \sqrt{\frac{R_{eH}}{235}}$$

where:
$C_w, C_f$: Slenderness coefficients given in Table 1.

If requirement b) is not fulfilled, the effective free flange outstand, in mm, used in strength assessment including the calculation of actual net section modulus, is to be taken as:
$$b_{f-out-max} = C_f t_f \sqrt{\frac{235}{R_{eH}}}$$

**Table 1: Slenderness coefficients**

| Type of Stiffener | $C_w$ | $C_f$ |
| :--- | :---: | :---: |
| Angle and L2 bars | 75 | 12 |
| T-bars | 75 | 12 |
| Bulb flats | 45 | - |
| Flat bars | 22 | - |

For built-up profile where the relevant yielding strength for the web of built-up profile without the edge stiffener is acceptable, as an alternative the web can be assessed according to the web requirements of Angle and L2 bars in Table 1, and the edge stiffener can be assessed as a flat bar stiffener according to [2.1.1]. The requirement to flange in [2.1.2] shall still apply.

##### 2.1.2 Net dimensions of angle and T-bars
The total flange breadth $b_f$, in mm, for angle and T-bars is to satisfy the following criterion:
$$b_f \ge 0.2 h_w$$

### 3. Primary Supporting Members

#### 3.1 Proportions and Stiffness

##### 3.1.1 Proportions of web plate and flange
The scantlings of webs and flanges of primary supporting members are to comply with the Rules of the Classification Society.

---

## SECTION 3 BUCKLING REQUIREMENTS FOR HULL GIRDER PRESCRIPTIVE ANALYSIS

### Symbols
*   $\eta_{all}$: Allowable buckling utilisation factor, as defined in Sec 1, [3.3.1].
*   LCP: Load Calculation Point, as defined in [1.2.1].

### 1. General

#### 1.1 Introduction

##### 1.1.1
This section applies to plate panels including plane and curved plate panels, stiffeners and corrugation of longitudinal corrugated bulkheads subject to hull girder compression and shear stresses.

##### 1.1.2
The ship longitudinal extent where the buckling check is performed for structural elements subject to hull girder stresses is to be in accordance with the Relevant UR-S.

##### 1.1.3
Design load sets: The buckling check is to be performed for all design load sets corresponding to the design loading conditions defined in the Relevant UR-S with the most unfavourable pressure combinations.
For each design load set, for all static and dynamic load cases, the lateral pressure is to be determined at the load calculation point defined in [1.2.1], and is to be applied together with the hull girder stress combinations defined in the Relevant UR-S.

#### 1.2 Definitions

##### 1.2.1 Load calculation point
The load calculation points (LCP) for both elementary plate panels (EPP) and stiffeners are defined as follows:

a) LCP for hull girder stresses of EPP
The hull girder stresses for EPP are to be calculated at the load calculation points defined in Table 1.

**Table 1: Load calculation points (LCP) coordinates for plate buckling assessment**

| LCP coordinates | Hull girder bending stress - Non horizontal plating | Hull girder bending stress - Horizontal plating | Hull girder shear stress |
| :--- | :--- | :--- | :--- |
| $x$ coordinate | Mid-length of the EPP | Mid-length of the EPP | Mid-length of the EPP |
| $y$ coordinate | Both upper and lower ends of the EPP (points A1 and A2 in Figure 1) | Outboard and inboard ends of the EPP (points A1 and A2 in Figure 1) | Mid-point of EPP (point B in Figure 1) |
| $z$ coordinate | Corresponding to $x$ and $y$ values | Corresponding to $x$ and $y$ values | Corresponding to $x$ and $y$ values |

![Figure 1: LCP for plate buckling assessment](Diagram showing LCP locations A1, A2 (ends) and B (mid) for Longitudinal Framing and Transverse Framing plate panels.)

b) LCP for hull girder stresses of longitudinal stiffeners
The hull girder stresses for longitudinal stiffeners are to be calculated at the following load calculation point:
- at the mid length of the considered stiffener.
- at the intersection point between the stiffener and its attached plate.

c) LCP for pressure of horizontal stiffeners
The load calculation point for the pressure is located at:
- Middle of the full length, $l$, of the considered stiffener.
- The intersection point between the stiffener and its attached plate.

d) LCP for pressure of non-horizontal stiffeners
The lateral pressure, $P$ is to be calculated as the maximum between the value obtained at middle of the full length, $l$, and the value obtained from the following formulae:
- $P = \frac{p_U + p_L}{2}$ when the upper end of the vertical stiffener is below the lowest zero pressure level.
- $P = \frac{l_1}{l} \frac{p_L}{2}$ when the upper end of the vertical stiffener is at or above the lowest zero pressure level, see Figure 2.

where:
*   $l_1$: Distance, in m, between the lower end of vertical stiffener and the lowest zero pressure level.
*   $p_U, p_L$: Lateral pressures at the upper and lower end of the vertical stiffener span $l$, respectively.

![Figure 2: Definition of pressure for vertical stiffeners](Diagram showing a triangular pressure distribution along a vertical stiffener of length $l$. $l_1$ is the portion under pressure.)

#### 1.3 Assumptions for Equivalent Plate Panels

##### 1.3.1 Longitudinal stiffening with varying plate thickness
In longitudinal stiffening arrangement, when the plate thickness varies over the width $b$, of a plate panel, the buckling check is to be performed for an equivalent plate panel width, combined with the smaller plate thickness, $t_1$. The width of this equivalent plate panel, $b_{eq}$, in mm, is defined by the following formula:
$$b_{eq} = l_1 + l_2 \left( \frac{t_1}{t_2} \right)^{1.5}$$

where:
*   $l_1$: Width of the part of the plate panel with the smaller plate thickness, $t_1$, in mm, as defined in Figure 3.
*   $l_2$: Width of the part of the plate panel with the greater plate thickness, $t_2$, in mm, as defined in Figure 3.

![Figure 3: Plate thickness change over the width](Diagram showing a cross section of a plate with two thicknesses $t_1$ and $t_2$ and widths $l_1$ and $l_2$ respectively, within a total panel width $b$.)

##### 1.3.2 Transverse stiffening with varying plate thickness
In transverse stiffening arrangement, when an EPP is made with different thicknesses, the buckling check of the plate and stiffeners is to be made for each thickness considered constant on the EPP, the stresses and pressures being estimated for the EPP at the LCP.

##### 1.3.3 Plate panel with different materials
When the plate panel is made of different materials, the minimum yield strength is to be used for the buckling assessment.

### 2. Buckling Criteria

#### 2.1 Overall Stiffened Panel

##### 2.1.1
The buckling strength of overall stiffened panels is to satisfy the following criterion:
$$\eta_{overall} \le \eta_{all}$$

where:
*   $\eta_{overall}$: Maximum overall buckling utilisation factor as defined in Sec 5, [2.1].

#### 2.2 Plates

##### 2.2.1
The buckling strength of elementary plate panels is to satisfy the following criterion:
$$\eta_{plate} \le \eta_{all}$$

where:
*   $\eta_{plate}$: Maximum plate buckling utilisation factor as defined in Sec 5, [2.2] where SP-A model is to be used.

For the determination of $\eta_{plate}$ of the vertically stiffened side shell plating of single side skin bulk carrier between hopper and topside tanks, the cases 12 and 16 of Sec 5, Table 3 corresponding to the shorter edge of the plate panel clamped are to be considered together with a mean $\sigma_y$ stress and $\psi_y = 1$.

#### 2.3 Stiffeners

##### 2.3.1
The buckling strength of stiffeners or of side frames of single side skin bulk carriers is to satisfy the following criterion:
$$\eta_{stiffener} \le \eta_{all}$$

where:
*   $\eta_{stiffener}$: Maximum stiffener buckling utilisation factor as defined in Sec 5, [2.3].

Note 1: This buckling check can only be fulfilled when the overall stiffened panel buckling check, as defined in [2.1], is satisfied.
Note 2: The buckling check of the stiffeners is only applicable to the stiffeners fitted along the long edge of the buckling panel.

#### 2.4 Vertically Corrugated Longitudinal Bulkheads
The shear buckling strength of vertically corrugated longitudinal bulkheads is to satisfy the following criterion:
$$\eta_{shear} \le \eta_{all}$$

where:
*   $\eta_{shear}$: Maximum shear buckling utilisation factor, defined as $\eta_{shear} = \frac{\tau_{bhd}}{\tau_c}$
*   $\tau_{bhd}$: Shear stress, in N/mm², in the bulkhead taken as the hull girder shear stress defined in the Relevant UR-S.
*   $\tau_c$: Shear critical stress, in N/mm², as defined in Sec 5, [2.2.3].

#### 2.5 Horizontally Corrugated Longitudinal Bulkheads

##### 2.5.1
Each corrugation unit within the extension of half flange, web and half flange (i.e. single corrugation as shown in grey in Figure 4) is to satisfy the following criterion:
$$\eta_{column} \le \eta_{all}$$

where:
*   $\eta_{column}$: Overall column buckling utilisation factor, as defined in Sec 5, [3.1].

![Figure 4: Single corrugation](A diagram of a corrugated bulkhead section with one full corrugation unit (web and half-flanges on each side) highlighted in grey.)

---

## SECTION 4 BUCKLING REQUIREMENTS FOR DIRECT STRENGTH ANALYSIS OF HATCH COVERS

### Symbols
*   $R_{eH\_P}$: Yield stress of the plate panel, as defined in [2.1.3].
*   $R_{eH\_S}$: Yield stress of the stiffener, as defined in [2.1.3].
*   $\alpha$: Aspect ratio of the plate panel, as defined in the Symbol list of Sec 5.
*   $\eta_{all}$: Allowable buckling utilisation factor, as defined in Sec 1, [3.3.1].

### 1. General

#### 1.1 Introduction

##### 1.1.1
The requirements of this Section apply to the buckling assessment of hatch cover structural members based on direct strength analysis (usually by finite element method) and subjected to normal stress, shear stress and lateral pressure.

##### 1.1.2
All structural elements in the direct strength analysis carried out according to the Relevant UR-S are to be assessed individually. The buckling checks are to be performed for the following structural elements:
- Stiffened and unstiffened panels.
- Web plate in way of openings.

### 2. Stiffened and Unstiffened Panels

#### 2.1 General

##### 2.1.1
The plate panel of a hatch cover structure is to be modelled as stiffened panel (SP) or unstiffened panel (UP), with either Method A or Method B as defined in Sec 1, [3.1.1] to be used for the calculation of the plate buckling capacity, which in combination is also equivalent to use the buckling assessment models defined in Sec 1, [3.1.2].

##### 2.1.2 Average thickness of plate panel
For FE analysis, where the plate thickness along a plate panel is not constant, the panel used for the buckling assessment is to be modelled with a weighted average thickness taken as:
$$t_{avr} = \frac{\sum_{i=1}^{n} A_i t_i}{\sum_{i=1}^{n} A_i}$$

where:
*   $A_i$: Area of the $i$-th plate element.
*   $t_i$: Net thickness of the $i$-th plate element.
*   $n$: Number of finite elements defining the buckling plate panel.

##### 2.1.3 Yield stress of the plate panel and stiffener
The panel yield stress $R_{eH\_P}$ is taken as the minimum value of the specified yield stresses of the elements within the plate panel.
The stiffener yield stress $R_{eH\_S}$ is taken as the minimum value of the specified yield stresses of the elements within the stiffener.

#### 2.2 Stiffened Panels

##### 2.2.1
For a stiffened panel (SP), each stiffener with attached plate is to be idealized as a stiffened panel model of the extent defined in the Relevant UR-S.

##### 2.2.2
If the stiffener properties or stiffener spacing varies within the stiffened panel, the calculations are to be performed separately for all configurations of the panels, i.e. for each stiffener and plate between the stiffeners. Plate thickness, stiffener properties and stiffener spacing at the considered location are to be assumed for the whole panel.

##### 2.3.1
The buckling check of the stiffeners of stiffened panels is only applicable to the stiffeners fitted along the longer side edges of the buckling panel.

#### 2.3 Unstiffened Panels

##### 2.3.1 Irregular plate panel
In way of web frames and brackets, the geometry of the panel (i.e. plate bounded by web stiffeners/face plate) may not have a rectangular shape. In this case, for FE analysis, an equivalent rectangular panel is to be defined according to [2.3.2] for irregular geometry and [2.3.3] for triangular geometry and to comply with buckling assessment.

##### 2.3.2 Equivalent EPP of an unstiffened panel with irregular geometry
Unstiffened panels with irregular geometry are to be idealised to equivalent panels for plate buckling assessment according to the following procedure:
a) The four corners closest to a right angle, 90 deg, in the bounding polygon for the plate are identified.
![Irregular panel corner identification](Diagram showing an irregular four-sided polygon.)
b) The distances along the plate bounding polygon between the corners are calculated, i.e. the sum of all the straight-line segments between the end points.
![Irregular panel side lengths](Diagram showing side lengths $d_1, d_2, d_3, d_4$ along an irregular boundary.)
c) The pair of opposite edges with the smallest total length is identified, i.e. minimum of $d_1 + d_3$ and $d_2 + d_4$.
![Irregular panel opposite edges](Diagram showing a line $a$ connecting midpoints of opposite sides.)
d) A line joins the middle points of the chosen opposite edges (i.e. a mid-point is defined as the point at half the distance from one end). This line defines the longitudinal direction for the capacity model. The length of the line defines the length of the capacity model, $a$, measured from one end point.
e) The length of shorter side, $b$, in mm, is to be taken as:
$$b = \frac{A}{a}$$
where:
*   $A$: Area of the plate, in mm²
*   $a$: Length defined in (d), in mm.
![Irregular panel equivalent dimensions](Diagram showing the equivalent rectangular length $a$ and breadth $b$ superimposed on the irregular shape.)
f) The stresses from the direct strength analysis are to be transformed into the local coordinate system of the equivalent rectangular panel. These stresses are to be used for the buckling assessment.

##### 2.3.3 Modelling of an unstiffened plate panel with triangular geometry
Unstiffened panels with triangular geometry are to be idealised to equivalent panels for plate buckling assessment according to the following procedure:
a) Medians are constructed as shown below.
![Triangular panel medians](Diagram of a triangle with medians drawn to each side.)
b) The longest median is identified. This median the length of which is $l_1$, in mm, defines the longitudinal direction for the capacity model.
![Triangular panel longest median](Diagram highlighting the longest median $l_1$.)
c) The width of the model, $l_2$, in mm, is to be taken as:
$$l_2 = \frac{A}{l_1}$$
where:
*   $A$: Area of the plate, in mm²
![Triangular panel width](Diagram showing $l_1$ and $l_2$ relative to the triangle.)
d) The lengths of shorter side, $b$, and of the longer side, $a$, in mm, of the equivalent rectangular plate panel are to be taken as:
$$b = \frac{l_2}{C_{tri}}$$
$$a = l_1 C_{tri}$$
where:
$C_{tri} = 0.4 \frac{l_2}{l_1} + 0.6$
e) The stresses from the direct strength analysis are to be transformed into the local coordinate system of the equivalent rectangular panel and are to be used for the buckling assessment of the equivalent rectangular plate panel.

#### 2.4 Reference Stress

##### 2.4.1
The stress distribution is to be taken from the direct strength analysis according to the Relevant UR-S and applied to the buckling model.

##### 2.4.2
For FE analysis, the reference stresses are to be calculated using the stress-based reference stresses as defined in Appendix 1.

#### 2.5 Lateral Pressure

##### 2.5.1
The lateral pressure applied to the direct strength analysis is also to be applied to the buckling assessment.
For FE analysis, where the lateral pressure is not constant over a buckling panel defined by a number of finite plate elements, an average lateral pressure, N/mm², is calculated using the following formula:
$$P_{avr} = \frac{\sum_{i=1}^{n} A_i P_i}{\sum_{i=1}^{n} A_i}$$
where:
*   $A_i$: Area of the $i$-th plate element, in mm².
*   $P_i$: Lateral pressure of the $i$-th plate element, in N/mm².
*   $n$: Number of finite elements in the buckling panel.

#### 2.6 Buckling Criteria

##### 2.6.1 UP-A
The compressive buckling strength of UP-A is to satisfy the following criterion:
$$\eta_{UP-A} \le \eta_{all}$$
where:
*   $\eta_{UP-A}$: Plate buckling utilisation factor, equal to $\eta_{plate}$ as defined in Sec 5, [2.2] where UP-A model is to be used.

##### 2.6.2 UP-B
The compressive buckling strength of UP-B is to satisfy the following criterion:
$$\eta_{UP-B} \le \eta_{all}$$
where:
*   $\eta_{UP-B}$: Plate buckling utilisation factor, equal to $\eta_{plate}$ as defined in Sec 5, [2.2] where UP-B model is to be used.

##### 2.6.3 SP-A
The compressive buckling strength of SP-A is to satisfy the following criterion:
$$\eta_{SP-A} \le \eta_{all}$$
where:
*   $\eta_{SP-A}$: Buckling utilisation factor of the stiffened panel, taken as the maximum of the buckling utilisation factors calculated as below:
    - The overall stiffened panel buckling utilisation factor $\eta_{overall}$ as defined in Sec 5, [2.1].
    - The plate buckling utilisation factor $\eta_{plate}$ as defined in Sec 5, [2.2] where SP-A model is to be used.
    - The stiffener buckling utilisation factor $\eta_{stiffener}$ as defined in Sec 5, [2.3] considering separately the properties (thickness, dimensions), the pressures defined in [2.5.2] and the reference stresses of each EPP at both sides of the stiffener.

Note 1: The stiffener buckling strength check can only be fulfilled when the overall stiffened panel capacity check, as defined in Sec 5, [2.1], is satisfied.

##### 2.6.4 SP-B
The compressive buckling strength of SP-B is to satisfy the following criterion:
$$\eta_{SP-B} \le \eta_{all}$$
where:
*   $\eta_{SP-B}$: Buckling utilisation factor of the stiffened panel, taken as the maximum of the buckling utilisation factors calculated as below:
    - The overall stiffened panel buckling utilisation factor $\eta_{overall}$ as defined in Sec 5, [2.1].
    - The plate buckling utilisation factor $\eta_{plate}$ as defined in Sec 5, [2.2] where SP-B model is to be used.
    - The stiffener buckling utilisation factor $\eta_{stiffener}$ as defined in Sec 5, [2.3] considering separately the properties (thickness, dimensions), the pressures defined in [2.5.2] and the reference stresses of each EPP at both sides of the stiffener.

Note 1: The stiffener buckling strength check can only be fulfilled when the overall stiffened panel capacity check, as defined in Sec 5, [2.1], is satisfied.

##### 2.6.5 Web plate in way of openings
The web plate of primary supporting members with openings is to satisfy the following criterion:
$$\eta_{opening} \le \eta_{all}$$
where:
*   $\eta_{opening}$: Maximum web plate utilisation factor in way of openings, calculated with the definition in Sec 1, [3.2.2] and the stress multiplier factor at failure $\gamma_c$ which can be calculated following the requirements in Sec 5, [2.4].

---

## SECTION 5 BUCKLING CAPACITY

### Symbols
*   $A_p$: Net sectional area of the stiffener attached plating, in mm², taken as $A_p = s t_p$.
*   $A_s$: Net sectional area of the stiffener without attached plating, in mm².
*   $a$: Length of the longer side of the plate panel, in mm.
*   $b$: Length of the shorter side of the plate panel, in mm.
*   $b_{eff}$: Effective width of the attached plating of a stiffener, in mm, as defined in [2.3.5].
*   $b_{eff1}$: Effective width of the attached plating of a stiffener, in mm, without the shear lag effect taken as:
    - For $\sigma_x > 0$:
        - For prescriptive assessment: $b_{eff1} = \frac{C_{x1}b_1 + C_{x2}b_2}{2}$
        - For FE analysis: $b_{eff1} = C_x b$
    - For $\sigma_x \le 0$: $b_{eff1} = b$
*   $b_f$: Breadth of the stiffener flange, in mm.
*   $b_1, b_2$: Width of plate panel on each side of the considered stiffener, in mm. For stiffened panels fitted with U-type stiffeners, $b_1$ and $b_2$ are as defined in Sec 1, Figure 4.
*   $C_{x1}, C_{x2}$: Reduction factor defined in Table 3 calculated for the EPP1 and EPP2 on each side of the considered stiffener according to case 1.
*   $d$: Length of the side parallel to the cylindrical axis of the cylinder corresponding to the curved plate panel as shown in Table 4, in mm.
*   $d_f$: Breadth of the extended part of the flange for L2 profiles, in mm, as shown in Sec 1, Figure 3.
*   $e_f$: Distance from attached plating to centre of flange, in mm, as shown in Sec 1, Figure 3 to be taken as:
    - $e_f = h_w$ for flat bar profile.
    - $e_f = h_w - 0.5 t_f$ for bulb profile.
    - $e_f = h_w + 0.5 t_f$ for angle, L2 and T profiles.
*   $F_{long}$: Coefficient defined in [2.2.4].
*   $F_{tran}$: Coefficient defined in [2.2.5].
*   $h_w$: Depth of stiffener web, in mm, as shown in Sec 1, Figure 3.
*   $l$: Span, in mm, of stiffener equal to spacing between primary supporting members or span of side frame equal to the distance between the hopper tank and top wing tank in way of the side shell.
*   $R$: Radius of curved plate panel, in mm.
*   $R_{eH\_P}$: Specified minimum yield stress of the plate in N/mm².
*   $R_{eH\_S}$: Specified minimum yield stress of the stiffener in N/mm².
*   $S$: Partial safety factor, unless otherwise specified in the Relevant UR-S, to be taken as 1.0.
*   $t_p$: Net thickness of plate panel, in mm.
*   $t_w$: Net stiffener web thickness, in mm.
*   $t_f$: Net flange thickness, in mm.
*   $x$-axis: Local axis of a rectangular buckling panel parallel to its long edge.
*   $y$-axis: Local axis of a rectangular buckling panel perpendicular to its long edge.
*   $\alpha$: Aspect ratio of the plate panel, defined in Table 3 to be taken as: $\alpha = \frac{a}{b}$.
*   $\beta$: Coefficient taken as: $\beta = \frac{1-\psi}{\alpha}$.
*   $\omega$: Coefficient taken as: $\omega = min(3, \alpha)$.
*   $\sigma_x$: Normal stress applied on the edge along $x$-axis of the buckling panel, in N/mm².
*   $\sigma_y$: Normal stress applied on the edge along $y$-axis of the buckling panel, in N/mm².
*   $\sigma_1$: Maximum normal stress along a panel edge, in N/mm².
*   $\sigma_2$: Minimum normal stress along a panel edge, in N/mm².
*   $\sigma_E$: Elastic buckling reference stress, in N/mm² to be taken as:
    - For the application of the limit state of plane plate panels according to [2.2.1]:
      $$\sigma_E = \frac{\pi^2 E}{12(1-\nu^2)} \left( \frac{t_p}{b} \right)^2$$
    - For the application of the limit state of curved plate panels according to [2.2.6]:
      $$\sigma_E = \frac{\pi^2 E}{12(1-\nu^2)} \left( \frac{t_p}{d} \right)^2$$
*   $\tau$: Applied shear stress, in N/mm².
*   $\tau_c$: Buckling strength in shear, in N/mm², as defined in [2.2.3].
*   $\psi$: Edge stress ratio to be taken as: $\psi = \frac{\sigma_2}{\sigma_1}$.
*   $\gamma$: Stress multiplier factor acting on loads. When the factor is such that the loads reach the interaction formulae, $\gamma = \gamma_c$.
*   $\gamma_c$: Stress multiplier factor at failure.
*   $\gamma_{GEB}$: Stress multiplier factor of global elastic buckling capacity.

### 1. General

#### 1.1 Introduction

##### 1.1.1
This section contains the methods for determination of the buckling capacities of plate panels, stiffeners, primary supporting members and columns.

##### 1.1.2
For the application of this section, the stresses $\sigma_x, \sigma_y$ and $\tau$ applied on the structural members are defined in:
- Sec 3 for hull girder prescriptive buckling requirements.
- Sec 4 for direct strength analysis buckling requirements of hatch covers.

##### 1.1.3 Buckling capacity
The buckling capacity is calculated by applying the actual stress combination and then increasing or decreasing the stresses proportionally until the interaction formulae defined in [2.1.1], [2.2.1] and [2.3.4] are equal to 1.0, respectively.

##### 1.1.4 Buckling utilisation factor
The buckling utilisation factor of the structural member is equal to the highest utilisation factor obtained for the different buckling modes.

##### 1.1.5 Lateral pressure
The lateral pressure is to be applied and considered as constant for the calculation of buckling capacities as defined in [1.1.3].

### 2. Buckling Capacity of Plate Panels

#### 2.1 Overall Stiffened Panels

##### 2.1.1
The elastic stiffened panel limit state is based on the following interaction formula, which sets a precondition for the buckling check of stiffeners in accordance with [2.3.4]:
$$\frac{\gamma_c}{\gamma_{GEB}} = 1$$
with the corresponding buckling utilization factor defined as
$$\eta_{overall} = \frac{1}{\gamma_c}$$
where the stress multiplier factors of global elastic buckling capacity, $\gamma_{GEB}$, are to be calculated based on the following formulae:
*   $\gamma_{GEB} = \gamma_{GEB,bi+\tau}$ for $\tau \neq 0$ and ($\sigma_x > 0$ or $\sigma_y > 0$)
*   $\gamma_{GEB} = \gamma_{GEB,bi}$ for $\tau = 0$ and ($\sigma_x > 0$ or $\sigma_y > 0$)
*   $\gamma_{GEB} = \gamma_{GEB,\tau}$ for $\tau \neq 0$ and ($\sigma_x \le 0$ and $\sigma_y \le 0$)

where $\gamma_{GEB,bi+\tau}$, $\gamma_{GEB,bi}$ and $\gamma_{GEB,\tau}$ are stress multiplier factors of the global elastic buckling capacity for different load combinations as defined in [2.1.2], [2.1.3] and [2.1.4], respectively. For the calculation of $\gamma_{GEB,bi+\tau}$, $\gamma_{GEB,bi}$ and $\gamma_{GEB,\tau}$, neither $\sigma_x$ nor $\sigma_y$ shall be taken less than 0.

*   $\sigma_x, \sigma_y$: Applied normal stress to the plate panel, in N/mm², to be taken as defined in [2.2.7].
*   $\tau$: Applied shear stress, in N/mm², to be taken as defined in [2.2.7].

##### 2.1.2
The stress multiplier factor $\gamma_{GEB,bi}$ for the stiffened panel subjected to biaxial loads is taken as:
$$\gamma_{GEB,bi} = \frac{\pi^2}{L_{B1}^2 L_{B2}^2} \frac{[D_{11} L_{B2}^4 + 2(D_{12} + D_{33}) n^2 L_{B1}^2 L_{B2}^2 + n^4 D_{22} L_{B1}^4]}{L_{B2}^2 N_x + n^2 L_{B1}^2 N_y}$$
where:
*   $N_x$: Load per unit length applied on the edge along $x$-axis of the stiffened panel, in N/mm, taken as $N_x = \sigma_{x,av}(A_p + A_s)/s$
    For stiffened panels fitted with U-type stiffeners, stiffener spacing $s$ is taken as: $s = b_1 + b_2$
    where $b_1$ and $b_2$ are as defined in Sec 1, Figure 4.
*   $N_y$: Load per unit length applied on the edge along $y$ axis of the stiffened panel, in N/mm, taken as $N_y = c \sigma_y t_p$
*   $L_{B1}$: Stiffener span, in mm, distance between primary supporting members, i.e. $L_{B1} = l$. Specially, for vertically stiffened side shell of single side skin bulk carriers, $L_{B1} = 0.8l$.
*   $L_{B2}$: Total width of stiffened panel between lateral supports, in mm, taken as 6 times of the stiffener spacing, i.e. $6s$.
*   $n$: Number of half waves along the direction perpendicular to the stiffener axis. The factor $\gamma_{GEB,bi}$ is to be minimized with respect to the wave parameters $n$, i.e. to be taken as the smallest value larger than zero.
*   $c$: Factor taking into account the normal stress distribution in the attached plating acting perpendicular to the stiffener’s axis:
    $c = 0.5(1 + \psi)$ for $0 \le \psi \le 1$
    $c = \frac{1}{2(1-\psi)}$ for $\psi < 0$
*   $\psi$: Edge stress ratio for case 2 according to Table 3.
*   $\sigma_{x,av}$: Average stress for both plate and stiffener, taken as:
    $\sigma_{x,av} = \sigma_x - \nu c \sigma_y A_s / (A_p + A_s) \ge 0$ for $\sigma_x > 0$ and $\sigma_y > 0$
    $\sigma_{x,av} = \sigma_x$ for $\sigma_x \le 0$ or $\sigma_y \le 0$

$D_{11}, D_{12}, D_{22}, D_{33}$: Bending stiffness coefficients, in Nmm, of the stiffened panel, defined in general as:
$$D_{11} = \frac{E I_{eff} 10^4}{s}$$
$$D_{12} = \frac{E t_p^3 \nu}{12(1-\nu^2)}$$
$$D_{22} = \frac{E t_p^3}{12(1-\nu^2)}$$
$$D_{33} = \frac{E t_p^3}{12(1+\nu)}$$
For stiffened panels fitted with U-type stiffeners, $D_{12}$ and $D_{22}$ are defined as:
$$D_{22} = \frac{E t_p^3}{12(1-\nu^2)} \left[ 1.2 + 4.8 \times Min \left( 1.0, \frac{b_1^2}{h_w(b_1 + b_2)} \right) \times Min \left( 1.0, \left( \frac{t_w}{t_p} \right)^3 \right) \right]$$
$$D_{12} = \nu D_{22}$$
$h_w$ is the breadth of U-type stiffener web as defined in Sec 1, Figure 4.
$I_{eff}$ is the moment of inertia, in cm⁴, of the stiffener including the effective width of the attached plating, same as $I$ defined in [2.3.4].

##### 2.1.3
The stress multiplier factor $\gamma_{GEB,\tau}$ for the stiffened panel subjected to pure shear load is taken as:
$\gamma_{GEB,\tau} = \frac{4 \sqrt[4]{D_{11}^3 D_{22}}}{(L_{B1}/2)^2 N_{xy}} \left[ 8.125 + 5.64 \sqrt{\frac{(D_{12}+D_{33})^2}{D_{11} D_{22}}} - 0.6 \frac{(D_{12}+D_{33})^2}{D_{11} D_{22}} \right]$ for $D_{11} D_{22} \ge (D_{12} + D_{33})^2$
$\gamma_{GEB,\tau} = \frac{\sqrt{2 D_{11} (D_{12}+D_{33})}}{(L_{B1}/2)^2 N_{xy}} \left[ 8.3 + 1.525 \frac{D_{11} D_{22}}{(D_{12}+D_{33})^2} - 0.493 \frac{D_{11}^2 D_{22}^2}{(D_{12}+D_{33})^4} \right]$ for $D_{11} D_{22} < (D_{12} + D_{33})^2$
where: $N_{xy} = \tau t_p$

##### 2.1.4
The stress multiplier factor $\gamma_{GEB,bi+\tau}$ for the stiffened panel subjected to combined loads is taken as:
$$\gamma_{GEB,bi+\tau} = \frac{1}{2} \gamma_{GEB,\tau}^2 \left[ - \frac{1}{\gamma_{GEB,bi}} + \sqrt{\frac{1}{\gamma_{GEB,bi}^2} + \frac{4}{\gamma_{GEB,\tau}^2}} \right]$$
where $\gamma_{GEB,bi}$ and $\gamma_{GEB,\tau}$ are as defined in [2.1.2] and [2.1.3], respectively.

#### 2.2 Plates

##### 2.2.1 Plate limit state
The plate limit state is based on the following interaction formulae:
$\left( \frac{\gamma_{c1} \sigma_x}{\sigma_{cx}} \right)^{e_0} - B \left( \frac{\gamma_{c1} \sigma_x}{\sigma_{cx}} \right)^{e_0/2} \left( \frac{\gamma_{c1} \sigma_y}{\sigma_{cy}} \right)^{e_0/2} + \left( \frac{\gamma_{c1} \sigma_y}{\sigma_{cy}} \right)^{e_0} + \left( \frac{\gamma_{c1} |\tau| S}{\tau_c} \right)^{e_0} = 1$
$\left( \frac{\gamma_{c2} \sigma_x S}{\sigma_{cx}} \right)^2 \beta_p^{0.25} + \left( \frac{\gamma_{c2} |\tau| S}{\tau_c} \right)^2 \beta_p^{0.25} = 1$ for $\sigma_x \ge 0$
$\left( \frac{\gamma_{c3} \sigma_y S}{\sigma_{cy}} \right)^2 \beta_p^{0.25} + \left( \frac{\gamma_{c3} |\tau| S}{\tau_c} \right)^2 \beta_p^{0.25} = 1$ for $\sigma_y \ge 0$
$\frac{\gamma_{c4} |\tau| S}{\tau_c} = 1$

with $\gamma_c = Min(\gamma_{c1}, \gamma_{c2}, \gamma_{c3}, \gamma_{c4})$
and the corresponding buckling utilization factor defined as $\eta_{plate} = \frac{1}{\gamma_c}$

where:
*   $\sigma_x, \sigma_y$: Applied normal stress to the plate panel, in N/mm², to be taken as defined in [2.2.7].
*   $\tau$: Applied shear stress to the plate panel, in N/mm².
*   $\sigma_{cx}$: Ultimate buckling stress, in N/mm², in direction parallel to the longer edge of the buckling panel as defined in [2.2.3].
*   $\sigma_{cy}$: Ultimate buckling stress, in N/mm², in direction parallel to the shorter edge of the buckling panel as defined in [2.2.3].
*   $\tau_c$: Ultimate buckling shear stress, in N/mm², as defined in [2.2.3].
*   $\gamma_{c1}, \gamma_{c2}, \gamma_{c3}, \gamma_{c4}$: Stress multiplier factors at failure for each of the above different limit states. $\gamma_{c2}$ and $\gamma_{c3}$ are only to be considered when $\sigma_x \ge 0$ and $\sigma_y \ge 0$ respectively.
*   $B$: Coefficient given in Table 1
*   $e_0$: Coefficient given in Table 1
*   $\beta_p$: Plate slenderness parameter taken as: $\beta_p = \frac{b}{t_p} \sqrt{\frac{R_{eH\_P}}{E}}$

**Table 1: Definition of coefficients $B$ and $e_0$**

| Applied stress | $B$ | $e_0$ |
| :--- | :---: | :---: |
| $\sigma_x \ge 0$ and $\sigma_y \ge 0$ | $0.7 - 0.3 \beta_p / \alpha^2$ | $2 / \beta_p^{0.25}$ |
| $\sigma_x < 0$ or $\sigma_y < 0$ | $1.0$ | $2.0$ |

##### 2.2.2 Reference degree of slenderness
The reference degree of slenderness is to be taken as:
$$\lambda = \sqrt{\frac{R_{eH\_P}}{K \sigma_E}}$$
where:
$K$: Buckling factor, as defined in Table 3 and Table 4.

##### 2.2.3 Ultimate buckling stresses
The ultimate buckling stresses of plate panels, in N/mm², are to be taken as:
$$\sigma_{cx} = C_x R_{eH\_P}$$
$$\sigma_{cy} = C_y R_{eH\_P}$$
The ultimate buckling stress of plate panels subject to shear, in N/mm², is to be taken as:
$$\tau_c = C_\tau \frac{R_{eH\_P}}{\sqrt{3}}$$
where:
$C_x, C_y, C_\tau$: Reduction factors, as defined in Table 3
- For the 1st Equation of [2.2.1], when $\sigma_x < 0$ or $\sigma_y < 0$, the reduction factors are to be taken as: $C_x = C_y = C_\tau = 1$.
- For other cases:
    - For SP-A and UP-A, $c_1$ is calculated according to Table 3 by using $c_1 = (1 - 1/\alpha) \ge 0$
    - For SP-B and UP-B, $c_1$ is calculated according to Table 3 by using $c_1 = 1$
    - For vertically stiffened single side skin of bulk carrier, $C_y$ is calculated according to Table 3 by using $c_1 = (1 - 1/\alpha) \ge 0$
    - For corrugation of corrugated bulkheads, $C_y$ is calculated according to Table 3 by using $c_1 = (1 - 1/\alpha) \ge 0$

The boundary conditions for plates are to be considered as simply supported, see cases 1, 2 and 15 of Table 3. If the boundary conditions differ significantly from simple support, a more appropriate boundary condition can be applied according to the different cases of Table 3 subject to the agreement of the Society.

##### 2.2.4 Correction factor $F_{long}$
The correction factor $F_{long}$ depending on the edge stiffener types on the longer side of the buckling panel is defined in Table 2.

**Table 2: Correction factor $F_{long}$**

| Structural element types | | $F_{long}$ | $c$ |
| :--- | :--- | :---: | :---: |
| Unstiffened Panel | | 1.0 | N/A |
| Stiffened Panel | Stiffener not fixed at both ends | 1.0 | N/A |
| | Stiffener fixed at both ends | | |
| | | Flat bar(1) | $F_{long} = c + 1$ for $t_w/t_p > 1$ | 0.10 |
| | | | $F_{long} = c(t_w/t_p)^3 + 1$ for $t_w/t_p \le 1$ | |
| | | Bulb profile | | 0.30 |
| | | Angle and L2 profiles | | 0.40 |
| | | T profile | | 0.30 |
| | | Girder of high rigidity (e.g. bottom transverse) | 1.4 | N/A |
| | | U-type profile fitted on hatch cover(2) | - Plate on which the U-type profile is fitted, including EPP $b_1$ and EPP $b_2$<br>- For $b_2 < b_1$: $F_{long} = 1$<br>- For $b_2 \ge b_1$:<br>$F_{long} = (1.55 - 0.55 \frac{b_1}{b_2}) [1 + c (\frac{t_w}{t_p})^3]$<br>- Other plates of the U-type profile: $F_{long} = 1$ | 0.2 |

*(1) $t_w$ is the net web thickness, in mm, without the correction defined in [2.3.2].*
*(2) $b_1, b_2$ and $t_w$ are defined in Sec.1, Figure 4.*

##### 2.2.5 Correction factor $F_{tran}$
The correction factor $F_{tran}$ is to be taken as:
- For transversely framed EPP of single side skin bulk carrier, between the hopper and top wing tank:
    - $F_{tran} = 1.25$ when the two adjacent frames are supported by one tripping bracket fitted in way of the adjacent plate panels.
    - $F_{tran} = 1.33$ when the two adjacent frames are supported by two tripping brackets each fitted in way of the adjacent plate panels.
    - $F_{tran} = 1.15$ elsewhere.
- For the attached plate of a U-type stiffener fitted on a hatch cover:
  $F_{tran} = Max(3 - 0.08(F_{tran0} - 6)^2, 1.0) \le 2.25$
  where:
  $F_{tran0} = Min\left(\left[\frac{b_2}{b_1} + \frac{6b_2^2}{\pi^2 h_w(b_1+b_2)}\right] \left(\frac{t_w}{t_p}\right)^3, 6\right)$ for EPP $b_2$
  $F_{tran0} = Min\left(\left[\frac{b_1}{b_2} + \frac{6b_1^2}{\pi^2 h_w(b_2+b_1)}\right] \left(\frac{t_w}{t_p}\right)^3, 6\right)$ for EPP $b_1$
  with $b_1, b_2$ and $h_w$ as defined in Sec.1, Figure 4.
  Coefficient $F$ defined in Case 2 of Table 3 is to be replaced by the following formula:
  $F = [1 - (\frac{K_y}{0.91 F_{tran}} - 1) / \lambda_p^2] c_1 \ge 0$
- For other cases: $F_{tran} = 1$.

##### 2.2.6 Curved plate panels
This requirement for curved plate limit state is applicable when $R/t_p \le 2500$. Otherwise, the requirement for plate limit state given in [2.2.1] is applicable.
The curved plate limit state is based on the following interaction formula:
$$\left( \frac{\gamma_c \sigma_{ax}}{C_{ax} R_{eH\_P}} \right)^{1.25} - 0.5 \left( \frac{\gamma_c \sigma_{ax}}{C_{ax} R_{eH\_P}} \right) \left( \frac{\gamma_c \sigma_{tg}}{C_{tg} R_{eH\_P}} \right) + \left( \frac{\gamma_c \sigma_{tg}}{C_{tg} R_{eH\_P}} \right)^{1.25} + \left( \frac{\gamma_c \tau \sqrt{3}}{C_\tau R_{eH\_P}} \right)^2 = 1.0$$
with the corresponding buckling utilization factor defined as $\eta_{curved\_plate} = \frac{1}{\gamma_c}$
where:
*   $\sigma_{ax}$: Applied axial stress to the cylinder corresponding to the curved plate panel, in N/mm². In case of tensile axial stresses, $\sigma_{ax} = 0$.
*   $\sigma_{tg}$: Applied tangential stress to the cylinder corresponding to the curved plate panel, in N/mm². In case of tensile tangential stresses, $\sigma_{tg} = 0$.
*   $C_{ax}, C_{tg}, C_\tau$: Buckling reduction factor of the curved plate panel, as defined in Table 4.

The stress multiplier factor, $\gamma_c$, of the curved plate panel need not be taken less than the stress multiplier factor, $\gamma_c$, for the expanded plane panel according to [2.2.1].

![Figure 1: Transverse stiffened bilge plating](A diagram showing a curved bilge plate with radius $R$ and transverse stiffeners.)

**Table 3: Buckling factor and reduction factor for plane plate panels**

| Case | Stress ratio $\psi$ | Aspect ratio $\alpha$ | Buckling factor $K$ | Reduction factor $C$ |
| :--- | :--- | :--- | :--- | :--- |
| **1**<br>![Case 1 diagram](Diagram of a plate with longitudinal normal stresses $\sigma_x$ and $\psi \sigma_x$.) | $1 \ge \psi \ge 0$ | | $K_x = F_{long} \frac{8.4}{\psi+1.1}$ | When $\sigma_x \le 0, C_x = 1$<br>When $\sigma_x > 0$:<br>$C_x = 1$ for $\lambda \le \lambda_c$<br>$C_x = c(\frac{1}{\lambda} - \frac{0.22}{\lambda^2})$ for $\lambda > \lambda_c$<br>where:<br>$c = (1.25 - 0.12\psi) \le 1.25$<br>$\lambda_c = \frac{c}{2} [1 + \sqrt{1 - \frac{0.88}{c}}]$ |
| | $0 > \psi > -1$ | | $K_x = F_{long} [7.63 - \psi(6.26 - 10\psi)]$ | |
| | $\psi \le -1$ | | $K_x = F_{long} [5.975(1-\psi)^2]$ | |
| **2**<br>![Case 2 diagram](Diagram of a plate with transverse normal stresses $\sigma_y$ and $\psi \sigma_y$.) | $1 \ge \psi \ge 0$ | | $K_y = \frac{F_{tran} \cdot 2 (1 + \frac{1}{\alpha^2})^2}{1 + \psi + \frac{(1-\psi)}{100} (\frac{2.4}{\alpha^2} + 6.9 f_1)}$ | When $\sigma_y \le 0, C_y = 1$<br>When $\sigma_y > 0$:<br>$C_y = c(\frac{1}{\lambda} - \frac{R+F^2(H-R)}{\lambda^2})$<br>where:<br>$c = (1.25 - 0.12\psi) \le 1.25$<br>$R = \lambda(1-\frac{1}{c})$ for $\lambda < \lambda_c$<br>$R = 0.22$ for $\lambda \ge \lambda_c$<br>$\lambda_c = 0.5c [1 + \sqrt{1 - \frac{0.88}{c}}]$ |
| | | $\alpha \le 6$ | $f_1 = (1-\psi)(\alpha-1)$ | |
| | | $\alpha > 6$ | $f_1 = 0.6(1-\frac{6\psi}{\alpha})(\alpha+\frac{14}{\alpha})$ but not greater than $14.5 - \frac{0.35}{\alpha^2}$ | |
| | $1 - \frac{4\alpha}{3} \le \psi < 0$ | | $K_y = \frac{200 F_{tran} (1 + \beta^2)^2}{(1-f_3)(100 + 2.4\beta^2 + 6.9f_1 + 23f_2)}$ | |
| | | $\alpha > 6(1-\psi)$ | $f_1 = 0.6(\frac{1}{\beta} + 14\beta)$ but not greater than $14.5 - 0.35\beta^2$<br>$f_2 = f_3 = 0$ | $F = (1 - \frac{(\frac{K}{0.91}-1)}{\lambda_p^2}) c_1 \ge 0$<br>$\lambda_p^2 = \lambda^2 - 0.5$ for $1 \le \lambda_p^2 \le 3$<br>$c_1$ as defined in [2.2.3]<br>$H = \lambda - \frac{2\lambda}{c(T+\sqrt{T^2-4})} \ge R$<br>$T = \lambda + \frac{14}{15\lambda} + \frac{1}{3}$ |
| | | $3(1-\psi) \le \alpha \le 6(1-\psi)$ | $f_1 = \frac{1}{\beta} - 1$<br>$f_2 = f_3 = 0$ | |
| | | $1.5(1-\psi) \le \alpha < 3(1-\psi)$ | $f_1 = \frac{1}{\beta} - (2-\omega\beta)^4 - 9(\omega\beta-1)(\frac{2}{3}-\beta)$<br>$f_2 = f_3 = 0$ | |
| | | $1-\psi \le \alpha < 1.5(1-\psi)$ | For $\alpha > 1.5$: $f_1 = 2(\frac{1}{\beta} - 16(1-\frac{\omega}{3})^4) (\frac{1}{\beta}-1)$, $f_2 = 3\beta-2, f_3 = 0$<br>For $\alpha \le 1.5$: $f_1 = 2(\frac{1.5}{1-\psi}-1)(\frac{1}{\beta}-1)$, $f_2 = \frac{\psi(1-16f_4^2)}{1-\alpha}, f_3 = 0, f_4 = (1.5-Min(1.5, \alpha))^2$ | |
| | | $0.75(1-\psi) \le \alpha < 1-\psi$ | $f_1 = 0, f_2 = 1 + 2.31(\beta-1) - 48(\frac{4}{3}-\beta)f_4^2$<br>$f_3 = 3f_4(\beta-1) - (\frac{f_4}{1.81} - \frac{\alpha-1}{1.31})$<br>$f_4 = (1.5-Min(1.5, \alpha))^2$ | |
| | $\psi < 1 - \frac{4\alpha}{3}$ | | $K_y = 5.972 F_{tran} \frac{\beta^2}{1-f_3}$ where $f_3 = f_5 (\frac{f_5}{1.81} + \frac{1+3\psi}{5.24})$, $f_5 = \frac{9}{16} (1+Max(-1, \psi))^2$ | |

*(Table 3 continues)*

| Case | Stress ratio $\psi$ | Aspect ratio $\alpha$ | Buckling factor $K$ | Reduction factor $C$ |
| :--- | :--- | :--- | :--- | :--- |
| **3**<br>![Case 3](Diagram showing $\sigma_x$ applied along the shorter side $b$.) | $1 \ge \psi \ge 0$ | | $K_x = \frac{4(0.425 + 1/\alpha^2)}{3\psi+1}$ | For UP-A:<br>$C_x = 1$ for $\lambda \le 0.75$<br>$C_x = 0.75/\lambda$ for $\lambda > 0.75$<br>For UP-B:<br>$C_x = 1$ for $\lambda \le 0.7$br>$C_x = \frac{1}{\lambda^2+0.51}$ for $\lambda > 0.7$ |
| | $0 > \psi \ge -1$ | | $K_x = 4(0.425 + \frac{1}{\alpha^2}) (1+\psi) - 5\psi(1-3.42\psi)$ | |
| **4**<br>![Case 4](Diagram showing $\psi \sigma_x$ on top/bottom and $\sigma_x$ on sides.) | $1 \ge \psi \ge -1$ | | $K_x = (0.425 + \frac{1}{\alpha^2}) \frac{3-\psi}{2}$ | |
| **5**<br>![Case 5](Diagram of a plate with one edge free.) | — | $\alpha \ge 1.64$ | $K_x = 1.28$ | $C_x = \frac{1}{\lambda^2+0.51}$ for $\lambda > 0.7$ |
| | | $\alpha < 1.64$ | $K_x = \frac{1}{\alpha^2} + 0.56 + 0.13\alpha^2$ | |
| **6**<br>![Case 6](Diagram showing $\sigma_y$ applied along the longer side $a$.) | $1 \ge \psi \ge 0$ | | $K_y = \frac{4(0.425 + \alpha^2)}{(3\psi+1)\alpha^2}$ | For UP-A:<br>$C_y = 1$ for $\lambda \le 0.75$<br>$C_y = 0.75/\lambda$ for $\lambda > 0.75$<br>For UP-B:<br>$C_y = 1$ for $\lambda \le 0.7$<br>$C_y = \frac{1}{\lambda^2+0.51}$ for $\lambda > 0.7$ |
| | $0 > \psi \ge -1$ | | $K_y = 4(0.425 + \alpha^2)(1+\psi) \frac{1}{\alpha^2} - 5\psi(1-3.42\psi) \frac{1}{\alpha^2}$ | |
| **7**<br>![Case 7](Diagram showing $\psi \sigma_y$ on sides and $\sigma_y$ on top/bottom.) | $1 \ge \psi \ge -1$ | | $K_y = (0.425 + \alpha^2) \frac{(3-\psi)}{2\alpha^2}$ | |
| **8**<br>![Case 8](Diagram of a plate with one longer edge free.) | — | | $K_y = 1 + \frac{0.56}{\alpha^2} + \frac{0.13}{\alpha^4}$ | |
| **9**<br>![Case 9](Diagram of a plate with both shorter edges clamped.) | — | | $K_x = 6.97$ | $C_x = 1$ for $\lambda \le 0.83$<br>$C_x = 1.13 (\frac{1}{\lambda} - \frac{0.22}{\lambda^2})$ for $\lambda > 0.83$ |
| **10**<br>![Case 10](Diagram of a plate with both longer edges clamped.) | — | | $K_y = 4 + \frac{2.07}{\alpha^2} + \frac{0.67}{\alpha^4}$ | $C_y = 1$ for $\lambda \le 0.83$<br>$C_y = 1.13 (\frac{1}{\lambda} - \frac{0.22}{\lambda^2})$ for $\lambda > 0.83$ |
| **11**<br>![Case 11](Diagram of a plate with all edges clamped.) | — | $\alpha \ge 4$ | $K_x = 4$ | $C_x = 1$ for $\lambda \le 0.83$<br>$C_x = 1.13 (\frac{1}{\lambda} - \frac{0.22}{\lambda^2})$ for $\lambda > 0.83$ |
| | | $\alpha < 4$ | $K_x = 4 + 2.74 (\frac{4-\alpha}{3})^4$ | |
| **12**<br>![Case 12](Diagram showing triangular transverse stress distribution.) | — | | $K_y = K_y$ determined as per case 2 | For $\alpha < 2: C_y = C_{y2}$<br>For $\alpha \ge 2: C_y = (1.06 + \frac{1}{10\alpha}) C_{y2}$ where $C_{y2}: C_y$ determined as per case 2 |
| **13**<br>![Case 13](Diagram of a plate with clamped shorter edges and simply supported longer edges.) | — | $\alpha \ge 4$ | $K_x = 6.97$ | $C_x = 1$ for $\lambda \le 0.83$<br>$C_x = 1.13 (\frac{1}{\lambda} - \frac{0.22}{\lambda^2})$ for $\lambda > 0.83$ |
| | | $\alpha < 4$ | $K_x = 6.97 + 3.1 (\frac{4-\alpha}{3})^4$ | |
| **14**<br>![Case 14](Diagram of a plate with clamped longer edges and simply supported shorter edges.) | — | | $K_y = \frac{6.97}{\alpha^2} + \frac{3.1}{\alpha^2} (\frac{4-1/\alpha}{3})^4$ | $C_y = 1$ for $\lambda \le 0.83$<br>$C_y = 1.13 (\frac{1}{\lambda} - \frac{0.22}{\lambda^2})$ for $\lambda > 0.83$ |
| **15**<br>![Case 15](Diagram of a plate under pure shear $\tau$.) | － | | $K_\tau = \sqrt{3} (5.34 + \frac{4}{\alpha^2})$ | $C_\tau = 1$ for $\lambda \le 0.84$<br>$C_\tau = \frac{0.84}{\lambda}$ for $\lambda > 0.84$ |
| **16**<br>![Case 16](Diagram of a plate under shear with clamped longer edges.) | － | | $K_\tau = \sqrt{3} [5.34 + Max (\frac{4}{\alpha^2}, \frac{7.15}{\alpha^{2.5}})]$ | |
| **17**<br>![Case 17](Diagram of a plate with a hole under shear.) | － | | $K_\tau = K_{\tau case 15} r$<br>$K_{\tau case 15}: K_\tau$ according to case 15<br>$r$: Opening reduction factor taken as $r = (1 - \frac{d_a}{a})(1 - \frac{d_b}{b})$ with $\frac{d_a}{a} \le 0.7$ and $\frac{d_b}{b} \le 0.7$ | |
| **18**<br>![Case 18](Diagram of a plate under shear with clamped shorter edges.) | － | | $K_\tau = \sqrt{3} (0.6 + \frac{4}{\alpha^2})$ | $C_\tau = 1$ for $\lambda \le 0.84$<br>$C_\tau = \frac{0.84}{\lambda}$ for $\lambda > 0.84$ |
| **19**<br>![Case 19](Diagram of a plate under shear with all edges clamped.) | － | | $K_\tau = 8$ | |

**Edge boundary conditions:**
- - - - Plate edge free
————— Plate edge simply supported
▬▬▬ Plate edge clamped

Note 1: Cases listed are general cases. Each stress component ($\sigma_x, \sigma_y$) is to be understood in local coordinates.

**Table 4: Buckling factor and reduction factor for curved plate panel with $R/t_p \le 2500$**

| Case | Aspect ratio | Buckling factor $K$ | Reduction factor $C$ |
| :--- | :--- | :--- | :--- |
| **1**<br>![Case 1 curved](Diagram of curved plate under axial stress $\sigma_{ax}$.) | $\frac{d}{R} \le 0.5 \sqrt{\frac{R}{t_p}}$ | $K = 1 + \frac{2 d^2}{3 R t_p}$ | For general application:<br>$C_{ax} = 1$ for $\lambda \le 0.25$<br>$C_{ax} = 1.233 - 0.933\lambda$ for $0.25 < \lambda \le 1$<br>$C_{ax} = 0.3/\lambda^3$ for $1 < \lambda \le 1.5$<br>$C_{ax} = 0.2/\lambda^2$ for $\lambda > 1.5$<br>For curved single fields (e.g. bilge strake):<br>$C_{ax} = \frac{0.65}{\lambda^2} \le 1.0$ |
| | $\frac{d}{R} > 0.5 \sqrt{\frac{R}{t_p}}$ | $K = 0.267 \frac{d^2}{R t_p} [3 - \frac{d}{R} \sqrt{\frac{t_p}{R}}] \ge 0.4 \frac{d^2}{R t_p}$ | |
| **2**<br>![Case 2 curved](Diagram of curved plate under tangential stress $\sigma_{tg}$.) | $\frac{d}{R} \le 1.63 \sqrt{\frac{R}{t_p}}$ | $K = \frac{d}{\sqrt{R t_p}} + \frac{3 (R t_p)^{0.175}}{d^{0.35}}$ | For general application:<br>$C_{tg} = 1$ for $\lambda \le 0.4$<br>$C_{tg} = 1.274 - 0.686\lambda$ for $0.4 < \lambda \le 1.2$<br>$C_{tg} = \frac{0.65}{\lambda^2}$ for $\lambda > 1.2$<br>For curved single fields (e.g. bilge strake):<br>$C_{tg} = \frac{0.8}{\lambda^2} \le 1.0$ |
| | $\frac{d}{R} > 1.63 \sqrt{\frac{R}{t_p}}$ | $K = 0.3 \frac{d^2}{R^2} + 2.25 (\frac{R^2}{d t_p})^2$ | |
| **3**<br>![Case 3 curved](Diagram of curved plate under axial and tangential stress.) | $\frac{d}{R} \le \sqrt{\frac{R}{t_p}}$ | $K = \frac{0.6d}{\sqrt{R t_p}} + \frac{\sqrt{R t_p}}{d} - 0.3 \frac{R t_p}{d^2}$ | As in load case 2. |
| | $\frac{d}{R} > \sqrt{\frac{R}{t_p}}$ | $K = 0.3 \frac{d^2}{R^2} + 0.291 (\frac{R^2}{d t_p})^2$ | |
| **4**<br>![Case 4 curved](Diagram of curved plate under shear stress $\tau$.) | $\frac{d}{R} \le 8.7 \sqrt{\frac{R}{t_p}}$ | $K = \sqrt{3} [28.3 + \frac{0.67 d^3}{R^{1.5} t_p^{1.5}}]$ | $C_\tau = 1$ for $\lambda \le 0.4$<br>$C_\tau = 1.274 - 0.686\lambda$ for $0.4 < \lambda \le 1.2$<br>$C_\tau = \frac{0.65}{\lambda^2}$ for $\lambda > 1.2$ |
| | $\frac{d}{R} > 8.7 \sqrt{\frac{R}{t_p}}$ | $K = \sqrt{3} \frac{0.28 d^2}{R \sqrt{R t_p}}$ | |

**Explanations for boundary conditions:**
- - - - Plate edge free.
————— Plate edge simply supported.
▬▬▬ Plate edge clamped.

##### 2.2.7 Applied normal and shear stresses to plate panels
The normal stress, $\sigma_x$ and $\sigma_y$, in N/mm², to be applied for the overall stiffened panel capacity and the plate panel capacity calculations as given in [2.1.1] and [2.2.1] respectively, are to be taken as follows:
- For FE analysis, the reference stresses as defined in Sec.4 [2.4].
- For prescriptive assessment of the overall stiffened panel capacity and the plate panel capacity, the axial or transverse compressive stresses calculated according to the Relevant UR-S, at load calculation points of the considered stiffener or the considered elementary plate panel, as defined in item a) and item b) of Sec 3, [1.2.1] respectively. However, in case of transverse stiffening arrangement, the transverse compressive stress used for the assessment of the overall stiffened panel capacity is to be taken as the compressive stress calculated at load calculation points of the stiffener attached plating, as defined in item a) of Sec 3, [1.2.1].
- For grillage analysis where the stresses are obtained based on beam theory, the stresses taken as:
  $\sigma_x = \frac{\sigma_{xb} + \nu \sigma_{yb}}{1 - \nu^2}$
  $\sigma_y = \frac{\sigma_{yb} + \nu \sigma_{xb}}{1 - \nu^2}$
  Where $\sigma_{xb}, \sigma_{yb}$ are stress, in N/mm², from grillage beam analysis respectively along $x$ or $y$ axis of the plate attached to the PSM web.

The shear stress $\tau$, in N/mm², to be applied for the overall stiffened panel capacity and the plate panel capacity calculations as given in [2.1.1] and [2.2.1] respectively, are to be taken as follows:
- For FE analysis, the reference shear stresses as defined in Sec 4, [2.4].
- For prescriptive assessment of the plate panel capacity, the shear stresses calculated according to the Relevant UR-S, at load calculation points of the considered elementary plate panel, as defined in item a) of Sec 3, [1.2.1].
- For prescriptive assessment of the overall stiffened panel capacity, the shear stresses calculated according to the Relevant UR-S, at the following load calculation point:
    - At the middle of the full span, $l$, of the considered stiffener.
    - At the intersection point between the stiffener and its attached plating.
- For grillage beam analysis, $\tau = 0$ in the plate attached to the PSM web.

#### 2.3 Stiffeners

##### 2.3.1 Buckling modes
The following buckling modes are to be checked:
- Stiffener induced failure ($SI$).
- Associated plate induced failure ($PI$).

##### 2.3.2 Web thickness of flat bar
For accounting the decrease of the stiffness due to local lateral deformation, the effective web thickness of flat bar stiffener, in mm, is to be used in [2.1] and [2.3.4] for the calculation of the net sectional area, $A_s$, the net section modulus, $Z$, and the moment of inertia, $I$, of the stiffener and is taken as:
$$t_{w\_red} = t_w \left( 1 - \frac{2\pi^2}{3} \left( \frac{h_w}{s} \right)^2 \left( 1 - \frac{b_{eff1}}{s} \right) \right)$$

##### 2.3.3 Idealisation of bulb profile
Bulb profiles are to be considered as equivalent angle profiles. The net dimensions of the equivalent built-up section are to be obtained, in mm, from the following formulae.
$h_w = h_w' - \frac{h_w'}{9.2} + 2$
$b_f = \alpha (t_w' + \frac{h_w'}{6.7} - 2)$
$t_f = \frac{h_w'}{9.2} - 2$
$t_w = t_w'$
where:
$h_w', t_w'$ are net height and thickness of a bulb section, in mm, as shown in Figure 2.
$\alpha$ is a coefficient equal to $\alpha = 1.1 + \frac{(120-h_w')^2}{3000}$ for $h_w' \le 120$, and $\alpha = 1.0$ for $h_w' > 120$.

![Figure 2: Idealisation of bulb stiffener](Diagrams showing the transformation of a bulb flat into an equivalent angle bar with dimensions $h_w, t_w, b_f, t_f$.)

##### 2.3.4 Ultimate buckling capacity
When $\sigma_a + \sigma_b + \sigma_w > 0$ while initially setting $\gamma = 1$, the ultimate buckling capacity for stiffeners is to be checked according to the following interaction formula:
$$\frac{\gamma_c \sigma_a + \sigma_b + \sigma_w}{R_{eH}} S = 1$$
with the corresponding buckling utilization factor defined as $\eta_{stiffener} = \frac{1}{\gamma_c}$
where:
*   $\sigma_a$: Effective axial stress, in N/mm², at mid span of the stiffener, acting on the stiffener with its attached plating.
    $\sigma_a = \sigma_x \frac{s t_p + A_s}{b_{eff1} t_p + A_s}$
*   $\sigma_x$: Nominal axial stress, in N/mm², acting on the stiffener with its attached plating.
    - For FE analysis, $\sigma_x$ is the FE corrected stress as defined in [2.3.6] in the attached plating in the direction of the stiffener axis.
    - For prescriptive assessment, $\sigma_x$ is the axial stress calculated according to Sec 3, [2.2.1] at load calculation point of the stiffener, as defined in Sec 3, [1.2.1].
    - For grillage beam analysis, $\sigma_x$ is the stress acting along the $x$-axis of the attached buckling panel.
*   $R_{eH}$: Specified minimum yield stress of the material, in N/mm²
    - $R_{eH} = R_{eH\_S}$ for stiffener induced failure ($SI$).
    - $R_{eH} = R_{eH\_P}$ for plate induced failure ($PI$).
*   $\sigma_b$: Bending stress in the stiffener, in N/mm²: $\sigma_b = \frac{M_0 + M_1 + M_2}{1000 Z}$
*   $Z$: Net section modulus of stiffener, in cm³, including effective width of plating according to [2.3.5], to be taken as:
    - The section modulus calculated at the top of stiffener flange for stiffener induced failure ($SI$).
    - The section modulus calculated at the attached plating for plate induced failure ($PI$).
*   $M_2$: Bending moment, in Nmm, due to eccentricity of sniped stiffeners, to be taken as
    - $M_2 = 0$ for continuous stiffeners
    - $M_2 = C_{snip} w_{na} \gamma \sigma_x (A_p + A_s)$ for stiffeners sniped at one or both ends.
*   $C_{snip}$: Coefficient to account for the end effect of the stiffener sniped at one or both ends, to be taken as
    - $C_{snip} = -1.2$ for stiffener induced failure ($SI$)
    - $C_{snip} = 1.2$ for plate induced failure ($PI$).
*   $M_1$: Bending moment, in Nmm, due to the lateral load $P$:
    - $M_1 = C_i \frac{|P| s l^2}{24 \times 10^3}$ for continuous stiffener
    - $M_1 = C_i \frac{|P| s l^2}{8 \times 10^3}$ for sniped stiffener
    - $M_1 = C_i \frac{|P| s l^2}{14.2 \times 10^3}$ for stiffener sniped at one end and continuous at the other end
*   $P$: Lateral load, in kN/m².
    - For FE analysis, $P$ is the average pressure as defined in Sec 4, [2.5.2] in the attached plating.
    - For prescriptive assessment, $P$ is the pressure calculated at load calculation point of the stiffener, as defined in Sec 3, [1.2.1].
*   $C_i$: Pressure coefficient:
    - $C_i = C_{SI}$ for stiffener induced failure ($SI$).
    - $C_i = C_{PI}$ for plate induced failure ($PI$).
*   $C_{PI}$: Plate induced failure pressure coefficient:
    - $C_{PI} = 1$ if the lateral pressure is applied on the side opposite to the stiffener.
    - $C_{PI} = -1$ if the lateral pressure is applied on the same side as the stiffener.
*   $C_{SI}$: Stiffener induced failure pressure coefficient:
    - $C_{SI} = -1$ if the lateral pressure is applied on the side opposite to the stiffener.
    - $C_{SI} = 1$ if the lateral pressure is applied on the same side as the stiffener.
*   $M_0$: Bending moment, in Nmm, due to the lateral deformation $w$ of stiffener:
    $M_0 = F_E C_{sl} \frac{\gamma}{\gamma_{GEB} - \gamma} w_0$ with precondition $\gamma_{GEB} - \gamma > 0$
*   $\gamma_{GEB}$: Stress multiplier factor of global elastic buckling capacity as defined in [2.1].
*   $F_E$: Ideal elastic buckling force of the stiffener, in N.
    $F_E = \left( \frac{\pi}{l} \right)^2 E I \cdot 10^4$
*   $I$: Moment of inertia, in cm⁴, of the stiffener including effective width of attached plating according to [2.3.5]. $I$ is to comply with the following requirement: $I \ge \frac{s t_p^3}{12 \cdot 10^4}$
*   $t_p$: Net thickness of plate, in mm, to be taken as
    - For prescriptive requirements: the mean thickness of the two attached plating panels,
    - For FE analysis: the thickness of the considered EPP on one side of the stiffener.
*   $C_{sl}$: Deformation reduction factor to account for global slenderness, to be taken as:
    - $C_{sl} = 1 - \frac{1}{12} \lambda_G^4$ for $\lambda_G \le 1.56$
    - $C_{sl} = 3 / \lambda_G^4$ for $\lambda_G > 1.56$
*   $\lambda_G$: The reference degree of global slenderness of the stiffened panel, to be taken as
    $\lambda_G = \sqrt{\frac{\gamma_{ReH}}{\gamma_{GEB}}}$ with $\gamma_{ReH} = \frac{Min(R_{eH\_P}, R_{eH\_S})}{\sqrt{\sigma_{x,av}^2 + \sigma_y^2 - \sigma_{x,av} \sigma_y + 3\tau^2}}$
*   $\sigma_{x,av}$: Average stress for both plate and stiffener as defined in [2.1.2].
*   $\sigma_y$: Applied transverse stress to the plate panel as defined in [2.1.1].
*   $\tau$: Applied shear stress to the plate panel as defined in [2.1.1].
*   $w_0$: Assumed imperfection, in mm, to be taken as: $w_0 = l / 1000$.
*   $\sigma_w$: Stress due to torsional deformation, in N/mm², to be taken as:
    - For stiffener induced failure ($SI$)
        - For $\sigma_a > 0$: $\sigma_w = E y_w e_f \Phi_0 \left( \frac{m_{tor} \pi}{l_{tor}} \right)^2 \left( \frac{1}{1 - \frac{\gamma \sigma_a}{\sigma_{ET}}} - 1 \right)$ with precondition $\sigma_{ET} - \gamma \sigma_a > 0$
        - For $\sigma_a \le 0$: $\sigma_w = 0$
    - For plate induced failure ($PI$): $\sigma_w = 0$
*   $y_w$: Distance, in mm, from centroid of stiffener cross section to the free edge of stiffener flange, to be taken as:
    - $y_w = \frac{t_w}{2}$ for flat bar
    - $y_w = b_f - \frac{h_w t_w^2 + t_f b_f^2}{2 A_s}$ for angle and bulb profiles
    - $y_w = b_{f-out} + 0.5 t_w - \frac{h_w t_w^2 + t_f (b_f^2 - 2 b_{f-out} d_f)}{2 A_s}$ for L2 profile
    - $y_w = \frac{b_f}{2}$ for T profile.
*   $\Phi_0$: Coefficient taken as: $\Phi_0 = \frac{l_{tor}}{m_{tor} h_w} 10^{-4}$
*   $\sigma_{ET}$: Reference stress for torsional buckling, in N/mm², to be taken as:
    $\sigma_{ET} = \frac{E}{I_p} \left[ \left( \frac{m_{tor} \pi}{l_{tor}} \right)^2 I_\omega \cdot 10^2 + \frac{1}{2(1+\nu)} I_T + \left( \frac{l_{tor}}{m_{tor} \pi} \right)^2 \epsilon \cdot 10^{-4} \right]$
*   $I_p$: Net polar moment of inertia of the stiffener, in cm⁴, about point C as shown in Sec 1, Figure 3, as defined in Table 5.
*   $I_T$: Net St. Venant’s moment of inertia of the stiffener, in cm⁴, as defined in Table 5.
*   $I_\omega$: Net sectorial moment of inertia of the stiffener, in cm⁶, about point C as shown in Sec 1, Figure 3, as defined in Table 5.
*   $l_{tor}$: Stiffener span, distance equal to spacing between primary supporting members, i.e. $l_{tor} = l$. When the stiffener is supported by tripping brackets, $l_{tor}$ should be taken as the maximum spacing between the adjacent primary supporting members and fitted tripping brackets.
*   $m_{tor}$: Number of half waves, taken as a positive integer so as to give smallest reference stress for torsional buckling.
*   $\epsilon$: Degree of fixation, in mm², to be taken as:
    - $\epsilon = \left( \frac{3b}{t_p^3} + \frac{2h_w}{t_w^3} \right)^{-1}$ for bulb, angle, L2 and T profiles;
    - $\epsilon = \left( \frac{t_p^3}{3b} \right)$ for flat bars.
*   $A_w$: Net web area, in mm².
*   $A_f$: Net flange area, in mm².

**Table 5: Moments of inertia**

| | Flat bars(1) | Bulb, angle, L2 and T profiles |
| :--- | :---: | :---: |
| $I_p$ | $\frac{h_w^3 t_w}{3 \cdot 10^4}$ | $\left( \frac{A_w (e_f - 0.5 t_f)^2}{3} + A_f e_f^2 \right) 10^{-4}$ |
| $I_T$ | $\frac{h_w t_w^3}{3 \cdot 10^4} (1 - 0.63 \frac{t_w}{h_w})$ | $\frac{(e_f - 0.5 t_f) t_w^3}{3 \cdot 10^4} (1 - 0.63 \frac{t_w}{e_f - 0.5 t_f}) + \frac{b_f t_f^3}{3 \cdot 10^4} (1 - 0.63 \frac{t_f}{b_f})$ |
| $I_\omega$ | $\frac{h_w^3 t_w^3}{36 \cdot 10^6}$ | **For bulb, angle and L2 profiles(2):**<br>$\frac{A_f^3 + A_w^3}{36 \cdot 10^6} + \frac{e_f^2}{10^6} \left( \frac{A_f b_f^2 + A_w t_w^2}{3} - \frac{(A_f(b_f - 2d_f) + A_w t_w)^2}{4(A_f + A_w)} - A_f d_f (b_f - d_f) \right)$<br>**For T profile:** $\frac{b_f^3 t_f e_f^2}{12 \cdot 10^6}$ |

*(1) $t_w$ is the net web thickness, in mm. $t_{w\_red}$ as defined in [2.3.2] is not to be used in this table.*
*(2) $d_f$ is to be taken as 0 for bulb and angle profiles.*

##### 2.3.5 Effective width of attached plating
The effective width of attached plating of stiffeners, $b_{eff}$, in mm, is to be taken as:
- For $\sigma_x > 0$:
    - For FE analysis, $b_{eff} = Min(C_x b, \chi_s s)$
    - For prescriptive assessment, $b_{eff} = Min(\frac{C_{x1}b_1 + C_{x2}b_2}{2}, \chi_s s)$
- For $\sigma_x \le 0$: $b_{eff} = \chi_s s$

where:
$\chi_s$ : Effective width coefficient to be taken as:
$\chi_s = \frac{1.12}{1 + \frac{1.75}{(\ell_{eff}/s)^{1.6}}} \le 1.0$ for $\ell_{eff}/s \ge 1$
$\chi_s = 0.407 \frac{\ell_{eff}}{s}$ for $\ell_{eff}/s < 1$

$\ell_{eff}$ : Effective length of the stiffener, in mm, taken as:
- $\ell_{eff} = \frac{l}{\sqrt{3}}$ for stiffener fixed at both ends.
- $\ell_{eff} = 0.75l$ for stiffener simply supported at one end and fixed at the other.
- $\ell_{eff} = l$ for stiffener simply supported at both ends.

##### 2.3.6 FE corrected stresses for stiffener capacity
When the reference stresses $\sigma_x$ and $\sigma_y$ obtained by FE analysis according to Sec 4, [2.4] are both compressive, $\sigma_x$ is to be corrected according to the following formulae:
- If $\sigma_x < \nu \sigma_y$: $\sigma_{xcor} = 0$
- If $\sigma_x \ge \nu \sigma_y$: $\sigma_{xcor} = \sigma_x - \nu \sigma_y$

#### 2.4 Primary Supporting Members

##### 2.4.1 Web plate in way of openings
The web plate of primary supporting members with openings is to be assessed for buckling based on the combined axial compressive and shear stresses.
The web plate adjacent to the opening on both sides is to be considered as individual unstiffened plate panels as shown in Table 6.
The interaction formulae of [2.2.1] are to be used with:
$\sigma_x = \sigma_{av}$
$\sigma_y = 0$
$\tau = \tau_{av}$
where:
$\sigma_{av}$: Weighted average compressive stress, in N/mm², in the area of web plate being considered, i.e. $P1, P2$, or $P3$ as shown in Table 6.

For the application of Table 6, the weighted average shear stress is to be taken as:
- Opening modelled in primary supporting members:
  $\tau_{av}$: Weighted average shear stress, in N/mm², in the area of web plate being considered, i.e. $P1, P2$, or $P3$ as shown in Table 6.
- Opening not modelled in primary supporting members:
  $\tau_{av}$: Weighted average shear stress, in N/mm², given in Table 6.

##### 2.4.2 Reduction factors of web plate in way of openings
The reduction factors, $C_x$ or $C_y$ in combination with, $C_\tau$ of the plate panel(s) of the web adjacent to the opening is to be taken as shown in Table 6.

##### 2.4.3
The equivalent plate panel of web plate of primary supporting members crossed by perpendicular stiffeners is to be idealised as shown in Figure 3.

![Figure 3: Web plate idealization](Diagram showing an equivalent plate panel for a PSM web with perpendicular stiffeners, illustrating the area to be considered around the opening.)

The correction of panel breadth is applicable also for other slot configurations provided that the web or collar plate is attached to at least one side of the passing stiffener.

**Table 6: Reduction factors**

| Configuration(1) | $C_x, C_y$ | $C_\tau$ (Opening modelled in PSM) | $C_\tau$ (Opening not modelled in PSM) |
| :--- | :--- | :--- | :--- |
| **(a) Without edge reinforcements:(2)**<br>![Configuration a](Diagram of an opening in a web without reinforcement showing areas P1 and P2.) | Separate reduction factors are to be applied to areas $P1$ and $P2$ using case 3 or case 6 in Table 3, with edge stress ratio: $\psi = 1.0$ | Separate reduction factors are to be applied to areas $P1$ and $P2$ using case 18 or case 19 in Table 3. | When case 17 of Table 3 is applicable: A common reduction factor is to be applied to areas $P1$ and $P2$ using case 17 in Table 3 with: $\tau_{av} = \tau_{av}(web)$<br>When case 17 of Table 3 is not applicable: Separate reduction factors are to be applied to areas $P1$ and $P2$ using case 18 or case 19 in Table 3 with: $\tau_{av} = \tau_{av}(web)h / (h - h_0)$ |
| **(b) With edge reinforcements:**<br>![Configuration b](Diagram of a reinforced opening showing areas P1 and P2.) | Separate reduction factors are to be applied for areas $P1$ and $P2$ using $C_x$ for case 1 or $C_y$ for case 2 in Table 3 with stress ratio: $\psi = 1.0$ | Separate reduction factors are to be applied for areas $P1$ and $P2$ using case 15 in Table 3. | Separate reduction factors are to be applied to areas $P1$ and $P2$ using case 15 in Table 3 with: $\tau_{av} = \tau_{av}(web)h / (h - h_0)$ |
| **(c) Example of hole in web:**<br>![Configuration c](Diagram of multiple holes in a web.) | Panels $P1$ and $P2$ are to be evaluated in accordance with (a). Panel $P3$ is to be evaluated in accordance with (b). | | |

Where:
*   $h$: Height, in m, of the web of the primary supporting member in way of the opening.
*   $h_0$: Height in m, of the opening measured in the depth of the web.
*   $\tau_{av}(web)$: Weighted average shear stress, in N/mm², over the web height h of the primary supporting member.

Note (1): Web panels to be considered for buckling in way of openings are shown shaded and numbered P1, P2, etc.
Note (2): For a PSM web panel with opening and without edge reinforcements as shown in configuration (a), the applicable buckling assessment method depends on its specific boundary conditions. If one of the long edges along the face plate or along the attached plating is not subject to "inline support", i.e. the edge is free to pull in, Method B should be applied. In other cases, typically such as when the short plate edge is attached to the plate flanges, Method A is applicable.

#### 2.5 Stiffened Panels with U-type Stiffeners

##### 2.5.1 Local plate buckling
For stiffened panels with U-type stiffeners, local plate buckling is to be checked for each of the plate panels EPP $b_1, b_2, b_f$ and $h_w$ (see Sec 1, Figure 4) separately as follows:
- The attached plate panels EPP $b_1$ and $b_2$ are to be assessed using SP-A model, where in the calculation of buckling factors $K_x$ as defined in Case 1 of Table 3, the correction factor $F_{long}$ for U-type stiffeners as defined in Table 2 is to be used; and in the calculation of $K_y$ as defined in Case 2 of Table 3, the $F_{tran}$ for U-type stiffeners as defined in [2.2.5] is to be used.
- The face plate and web plate panels $b_f$ and $h_w$ are to be assessed using UP-B model with $F_{long} = 1$ and $F_{tran} = 1$.

##### 2.5.2 Overall stiffened panel buckling and stiffener buckling
For a stiffened panel with U-type stiffeners, the overall buckling capacity and ultimate capacity of the stiffeners are to be checked with warping stress $\sigma_w = 0$, and with bending moment of inertia including effective width of attached plating being calculated based on the following assumptions:
- The two web panels of a U-type stiffener are to be taken as perpendicular to the attached plate with thickness equal to $t_w$ and height equal to the distance between the attached plate and the face plate of the stiffener.
- Effective width of the attached plating, $b_{eff}$, taken as the sum of the $b_{eff}$ calculated for the EPP $b_1$ and $b_2$ respectively according to SP-A model.
- Effective width of the attached plating of a stiffener without shear lag effect, $b_{eff1}$, taken as the sum of the $b_{eff1}$ calculated for the EPP $b_1$ and $b_2$ respectively.

### 3. Buckling capacity of column structures

#### 3.1 Column Buckling of Corrugations

##### 3.1.1 Buckling utilisation factor
The column buckling utilisation factor, $\eta$, for axially compressed corrugations is to be taken as:
$$\eta_{column} = \frac{\sigma_{av}}{\sigma_{cr}}$$
where:
*   $\sigma_{av}$: Average axial compressive stress in the member, in N/mm².
*   $\sigma_{cr}$: Minimum critical buckling stress, in N/mm², taken as:
    - $\sigma_{cr} = \sigma_E$ for $\sigma_E \le 0.5 R_{eH\_S}$
    - $\sigma_{cr} = (1 - \frac{R_{eH\_S}}{4\sigma_E}) R_{eH\_S}$ for $\sigma_E > 0.5 R_{eH\_S}$
*   $\sigma_E$: Elastic column compressive buckling stress, in N/mm², according to [3.1.2].
*   $R_{eH\_S}$: Specified minimum yield stress of the considered member, in N/mm². For built-up members, the lowest specified minimum yield stress is to be used.

##### 3.1.2 Elastic column buckling stress
The elastic compressive column buckling stress, $\sigma_E$ in N/mm² of members subject to axial compression is to be taken as:
$$\sigma_E = \pi^2 E f_{end} \frac{I}{A l_{pill}^2} 10^{-4}$$
where:
*   $I$: Net moment of inertia about the weakest axis of the cross section, in cm⁴.
*   $A$: Net cross-sectional area of the member, in cm².
*   $l_{pill}$: Unsupported length of the member, in m.
*   $f_{end}$: End constraint factor, corresponding to simply supported ends is to be applied except for fixed end support to be used in way of stool with width exceeding 2 times the depth of the corrugation, taken as:
    - $f_{end} = 1.0$ where both ends are simply supported.
    - $f_{end} = 2.0$ where one end is simply supported and the other end is fixed.
    - $f_{end} = 4.0$ where both ends are fixed.

---

## APPENDIX 1 STRESS BASED REFERENCE STRESSES

### Symbols
*   $a$: Length, in mm, of the longer side of the plate panel as defined in Sec 5.
*   $b$: Length, in mm, of the shorter side of the plate panel as defined in Sec 5.
*   $A_i$: Area, in mm², of the $i$-th plate element of the buckling panel.
*   $n$: Number of plate elements in the buckling panel.
*   $\sigma_{xi}$: Actual stress, in N/mm², at the centroid of the $i$-th plate element in $x$ direction, applied along the shorter edge of the buckling panel.
*   $\sigma_{yi}$: Actual stress, in N/mm², at the centroid of the $i$-th plate element in $y$ direction, applied along the longer edge of the buckling panel.
*   $\psi$: Edge stress ratio as defined in Sec 5.
*   $\tau_i$: Actual membrane shear stress, in N/mm², at the centroid of the $i$-th plate element of the buckling panel.

### 1. Stress Based Method

#### 1.1 Introduction

##### 1.1.1
This section provides a method to determine stress distribution along edges of the considered buckling panel by second-order polynomial curve, by linear distribution using least square method and by weighted average approach. This method is called Stress based Method. The reference stress is the stress components at centre of plate element transferred into the local system of the considered buckling panel.

##### 1.1.2 Definition:
A regular panel is a plate panel of rectangular shape. An irregular panel is plate panel which is not regular, as detailed in Sec 4, [2.3.1].

#### 1.2 Stress Application

##### 1.2.1 Regular panel
The reference stresses are to be taken as defined in [2.1] for a regular panel when the following conditions are satisfied:
- At least, one plate element centre is located in each third part of the long edge $a$ of a regular panel and
- This element centre is located at a distance in the panel local $x$ direction not less than $a/4$ to at least one of the element centres in the adjacent third part of the panel.

Otherwise, the reference stresses are to be taken as defined in [2.2] for an irregular panel.

##### 1.2.2 Irregular panel and curved panel
The reference stresses of an irregular panel or of a curved panel are to be taken as defined in [2.2].

### 2. Reference Stresses

#### 2.1 Regular Panel

##### 2.1.1 Longitudinal stress
The longitudinal stress $\sigma_x$ applied on the shorter edge of the buckling panel is to be calculated as follows:
- For plate buckling assessment, the distribution of $\sigma_x(x)$ is assumed as second order polynomial curve as:
  $\sigma_x = Cx^2 + Dx + E$
  The best fitting curve $\sigma_x(x)$ is to be obtained by minimising the square error $\Pi$ considering the area of each element as a weighting factor.
  $\Pi = \sum_{i=1}^{n} A_i [\sigma_{xi} - (Cx_i^2 + Dx_i + E)]^2$
  The unknown coefficients $C, D$ and $E$ must yield zero first derivatives, $\partial \Pi$ with respect to $C, D$ and $E$, respectively.
  $\frac{\partial \Pi}{\partial C} = 2 \sum_{i=1}^{n} A_i x_i^2 [\sigma_{xi} - (Cx_i^2 + Dx_i + E)] = 0$
  $\frac{\partial \Pi}{\partial D} = 2 \sum_{i=1}^{n} A_i x_i [\sigma_{xi} - (Cx_i^2 + Dx_i + E)] = 0$
  $\frac{\partial \Pi}{\partial E} = 2 \sum_{i=1}^{n} A_i [\sigma_{xi} - (Cx_i^2 + Dx_i + E)] = 0$
  The unknown coefficients $C, D$ and $E$ can be obtained by solving the 3 above equations.

  $\sigma_{x1} = \frac{1}{b} \int_0^b \sigma_x(x) dx = \frac{b^2}{3} C + \frac{b}{2} D + E$
  $\sigma_{x2} = \frac{1}{b} \int_{a-b}^a \sigma_x(x) dx = (a^2 - ab + \frac{b^2}{3}) C + (a - \frac{b}{2}) D + E$
  If $-\frac{D}{2C} < \frac{b}{2}$ or $-\frac{D}{2C} > a - \frac{b}{2}, \sigma_{x3}$ is to be ignored. Otherwise, $\sigma_{x3}$ is taken as:
  $\sigma_{x3} = \frac{1}{b} \int_{x_{min}}^{x_{max}} \sigma_x(x) dx = \frac{b^2}{12} C - \frac{D^2}{4C} + E$
  where: $x_{min} = - \frac{b}{2} - \frac{D}{2C}$, $x_{max} = \frac{b}{2} - \frac{D}{2C}$

  The longitudinal stress is to be taken as: $\sigma_x = Max(\sigma_{x1}, \sigma_{x2}, \sigma_{x3})$
  The edge stress ratio is to be taken as: $\psi_x = 1$
- For overall stiffened panel buckling and stiffener buckling assessments, the longitudinal stress $\sigma_x$ applied on the shorter edge of the attached plate is to be taken as:
  $\sigma_x = \frac{\sum_{i=1}^{n} A_i \sigma_{xi}}{\sum_{i=1}^{n} A_i}$
  The edge stress ratio $\psi_x$ for the stress $\sigma_x$ is equal to 1.0.

##### 2.1.2 Transverse stress
The transverse stress $\sigma_y$ applied along the longer edges of the buckling panel is to be calculated by extrapolation of the transverse stresses of all elements up to the shorter edges of the considered buckling panel.

![Figure 1: Buckling panel](Diagram showing a plate panel discretized into finite elements with local $u, v$ (or $x, y$) axes and element stresses $\sigma_{xi}, \sigma_{yi}$.)

The distribution of $\sigma_y(x)$ is assumed as straight line. Therefore: $\sigma_y(x) = A + Bx$
The best fitting curve $\sigma_y(x)$ is to be obtained by the least square method minimising the square error $\Pi$ considering area of each element as a weighting factor.
$\Pi = \sum_{i=1}^{n} A_i [\sigma_{yi} - (A + Bx_i)]^2$
The unknown coefficients $A$ and $B$ must yield zero first partial derivatives, $\partial \Pi$ with respect to $A$ and $B$, respectively.
$\frac{\partial \Pi}{\partial A} = 2 \sum_{i=1}^{n} A_i [\sigma_{yi} - (A + Bx_i)] = 0$
$\frac{\partial \Pi}{\partial B} = 2 \sum_{i=1}^{n} A_i x_i [\sigma_{yi} - (A + Bx_i)] = 0$
The unknown coefficients A and B are obtained by solving the 2 above equations and are given as follow:
$A = \frac{(\sum_{i=1}^n A_i \sigma_{yi})(\sum_{i=1}^n A_i x_i^2) - (\sum_{i=1}^n A_i x_i)(\sum_{i=1}^n A_i x_i \sigma_{yi})}{(\sum_{i=1}^n A_i)(\sum_{i=1}^n A_i x_i^2) - (\sum_{i=1}^n A_i x_i)^2}$
$B = \frac{(\sum_{i=1}^n A_i)(\sum_{i=1}^n A_i x_i \sigma_{yi}) - (\sum_{i=1}^n A_i x_i)(\sum_{i=1}^n A_i \sigma_{yi})}{(\sum_{i=1}^n A_i)(\sum_{i=1}^n A_i x_i^2) - (\sum_{i=1}^n A_i x_i)^2}$

The transverse stress is to be taken as: $\sigma_y = max(A, A + Ba)$
The edge stress ratio is to be taken as:
$\psi_y = \frac{min(A, A + Ba)}{max(A, A + Ba)}$ for $\sigma_y > 0$
$\psi_y = 1$ for $\sigma_y \le 0$.

##### 2.1.3 Shear stress
The shear stress $\tau$ is to be calculated using a weighted average approach, and is to be taken as:
$\tau = \frac{\sum_{i=1}^{n} A_i \tau_i}{\sum_{i=1}^{n} A_i}$

#### 2.2 Irregular Panel and Curved Panel

##### 2.2.1 Reference stresses
The longitudinal, transverse and shear stresses are to be calculated using a weighted average approach. They are to be taken as:
$\sigma_x = \frac{\sum_{i=1}^{n} A_i \sigma_{xi}}{\sum_{i=1}^{n} A_i}$
$\sigma_y = \frac{\sum_{i=1}^{n} A_i \sigma_{yi}}{\sum_{i=1}^{n} A_i}$
$\tau = \frac{\sum_{i=1}^{n} A_i \tau_i}{\sum_{i=1}^{n} A_i}$

The edge stress ratios are to be taken as
$\psi_x = 1$
$\psi_y = 1$

**End of Document**