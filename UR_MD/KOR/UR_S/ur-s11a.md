# S11A Longitudinal Strength Standard for Container Ships (June 2015)

## S11A.1 General

### S11A.1.1 Application

#### S11A.1.1.1 Application

This UR applies to the following types of steel ships with a length $L$ of 90 m and greater and operated in unrestricted service:

1. Container ships
2. Ships dedicated primarily to carry their load in containers.

#### S11A.1.1.2 Load limitations

The wave induced load requirements apply to monohull displacement ships in unrestricted service and are limited to ships meeting the following criteria:

(i) Length: $90 \text{ m} \le L \le 500 \text{ m}$
(ii) Proportion: $5 \le L/B \le 9$; $2 \le B/T \le 6$
(iii) Block coefficient at scantling draught: $0.55 \le C_B \le 0.9$

For ships that do not meet all of the aforementioned criteria, special considerations such as direct calculations of wave induced loads may be required by the Classification Society.

#### S11A.1.1.3 Longitudinal extent of strength assessment

The stiffness, yield strength, buckling strength and hull girder ultimate strength assessment are to be carried out in way of $0.2L$ to $0.75L$ with due consideration given to locations where there are significant changes in hull cross section, e.g. changing of framing system and the fore and aft end of the forward bridge block in case of two-island designs.

In addition, strength assessments are to be carried out outside this area. As a minimum assessments are to be carried out at forward end of the foremost cargo hold and the aft end of the aft most cargo hold. Evaluation criteria used for these assessments are determined by the Classification Society.

---

**Note:**
1. This UR is to be uniformly implemented by IACS Societies for ships contracted for construction on or after 1 July 2016.
2. The "contracted for construction" date means the date on which the contract to build the vessel is signed between the prospective owner and the shipbuilder. For further details regarding the date of "contract for construction", refer to IACS Procedural Requirement (PR) No. 29.

---

### S11A.1.2 Symbols and definitions

#### S11A.1.2.1 Symbols

- $L$: Rule length, in m, as defined in UR S2
- $B$: Moulded breadth, in m
- $C$: Wave parameter, see 2.3.1
- $T$: Scantling draught in m
- $C_B$: Block coefficient at scantling draught
- $C_w$: Waterplane coefficient at scantling draught, to be taken as: $C_w = \frac{A_w}{(LB)}$
- $A_w$: Waterplane area at scantling draught, in m²
- $R_{eH}$: Specified minimum yield stress of the material, in N/mm²
- $k$: Material factor as defined in UR S4 for higher tensile steels, $k=1.0$ for mild steel having a minimum yield strength equal to 235 N/mm²
- $E$: Young's modulus in N/mm² to be taken as $E = 2.06 \times 10^5$ N/mm² for steel
- $M_S$: Vertical still water bending moment in seagoing condition, in kNm, at the cross section under consideration
- $M_{Smax}, M_{Smin}$: Permissible maximum and minimum vertical still water bending moments in seagoing condition, in kNm, at the cross section under consideration, see 2.2.2
- $M_W$: Vertical wave induced bending moment, in kNm, at the cross section under consideration
- $F_S$: Vertical still water shear force in seagoing condition, in kN, at the cross section under consideration
- $F_{Smax}, F_{Smin}$: Permissible maximum and minimum still water vertical shear force in seagoing condition, in kN, at the cross section under consideration, see 2.2.2
- $F_W$: Vertical wave induced shear force, in kN, at the cross section under consideration
- $q_v$: Shear flow along the cross section under consideration, to be determined according to Annex 1
- $f_{NL-Hog}$: Non-linear correction factor for hogging, see 2.3.2
- $f_{NL-Sag}$: Non-linear correction factor for sagging, see 2.3.2
- $f_R$: Factor related to the operational profile, see 2.3.2
- $t_{net}$: Net thickness, in mm, see 1.3.1
- $t_{res}$: Reserve thickness, to be taken as 0.5mm
- $I_{net}$: Net vertical hull girder moment of inertia at the cross section under consideration, to be determined using net scantlings as defined in 1.3, in m⁴
- $\sigma_{HG}$: Hull girder bending stress, in N/mm², as defined in 2.5
- $\tau_{HG}$: Hull girder shear stress, in N/mm², as defined in 2.5
- $x$: Longitudinal co-ordinate of a location under consideration, in m
- $z$: Vertical co-ordinate of a location under consideration, in m
- $z_n$: Distance from the baseline to the horizontal neutral axis, in m.

#### S11A.1.2.2 Fore end and aft end

The fore end (FE) of the rule length $L$, see Figure 1, is the perpendicular to the scantling draught waterline at the forward side of the stem.

The aft end (AE) of the rule length $L$, see Figure 1, is the perpendicular to the scantling draught waterline at a distance $L$ aft of the fore end (FE).

![Figure 1: Ends of length L](A profile view of a ship hull showing the locations of AE (Aft End) and FE (Fore End) at the scantling draught waterline, with the total length L and L/2 markings indicated from the midship.)

#### S11A.1.2.3 Reference coordinate system

The ships geometry, loads and load effects are defined with respect to the following right-hand coordinate system (see Figure 2):

- **Origin:** At the intersection of the longitudinal plane of symmetry of ship, the aft end of $L$ and the baseline.
- **X axis:** Longitudinal axis, positive forwards.
- **Y axis:** Transverse axis, positive towards portside.
- **Z axis:** Vertical axis, positive upwards.

![Figure 2: Reference coordinate system](A 3D perspective diagram of a container ship hull showing the X, Y, and Z axes. The origin is at the baseline at the AE. X points forward, Y points to port, and Z points upward. Rotation arrows indicate positive conventions for moments.)

### S11A.1.3 Corrosion margin and net thickness

#### S11A.1.3.1 Net scantling definitions

The strength is to be assessed using the net thickness approach on all scantlings.

The net thickness, $t_{net}$, for the plates, webs and flanges is obtained by subtracting the voluntary addition $t_{vol\_add}$ and the factored corrosion addition $t_c$ from the as built thickness $t_{as\_built}$, as follows:

$$t_{net} = t_{as\_built} - t_{vol\_add} - \alpha t_c$$

where $\alpha$ is a corrosion addition factor whose values are defined in Table 1.

The voluntary addition, if being used, is to be clearly indicated on the drawings.

**Table 1: Values of corrosion addition factor**

| Structural requirement | Property / analysis type | $\alpha$ |
| :--- | :--- | :--- |
| Strength assessment (S11A.3) | Section properties | 0.5 |
| Buckling strength (S11A.4) | Section properties (stress determination) | 0.5 |
| | Buckling capacity | 1.0 |
| Hull girder ultimate strength (S11A.5) | Section properties | 0.5 |
| | Buckling / collapse capacity | 0.5 |

#### S11A.1.3.2 Determination of corrosion addition

The corrosion addition for each of the two sides of a structural member, $t_{c1}$ or $t_{c2}$ is specified in Table 2. The total corrosion addition, $t_c$, in mm, for both sides of the structural member is obtained by the following formula:

$$t_c = (t_{c1} + t_{c2}) + t_{res}$$

For an internal member within a given compartment, the total corrosion addition, $t_c$ is obtained from the following formula:

$$t_c = (2t_{c1}) + t_{res}$$

The corrosion addition of a stiffener is to be determined according to the location of its connection to the attached plating.

**Table 2: Corrosion addition for one side of a structural member**

| Compartment type | One side corrosion addition $t_{c1}$ or $t_{c2}$ [mm] |
| :--- | :---: |
| Exposed to sea water | 1.0 |
| Exposed to atmosphere | 1.0 |
| Ballast water tank | 1.0 |
| Void and dry spaces | 0.5 |
| Fresh water, fuel oil and lube oil tank | 0.5 |
| Accommodation spaces | 0.0 |
| Container holds | 1.0 |
| Compartment types not mentioned above | 0.5 |

#### S11A.1.3.3 Determination of net section properties

The net section modulus, moment of inertia and shear area properties of a supporting member are to be carried out using the net dimensions of the attached plate, web and flange, as defined in Figure 3. The net cross-sectional area, the moment of inertia about the axis parallel to the attached plate and the associated neutral axis position are to be determined through applying a corrosion magnitude of $0.5 \alpha t_c$ deducted from the surface of the profile cross-section.

![Figure 3: Net sectional properties of supporting members](A series of diagrams showing cross-sections of T-profiles, L-profiles, Flat Bar (FB) profiles, and Bulb profiles. Each shows the 'as-built' (gross) dimensions and the 'net' dimensions shaded or outlined, indicating the reduction due to corrosion addition.)

## S11A.2 Loads

### S11A.2.1 Sign convention for hull girder loads

The sign conventions of vertical bending moments and vertical shear forces at any ship transverse section are as shown in Figure 4, namely:

- The vertical bending moments $M_S$ and $M_W$ are positive when they induce tensile stresses in the strength deck (hogging bending moment) and negative when they induce tensile stresses in the bottom (sagging bending moment).
- The vertical shear forces $F_S, F_W$ are positive in the case of downward resulting forces acting aft of the transverse section and upward resulting forces acting forward of the transverse section under consideration. The shear forces in the directions opposite to above are negative.

![Figure 4: Sign conventions of bending moments and shear forces](Diagrams illustrating the positive conventions for bending moments (causing hogging) and shear forces (downward aft, upward forward).)

### S11A.2.2 Still water bending moments and shear forces

#### S11A.2.2.1 General

Still water bending moments, $M_S$ in kNm, and still water shear forces, $F_S$ in kN, are to be calculated at each section along the ship length for design loading conditions as specified in 2.2.2.

#### S11A.2.2.2 Design loading conditions

In general, the design cargo and ballast loading conditions, based on amount of bunker, fresh water and stores at departure and arrival, are to be considered for the $M_S$ and $F_S$ calculations. Where the amount and disposition of consumables at any intermediate stage of the voyage are considered more severe, calculations for such intermediate conditions are to be submitted in addition to those for departure and arrival conditions. Also, where any ballasting and/or de-ballasting is intended during voyage, calculations of the intermediate condition just before and just after ballasting and/or de-ballasting any ballast tank are to be submitted and where approved included in the loading manual for guidance.

The permissible vertical still water bending moments $M_{Smax}$ and $M_{Smin}$ and the permissible vertical still water shear forces $F_{Smax}$ and $F_{Smin}$ in seagoing conditions at any longitudinal position are to envelop:

- The maximum and minimum still water bending moments and shear forces for the seagoing loading conditions defined in the Loading Manual.
- The maximum and minimum still water bending moments and shear forces specified by the designer.

The Loading Manual should include the relevant loading conditions, which envelop the still water hull girder loads for seagoing conditions, including those specified in UR S1 Annex 1.

### S11A.2.3 Wave loads

#### S11A.2.3.1 Wave parameter

The wave parameter is defined as follows:

$$C = 1 - 1.50 \left( 1 - \sqrt{\frac{L}{L_{ref}}} \right)^{2.2} \quad \text{for } L \le L_{ref}$$
$$C = 1 - 0.45 \left( \sqrt{\frac{L}{L_{ref}}} - 1 \right)^{1.7} \quad \text{for } L > L_{ref}$$

where:
- $L_{ref}$ = Reference length, in m, taken as:
- $L_{ref} = 315 C_w^{-1.3}$ for the determination of vertical wave bending moments according to 2.3.2
- $L_{ref} = 330 C_w^{-1.3}$ for the determination of vertical wave shear forces according to 2.3.3

#### S11A.2.3.2 Vertical wave bending moments

The distribution of the vertical wave induced bending moments, $M_W$ in kNm, along the ship length is given in Figure 6, where:

$$M_{W-Hog} = +1.5 f_R L^3 C C_w \left( \frac{B}{L} \right)^{0.8} f_{NL-Hog}$$
$$M_{W-Sag} = -1.5 f_R L^3 C C_w \left( \frac{B}{L} \right)^{0.8} f_{NL-Sag}$$

where:
- $f_R$: Factor related to the operational profile, to be taken as: $f_R = 0.85$
- $f_{NL-Hog}$: Non-linear correction factor for hogging, to be taken as:
  $f_{NL-Hog} = 0.3 \frac{C_B}{C_w} \sqrt{T}$, not to be taken greater than 1.1
- $f_{NL-Sag}$: Non-linear correction factor for sagging, to be taken as:
  $f_{NL-Sag} = 4.5 \frac{1 + 0.2 f_{Bow}}{C_w \sqrt{C_B} L^{0.3}}$, not to be taken less than 1.0
- $f_{Bow}$: Bow flare shape coefficient, to be taken as:
  $f_{Bow} = \frac{A_{DK} - A_{WL}}{0.2 L z_f}$
- $A_{DK}$: Projected area in horizontal plane of uppermost deck, in m² including the forecastle deck, if any, extending from $0.8L$ forward (see Figure 5). Any other structures, e.g. plated bulwark, are to be excluded.
- $A_{WL}$: Waterplane area, in m², at draught $T$, extending from $0.8L$ forward.
- $z_f$: Vertical distance, in m, from the waterline at draught $T$ to the uppermost deck (or forecastle deck), measured at FE (see Figure 5). Any other structures, e.g. plated bulwark, are to be excluded.

![Figure 5: Projected area $A_{DK}$ and vertical distance $z_f$](Three diagrams showing different hull bow shapes (with and without forecastle decks). Shaded areas indicate $A_{DK}$ from 0.8L to FE. Vertical measurements for $z_f$ are shown at the FE from the waterline to the deck.)

![Figure 6: Distribution of vertical wave bending moment $M_W$ along the ship length](A trapezoidal distribution graph of wave bending moment $M_W$ along the ship length L. It shows peaks between 0.35L and 0.55L for hogging, and 0.35L and 0.6L for sagging. Scaling factors (0.15, 0.25) are indicated at 0.1L and 0.8L.)

#### S11A.2.3.3 Vertical wave shear force

The distribution of the vertical wave induced shear forces, $F_W$ in kN, along the ship length is given in Figure 7, where,

$$F_{W-Hog}^{Aft} = +5.2 f_R L^2 C C_w \left( \frac{B}{L} \right)^{0.8} (0.3 + 0.7 f_{NL-Hog})$$
$$F_{W-Hog}^{Fore} = -5.7 f_R L^2 C C_w \left( \frac{B}{L} \right)^{0.8} f_{NL-Hog}$$
$$F_{W-Sag}^{Aft} = -5.2 f_R L^2 C C_w \left( \frac{B}{L} \right)^{0.8} (0.3 + 0.7 f_{NL-Sag})$$
$$F_{W-Sag}^{Fore} = +5.7 f_R L^2 C C_w \left( \frac{B}{L} \right)^{0.8} (0.25 + 0.75 f_{NL-Sag})$$
$$F_W^{Mid} = +4.0 f_R L^2 C C_w \left( \frac{B}{L} \right)^{0.8}$$

![Figure 7: Distribution of vertical wave shear force $F_W$ along the ship length](A graph showing the distribution of vertical wave shear force $F_W$ along the length of the ship. It has a complex shape with multiple peaks and troughs, reaching maximums around 0.15L and 0.85L. Coordinate points for longitudinal positions (0.15L, 0.3L, 0.4L, 0.5L, 0.6L, 0.75L, etc.) are labeled.)

### S11A.2.4 Load cases

For the strength assessment, the maximum hogging and sagging load cases given in Table 3 are to be checked. For each load case the still water condition at each section as defined in 2.2 is to be combined with the wave condition as defined in 2.3, refer also to Figure 8.

**Table 3: Combination of still water and wave bending moments and shear forces**

| Load case | Bending moment | | Shear force | |
| :--- | :---: | :---: | :---: | :---: |
| | $M_S$ | $M_W$ | $F_S$ | $F_W$ |
| Hogging | $M_{Smax}$ | $M_{WH}$ | $F_{Smax}$ for $x \le 0.5L$ | $F_{Wmax}$ for $x \le 0.5L$ |
| | | | $F_{Smin}$ for $x > 0.5L$ | $F_{Wmin}$ for $x > 0.5L$ |
| Sagging | $M_{Smin}$ | $M_{WS}$ | $F_{Smin}$ for $x \le 0.5L$ | $F_{Wmin}$ for $x \le 0.5L$ |
| | | | $F_{Smax}$ for $x > 0.5L$ | $F_{Wmax}$ for $x > 0.5L$ |

- $M_{WH}$: Wave bending moment in hogging at the cross section under consideration, to be taken as the positive value of $M_W$ as defined in Figure 6.
- $M_{WS}$: Wave bending moment in sagging at the cross section under consideration, to be taken as the negative value of $M_W$ as defined in Figure 6.
- $F_{Wmax}$: Maximum value of the wave shear force at the cross section under consideration, to be taken as the positive value of $F_W$ as defined in Figure 7.
- $F_{Wmin}$: Minimum value of the wave shear force at the cross section under consideration, to be taken as the negative value of $F_W$ as defined in Figure 7.

![Figure 8: Load combination to determine the maximum hogging and sagging load cases as given in Table 3](A set of plots showing representative still water ($M_S, F_S$) and wave ($M_W, F_W$) distributions for hogging and sagging conditions.)

### S11A.2.5 Hull girder stress

The hull girder stresses in N/mm² are to be determined at the load calculation point under consideration, for the "hogging" and "sagging" load cases defined in 2.4 as follows:

Bending stress:
$$\sigma_{HG} = \frac{\gamma_s M_s + \gamma_W M_W}{I_{net}} (z - z_n) 10^{-3}$$

Shear stress:
$$\tau_{HG} = \frac{\gamma_s F_s + \gamma_W F_W}{t_{net} / q_v} 10^3$$

where:
- $\gamma_s, \gamma_W$: Partial safety factors, to be taken as:
- $\gamma_s = 1.0$
- $\gamma_W = 1.0$

## S11A.3 Strength Assessment

### S11A.3.1 General

Continuity of structure is to be maintained throughout the length of the ship. Where significant changes in structural arrangement occur adequate transitional structure is to be provided.

### S11A.3.2 Stiffness criterion

The two load cases "hogging" and "sagging" as listed in 2.4 are to be checked.
The net moment of inertia, in m⁴, is not to be less than:

$$I_{net} \ge 1.55 L |M_s + M_W| 10^{-7}$$

### S11A.3.3 Yield strength assessment

#### S11A.3.3.1 General acceptance criteria

The yield strength assessment is to check, for each of the load cases "hogging" and "sagging" as defined in 2.4, that the equivalent hull girder stress $\sigma_{eq}$, in N/mm², is less than the permissible stress $\sigma_{perm}$, in N/mm², as follows:

$$\sigma_{eq} < \sigma_{perm}$$

where:
- $\sigma_{eq} = \sqrt{\sigma_x^2 + 3\tau^2}$
- $\sigma_{perm} = \frac{R_{eH}}{\gamma_1 \gamma_2}$
- $\gamma_1$: Partial safety factor for material, to be taken as: $\gamma_1 = k \frac{R_{eH}}{235}$
- $\gamma_2$: Partial safety factor for load combinations and permissible stress, to be taken as:
  - $\gamma_2 = 1.24$, for bending strength assessment according to 3.3.2.
  - $\gamma_2 = 1.13$, for shear stress assessment according to 3.3.3.

#### S11A.3.3.2 Bending strength assessment

The assessment of the bending stresses is to be carried out according to 3.3.1 at the following locations of the cross section:
- At bottom
- At deck
- At top of hatch coaming
- At any point where there is a change of steel yield strength

The following combination of hull girder stress as defined in 2.5 is to be considered:
- $\sigma_x = \sigma_{HG}$
- $\tau = 0$

#### S11A.3.3.3 Shear strength assessment

The assessment of shear stress is to be carried out according to 3.3.1 for all structural elements that contribute to the shear strength capability.

The following combination of hull girder stress as defined in 2.5 is to be considered:
- $\sigma_x = 0$
- $\tau = \tau_{HG}$

## S11A.4 Buckling strength

### S11A.4.1 Application

These requirements apply to plate panels and longitudinal stiffeners subject to hull girder bending and shear stresses.

Definitions of symbols used in the present article S11A.4 are given in Annex 2 "Buckling Capacity".

### S11A.4.2 Buckling criteria

The acceptance criterion for the buckling assessment is defined as follows:

$$\eta_{act} \le 1$$

where:
- $\eta_{act}$: Maximum utilisation factor as defined in S11A 4.3.

### S11A.4.3 Buckling utilisation factor

The utilisation factor, $\eta_{act}$, is defined as the inverse of the stress multiplication factor at failure $\gamma_c$, see Figure 9.

$$\eta_{act} = \frac{1}{\gamma_c}$$

Failure limit states are defined in:
- Annex 2, 2 for elementary plate panels,
- Annex 2, 3 for overall stiffened panels,
- Annex 2, 4 for longitudinal stiffeners.

Each failure limit state is defined by an equation, and $\gamma_c$ is to be determined such that it satisfies the equation.

Figure 9 illustrates how the stress multiplication factor at failure $\gamma_c$, of a structural member is determined for any combination of longitudinal and shear stress. Where:
- $\sigma_x, \tau$: Applied stress combination for buckling given in S11A.4.4.1
- $\sigma_c, \tau_c$: Critical buckling stresses to be obtained according to Annex 2 for the stress combination for buckling $\sigma_x$ and $\tau$.

![Figure 9: Example of failure limit state curve and stress multiplication factor at failure](A graph showing a 'Failure limit state curve' in a coordinate system of shear stress ($\tau$) vs longitudinal stress ($\sigma_x$). An 'Applied stress' point is shown, and a vector extends from the origin through this point to the curve, defining the 'Stress at failure' ($\gamma_c \sigma_x, \gamma_c \tau$).)

### S11A.4.4 Stress determination

#### S11A.4.4.1 Stress combinations for buckling assessment

The following two stress combinations are to be considered for each of the load cases "hogging" and "sagging" as defined in S11A.2.4. The stresses are to be derived at the load calculation points defined in S11A.4.4.2

**a) Longitudinal stiffening arrangement:**

- **Stress combination 1 with:**
  - $\sigma_x = \sigma_{HG}$
  - $\sigma_y = 0$
  - $\tau = 0.7 \tau_{HG}$

- **Stress combination 2 with:**
  - $\sigma_x = 0.7 \sigma_{HG}$
  - $\sigma_y = 0$
  - $\tau = \tau_{HG}$

**b) Transverse stiffening arrangement:**

- **Stress combination 1 with:**
  - $\sigma_x = 0$
  - $\sigma_y = \sigma_{HG}$
  - $\tau = 0.7 \tau_{HG}$

- **Stress combination 2 with:**
  - $\sigma_x = 0$
  - $\sigma_y = 0.7 \sigma_{HG}$
  - $\tau = \tau_{HG}$

#### S11A.4.4.2 Load calculation points

The hull girder stresses for elementary plate panels (EPP) are to be calculated at the load calculation points defined in Table 4.

**Table 4: Load calculation points (LCP) coordinates for plate buckling assessment**

| LCP coordinates | Hull girder bending stress | | Hull girder shear stress |
| :--- | :--- | :--- | :--- |
| | Non horizontal plating | Horizontal plating | |
| **x coordinate** | | Mid-length of the EPP | |
| **y coordinate** | Both upper and lower ends of the EPP (points A1 and A2 in Figure 10) | Outboard and inboard ends of the EPP (points A1 and A2 in Figure 10) | Mid-point of EPP (point B in Figure 10) |
| **z coordinate** | | Corresponding to x and y values | |

![Figure 10: LCP for plate buckling - assessment, PSM stands for primary supporting members](Diagrams showing 'Longitudinal Framing' and 'Transverse Framing' with labeled points A1, A2, and B representing load calculation points for plate panels relative to stiffeners and primary supporting members (PSM).)

The hull girder stresses for longitudinal stiffeners are to be calculated at the following load calculation point:
- at the mid length of the considered stiffener.
- at the intersection point between the stiffener and its attached plate.

## S11A.5 Hull girder ultimate strength

### S11A.5.1 General

The hull girder ultimate strength is to be assessed for ships with length $L$ equal or greater than 150m.
The acceptance criteria, given in 5.4 are applicable to intact ship structures.
The hull girder ultimate bending capacity is to be checked for the load cases "hogging" and "sagging" as defined in 2.4.

### S11A.5.2 Hull girder ultimate bending moments

The vertical hull girder bending moment, $M$ in hogging and sagging conditions, to be considered in the ultimate strength check is to be taken as:

$$M = \gamma_s M_s + \gamma_W M_W$$

where:
- $M_s$ = Permissible still water bending moment, in kNm, defined in 2.4
- $M_W$ = Vertical wave bending moment, in kNm, defined in 2.4.
- $\gamma_s$ = Partial safety factor for the still water bending moment, to be taken as: $\gamma_s = 1.0$
- $\gamma_W$ = Partial safety factor for the vertical wave bending moment, to be taken as: $\gamma_W = 1.2$

### S11A.5.3 Hull girder ultimate bending capacity

#### S11A.5.3.1 General

The hull girder ultimate bending moment capacity, $M_U$ is defined as the maximum bending moment capacity of the hull girder beyond which the hull structure collapses.

#### S11A.5.3.2 Determination of hull girder ultimate bending moment capacity

The ultimate bending moment capacities of a hull girder transverse section, in hogging and sagging conditions, are defined as the maximum values of the curve of bending moment $M$ versus the curvature $\chi$ of the transverse section considered ($M_{UH}$ for hogging condition and $M_{US}$ for sagging condition, see Figure 11). The curvature $\chi$ is positive for hogging condition and negative for sagging condition.

![Figure 11: Bending moment M versus curvature $\chi$](A graph of bending moment $M$ vs curvature $\chi$. The curve starts from the origin, goes positive to a peak $M_{UH}$ (hogging) and then drops. It also goes negative to a trough $M_{US}$ (sagging) and then rises. Key points $\chi_F$ and $-\chi_F$ are marked on the axes.)

The hull girder ultimate bending moment capacity $M_U$ is to be calculated using the incremental-iterative method as given in 2 of Annex 3 or using an alternative method as indicated in 3 of Annex 3.

### S11A.5.4 Acceptance criteria

The hull girder ultimate bending capacity at any hull transverse section is to satisfy the following criteria:

$$M \le \frac{M_U}{\gamma_M \gamma_{DB}}$$

where:
- $M$ = Vertical bending moment, in kNm, to be obtained as specified in 5.2.
- $M_U$ = Hull girder ultimate bending moment capacity, in kNm, to be obtained as specified in 5.3.
- $\gamma_M$ = Partial safety factor for the hull girder ultimate bending capacity, covering material, geometric and strength prediction uncertainties, to be taken as: $\gamma_M = 1.05$
- $\gamma_{DB}$ = Partial safety factor for the hull girder ultimate bending moment capacity, covering the effect of double bottom bending, to be taken as:
  - For hogging condition: $\gamma_{DB} = 1.15$
  - For sagging condition: $\gamma_{DB} = 1.0$

For cross sections where the double bottom breadth of the inner bottom is less than that at amidships or where the double bottom structure differs from that at amidships (e.g. engine room sections), the factor $\gamma_{DB}$ for hogging condition may be reduced based upon agreement with the Classification Society.

## S11A.6 Additional requirements for large container ships

### S11A.6.1 General

The requirements in S11A.6.2 and S11A.6.3 are applicable, in addition to requirements in S11A.3 to S11A.5, to container ships with a breadth $B$ greater than 32.26 m.

### S11A.6.2 Yielding and buckling assessment

Yielding and buckling assessments are to be carried out in accordance with the Rules of the Classification Society, taking into consideration additional hull girder loads (wave torsion, wave horizontal bending and static cargo torque), as well as local loads. All in-plane stress components (i.e. bi-axial and shear stresses) induced by hull girder loads and local loads are to be considered.

### S11A.6.3 Whipping

Hull girder ultimate strength assessment is to take into consideration the whipping contribution to the vertical bending moment according to the Classification Society procedures.

***

# S11A Annex 1 – Calculation of shear flow

## 1. General

This annex describes the procedures of direct calculation of shear flow around a ship's cross section due to hull girder vertical shear force. The shear flow $q_v$ at each location in the cross section, is calculated by considering the cross section is subjected to a unit vertical shear force of 1 N.

The unit shear flow per mm, $q_v$, in N/mm, is to be taken as:
$$q_v = q_D + q_I$$

where:
- $q_D$: Determinate shear flow, as defined in 2.
- $q_I$: Indeterminate shear flow which circulates around the closed cells, as defined in 3.

In the calculation of the unit shear flow, $q_v$, the longitudinal stiffeners are to be taken into account.

## 2. Determinate shear flow

The determinate shear flow, $q_D$, in N/mm at each location in the cross section is to be obtained from the following line integration:
$$q_D(s) = -\frac{1}{10^6 I_{y-net}} \int_0^s (z - z_n) t_{net} ds$$

where:
- $s$: Coordinate value of running coordinate along the cross section, in m.
- $I_{y-net}$: Net moment of inertia of the cross section, in m⁴.
- $t_{net}$: Net thickness of plating, in mm.
- $z_n$: Z coordinate of horizontal neutral axis from baseline, in m.

It is assumed that the cross section is composed of line segments as shown in Figure 1: where each line segment has a constant plate net thickness. The determinate shear flow is obtained by the following equation.
$$q_{Dk} = -\frac{t_{net} \ell}{2 \cdot 10^6 I_{y-net}} (z_k + z_i - 2z_n) + q_{Di}$$

where:
- $q_{Dk}, q_{Di}$: Determinate shear flow at node $k$ and node $i$ respectively, in N/mm.
- $\ell$: Length of line segments, in m.
- $y_k, y_i$: Y coordinate of the end points $k$ and $i$ of line segment, in m, as defined in Figure 1.
- $z_k, z_i$: Z coordinate of the end points $k$ and $i$ of line segment, in m, as defined in Figure 1.

Where the cross section includes closed cells, the closed cells are to be cut with virtual slits, as shown in Figure 2: in order to obtain the determinate shear flow. These virtual slits must not be located in walls which form part of another closed cell.

Determinate shear flow at bifurcation points is to be calculated by water flow calculations, or similar, as shown in Figure 2.

![Figure 1: Definition of line segment](A diagram showing a single line segment in a Y-Z coordinate system, with endpoints labeled $i$ ($y_i, z_i$) and $k$ ($y_k, z_k$), length $\ell$, and running coordinate $s$.)

![Figure 2: Placement of virtual slits and calculation of determinate shear flow at bifurcation points](A diagram of a multi-cell cross-section with 'Virtual slits' indicated by double parallel lines, and 'Start/End points' for paths. It illustrates how path flows ($q_{d1end}, q_{d2end}, etc.$) are summed at bifurcation points.)

## 3. Indeterminate shear flow

The indeterminate shear flow around closed cells of a cross section is considered as a constant value within the same closed cell. The following system of equation for determination of indeterminate shear flows can be developed. In the equations, contour integrations of several parameters around all closed cells are performed.

$$q_{Ic} \oint_c \frac{1}{t_{net}} ds - \sum_{m=1}^{N_w} \left( q_{Im} \oint_{c\&m} \frac{1}{t_{net}} ds \right) = -\oint_c \frac{q_D}{t_{net}} ds$$

where:
- $N_w$: Number of common walls shared by cell $c$ and all other cells.
- $c\&m$: Common wall shared by cells $c$ and $m$
- $q_{Ic}, q_{Im}$: Indeterminate shear flow around the closed cell $c$ and $m$ respectively, in N/mm.

Under the assumption of the assembly of line segments shown in Figure 1 and constant plate thickness of each line segment, the above equation can be expressed as follows:

$$q_{Ic} \sum_{j=1}^{N_c} \left( \frac{\ell}{t_{net}} \right)_j - \sum_{m=1}^{N_w} \left\{ q_{Im} \left[ \sum_{j=1}^{N_m} \left( \frac{\ell}{t_{net}} \right)_j \right]_m \right\} = -\sum_{j=1}^{N_c} \phi_j$$

$$\phi_j = \left[ -\frac{\ell^2}{6 \cdot 10^3 I_{y-net}} (z_k + 2z_i - 3z_n) + \frac{\ell}{t_{net}} q_{Di} \right]_j$$

where:
- $N_c$: Number of line segments in cell $c$.
- $N_m$: Number of line segments on the common wall shared by cells $c$ and $m$.
- $q_{Di}$: Determinate shear flow, in N/mm, calculated according to Annex 1, 2.

The difference in the directions of running coordinates specified in Annex 1, 2 and in this section has to be considered.

![Figure 3: Closed cells and common wall](A sketch showing two adjacent closed cells, Cell 'm' and Cell 'c', sharing a 'Common wall'.)

## 4. Computation of sectional properties

Properties of the cross section are to be obtained by the following formulae where the cross section is assumed as the assembly of line segments:

$$\ell = \sqrt{(y_k - y_i)^2 + (z_k - z_i)^2}$$
$$a_{net} = 10^{-3} \ell t_{net}$$
$$A_{net} = \sum a_{net}$$
$$s_{y-net} = \frac{a_{net}}{2} (z_k + z_i)$$
$$S_{y-net} = \sum s_{y-net}$$
$$i_{y0-net} = \frac{a_{net}}{3} (z_k^2 + z_k z_i + z_i^2)$$
$$I_{y0-net} = \sum i_{y0-net}$$

where:
- $a_{net}, A_{net}$: Area of the line segment and the cross section respectively, in m².
- $s_{y-net}, S_{y-net}$: First moment of the line segment and the cross section about the baseline, in m³.
- $i_{y0-net}, I_{y0-net}$: Moment of inertia of the line segment and the cross section about the baseline, in m⁴.

The height of horizontal neutral axis, $z_n$, in m, is to be obtained as follows:
$$z_n = \frac{S_{y-net}}{A_{net}}$$

Inertia moment about the horizontal neutral axis, in m⁴, is to be obtained as follows:
$$I_{y-net} = I_{y0-net} - z_n^2 A_{net}$$

***

# S11A Annex 2 – Buckling Capacity

## Symbols

- $x$ axis: Local axis of a rectangular buckling panel parallel to its long edge.
- $y$ axis: Local axis of a rectangular buckling panel perpendicular to its long edge.
- $\sigma_x$: Membrane stress applied in x direction, in N/mm².
- $\sigma_y$: Membrane stress applied in y direction, in N/mm².
- $\tau$: Membrane shear stress applied in xy plane, in N/mm².
- $\sigma_a$: Axial stress in the stiffener, in N/mm²
- $\sigma_b$: Bending stress in the stiffener, in N/mm²
- $\sigma_w$: Warping stress in the stiffener, in N/mm²
- $\sigma_{cx}, \sigma_{cy}, \tau_c$: Critical stress, in N/mm², defined in [2.1.1] for plates.
- $R_{eH\_S}$: Specified minimum yield stress of the stiffener, in N/mm²
- $R_{eH\_P}$: Specified minimum yield stress of the plate, in N/mm²
- $a$: Length of the longer side of the plate panel as shown in Table 2, in mm.
- $b$: Length of the shorter side of the plate panel as shown in Table 2, in mm.
- $d$: Length of the side parallel to the axis of the cylinder corresponding to the curved plate panel as shown in Table 3, in mm.
- $\sigma_E$: Elastic buckling reference stress, in N/mm² to be taken as:
  - For the application of plate limit state according to [2.1.2]:
    $$\sigma_E = \frac{\pi^2 E}{12(1-\nu^2)} \left( \frac{t_p}{b} \right)^2$$
  - For the application of curved plate panels according to [2.2]:
    $$\sigma_E = \frac{\pi^2 E}{12(1-\nu^2)} \left( \frac{t_p}{d} \right)^2$$
- $\nu$: Poisson's ratio to be taken equal to 0.3
- $t_p$: Net thickness of plate panel, in mm
- $t_w$: Net stiffener web thickness, in mm
- $t_f$: Net flange thickness, in mm
- $b_f$: Breadth of the stiffener flange, in mm
- $h_w$: Stiffener web height, in mm
- $e_f$: Distance from attached plating to centre of flange, in mm, to be taken as:
  - $e_f = h_w$ for flat bar profile.
  - $e_f = h_w - 0.5 t_f$ for bulb profile.
  - $e_f = h_w + 0.5 t_f$ for angle and Tee profiles.
- $\alpha$: Aspect ratio of the plate panel, to be taken as $\alpha = a / b$
- $\beta$: Coefficient taken as $\beta = \frac{1-\psi}{\alpha}$
- $\psi$: Edge stress ratio to be taken as $\psi = \sigma_2 / \sigma_1$
- $\sigma_1$: Maximum stress, in N/mm²
- $\sigma_2$: Minimum stress, in N/mm²
- $R$: Radius of curved plate panel, in mm
- $\ell$: Span, in mm, of stiffener equal to the spacing between primary supporting members
- $s$: Spacing of stiffener, in mm, to be taken as the mean spacing between the stiffeners of the considered stiffened panel.

## 1. Elementary Plate Panel (EPP)

### 1.1 Definition

An Elementary Plate Panel (EPP) is the unstiffened part of the plating between stiffeners and/or primary supporting members.
All the edges of the elementary plate panel are forced to remain straight (but free to move in the in-plane directions) due to the surrounding structure/neighbouring plates (usually longitudinal stiffened panels in deck, bottom and inner-bottom plating, shell and longitudinal bulkheads).

### 1.2 EPP with different thicknesses

#### 1.2.1 Longitudinally stiffened EPP with different thicknesses

In longitudinal stiffening arrangement, when the plate thickness varies over the width, $b$, in mm, of a plate panel, the buckling capacity is calculated on an equivalent plate panel width, having a thickness equal to the smaller plate thickness, $t_1$. The width of this equivalent plate panel, $b_{eq}$, in mm, is defined by the following formula:
$$b_{eq} = \ell_1 + \ell_2 \left( \frac{t_1}{t_2} \right)^{1.5}$$

where:
- $\ell_1$: Width of the part of the plate panel with the smaller plate thickness, $t_1$, in mm, as defined in Figure 1.
- $\ell_2$: Width of the part of the plate panel with the greater plate thickness, $t_2$, in mm, as defined in Figure 1.

![Figure 1: Plate thickness change over the width](A cross-section diagram of a plate panel supported by two stiffeners. The plate has two different thicknesses, $t_1$ and $t_2$, over widths $\ell_1$ and $\ell_2$. Total width is $b$.)

#### 1.2.2 Transversally stiffened EPP with different thicknesses

In transverse stiffening arrangement, when an EPP is made of different thicknesses, the buckling check of the plate and stiffeners is to be made for each thickness considered constant on the EPP.

## 2. Buckling capacity of plates

### 2.1 Plate panel

#### 2.1.1 Plate limit state

The plate limit state is based on the following interaction formulae:

**a) Longitudinal stiffening arrangement:**
$$\left( \frac{\gamma_c \sigma_x}{\sigma_{cx}} \right)^{2/\beta_p^{0.25}} + \left( \frac{\gamma_c |\tau|}{\tau_c} \right)^{2/\beta_p^{0.25}} = 1$$

**b) Transverse stiffening arrangement:**
$$\left( \frac{\gamma_c \sigma_y}{\sigma_{cy}} \right)^{2/\beta_p^{0.25}} + \left( \frac{\gamma_c |\tau|}{\tau_c} \right)^{2/\beta_p^{0.25}} = 1$$

where:
- $\sigma_x, \sigma_y$: Applied normal stress to the plate panel in N/mm², as defined in S11A 4.4, at load calculation points of the considered elementary plate panel.
- $\tau$: Applied shear stress to the plate panel, in N/mm², as defined in S11A 4.4, at load calculation points of the considered elementary plate panel.
- $\sigma_{cx}$: Ultimate buckling stress in N/mm² in direction parallel to the longer edge of the buckling panel as defined in 2.1.3
- $\sigma_{cy}$: Ultimate buckling stress in N/mm² in direction parallel to the shorter edge of the buckling panel as defined in 2.1.3
- $\tau_c$: Ultimate buckling shear stress, in N/mm² as defined in 2.1.3
- $\beta_p$: Plate slenderness parameter taken as:
  $$\beta_p = \frac{b}{t_p} \sqrt{\frac{R_{eH\_P}}{E}}$$

#### 2.1.2 Reference degree of slenderness

The reference degree of slenderness is to be taken as:
$$\lambda = \sqrt{\frac{R_{eH\_P}}{K \sigma_E}}$$

where:
- $K$: Buckling factor, as defined in Table 2 and Table 3.

#### 2.1.3 Ultimate buckling stresses

The ultimate buckling stress of plate panels, in N/mm², is to be taken as:
$$\sigma_{cx} = C_x R_{eH\_P}$$
$$\sigma_{cy} = C_y R_{eH\_P}$$

The ultimate buckling stress of plate panels subject to shear, in N/mm², is to be taken as:
$$\tau_c = C_\tau \frac{R_{eH\_P}}{\sqrt{3}}$$

where:
- $C_x, C_y, C_\tau$: Reduction factors, as defined in Table 2

The boundary conditions for plates are to be considered as simply supported (see cases 1, 2 and 15 of Table 2). If the boundary conditions differ significantly from simple support, a more appropriate boundary condition can be applied according to the different cases of Table 2 subject to the agreement of the Classification Society.

#### 2.1.4 Correction Factor $F_{long}$

The correction factor $F_{long}$ depending on the edge stiffener types on the longer side of the buckling panel is defined in Table 1. An average value of $F_{long}$ is to be used for plate panels having different edge stiffeners. For stiffener types other than those mentioned in Table 1, the value of $c$ is to be agreed by the Society. In such a case, value of $c$ higher than those mentioned in Table 1 can be used, provided it is verified by buckling strength check of panel using non-linear FE analysis and deemed appropriate by the Classification Society.

**Table 1: Correction Factor $F_{long}$**

| Structural element types | | $F_{long}$ | $c$ |
| :--- | :--- | :---: | :---: |
| Unstiffened Panel | | 1.0 | N/A |
| Stiffened Panel | Stiffener not fixed at both ends | 1.0 | N/A |
| | Stiffener fixed at both ends | Flat bar (1) | $F_{long} = c + 1 \text{ for } \frac{t_w}{t_p} > 1$ | 0.10 |
| | | | $F_{long} = c \left( \frac{t_w}{t_p} \right)^3 + 1 \text{ for } \frac{t_w}{t_p} \le 1$ | 0.30 |
| | | Bulb profile | | 0.30 |
| | | Angle profile | | 0.40 |
| | | T profile | | 0.30 |
| | | Girder of high rigidity (e.g. bottom transverse) | 1.4 | N/A |

*(1) $t_w$ is the net web thickness, in mm, without the correction defined in 4.3.5*

---

**Table 2: Buckling Factor and reduction factor for plane plate panels**
*(Note: This table is highly complex; refer to the original PDF for complete details on formulas for K and C for each case.)*

| Case | Stress ratio $\psi$ | Aspect ratio $\alpha$ | Buckling factor $K$ | Reduction factor $C$ |
| :---: | :---: | :---: | :---: | :---: |
| **1** (Normal stress $\sigma_x$) | $1 \ge \psi \ge 0$ | | $K_x = F_{long} \frac{8.4}{\psi + 1.1}$ | $C_x$ formulas based on $\lambda_c$ |
| | $0 > \psi > -1$ | | $K_x = F_{long} [7.63 - \psi(6.26 - 10\psi)]$ | |
| | $\psi \le -1$ | | $K_x = F_{long} [5.975(1-\psi)^2]$ | |
| **2** (Normal stress $\sigma_y$) | $1 \ge \psi \ge 0$ | | $K_y = \dots$ | $C_y$ formulas based on $\lambda$ |
| **3** (Normal stress $\sigma_x$ with free edge) | $1 \ge \psi \ge 0$ | | $K_x = \frac{4(0.425 + 1/\alpha^2)}{3\psi + 1}$ | $C_x$ formulas |
| **15** (Shear stress $\tau$) | - | | $K_\tau = \sqrt{3} [5.34 + \frac{4}{\alpha^2}]$ | $C_\tau$ formulas |

*(Refer to pages 5-9 of Annex 2 in the PDF for the full set of Cases 1 to 19 and associated formulas.)*

---

## 2.2 Curved plate panels

This requirement for curved plate limit state is applicable when $R/t_p \le 2500$. Otherwise, the requirement for plate limit state given in 2.1.1 is applicable.

The curved plate limit state is based on the following interaction formula:
$$\left( \frac{\gamma_c \sigma_{ax}}{C_{ax} R_{eH\_P}} \right)^{1.25} + \left( \frac{\gamma_c \tau \sqrt{3}}{C_\tau R_{eH\_P}} \right)^2 = 1.0$$

where:
- $\sigma_{ax}$: Applied axial stress to the cylinder corresponding to the curved plate panel, in N/mm². In case of tensile axial stresses, $\sigma_{ax}=0$.
- $C_{ax}, C_\tau$: Buckling reduction factor of the curved plate panel, as defined in Table 3.

The stress multiplier factor $\gamma_c$ of the curved plate panel needs not be taken less than the stress multiplier factor $\gamma_c$ for the expanded plane panel according to 2.1.1.

**Table 3: Buckling Factor and reduction factor for curved plate panel with $R/t_p \le 2500$**
*(Refer to PDF page 10 for full formulas.)*

## 3. Buckling capacity of overall stiffened panel

The elastic stiffened panel limit state is based on the following interaction formula:
$$\frac{P_z}{c_f} = 1$$
where $P_z$ and $c_f$ are defined in 4.4.3.

## 4. Buckling capacity of longitudinal stiffeners

### 4.1 Stiffeners limit states

The buckling capacity of longitudinal stiffeners is to be checked for the following limit states:
- Stiffener induced failure (SI).
- Associated plate induced failure (PI).

### 4.2 Lateral pressure

The lateral pressure is to be considered as constant in the buckling strength assessment of longitudinal stiffeners.

### 4.3 Stiffener idealization

#### 4.3.1 Effective length of the stiffener $\ell_{eff}$

The effective length of the stiffener $\ell_{eff}$, in mm, is to be taken equal to:
- $\ell_{eff} = \frac{\ell}{\sqrt{3}}$ for stiffener fixed at both ends.
- $\ell_{eff} = 0.75 \ell$ for stiffener simply supported at one end and fixed at the other.
- $\ell_{eff} = \ell$ for stiffener simply supported at both ends.

#### 4.3.2 Effective width of the attached plating $b_{eff1}$

$$b_{eff1} = \frac{C_{x1}b_1 + C_{x2}b_2}{2}$$

#### 4.3.3 Effective width of attached plating $b_{eff}$

$$b_{eff} = \min(b_{eff1}, \chi_s s)$$

### 4.4 Ultimate buckling capacity

#### 4.4.1 Longitudinal stiffener limit state

When $\sigma_a + \sigma_b + \sigma_w > 0$, the ultimate buckling capacity for stiffeners is to be checked according to the following interaction formula:
$$\frac{\gamma_c \sigma_a + \sigma_b + \sigma_w}{R_{eH}} = 1$$

***

# S11A Annex 3 - Hull girder ultimate bending capacity

## Symbols

- $I_{y-net}$: Net moment of inertia, in m⁴, of the hull transverse section around its horizontal neutral axis
- $Z_{B-net}, Z_{D-net}$: Section moduli, in m³, at bottom and deck, respectively,
- $R_{eH\_S}$: Minimum yield stress, in N/mm², of the material of the considered stiffener.
- $R_{eH\_P}$: Minimum yield stress, in N/mm², of the material of the considered plate.
- $A_{s-net}$: Net sectional area, in cm², of stiffener, without attached plating.
- $A_{p-net}$: Net sectional area, in cm², of attached plating.

## 1. General Assumptions

### 1.1
The method for calculating the ultimate hull girder capacity is to identify the critical failure modes of all main longitudinal structural elements.

### 1.2
Structures compressed beyond their buckling limit have reduced load carrying capacity. All relevant failure modes for individual structural elements, such as plate buckling, torsional stiffener buckling, stiffener web buckling, lateral or global stiffener buckling and their interactions, are to be considered in order to identify the weakest inter-frame failure mode.

## 2. Incremental-iterative method

### 2.1 Assumptions

In applying the incremental-iterative method, the following assumptions are generally to be made:
- The ultimate strength is calculated at hull transverse sections between two adjacent transverse webs.
- The hull girder transverse section remains plane during each curvature increment.
- The hull material has an elasto-plastic behaviour.
- The hull girder transverse section is divided into a set of elements, which are considered to act independently.

According to the iterative procedure, the bending moment $M_i$ acting on the transverse section at each curvature value $\chi_i$ is obtained by summing the contribution given by the stress $\sigma$ acting on each element. The stress $\sigma$ corresponding to the element strain, $\epsilon$ is to be obtained for each curvature increment from the non-linear load-end shortening curves $\sigma-\epsilon$ of the element.

The procedure is to be repeated until the value of the imposed curvature reaches the value $\chi_F$ in m⁻¹, in hogging and sagging condition, obtained from the following formula:
$$\chi_F = \pm 0.003 \frac{M_y}{E I_{y-net}}$$

where $M_y$ is the lesser of $10^3 R_{eH} Z_{B-net}$ and $10^3 R_{eH} Z_{D-net}$.

### 2.2 Procedure

#### 2.2.1 General

The curve $M-\chi$ is to be obtained by means of an incremental-iterative approach, summarised in the flow chart in Figure 1.

![Figure 1: Flow chart of the procedure for the evaluation of the curve $M-\chi$](A process flow chart starting from 'Start', through 'First step $\chi_{i-1} = 0$', 'Calculation of neutral axis position', 'Increment of curvature', 'Calculation of strain $\epsilon$', 'Calculation of stress $\sigma$' (using Curve $\sigma-\epsilon$), 'Calculation of new neutral axis position' (with an equilibrium loop), 'Calculation of bending moment $M_i$' (using Curve $M-\chi$), and checking if $\chi > \chi_F$ to reach 'End'.)

## 3. Alternative methods

### 3.1 General

Application of alternative methods (such as non-linear finite element analysis) is to be agreed by the Society prior to commencement.

---
**End of Document**