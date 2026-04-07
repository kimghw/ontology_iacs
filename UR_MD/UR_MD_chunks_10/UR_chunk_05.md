# FILE: UR_S/ur-s19rev5.md
================================================================================

# S19 Evaluation of Scantlings of the Transverse Watertight Corrugated Bulkhead between Cargo Holds Nos. 1 and 2, with Cargo Hold No. 1 Flooded, for Existing Bulk Carriers

(1997)
(Rev. 1 1997)
(Rev. 2 Feb. 1998)
(Rev. 3 Jun. 1998)
(Rev. 4 Sept. 2000)
(Rev. 5 July 2004)

### S19.1 - Application and definitions

These requirements apply to all bulk carriers of 150 m in length and above, in the foremost hold, intending to carry solid bulk cargoes having a density of 1.78 t/m³, or above, with single deck, topside tanks and hopper tanks, fitted with vertically corrugated transverse watertight bulkheads between cargo holds No. 1 and 2 where:

(i) the foremost hold is bounded by the side shell only for ships which were contracted for construction prior to 1 July 1998, and have not been constructed in compliance with IACS Unified Requirement S18,

(ii) the foremost hold is double side skin construction of less than 760 mm breadth measured perpendicular to the side shell in ships, the keels of which were laid, or which were at a similar stage of construction, before 1 July 1999 and have not been constructed in compliance with IACS Unified Requirement S18 (Rev. 2, Sept. 2000).

The net scantlings of the transverse bulkhead between cargo holds Nos. 1 and 2 are to be calculated using the loads given in S19.2, the bending moment and shear force given in S19.3 and the strength criteria given in S19.4.

Where necessary, steel renewal and/or reinforcements are required as per S19.6.

In these requirements, homogeneous loading condition means a loading condition in which the ratio between the highest and the lowest filling ratio, evaluated for the two foremost cargo holds, does not exceed 1.20, to be corrected for different cargo densities.

### S19.2 - Load model

#### S19.2.1 - General

The loads to be considered as acting on the bulkhead are those given by the combination of the cargo loads with those induced by the flooding of cargo hold No.1.

The most severe combinations of cargo induced loads and flooding loads are to be used for the check of the scantlings of the bulkhead, depending on the loading conditions included in the loading manual:
- homogeneous loading conditions;
- non homogeneous loading conditions.

Non homogeneous part loading conditions associated with multiport loading and unloading operations for homogeneous loading conditions need not to be considered according to these requirements.

**Notes:**
1. Changes introduced in Revision 2 to UR S19, i.e. the introduction of the first sentence of S19.6 as well as the Annex are to be applied by all Member societies and Associates not later than 1 July 1998.
2. Annex 2 contains, for guidance only, a flow chart entitled "Guidance to assess capability of Carriage of High Density Cargoes on Existing Bulk Carriers according to the Strength of Transverse Bulkhead between Cargo Holds Nos. 1 and 2".
3. Changes introduced in Rev.4 are to be uniformly implemented by IACS Members and Associates from 1 July 2001.
4. The "contracted for construction" date means the date on which the contract to build the vessel is signed between the prospective owner and the shipbuilder. For further details regarding the date of "contract for construction", refer to IACS Procedural Requirement (PR) No. 29.

---

#### S19.2.2 - Bulkhead corrugation flooding head

The flooding head $h_f$ (see Figure 1) is the distance, in m, measured vertically with the ship in the upright position, from the calculation point to a level located at a distance $d_f$, in m, from the baseline equal to:

a) in general:
- $D$

b) for ships less than 50,000 tonnes deadweight with Type B freeboard:
- $0.95 \cdot D$

$D$ being the distance, in m, from the baseline to the freeboard deck at side amidship (see Figure 1).

c) for ships to be operated at an assigned load line draught $T_r$ less than the permissible load line draught $T$, the flooding head defined in a) and b) above may be reduced by $T - T_r$.

#### S19.2.3 - Pressure in the flooded hold

##### S19.2.3.1 - Bulk cargo loaded hold

Two cases are to be considered, depending on the values of $d_1$ and $d_f$, $d_1$ (see Figure 1) being a distance from the baseline given, in m, by:

$$d_1 = \frac{M_c}{\rho_c \cdot l_c \cdot B} + \frac{V_{LS}}{l_c \cdot B} + (h_{HT} - h_{DB}) \cdot \frac{b_{HT}}{B} + h_{DB}$$

where:
- $M_c$ = mass of cargo, in tonnes, in hold No. 1
- $\rho_c$ = bulk cargo density, in t/m³
- $l_c$ = length of hold No. 1, in m
- $B$ = ship's breadth amidship, in m
- $V_{LS}$ = volume, in m³, of the bottom stool above the inner bottom
- $h_{HT}$ = height of the hopper tanks amidship, in m, from the baseline
- $h_{DB}$ = height of the double bottom, in m
- $b_{HT}$ = breadth of the hopper tanks amidship, in m.

---

a) $d_f \geq d_1$

At each point of the bulkhead located at a distance between $d_1$ and $d_f$ from the baseline, the pressure $p_{c,f}$, in kN/m², is given by:

$$p_{c,f} = \rho \cdot g \cdot h_f$$

where:
- $\rho$ = sea water density, in t/m³
- $g$ = 9.81 m/s², gravity acceleration
- $h_f$ = flooding head as defined in S19.2.2.

At each point of the bulkhead located at a distance lower than $d_1$ from the baseline, the pressure $p_{c,f}$, in kN/m², is given by:

$$p_{c,f} = \rho \cdot g \cdot h_f + [\rho_c - \rho \cdot (1 - \text{perm})] \cdot g \cdot h_1 \cdot \tan^2 \gamma$$

where:
- $\rho, g, h_f$ = as given above
- $\rho_c$ = bulk cargo density, in t/m³
- $\text{perm}$ = permeability of cargo, to be taken as 0.3 for ore (corresponding bulk cargo density for iron ore may generally be taken as 3.0 t/m³),
- $h_1$ = vertical distance, in m, from the calculation point to a level located at a distance $d_1$, as defined above, from the base line (see Figure 1)
- $\gamma = 45^\circ - (\phi / 2)$
- $\phi$ = angle of repose of the cargo, in degrees, and may generally be taken as 35° for iron ore.

The force $F_{c,f}$, in kN, acting on a corrugation is given by:

$$F_{c,f} = s_1 \cdot \left( \rho \cdot g \cdot \frac{(d_f - d_1)^2}{2} + \frac{\rho \cdot g \cdot (d_f - d_1) + (p_{c,f})_{le}}{2} \cdot (d_1 - h_{DB} - h_{LS}) \right)$$

where:
- $s_1$ = spacing of corrugations, in m (see Figure 2a)
- $\rho, g, d_1, h_{DB}$ = as given above
- $d_f$ = as given in S19.2.2
- $(p_{c,f})_{le}$ = pressure, in kN/m², at the lower end of the corrugation
- $h_{LS}$ = height of the lower stool, in m, from the inner bottom.

---

b) $d_f < d_1$

At each point of the bulkhead located at a distance between $d_f$ and $d_1$ from the baseline, the pressure $p_{c,f}$, in kN/m², is given by:

$$p_{c,f} = \rho_c \cdot g \cdot h_1 \cdot \tan^2 \gamma$$

where:
- $\rho_c, g, h_1, \gamma$ = as given in a) above

At each point of the bulkhead located at a distance lower than $d_f$ from the baseline, the pressure $p_{c,f}$, in kN/m², is given by:

$$p_{c,f} = \rho \cdot g \cdot h_f + [\rho_c \cdot h_1 - \rho \cdot (1 - \text{perm}) \cdot h_f] \cdot g \cdot \tan^2 \gamma$$

where:
- $\rho, g, h_f, \rho_c, h_1, \text{perm}, \gamma$ = as given in a) above

The force $F_{c,f}$, in kN, acting on a corrugation is given by:

$$F_{c,f} = s_1 \cdot \left( \rho_c \cdot g \cdot \frac{(d_1 - d_f)^2}{2} \cdot \tan^2 \gamma + \frac{\rho_c \cdot g \cdot (d_1 - d_f) \cdot \tan^2 \gamma + (p_{c,f})_{le}}{2} \cdot (d_f - h_{DB} - h_{LS}) \right)$$

where:
- $s_1, \rho_c, g, \gamma, (p_{c,f})_{le}, h_{LS}$ = as given in a) above
- $d_1, h_{DB}$ = as given in S19.2.3.1
- $d_f$ = as given in S19.2.2.

##### S19.2.3.2 - Empty hold

At each point of the bulkhead, the hydrostatic pressure $p_f$ induced by the flooding head $h_f$ is to be considered.

The force $F_f$, in kN, acting on a corrugation is given by:

$$F_f = s_1 \cdot \rho \cdot g \cdot \frac{(d_f - h_{DB} - h_{LS})^2}{2}$$

where:
- $s_1, \rho, g, h_{LS}$ = as given in S19.2.3.1 a)
- $h_{DB}$ = as given in S19.2.3.1
- $d_f$ = as given in S19.2.2.

---

#### S19.2.4 - Pressure in the non-flooded bulk cargo loaded hold

At each point of the bulkhead, the pressure $p_c$, in kN/m², is given by:

$$p_c = \rho_c \cdot g \cdot h_1 \cdot \tan^2 \gamma$$

where:
- $\rho_c, g, h_1, \gamma$ = as given in S19.2.3.1 a)

The force $F_c$, in kN, acting on a corrugation is given by:

$$F_c = \rho_c \cdot g \cdot s_1 \cdot \frac{(d_1 - h_{DB} - h_{LS})^2}{2} \cdot \tan^2 \gamma$$

where:
- $\rho_c, g, s_1, h_{LS}, \gamma$ = as given in S19.2.3.1 a)
- $d_1, h_{DB}$ = as given in S19.2.3.1

#### S19.2.5 - Resultant pressure

##### S19.2.5.1 - Homogeneous loading conditions

At each point of the bulkhead structures, the resultant pressure $p$, in kN/m², to be considered for the scantlings of the bulkhead is given by:

$$p = p_{c,f} - 0.8 \cdot p_c$$

The resultant force $F$, in kN, acting on a corrugation is given by:

$$F = F_{c,f} - 0.8 \cdot F_c$$

##### S19.2.5.2 - Non homogeneous loading conditions

At each point of the bulkhead structures, the resultant pressure $p$, in kN/m², to be considered for the scantlings of the bulkhead is given by:

$$p = p_{c,f}$$

The resultant force $F$, in kN, acting on a corrugation is given by:

$$F = F_{c,f}$$

In case hold No.1, in non homogeneous loading conditions, is not allowed to be loaded, the resultant pressure $p$, in kN/m², to be considered for the scantlings of the bulkhead is given by:

$$p = p_f$$

and the resultant force $F$, in kN, acting on a corrugation is given by:

$$F = F_f$$

---

### S19.3 - Bending moment and shear force in the bulkhead corrugations

The bending moment $M$ and the shear force $Q$ in the bulkhead corrugations are obtained using the formulae given in S19.3.1 and S19.3.2. The $M$ and $Q$ values are to be used for the checks in S19.4.

#### S19.3.1 - Bending moment

The design bending moment $M$, in kN·m, for the bulkhead corrugations is given by:

$$M = \frac{F \cdot l}{8}$$

where:
- $F$ = resultant force, in kN, as given in S19.2.5
- $l$ = span of the corrugation, in m, to be taken according to Figures 2a and 2b

#### S19.3.2 - Shear force

The shear force $Q$, in kN, at the lower end of the bulkhead corrugations is given by:

$$Q = 0.8 \cdot F$$

where:
- $F$ = as given in S19.2.5

---

### S19.4 - Strength criteria

#### S19.4.1 - General

The following criteria are applicable to transverse bulkheads with vertical corrugations (see Figure 2a).

Requirements for local net plate thickness are given in S19.4.7.

In addition, the criteria given in S19.4.2 and S19.4.5 are to be complied with.

Where the corrugation angle $\phi$ shown in Figure 2a if less than 50°, an horizontal row of staggered shedder plates is to be fitted at approximately mid depth of the corrugations (see Figure 2a) to help preserve dimensional stability of the bulkhead under flooding loads. The shedder plates are to be welded to the corrugations by double continuous welding, but they are not to be welded to the side shell.

The thicknesses of the lower part of corrugations considered in the application of S19.4.2 and S19.4.3 are to be maintained for a distance from the inner bottom (if no lower stool is fitted) or the top of the lower stool not less than $0.15 \cdot l$.

The thicknesses of the middle part of corrugations considered in the application of S19.4.2 and S19.4.4 are to be maintained to a distance from the deck (if no upper stool is fitted) or the bottom of the upper stool not greater than $0.3 \cdot l$.

#### S19.4.2 - Bending capacity and shear stress $\tau$

The bending capacity is to comply with the following relationship:

$$10^3 \cdot \frac{M}{0.5 \cdot Z_{le} \cdot \sigma_{a,le} + Z_m \cdot \sigma_{a,m}} \leq 1.0$$

where:
- $M$ = bending moment, in kN·m, as given in S19.3.1.
- $Z_{le}$ = section modulus of one half pitch corrugation, in cm³, at the lower end of corrugations, to be calculated according to S19.4.3.
- $Z_m$ = section modulus of one half pitch corrugation, in cm³, at the mid-span of corrugations, to be calculated according to S19.4.4.
- $\sigma_{a,le}$ = allowable stress, in N/mm², as given in S19.4.5, for the lower end of corrugations
- $\sigma_{a,m}$ = allowable stress, in N/mm², as given in S19.4.5, for the mid-span of corrugations.

In no case $Z_m$ is to be taken greater than the lesser of $1.15 \cdot Z_{le}$ and $1.15 \cdot Z'_{le}$ for calculation of the bending capacity, $Z'_{le}$ being defined below.

---

In case effective shedders plates are fitted which:
- are not knuckled;
- are welded to the corrugations and the top of the lower stool by one side penetration welds or equivalent;
- are fitted with a minimum slope of 45° and their lower edge is in line with the stool side plating;

or effective gusset plates are fitted which:
- are fitted in line with the stool side plating;
- have material properties at least equal to those provided for the flanges,

the section modulus $Z_{le}$, in cm³, is to be taken not larger than the value $Z'_{le}$, in cm³, given by:

$$Z'_{le} = Z_g + 10^3 \cdot \frac{Q \cdot h_g - 0.5 \cdot h_g^2 \cdot s_1 \cdot p_g}{\sigma_a}$$

where:
- $Z_g$ = section modulus of one half pitch corrugation, in cm³, according to S19.4.4, in way of the upper end of shedder or gusset plates, as applicable
- $Q$ = shear force, in kN, as given in S19.3.2
- $h_g$ = height, in m, of shedders or gusset plates, as applicable (see Figures 3a, 3b, 4a and 4b)
- $s_1$ = as given in S19.2.3.1 a)
- $p_g$ = resultant pressure, in kN/m², as defined in S19.2.5, calculated in way of the middle of the shedders or gusset plates, as applicable
- $\sigma_a$ = allowable stress, in N/mm², as given in S19.4.5.

Stresses $\tau$ are obtained by dividing the shear force $Q$ by the shear area. The shear area is to be reduced in order to account for possible non-perpendicularity between the corrugation webs and flanges. In general, the reduced shear area may be obtained by multiplying the web sectional area by $(\sin \phi)$, $\phi$ being the angle between the web and the flange.

When calculating the section moduli and the shear area, the net plate thicknesses are to be used.

The section moduli of corrugations are to be calculated on the basis of the requirements given in S19.4.3 and S19.4.4.

#### S19.4.3 - Section modulus at the lower end of corrugations

The section modulus is to be calculated with the compression flange having an effective flange width, $b_{ef}$, not larger than as given in S19.4.6.1.

If the corrugation webs are not supported by local brackets below the stool top (or below the inner bottom) in the lower part, the section modulus of the corrugations is to be calculated considering the corrugation webs 30% effective.

a) Provided that effective shedder plates, as defined in S19.4.2, are fitted (see Figures 3a and 3b), when calculating the section modulus of corrugations at the lower end (cross-section ① in Figures 3a and 3b), the area of flange plates, in cm², may be increased by

$$\left( 2.5 \cdot a \cdot \sqrt{t_f \cdot t_{sh}} \cdot \sqrt{\frac{\sigma_{Fsh}}{\sigma_{Ffl}}} \right)$$

(not to be taken greater than $2.5 \cdot a \cdot t_f$) where:
- $a$ = width, in m, of the corrugation flange (see Figure 2a)
- $t_{sh}$ = net shedder plate thickness, in mm
- $t_f$ = net flange thickness, in mm
- $\sigma_{Fsh}$ = minimum upper yield stress, in N/mm², of the material used for the shedder plates
- $\sigma_{Ffl}$ = minimum upper yield stress, in N/mm², of the material used for the corrugation flanges.

---

b) Provided that effective gusset plates, as defined in S19.4.2, are fitted (see Figures 4a and 4b), when calculating the section modulus of corrugations at the lower end (cross-section ① in Figures 4a and 4b), the area of flange plates, in cm², may be increased by $(7 \cdot h_g \cdot t_{gu})$ where:
- $h_g$ = height of gusset plate in m, see Figures 4a and 4b, not to be taken greater than:
$$\frac{10}{7} \cdot s_{gu}$$
- $s_{gu}$ = width of the gusset plates, in m
- $t_{gu}$ = net gusset plate thickness, in mm, not to be taken greater than $t_f$
- $t_f$ = net flange thickness, in mm, based on the as built condition.

c) If the corrugation webs are welded to a sloping stool top plate, which is at an angle not less than 45º with the horizontal plane, the section modulus of the corrugations may be calculated considering the corrugation webs fully effective. In case effective gusset plates are fitted, when calculating the section modulus of corrugations the area of flange plates may be increased as specified in b) above. No credit can be given to shedder plates only.

For angles less than 45º, the effectiveness of the web may be obtained by linear interpolation between 30% for 0º and 100% for 45º.

#### S19.4.4 - Section modulus of corrugations at cross-sections other than the lower end

The section modulus is to be calculated with the corrugation webs considered effective and the compression flange having an effective flange width, $b_{ef}$, not larger than as given in S19.4.6.1.

#### S19.4.5 - Allowable stress check

The normal and shear stresses $\sigma$ and $\tau$ are not to exceed the allowable values $\sigma_a$ and $\tau_a$, in N/mm², given by:

- $\sigma_a = \sigma_F$
- $\tau_a = 0.5 \cdot \sigma_F$

$\sigma_F$ = minimum upper yield stress, in N/mm², of the material.

#### S19.4.6 - Effective compression flange width and shear buckling check

##### S19.4.6.1 - Effective width of the compression flange of corrugations

The effective width $b_{ef}$, in m, of the corrugation flange is given by:

$$b_{ef} = C_e \cdot a$$

where:
- $C_e = \frac{2.25}{\beta} - \frac{1.25}{\beta^2}$ for $\beta > 1.25$
- $C_e = 1.0$ for $\beta \leq 1.25$
- $\beta = 10^3 \cdot \frac{a}{t_f} \cdot \sqrt{\frac{\sigma_F}{E}}$
- $t_f$ = net flange thickness, in mm
- $a$ = width, in m, of the corrugation flange (see Figure 2a)
- $\sigma_F$ = minimum upper yield stress, in N/mm², of the material
- $E$ = modulus of elasticity, in N/mm², to be assumed equal to $2.06 \cdot 10^5$ N/mm² for steel

##### S19.4.6.2 - Shear

The buckling check is to be performed for the web plates at the corrugation ends.

The shear stress $\tau$ is not to exceed the critical value $\tau_C$, in N/mm² obtained by the following:

- $\tau_C = \tau_E$ when $\tau_E \leq \frac{\tau_F}{2}$
- $\tau_C = \tau_F \cdot (1 - \frac{\tau_F}{4 \cdot \tau_E})$ when $\tau_E > \frac{\tau_F}{2}$

---

where:
- $\tau_F = \frac{\sigma_F}{\sqrt{3}}$
- $\sigma_F$ = minimum upper yield stress, in N/mm², of the material
- $\tau_E = 0.9 \cdot k_t \cdot E \cdot \left( \frac{t}{1000 \cdot c} \right)^2$ (N/mm²)

$k_t, E, t$ and $c$ are given by:
- $k_t = 6.34$
- $E$ = modulus of elasticity of material as given in S19.4.6.1
- $t$ = net thickness, in mm, of corrugation web
- $c$ = width, in m, of corrugation web (See Figure 2a)

#### S19.4.7 - Local net plate thickness

The bulkhead local net plate thickness $t$, in mm, is given by:

$$t = 14.9 \cdot s_w \cdot \sqrt{\frac{p}{\sigma_F}}$$

where:
- $s_w$ = plate width, in m, to be taken equal to the width of the corrugation flange or web, whichever is the greater (see Figure 2a)
- $p$ = resultant pressure, in kN/m², as defined in S19.2.5, at the bottom of each strake of plating; in all cases, the net thickness of the lowest strake is to be determined using the resultant pressure at the top of the lower stool, or at the inner bottom, if no lower stool is fitted or at the top of shedders, if shedder or gusset/shedder plates are fitted.
- $\sigma_F$ = minimum upper yield stress, in N/mm², of the material.

For built-up corrugation bulkheads, when the thicknesses of the flange and web are different, the net thickness of the narrower plating is to be not less than $t_n$, in mm, given by:

$$t_n = 14.9 \cdot s_n \cdot \sqrt{\frac{p}{\sigma_F}}$$

$s_n$ being the width, in m, of the narrower plating.

The net thickness of the wider plating, in mm, is not to be taken less than the maximum of the following values:

- $t_w = 14.9 \cdot s_w \cdot \sqrt{\frac{p}{\sigma_F}}$
- $t_w = \sqrt{\frac{440 \cdot s_w^2 \cdot p}{\sigma_F} - t_{np}^2}$

where $t_{np} \leq$ actual net thickness of the narrower plating and not to be greater than:

$$14.9 \cdot s_w \cdot \sqrt{\frac{p}{\sigma_F}}$$

---

### S19.5 - Local details

As applicable, the design of local details is to comply with the Society's requirements for the purpose of transferring the corrugated bulkhead forces and moments to the boundary structures, in particular to the double bottom and cross-deck structures.

In particular, the thickness and stiffening of gusset and shedder plates, installed for strengthening purposes, is to comply with the Society's requirements, on the basis of the load model in S19.2.

Unless otherwise stated, weld connections and materials are to be dimensioned and selected in accordance with the Society's requirements.

### S19.6 - Corrosion addition and steel renewal

Renewal/reinforcement shall be done in accordance with the following requirements and the guidelines contained in the Annex.

a) Steel renewal is required where the gauged thickness is less than $t_{net} + 0.5$ mm, $t_{net}$ being the thickness used for the calculation of bending capacity and shear stresses as given in S19.4.2. or the local net plate thickness as given in S19.4.7. Alternatively, reinforcing doubling strips may be used providing the net thickness is not dictated by shear strength requirements for web plates (see S19.4.5 and S19.4.6.2) or by local pressure requirements for web and flange plates (see S19.4.7).

Where the gauged thickness is within the range $t_{net} + 0.5$ mm and $t_{net} + 1.0$ mm, coating (applied in accordance with the coating manufacturer's requirements) or annual gauging may be adopted as an alternative to steel renewal.

b) Where steel renewal or reinforcement is required, a minimum thickness of $t_{net} + 2.5$ mm is to be replenished for the renewed or reinforced parts.

c) When:
$$0.8 \cdot (\sigma_{Ffl} \cdot t_{fl}) \geq \sigma_{Fs} \cdot t_{st}$$

where:
- $\sigma_{Ffl}$ = minimum upper yield stress, in N/mm², of the material used for the corrugation flanges
- $\sigma_{Fs}$ = minimum upper yield stress, in N/mm², of the material used for the lower stool side plating or floors (if no stool is fitted)
- $t_{fl}$ = flange thickness, in mm, which is found to be acceptable on the basis of the criteria specified in a) above or, when steel renewal is required, the replenished thickness according to the criteria specified in b) above. The above flange thickness dictated by local pressure requirements (see S19.4.7) need not be considered for this purpose
- $t_{st}$ = as built thickness, in mm, of the lower stool side plating or floors (if no stool is fitted)

gussets with shedder plates, extending from the lower end of corrugations up to $0.1 \cdot l$, or reinforcing doubling strips (on bulkhead corrugations and stool side plating) are to be fitted.

If gusset plates are fitted, the material of such gusset plates is to be the same as that of the corrugation flanges. The gusset plates are to be connected to the lower stool shelf plate or inner bottom (if no lower stool is fitted) by deep penetration welds (see Figure 5).

d) Where steel renewal is required, the bulkhead connections to the lower stool shelf plate or inner bottom (if no stool is fitted) are to be at least made by deep penetration welds (see Figure 5).

e) Where gusset plates are to be fitted or renewed, their connections with the corrugations and the lower stool shelf plate or inner bottom (if no stool is fitted) are to be at least made by deep penetration welds (see Figure 5).

---

![Figure 1: Load model parameters showing cargo volume V, calculation point P, and distances d_f, d_1, D, and h_f](Diagram of a ship cargo hold section showing liquid and cargo levels for flooding head calculations)

![Figure 2a: Corrugation geometry and parameters showing span l, neutral axis n, spacing s_1, width a, and angle phi](Detailed views of corrugated bulkhead scantlings and shedder plates)

![Figure 2b: Transverse section showing corrugation span l and upper stool constraints](Bulkhead section showing various span measurements l across the width)

![Figure 3a: Symmetric shedder plates showing height h_g and connection at the lower stool](Side view of symmetric shedder plate arrangement)

![Figure 3b: Asymmetric shedder plates showing height h_g and connection at the lower stool](Side view of asymmetric shedder plate arrangement)

![Figure 4a: Symmetric gusset / shedder plates showing height h_g and width s_gu](Side view of symmetric gusset and shedder plate combination)

![Figure 4b: Asymmetric gusset / shedder plates showing height h_g](Side view of asymmetric gusset and shedder plate combination)

![Figure 5: Weld details for connections showing root face f and groove angle alpha](Technical illustration of deep penetration weld geometries for bulkhead connections)

---

### ANNEX 1 - Guidance on renewal/reinforcement of vertically corrugated transverse watertight bulkhead between cargo holds Nos. 1 and 2

1. The need for renewal or reinforcement of the vertically corrugated transverse watertight bulkhead between cargo holds Nos. 1 and 2 will be determined by the classification society on a case by case basis using the criteria given in S19 in association with the most recent gaugings and findings from survey.

2. In addition to class requirements, the S19 assessment of the transverse corrugated bulkhead will take into account the following:-
   (a) Scantlings of individual vertical corrugations will be assessed for reinforcement/renewal based on thickness measurements obtained in accordance with Annex III to UR Z10.2 at their lower end, at mid-depth and in way of plate thickness changes in the lower 70%. These considerations will take into account the provision of gussets and shedder plates and the benefits they offer, provided that they comply with S19.4.2 and S19.6.
   (b) Taking into account the scantlings and arrangements for each case, permissible levels of diminution will be determined and appropriate measures taken in accordance with S19.6.

3. Where renewal is required, the extent of renewal is to be shown clearly in plans. The vertical distance of each renewal zone is to be determined by considering S19 and in general is to be not less than 15% of the vertical distance between the upper and lower end of the corrugation - measured at the ship's centreline.

4. Where the reinforcement is accepted by adding strips, the length of the reinforcing strips is to be sufficient to allow it to extend over the whole depth of the diminished plating. In general, the width and thickness of strips should be sufficient to comply with the S19 requirements. The material of the strips is to be the same as that of the corrugation plating. The strips are to be attached to the existing bulkhead plating by continuous fillet welds. The strips are to be suitably tapered or connected at ends in accordance with Class Society practice.

5. Where reinforcing strips are connected to the inner bottom or lower stool shelf plates, one side full penetration welding is to be used. When reinforcing strips are fitted to the corrugation flange and are connected to the lower stool shelf plate, they are normally to be aligned with strips of the same scantlings welded to the stool side plating and having a minimum length equal to the breadth of the corrugation flange.

6. Figure 1 gives a general arrangement of structural reinforcement.

---

![Figure 1 (Annex 1): Structural reinforcement details showing reinforcement strips, shedder plates, and gusset plates at the stool connection](Detailed diagrams of reinforcement strip applications on corrugation flanges with shedder and gusset plates)

**Notes to Figure 1 on reinforcement:-**
1. Square or trapezoidal corrugations are to be reinforced with plate strips fitted to each corrugation flange sufficient to meet the requirements of S19.
2. The number of strips fitted to each corrugation flange is to be sufficient to meet the requirements of S19.
3. The shedder plate may be fitted in one piece or prefabricated with a welded knuckle (gusset plate).
4. Gusset plates, where fitted, are to be welded to the shelf plate in line with the flange of the corrugation, to reduce the stress concentrations at the corrugation corners. Ensure good alignment between gusset plate, corrugation flange and lower stool sloping plate. Use deep penetration welding at all connections. Ensure start and stop of welding is as far away as practically possible from corners of corrugation.
5. Shedder plates are to be attached by one side full penetration welds onto backing bars.
6. Shedder and gusset plates are to have a thickness equal to or greater than the original bulkhead thickness. Gusset plate is to have a minimum height (on the vertical part) equal to half of the width of the corrugation flange. Shedders and gussets are to be same material as flange material.

---

### ANNEX 2 - Guidance to Assess Capability of Carriage of High Density Cargoes on Existing Bulk Carriers according to the Strength of Transverse Bulkhead between Cargo Holds Nos. 1 and 2

![Annex 2 Figure: Flow chart for assessment of cargo carriage capability](Flow chart starting with 'Carriage of cargoes having rho_c >= 1.78 t/m3' and leading through checks for rho_c = 1.78, reinforcements, and calculations of allowable density)


================================================================================
# FILE: UR_S/ur-s1arev6.md
================================================================================

# S1A Additional Requirements for Loading Conditions, Loading Manuals and Loading Instruments for Bulk Carriers, Ore Carriers and Combination Carriers

**S1A**
(1997)
(Rev.1 April 1998)
(Rev.2 May 1998)
(Rev.3 Sept 2000)
(Rev.4 Nov 2001)
(Rev.5 July 2004)
(Rev.6 May 2010)

## S1A.1 Application

Bulk Carriers, Ore Carriers and Combination Carriers (see UR Z11) of 150 m length and above, which are contracted for construction before 1st July 1998 are to be provided with an approved loading instrument of a type to the satisfaction of the Society not later than their entry into service or 1st January 1999, whichever occurs later.

In addition, Bulk Carriers of 150 m length and above where one or more cargo holds are bounded by the side shell only, which were contracted for construction before 1st July 1998, are to be provided, with an approved loading manual with typical loading sequences where the vessel is loaded from commencement of cargo loading to reaching full deadweight capacity for homogeneous conditions, relevant part load conditions and alternate conditions where applicable. Typical unloading sequences for these conditions shall also be included. Annex 1 contains, as guidance only, an example of a Loading Sequence Summary Form. Annex 2 contains guidance for loading and unloading sequences for existing bulk carriers.

Bulk Carriers, Ore Carriers and Combination Carriers of 150 m length and above, which are contracted for construction on or after 1st July 1998, are to be provided with an approved Loading Manual and approved computer-based Loading Instrument, in accordance with S1A.2, S1A.3 and S1A.4. Annex 3 contains guidance for loading and unloading sequences for new bulk carriers.

This UR does not apply to CSR Bulk Carriers.

---

**Notes:**

1. The latest date for implementation for requirements in S1A.2.1(f) is 1st July 1999.
2. The latest date for implementation for requirements in S1A.2.2(b) is 1st July 1999.
3. The latest date for implementation for requirements in S1A.4(d) is 1st July 1999.
4. Changes introduced in Rev.3 are to be uniformly implemented by IACS Members and Associates from 1 July 2001.
5. The "contracted for construction" date means the date on which the contract to build the vessel is signed between the prospective owner and the shipbuilder. For further details regarding the date of "contract for construction", refer to IACS Procedural Requirement (PR) No. 29.

***

## S1A.2 Definitions

### S1A.2.1 Loading Manual

Loading Manual is a document which describes:

a) the loading conditions on which the design of the ship has been based, including permissible limits of still water bending moments and shear forces;

b) the results of the calculations of still water bending moments, shear forces and where applicable, limitations due to torsional loads;

c) for bulk carriers, envelope results and permissible limits of still water bending moments and shear forces in the hold flooded condition according to S17 as applicable;

d) the cargo hold(s) or combination of cargo holds that might be empty at full draught. If no cargo hold is allowed to be empty at full draught, this is to be clearly stated in the loading manual;

e) maximum allowable and minimum required mass of cargo and double bottom contents of each hold as a function of the draught at mid-hold position;

f) maximum allowable and minimum required mass of cargo and double bottom contents of any two adjacent holds as a function of the mean draught in way of these holds. This mean draught may be calculated by averaging the draught of the two mid-hold positions;

g) maximum allowable tank top loading together with specification of the nature of the cargo for cargoes other than bulk cargoes;

h) maximum allowable load on deck and hatch covers. If the vessel is not approved to carry load on deck or hatch covers, this is to be clearly stated in the loading manual;

i) the maximum rate of ballast change together with the advice that a load plan is to be agreed with the terminal on the basis of the achievable rates of change of ballast.

### S1A.2.2 Loading Instrument

A loading instrument is an approved digital system as defined in S1. In addition to the requirements in S1, it shall ascertain as applicable that:

a) the mass of cargo and double bottom contents in way of each hold as a function of the draught at mid-hold position;

b) the mass of cargo and double bottom contents of any two adjacent holds as a function of the mean draught in way of these holds;

c) the still water bending moment and shear forces in the hold flooded conditions according to S17;

are within permissible values.

***

## S1A.3 Conditions of Approval of Loading Manuals

In addition to the requirements given in S1.2.2, the following conditions, subdivided into departure and arrival conditions as appropriate, are to be included in the Loading Manual:

a) alternate light and heavy cargo loading conditions at maximum draught, where applicable;

b) homogeneous light and heavy cargo loading conditions at maximum draught;

c) ballast conditions. For vessels having ballast holds adjacent to topside wing, hopper and double bottom tanks, it shall be strengthwise acceptable that the ballast holds are filled when the topside wing, hopper and double bottom tanks are empty;

d) short voyage conditions where the vessel is to be loaded to maximum draught but with limited amount of bunkers;

e) multiple port loading / unloading conditions;

f) deck cargo conditions, where applicable;

g) typical loading sequences where the vessel is loaded from commencement of cargo loading to reaching full deadweight capacity, for homogeneous conditions, relevant part load conditions and alternate conditions where applicable. Typical unloading sequences for these conditions shall also be included. The typical loading / unloading sequences shall also be developed to not exceed applicable strength limitations. The typical loading sequences shall also be developed paying due attention to loading rate and the deballasting capability. Annex 1 contains, as guidance only, an example of a Loading Sequence Summary Form;

h) typical sequences for change of ballast at sea, where applicable.

## S1A.4 Condition of Approval of Loading Instruments

The loading instrument is subject to approval. In addition to the requirements given in S1.2.3, the approval is to include as applicable:

a) acceptance of hull girder bending moment limits for all read-out points;

b) acceptance of hull girder shear force limits for all read-out points;

c) acceptance of limits for mass of cargo and double bottom contents of each hold as a function of draught;

d) acceptance of limits for mass of cargo and double bottom contents in any two adjacent holds as a function of draught.

***

## ANNEX 1
### GUIDANCE ON TYPICAL LOADING SEQUENCE SUMMARY FORM

![Figure 1: Guidance on Typical Loading Sequence Summary Form](A complex technical form titled 'Loading Sequence Summary Form' used for planning ship loading and deballasting operations. The form includes:
- A longitudinal profile diagram of a bulk carrier with numbered cargo holds (1-5) and ballast tanks (APT, FPT).
- Sections for vessel details (name, yard, id. number).
- Tables for 'Hold content at commencement of loading/deballasting' including cargo mass, density, and height.
- A central 'CARGO OPERATIONS' and 'BALLAST OPERATIONS' matrix to track step-by-step changes for each hold and tank (APT, Ballast tanks 1-5, FPT).
- Data columns for recording time, draught, trim, shear force (S.F.), and bending moment (B.M.) at the end of each pour.
- Calculation sections for 'Hold content at end of loading/deballasting' and 'Ballast content at end of loading/deballasting'.
- Formulas for structural checks, such as 'Net load on double bottom = (Mh / Vh) * h - (T - db) * 1.025'.
- Space for approval signatures and dates.)

***

## ANNEX 2
### EXISTING BULK CARRIERS
### GUIDANCE FOR LOADING / UNLOADING SEQUENCES

1. UR S1A.1 requires that bulk carriers of 150 m length and above, where one or more cargo holds are bounded by the side shell only, which were contracted for construction before 1st July 1998, are to be provided, with an approved loading manual with typical loading sequences where the ship is loaded from commencement of cargo loading to reaching full deadweight capacity, for homogeneous conditions, relevant part load conditions and alternate conditions where applicable. Typical unloading sequences shall be included.

2. This requirement will necessitate shipowners and operators to prepare and submit for approval typical loading and unloading sequences.

3. The minimum acceptable number of typical sequences is:
   - one homogeneous full load condition,
   - one part load condition where relevant, such as block loading or two port unloading,
   - one full load alternate hold condition, if the ship is approved for alternate hold loading.

4. The shipowner / operator should select actual loading / unloading sequences, where possible, which may be port specific or typical.

5. The sequence may be prepared using the onboard loading instrument. The selected loading conditions should be built up step by step from commencement of cargo loading to reaching full deadweight capacity. Each time the loading equipment changes position to a new hold defines a step. Each step is to be documented and submitted to the class society. The printout from the loading instrument is generally acceptable. This allows the actual bending moments and shear forces to be verified and prevent the permissible values being exceeded. In addition, the local strength of each hold may need to be considered during the loading.

6. For each loading condition a summary of all steps is to be included. This summary is to highlight the essential information for each step such as:
   - How much cargo is filled in each hold during the different steps,
   - How much ballast is discharged from each ballast tank during the different steps,
   - The maximum still water bending moment and shear at the end of each step,
   - The ship's trim and draught at the end of each step.

   Blank summary sheets are attached for reference for typical 5, 7 and 9 hold bulk carriers.

7. The approved typical loading / unloading sequences, may be included in the approved loading manual or take the form of an addendum prepared for purposes of complying with class society requirements. A copy of the approved typical loading / unloading sequences is to be placed onboard the ship.

***

## ANNEX 3
### NEW BULK CARRIERS
### GUIDANCE FOR LOADING / UNLOADING SEQUENCES

1. UR S1A.1 requires that Bulk Carriers, Ore Carriers and Combination Carriers of 150 m length and above, which are contracted for construction on or after 1st July 1998, are to be provided with an approved loading manual with typical loading sequences where the ship is loaded from commencement of cargo loading to reaching full deadweight capacity, for homogeneous conditions, relevant part load conditions and alternate conditions where applicable. The typical unloading sequences shall be developed paying due attention to the loading rate, the deballasting capacity and the applicable strength limitations.

2. The shipbuilder will be required to prepare and submit for approval typical loading and unloading sequences.

3. The typical loading sequences as relevant should include:
   - alternate light and heavy cargo load condition,
   - homogeneous light and heavy cargo load condition,
   - short voyage condition where the ship is loaded to maximum draught but with limited bunkers,
   - multiple port loading / unloading condition,
   - deck cargo condition,
   - block loading.

4. The loading / unloading sequences may be port specific or typical.

5. The sequence is to be built up step by step from commencement of cargo loading to reaching full deadweight capacity. Each time the loading equipment changes position to a new hold defines a step. Each step is to be documented and submitted to the class society. In addition to longitudinal strength, the local strength of each hold is to be considered.

6. For each loading condition a summary of all steps is to be included. This summary is to highlight the essential information for each step such as:
   - How much cargo is filled in each hold during the different steps,
   - How much ballast is discharged from each ballast tank during the different steps,
   - The maximum still water bending moment and shear at the end of each step,
   - The ship's trim and draught at the end of each step.

**End of Document**

================================================================================
# FILE: UR_S/ur-s1rev7.md
================================================================================

# S1 Requirements for Loading Conditions, Loading Manuals and Loading Instruments

**S1**
(1971)
(Rev.1 1981)
(Rev.2 1983)
(Rev.3 1995)
(Rev.4 1997)
(Rev.5 June 2001)
(Rev.6 July 2004)
(Rev.7 May 2010)

IACS considers that this Requirement satisfies Regulation 10(1) of the International Convention on Load Lines, 1966.

## S1.1 General

### S1.1.1 Application

These requirements* apply to all classed sea-going ships of 65m in length and above which are contracted for construction on or after 1st July 1998, and contain minimum requirements for loading guidance information.

For CSR Bulk Carriers and Oil Tankers, these requirements apply in addition to those of the Common Structural Rules.

### S1.1.2 Definitions

**Loading Manual:**

A Loading Manual is a document which describes:

- the loading conditions on which the design of the ship has been based, including permissible limits of still water bending moment and shear force
- the results of the calculations of still water bending moments, shear forces and where applicable, limitations due to torsional and lateral loads
- the allowable local loading for the structure (hatch covers, decks, double bottom, etc.)

**Notes**

\* For ships which were contracted for construction before 1st July 1998, the relevant prior revisions of this Unified Requirement as well as Members' reservations to those revisions of this Unified Requirement apply. Certain additional requirements of Unified Requirement S1A also apply to bulk carriers, ore carriers and combination carriers (see UR Z11), of 150m length and above.

\* The "contracted for construction" date means the date on which the contract to build the vessel is signed between the prospective owner and the shipbuilder. For further details regarding the date of "contract for construction", refer to IACS Procedural Requirement (PR) No. 29.

---

**Loading Instrument**

A loading instrument is an instrument, which is either analogue or digital, by means of which it can be easily and quickly ascertained that, at specified read-out points, the still water bending moments, shear forces, and the still water torsional moments and lateral loads, where applicable, in any load or ballast condition will not exceed the specified permissible values.

An operational manual is always to be provided for the loading instrument.

Single point loading instruments are not acceptable.

**Category I Ships**

• Ships with large deck openings where combined stresses due to vertical and horizontal hull girder bending and torsional and lateral loads have to be considered;

• Ships liable to carry non-homogeneous loadings, where the cargo and/or ballast may be unevenly distributed. Ships less than 120 metres in length, when their design takes into account uneven distribution of cargo or ballast, belong to Category II;

• Chemical tankers and gas carriers.

**Category II Ships**

• Ships with arrangement giving small possibilities for variation in the distribution of cargo and ballast, and ships on regular and fixed trading pattern where the Loading Manual gives sufficient guidance, and in addition the exception given under Category I.

### S1.1.3 Annual and Special Survey

At each Annual and Special Survey, it is to be checked that the approved loading guidance information is available on board.

The loading instrument is to be checked for accuracy at regular intervals by the ship's Master by applying test loading conditions.

At each Special Survey this checking is to be done in the presence of the Surveyor.

## S1.2 Loading Conditions, Loading Manuals and Loading Instruments

### S1.2.1 General

An approved loading manual is to be supplied for all ships except those of Category II with length less than 90m in which the deadweight does not exceed 30% of the displacement at the summer loadline draft.

In addition, an approved loading instrument is to be supplied for all ships of Category I of 100m in length and above.

### S1.2.2 Conditions of Approval of Loading Manuals

The approved Loading Manual is to be based on the final data of the ship. The Manual is to include the design loading and ballast conditions upon which the approval of the hull scantlings is based.

Annex 1 contains, as guidance only, a list of the loading conditions which normally should be included in the Loading Manual.

In case of modifications resulting in changes to the main data of the ship, a new approved Loading Manual is to be issued.

The Loading Manual must be prepared in a language understood by the users. If this language is not English, a translation into English is to be included.

### S1.2.3 Condition of Approval of Loading Instruments

The loading instrument is subject to approval, which is to include:

- verification of type approval, if any
- verification that the final data of the ship has been used
- acceptance of number and position of read-out points
- acceptance of relevant limits for all read-out points
- checking of proper installation and operation of the instrument on board, in accordance with agreed test conditions, and that a copy of the operation manual is available.

Recommendations on the approval of Loading instruments are given in the IACS document "Recommendations on loading instruments".

In case of modifications implying changes in the main data of the ship, the loading instrument is to be modified accordingly and approved.

The operation manual and the instrument output must be prepared in a language understood by the users. If this language is not English, a translation into English is to be included.

The operation of the loading instrument is to be verified upon installation. It is to be checked that the agreed test conditions and the operation manual for the instrument is available on board.

---

## ANNEX 1 TO REQUIREMENT S1
## GUIDANCE ON CONDITIONS

1. The Loading Manual should contain the design loading and ballast conditions, subdivided into departure and arrival conditions, and ballast exchange at sea conditions, where applicable, upon which the approval of the hull scantlings is based.

2. In particular the following loading conditions should be included:

### 2.1 Cargo Ships, Container Ships, Roll-on/Roll-off and Refrigerated Carriers, Ore Carriers and Bulk Carriers:

- Homogeneous loading conditions at maximum draught
- Ballast conditions
- Special loading conditions, e.g. container or light load conditions at less than the maximum draught, heavy cargo, empty holds or non-homogeneous cargo conditions deck cargo conditions, etc., where applicable
- Short voyage or harbour conditions, where applicable
- Docking condition afloat
- Loading and unloading transitory conditions, where applicable

### 2.2 Oil Tankers:

- Homogeneous loading conditions (excluding dry and clean ballast tanks) and ballast or part-loaded conditions for both departure and arrival
- Any specified non-uniform distribution of loading
- Mid-voyage conditions relating to tank cleaning or other operations where these differ significantly from the ballast conditions
- Docking condition afloat
- Loading and unloading transitory conditions

### 2.3 Chemical Tankers:

- Conditions as specified for oil tankers
- Conditions for high density or heated cargo and segregated cargo where these are included in the approved cargo list

### 2.4 Liquefied Gas Carriers:

- Homogeneous loading conditions for all approved cargoes for both arrival and departure
- Ballast conditions for both arrival and departure
- Cargo condition where one or more tanks are empty or partially filled or where more than one type of cargo having significantly different densities is carried, for both arrival and departure
- Harbour condition for which an increased vapour pressure has been approved
- Docking condition afloat

### 2.5 Combination Carriers:

- Conditions as specified in 2.1 and 2.2, above.

**End of Document**

================================================================================
# FILE: UR_S/ur-s20-rev6.md
================================================================================

# S20 Evaluation of Allowable Hold Loading for Non-CSR Bulk Carriers Considering Hold Flooding

(1997)
(Rev.1 1997)
(Rev.2 Sept 2000)
(Rev.3 July 2004)
(Rev.4 Feb 2006)
(Corr.1 Oct 2009)
(Rev.5 May 2010)
(Rev.6 Apr 2014)

### S20.1 - Application and definitions

Revision 4 or subsequent revisions or corrigenda as applicable of this UR is to be applied to non-CSR bulk carriers of 150 m in length and upwards, intending to carry solid bulk cargoes having a density of 1.0 t/m³ or above, and with,

a) Single side skin construction, or
b) Double side skin construction in which any part of longitudinal bulkhead is located within B/5 or 11.5 m, whichever is less, inboard from the ship's side at right angle to the centreline at the assigned summer load line

in accordance with Note 2.

The loading in each hold is not to exceed the allowable hold loading in flooded condition, calculated as per S20.4, using the loads given in S20.2 and the shear capacity of the double bottom given in S20.3.
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
