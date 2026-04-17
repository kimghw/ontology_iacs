# Marine gears – load capacity of involute parallel axis spur and helical gears

M56
(1990)
(Rev.1 1994/Corr. 1996)
(Rev.2 Oct 2013)
(Rev.3 Oct 2015)
(Rev.4 Feb 2021)
(Corr.1 Oct 2021)
(Corr. 2 Mar 2023)
(Corr. 3 Sep 2025)

## M56.1 Basic principles - introduction and general influence factors

### M56.1.1 Introduction

The following definitions are mainly based on the ISO 6336 series standard (hereinafter called "reference standard") for the calculation of load capacity of spur and helical gears.

### M56.1.2 Scope and field of application

These requirements apply to enclosed gears, both intended for main propulsion and for essential auxiliary services, which accumulate a large number of load cycles (several millions), whose gear set is intended to transmit a maximum continuous power equal to, or greater than:

- 220 kW for gears intended for main propulsion
- 110 kW for gears intended for essential auxiliary services

These requirements, however, may be applied to the enclosed gears, whose gear set is intended to transmit a maximum continuous power less than those specified above at the request of the individual society.

**Notes:**

1. The requirements of UR M56 Rev.2 are to be uniformly implemented from 1 January 2015 by all IACS Societies to any marine gear subject to approval and to any Type Approved marine gear from the date of the first renewal after 1 January 2015. For a marine gear approved prior to 1 January 2015 where no failure has occurred, and no changes in design / scantlings of the gear meshes or materials or declared load capacity data has taken place the requirements by UR M56 Rev.2 may be waived.

2. The requirements of UR M56 Rev.3 are to be uniformly implemented from 1 January 2017 by all IACS Societies to any marine gear subject to approval and to any Type Approved marine gear from the date of the first renewal after 1 January 2017. For a marine gear approved prior to 1 January 2017 where no failure has occurred, and no changes in design / scantlings of the gear meshes or materials or declared load capacity data has taken place the requirements by UR M56 Rev.3 may be waived.

3. Rev.4 of this UR is to be uniformly implemented by IACS Societies from 1 July 2022 to any marine gear subject to approval and to any Type Approved marine gear from the date of the first renewal after 1 July 2022. For a marine gear approved prior to 1 July 2022 where no failure has occurred, and no changes in design / scantlings of the gear meshes or materials or declared load capacity data has taken place the requirements of UR M56 Rev.4 may be waived.

The following definitions deal with the determination of load capacity of external and internal involute spur and helical gears, having parallel axis, with regard to surface durability (pitting) and tooth root bending strength and to this purpose the relevant basic equations are provided in Parts 2 and 3.

The influence factors common to said equations are described in the present Part 1.

The others, introduced in connection with each basic equation, are described in the following Parts 2 and 3.

All influence factors are defined regarding their physical interpretation. Some of the influence factors are determined by the gear geometry or have been established by conventions. These factors are to be calculated in accordance with the equations provided. Other factors, which are approximations, can be calculated according to methods acceptable to the Society.

### M56.1.3 Symbols and units

The main symbols used are listed below.

Other symbols introduced in connection with the definition of influence factors are described in the appropriate sections.

SI units have been adopted.

| Symbol | Description | Unit |
|---|---|---|
| *a* | centre distance | mm |
| *b* | common face width | mm |
| *b*<sub>1,2</sub> | face width of pinion, wheel | mm |
| *d* | reference diameter | mm |
| *d*<sub>1,2</sub> | reference diameter of pinion, wheel | mm |
| *d*<sub>a1,2</sub> | tip diameter of pinion, wheel | mm |
| *d*<sub>b1,2</sub> | base diameter of pinion, wheel | mm |
| *d*<sub>f1,2</sub> | root diameter of pinion, wheel | mm |
| *d*<sub>w1,2</sub> | working diameter of pinion, wheel | mm |
| *F*<sub>t</sub> | nominal tangential load | N |
| *F*<sub>bt</sub> | nominal tangential load on base cylinder in the transverse section | N |
| *h* | tooth depth | mm |
| *m*<sub>n</sub> | normal module | mm |
| *m*<sub>t</sub> | transverse module | mm |
| *n*<sub>1,2</sub> | rotational speed of pinion, wheel | revs/min (rpm) |
| *P* | maximum continuous power transmitted by the gear set | kW |
| *T*<sub>1,2</sub> | torque in way of pinion, wheel | Nm |
| *u* | gear ratio |  |
| *v* | linear velocity at pitch diameter | m/s |
| *x*<sub>1,2</sub> | addendum modification coefficient of pinion, wheel |  |
| *z* | number of teeth |  |
| *z*<sub>1,2</sub> | number of teeth of pinion, wheel |  |
| *z*<sub>n</sub> | virtual number of teeth |  |
| *α*<sub>n</sub> | normal pressure angle at reference cylinder | ° |
| *α*<sub>t</sub> | transverse pressure angle at ref. cylinder | ° |
| *α*<sub>tw</sub> | transverse pressure angle at working pitch cylinder | ° |
| *β* | helix angle at reference cylinder | ° |
| *β*<sub>b</sub> | helix angle at base cylinder | ° |
| *ε*<sub>α</sub> | transverse contact ratio |  |
| *ε*<sub>β</sub> | overlap ratio |  |
| *ε*<sub>γ</sub> | total contact ratio |  |

### M56.1.4 Geometrical definitions

For internal gearing *z*<sub>2</sub>, *a*, *d*<sub>2</sub>, *d*<sub>a2</sub>, *d*<sub>b2</sub> and *d*<sub>w2</sub> are negative. The pinion is defined as the gear with the smaller number of teeth, therefore the absolute value of the gear ratio, defined as follows, is always greater or equal to the unity:

$$u = z_2/z_1 \quad = d_{w2}/d_{w1} \quad = d_2/d_1$$

For external gears *u* is positive, for internal gears *u* is negative.

In the equation of surface durability *b* is the common face width on the pitch diameter.

In the equation of tooth root bending stress *b*<sub>1</sub> or *b*<sub>2</sub> are the face widths at the respective tooth roots. In any case, *b*<sub>1</sub> and *b*<sub>2</sub> are not to be taken as greater than *b* by more than one module (*m*<sub>n</sub>) on either side.

The common face width *b* may be used also in the equation of teeth root bending stress if significant crowning or end relief have been adopted.

$$\tan \alpha_t = \frac{\tan \alpha_n}{\cos \beta}$$

$$\tan \beta_b = \tan \beta \cdot \cos \alpha_t$$

$$d_{1,2} = \frac{z_{1,2} m_n}{\cos \beta}$$

$$d_{b1,2} = d_{1,2} \cos \alpha_t$$

$$\left. \begin{array}{l} d_{w1} = \dfrac{2a}{u+1} \\ d_{w2} = \dfrac{2au}{u+1} \end{array} \right\} \quad \text{where} \quad a = 0.5 \left( d_{w1} + d_{w2} \right)$$

$$z_{n1,2} = \frac{z_{1,2}}{\cos^2 \beta_b \cdot \cos \beta}$$

$$m_t = \frac{m_n}{\cos \beta}$$

$$\operatorname{inv} \alpha = \tan \alpha - \frac{\pi \alpha}{180}; \quad \alpha \, [°]$$

$$\operatorname{inv} \alpha_{tw} = \operatorname{inv} \alpha_t + 2 \tan \alpha_n \frac{x_1 + x_2}{z_1 + z_2} \quad \text{or} \quad \cos \alpha_{tw} = \frac{m_t (z_1 + z_2)}{2a} \cos \alpha_t$$

$$\varepsilon_\alpha = \frac{0{,}5 \sqrt{d_{a1}^2 - d_{b1}^2} \pm 0{,}5 \sqrt{d_{a2}^2 - d_{b2}^2} - a \cdot \sin \alpha_{tw}}{\pi \cdot m_t \cdot \cos \alpha_t}$$

the positive sign is used for external gears, the negative sign for internal gears

$$\varepsilon_\beta = \frac{b \cdot \sin \beta}{\pi \cdot m_n}$$

for double helix, *b* is to be taken as the width of one helix

$$\varepsilon_\gamma = \varepsilon_\alpha + \varepsilon_\beta$$

$$v = \pi \cdot d_{1,2} n_{1,2} / 60 \cdot 10^3$$

### M56.1.5 Nominal tangential load, *F*<sub>t</sub>

The nominal tangential load, *F*<sub>t</sub>, tangential to the reference cylinder and perpendicular to the relevant axial plane, is calculated directly from the maximum continuous power transmitted by the gear set by means of the following equations:

$$T_{1,2} = \frac{30 \cdot 10^3 P}{\pi \cdot n_{1,2}}$$

$$F_t = 2000 \cdot T_{1,2} / d_{1,2}$$

### M56.1.6 General influence factors

#### M56.1.6.1 Application factor, K<sub>A</sub> <sup>1)</sup>

The application factor, *K*<sub>A</sub>, accounts for dynamic overloads from sources external to the gearing.

*K*<sub>A</sub>, for gears designed for infinite life is defined as the ratio between the maximum repetitive cyclic torque applied to the gear set and the nominal rated torque.

The nominal rated torque is defined by the rated power and speed and is the torque used in the rating calculations.

The factor mainly depends on:

- characteristics of driving and driven machines;
- ratio of masses;
- type of couplings;
- operating conditions (overspeeds, changes in propeller load conditions, ...).

When operating near a critical speed of the drive system, a careful analysis of conditions must be made.

The application factor, *K*<sub>A</sub>, should be determined by measurements or by system analysis acceptable to the Society. Where a value determined in such a way cannot be supplied, the following values can be considered.

a) Main propulsion

- diesel engine with hydraulic or electromagnetic slip coupling : 1.00
- diesel engine with high elasticity coupling : 1.30
- diesel engine with other couplings : 1.50

<sup>1)</sup> Where the vessel, on which the reduction gear is being used, is receiving an Ice Class notation, the Application Factor or the Nominal Tangential Force should be adjusted to reflect the ice load associated with the requested Ice Class, i.e. applying the design approach in UR I3 when applicable.

b) Auxiliary gears

- electric motor, diesel engine with hydraulic or electromagnetic slip coupling : 1.00
- diesel engine with high elasticity coupling : 1.20
- diesel engine with other couplings : 1.40

#### M56.1.6.2 Load sharing factor, K<sub>γ</sub>

The load sharing factor, *K*<sub>γ</sub> accounts for the maldistribution of load in multiple path transmissions (dual tandem, epicyclic, double helix, etc.).

*K*<sub>γ</sub> is defined as the ratio between the maximum load through an actual path and the evenly shared load. The factor mainly depends on accuracy and flexibility of the branches.

The load sharing factor, *K*<sub>γ</sub>, should be determined by measurements or by system analysis. Where a value determined in such a way cannot be supplied, the following values can be considered for epicyclic gears:

- up to 3 planetary gears : 1.00
- 4 planetary gears : 1.20
- 5 planetary gears : 1.30
- 6 planetary gears and over : 1.40

#### M56.1.6.3 Internal dynamic factor, K<sub>v</sub>

The internal dynamic factor, *K*<sub>v</sub>, accounts for internally generated dynamic loads due to vibrations of pinion and wheel against each other.

*K*<sub>v</sub> is defined as the ratio between the maximum load which dynamically acts on the tooth flanks and the maximum externally applied load (*F*<sub>t</sub>*K*<sub>A</sub>*K*<sub>γ</sub>).

The factor mainly depends on:

- transmission errors (depending on pitch and profile errors);
- masses of pinion and wheel;
- gear mesh stiffness variation as the gear teeth pass through the meshing cycle;
- transmitted load including application factor;
- pitch line velocity;
- dynamic unbalance of gears and shaft;
- shaft and bearing stiffnesses;
- damping characteristics of the gear system.

The dynamic factor, *K*<sub>v</sub>, is to be calculated as follows:

This method may be applied only to cases where all the following conditions are satisfied:

- running velocity in the subcritical range, i.e.:

$$\frac{v z_1}{100} \sqrt{\frac{u^2}{1+u^2}} < 10 \text{ m/s}$$

- spur gears (*β* = 0°) and helical gears with *β* ≤ 30°
- pinion with relatively low number of teeth, *z*<sub>1</sub> < 50
- solid disc wheels or heavy steel gear rim

This method may be applied to all types of gears if $\frac{v z_1}{100} \sqrt{\frac{u^2}{1+u^2}} < 3 \text{ m/s}$, as well as to helical gears where *β* > 30°.

For gears other than the above, reference is to be made to Method B outlined in the reference standard ISO 6336-1:2019.

a) For spur gears and for helical gears with overlap ratio *ε*<sub>β</sub> ≥ 1

$$K_v = 1 + \left( \frac{K_1}{K_A \frac{F_t}{b}} + K_2 \right) \cdot \frac{v z_1}{100} K_3 \sqrt{\frac{u^2}{1+u^2}}$$

If *K*<sub>A</sub>*F*<sub>t</sub>/*b* is less than 100 N/mm, this value is assumed to be equal to 100 N/mm.

Numerical values for the factor *K*<sub>1</sub> are to be as specified in the Table 1.1

|  | *K*<sub>1</sub> ISO accuracy grades <sup>2)</sup> |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  | 3 | 4 | 5 | 6 | 7 | 8 |
| spur gears | 2.1 | 3.9 | 7.5 | 14.9 | 26.8 | 39.1 |
| helical gears | 1.9 | 3.5 | 6.7 | 13.3 | 23.9 | 34.8 |

**Table 1.1 Values of the factor *K*<sub>1</sub> for the calculation of *K*<sub>v</sub>**

For all accuracy grades the factor *K*<sub>2</sub> is to be in accordance with the following:

- for spur gears, *K*<sub>2</sub>=0.0193
- for helical gears, *K*<sub>2</sub>=0.0087

Factor *K*<sub>3</sub> is to be in accordance with the following:

If $\frac{v z_1}{100} \sqrt{\frac{u^2}{1+u^2}} \leq 0.2$ then $K_3 = 2.0$

If $\frac{v z_1}{100} \sqrt{\frac{u^2}{1+u^2}} > 0.2$ then $K_3 = 2.071 - 0.357 \cdot \frac{v z_1}{100} \sqrt{\frac{u^2}{1+u^2}}$

b) For helical gears with overlap ratio *ε*<sub>β</sub><1 the value *K*<sub>v</sub> is determined by linear interpolation between values determined for spur gears (*K*<sub>vα</sub>) and helical gears (*K*<sub>vβ</sub>) in accordance with:

$$K_v = K_{v\alpha} - \varepsilon_\beta \left( K_{v\alpha} - K_{v\beta} \right)$$

Where:

*K*<sub>vα</sub> is the *K*<sub>v</sub> value for spur gears, in accordance with a);
*K*<sub>vβ</sub> is the *K*<sub>v</sub> value for helical gears, in accordance with a).

<sup>2)</sup> ISO accuracy grades according to ISO 1328-1:2013. In case of mating gears with different accuracy grades, the grade corresponding to the lower accuracy should be used.

#### M56.1.6.4 Face load distribution factors, K<sub>Hβ</sub> and K<sub>Fβ</sub>

The face load distribution factors, *K*<sub>Hβ</sub> for contact stress, *K*<sub>Fβ</sub> for tooth root bending stress, account for the effects of non-uniform distribution of load across the face width.

*K*<sub>Hβ</sub> is defined as follows:

$$K_{H\beta} = \frac{\text{maximum load per unit face width}}{\text{mean load per unit face width}}$$

*K*<sub>Fβ</sub> is defined as follows:

$$K_{F\beta} = \frac{\text{maximum bending stress at tooth root per unit face width}}{\text{mean bending stress at tooth roo per unit face width}}$$

The mean bending stress at tooth root relates to the considered face width *b*<sub>1</sub> resp. *b*<sub>2</sub>.

*K*<sub>Fβ</sub> can be expressed as a function of the factor *K*<sub>Hβ</sub>.

The factors *K*<sub>Hβ</sub> *and K*<sub>Fβ</sub> mainly depend on:

- gear tooth manufacturing accuracy;
- errors in mounting due to bore errors;
- bearing clearances;
- wheel and pinion shaft alignment errors;
- elastic deflections of gear elements, shafts, bearings, housing and foundations which support the gear elements;
- thermal expansion and distortion due to operating temperature;
- compensating design elements (tooth crowning, end relief, etc.).

The face load distribution factors, *K*<sub>Hβ</sub> for contact stress, and *K*<sub>Fβ</sub> for tooth root bending stress, are to be determined according to the Method C outlined in the reference standard ISO 6336-1:2019.

Alternative methods acceptable to the Society may be applied.

a) In case the hardest contact is at the end of the face width *K*<sub>Fβ</sub> is given by the following equations:

$$K_{F\beta} = K_{H\beta}^N$$

$$N = \frac{(b/h)^2}{1 + (b/h) + (b/h)^2}$$

(*b/h*) = face width/tooth height ratio, the minimum of *b*<sub>1</sub>/*h*<sub>1</sub> or *b*<sub>2</sub>/*h*<sub>2</sub>.
For double helical gears, the face width of only one helix is to be used.
When *b/h*<3 the value *b/h*=3 is to be used.

b) In case of gears where the ends of the face width are lightly loaded or unloaded (end relief or crowning):

$$K_{F\beta} = K_{H\beta}$$

#### M56.1.6.5 Transverse load distribution factors, K<sub>Hα</sub> and K<sub>Fα</sub>

The transverse load distribution factors, *K*<sub>Hα</sub> for contact stress and *K*<sub>Fα</sub> for tooth root bending stress, account for the effects of pitch and profile errors on the transversal load distribution between two or more pairs of teeth in mesh.

The factors *K*<sub>Hα</sub> *and K*<sub>Fα</sub> mainly depend on:

- total mesh stiffness;
- total tangential load *F*<sub>t</sub>, *K*<sub>A</sub>, *K*<sub>γ</sub>, *K*<sub>v</sub>, *K*<sub>Hβ</sub>;
- base pitch error;
- tip relief;
- running-in allowances.

The transverse load distribution factors, *K*<sub>Hα</sub> for contact stress and *K*<sub>Fα</sub> for tooth root bending stress, are to be determined according to Method B outlined in the reference standard ISO 6336-1:2019.

## M56.2 Surface durability (pitting)

### M56.2.1 Scope and general remarks

The criterion for surface durability is based on the Hertz pressure on the operating pitch point or at the inner point of single pair contact. The contact stress *σ*<sub>H</sub> must be equal to or less than the permissible contact stress *σ*<sub>HP</sub>.

### M56.2.2 Basic equations

#### M56.2.2.1 Contact stress

$$\sigma_H = \sigma_{H0} \sqrt{K_A \cdot K_\gamma \cdot K_v \cdot K_{H\alpha} \cdot K_{H\beta}} \leq \sigma_{HP}$$

where:

*σ*<sub>H0</sub> = basic value of contact stress for pinion and wheel

$$\sigma_{H0} = Z_B \cdot Z_H \cdot Z_E \cdot Z_\varepsilon \cdot Z_\beta \sqrt{\frac{F_t}{d_1 \cdot b} \frac{(u+1)}{u}} \quad \text{for pinion}$$

$$\sigma_{H0} = Z_D \cdot Z_H \cdot Z_E \cdot Z_\varepsilon \cdot Z_\beta \sqrt{\frac{F_t}{d_1 \cdot b} \frac{(u+1)}{u}} \quad \text{for wheel}$$

where:

| Symbol | Description | Reference |
|---|---|---|
| *Z*<sub>B</sub> | single pair tooth contact factor for pinion | (see clause 2.3) |
| *Z*<sub>D</sub> | single pair tooth contact factor for wheel | (see clause 2.3) |
| *Z*<sub>H</sub> | zone factor | (see clause 2.4) |
| *Z*<sub>E</sub> | elasticity factor | (see clause 2.5) |
| *Z*<sub>ε</sub> | contact ratio factor | (see clause 2.6) |
| *Z*<sub>β</sub> | helix angle factor | (see clause 2.7) |
| *F*<sub>t</sub> | nominal tangential load at reference cylinder in the transverse section | (see Part 1) |
| *b* | common face width |  |
| *d*<sub>1</sub> | reference diameter of pinion |  |
| *u* | gear ratio (for external gears *u* is positive, for internal gears *u* is negative) |  |

Regarding factors *K*<sub>A</sub>, *K*<sub>γ</sub>, *K*<sub>v</sub>, *K*<sub>Hα</sub> and *K*<sub>Hβ</sub>, see Part 1.

#### M56.2.2.2 Permissible contact stress

The permissible contact stress *σ*<sub>HP</sub> is to be evaluated separately for pinion and wheel:

$$\sigma_{HP} = \frac{\sigma_{H\lim} \cdot Z_N}{S_H} \cdot Z_L \cdot Z_v \cdot Z_R \cdot Z_W \cdot Z_X$$

where:

| Symbol | Description | Reference |
|---|---|---|
| *σ*<sub>Hlim</sub> | endurance limit for contact stress | (see clause 2.8) |
| *Z*<sub>N</sub> | life factor for contact stress | (see clause 2.9) |
| *Z*<sub>L</sub> | lubrication factor | (see clause 2.10) |
| *Z*<sub>v</sub> | velocity factor | (see clause 2.10) |
| *Z*<sub>R</sub> | roughness factor | (see clause 2.10) |
| *Z*<sub>W</sub> | hardness ratio factor | (see clause 2.11) |
| *Z*<sub>X</sub> | size factor for contact stress | (see clause 2.12) |
| *S*<sub>H</sub> | safety factor for contact stress | (see clause 2.13) |

### M56.2.3 Single pair tooth contact factors, *Z*<sub>B</sub> and *Z*<sub>D</sub>

The single pair tooth contact factors, *Z*<sub>B</sub> for pinion and *Z*<sub>D</sub> for wheel, account for the influence of the tooth flank curvature on contact stresses at the inner point of single pair contact in relation to *Z*<sub>H</sub>.

The factors transform the contact stresses determined at the pitch point to contact stresses considering the flank curvature at the inner point of single pair contact.

The single pair tooth contact factors, *Z*<sub>B</sub> for pinions and *Z*<sub>D</sub> for wheels, are to be determined as follows:

For spur gears, *ε*<sub>β</sub>=0

*Z*<sub>B</sub> = *M*<sub>1</sub> or 1 whichever is the larger value

*Z*<sub>D</sub> = *M*<sub>2</sub> or 1 whichever is the larger value

$$M_1 = \frac{\tan \alpha_{tw}}{\sqrt{\left( \sqrt{\frac{d_{a1}^2}{d_{b1}^2} - 1} - \frac{2\pi}{z_1} \right) \left( \sqrt{\frac{d_{a2}^2}{d_{b2}^2} - 1} - (\varepsilon_\alpha - 1) \frac{2\pi}{z_2} \right)}}$$

$$M_2 = \frac{\tan \alpha_{tw}}{\sqrt{\left( \sqrt{\frac{d_{a2}^2}{d_{b2}^2} - 1} - \frac{2\pi}{z_2} \right) \left( \sqrt{\frac{d_{a1}^2}{d_{b1}^2} - 1} - (\varepsilon_\alpha - 1) \frac{2\pi}{z_1} \right)}}$$

For helical gears when *ε*<sub>β</sub> ≥1

*Z*<sub>B</sub> = 1
*Z*<sub>D</sub> = 1

For helical gears when *ε*<sub>β</sub> <1 the values of *Z*<sub>B</sub> and *Z*<sub>D</sub> are determined by linear interpolation between *Z*<sub>B</sub> and *Z*<sub>D</sub> for spur gears and *Z*<sub>B</sub> and *Z*<sub>D</sub> for helical gears having *ε*<sub>β</sub> ≥1.

Thus:

$$Z_B = M_1 - \varepsilon_\beta (M_1 - 1) \text{ and } Z_B \geq 1$$

$$Z_D = M_2 - \varepsilon_\beta (M_2 - 1) \text{ and } Z_D \geq 1$$

For internal gears, *Z*<sub>D</sub> shall be taken as equal to 1.

### M56.2.4 Zone factor, *Z*<sub>H</sub>

The zone factor, *Z*<sub>H</sub>, accounts for the influence on the Hertzian pressure of tooth flank curvature at pitch point and transforms the tangential load at the reference cylinder to the normal load at the pitch cylinder.

The zone factor, *Z*<sub>H</sub>, is to be calculated as follows:

$$Z_H = \sqrt{\frac{2 \cos \beta_b}{\cos^2 \alpha_t \tan \alpha_{tw}}}$$

### M56.2.5 Elasticity factor, *Z*<sub>E</sub>

The elasticity factor, *Z*<sub>E</sub>, accounts for the influence of the material properties *E* (modulus of elasticity) and *v* (Poisson's ratio) on the contact stress.

The elasticity factor, *Z*<sub>E</sub>, for steel gears (*E*= 206 000 N/mm<sup>2</sup>, *v*= 0.3) is equal to:

*Z*<sub>E</sub> = 189.8 $\sqrt{\text{N/mm}^2}$

In other cases, reference is to be made to the reference standard ISO 6336-2:2019.

### M56.2.6 Contact ratio factor, *Z*<sub>ε</sub>

The contact ratio factor, *Z*<sub>ε</sub>, accounts for the influence of the transverse contact ratio and the overlap ratio on the specific surface load of gears.

The contact ratio factor, *Z*<sub>ε</sub>, is to be calculated as follows:

Spur gears:

$$Z_\varepsilon = \sqrt{\frac{4 - \varepsilon_\alpha}{3}}$$

Helical gears:

- for *ε*<sub>β</sub> <1

$$Z_\varepsilon = \sqrt{\frac{4 - \varepsilon_\alpha}{3} (1 - \varepsilon_\beta) + \frac{\varepsilon_\beta}{\varepsilon_\alpha}}$$

- for *ε*<sub>β</sub> ≥1

$$Z_\varepsilon = \sqrt{\frac{1}{\varepsilon_\alpha}}$$

### M56.2.7 Helix angle factor, *Z*<sub>β</sub>

The helix angle factor, *Z*<sub>β</sub>, accounts for the influence of helix angle on surface durability, allowing for such variables as the distribution of load along the lines of contact. *Z*<sub>β</sub> is dependent only on the helix angle.

The helix angle factor, *Z*<sub>β</sub>, is to be calculated as follows:

$$Z_\beta = \sqrt{\frac{1}{\cos \beta}}$$

Where *β* is the reference helix angle.

### M56.2.8 Endurance limit for contact stress, *σ*<sub>Hlim</sub>

For a given material, *σ*<sub>Hlim</sub> is the limit of repeated contact stress which can be permanently endured. The value of *σ*<sub>Hlim</sub> can be regarded as the level of contact stress which the material will endure without pitting for at least 5x10<sup>7</sup> load cycles.

For this purpose, pitting is defined by:

- for not surface hardened gears:
    pitted area > 2% of total active flank area
- for surface hardened gears:
    pitted area > 0,5% of total active flank area, or
    > 4% of one particular tooth flank area.

The *σ*<sub>Hlim</sub> values are to correspond to a failure probability of 1% or less.

The endurance limit mainly depends on:

- material composition, cleanliness and defects;
- mechanical properties;
- residual stresses;
- hardening process, depth of hardened zone, hardness gradient;
- material structure (forged, rolled bar, cast).

The endurance limit for contact stress *σ*<sub>Hlim</sub>, is to be determined, in general, making reference to values indicated in the standard ISO 6336-5:2016, for material quality MQ.

### M56.2.9 Life factor, *Z*<sub>N</sub>

The life factor *Z*<sub>N</sub>, accounts for the higher permissible contact stress in case a limited life (number of cycles) is required.

The factor mainly depends on:

- material and heat treatment;
- number of cycles;
- influence factors (*Z*<sub>R</sub>, *Z*<sub>v</sub>, *Z*<sub>L</sub>, *Z*<sub>W</sub>, *Z*<sub>X</sub>).

The life factor, *Z*<sub>N</sub> , is to be determined according to Method B outlined in the reference standard ISO 6336-2:2019.

### M56.2.10 Influence factors of lubrication film on contact stress, *Z*<sub>L</sub>, *Z*<sub>v</sub> and *Z*<sub>R</sub>

The lubricant factor, *Z*<sub>L</sub>, accounts for the influence of the type of lubricant and its viscosity. The velocity factor, *Z*<sub>v</sub>, accounts for the influence of the pitch line velocity. The roughness factor, *Z*<sub>R</sub>, accounts for the influence of the surface roughness on the surface endurance capacity.

The factors may be determined for the softer material where gear pairs are of different hardness.

The factors mainly depend on:

- viscosity of lubricant in the contact zone;
- the sum of the instantaneous velocities of the tooth surfaces;
- load;
- relative radius of curvature at the pitch point;
- surface roughness of teeth flanks;
- hardness of pinion and gear.

The lubricant factor, *Z*<sub>L</sub>, the velocity factor, *Z*<sub>v</sub>, and the roughness factor *Z*<sub>R</sub> are to be calculated as follows:

a) Lubricant factor, *Z*<sub>L</sub>

The factor, *Z*<sub>L</sub>, is to be calculated from the following equation:

$$Z_L = C_{ZL} + \frac{4 (1 - C_{ZL})}{\left( 1.2 + \dfrac{134}{v_{40}} \right)^2}$$

In the range 850 N/mm<sup>2</sup> ≤ *σ*<sub>Hlim</sub> ≤ 1200 N/mm<sup>2</sup>, *C*<sub>ZL</sub> is to be calculated as follows:

$$C_{ZL} = \left( 0.08 \frac{\sigma_{H\lim} - 850}{350} \right) + 0.83$$

If *σ*<sub>Hlim</sub> < 850 N/mm<sup>2</sup>, take *C*<sub>ZL</sub> = 0.83

If *σ*<sub>Hlim</sub> > 1200 N/mm<sup>2</sup>, take *C*<sub>ZL</sub> = 0.91

Where:

*v*<sub>40</sub> = nominal kinematic viscosity of the oil at 40°C, mm<sup>2</sup>/s

b) Velocity factor, *Z*<sub>v</sub>

The velocity factor, *Z*<sub>v</sub>, is to be calculated from the following equations:

$$Z_v = C_{ZV} + \frac{2 (1 - C_{ZV})}{\sqrt{0.8 + \dfrac{32}{v}}}$$

In the range 850 N/mm<sup>2</sup> ≤ *σ*<sub>Hlim</sub> ≤ 1200 N/mm<sup>2</sup>, *C*<sub>ZV</sub> is to be calculated as follows:

$$C_{ZV} = C_{ZL} + 0.02$$

c) Roughness factor, *Z*<sub>R</sub>

The roughness factor, *Z*<sub>R</sub>, is to be calculated from the following equations:

$$Z_R = \left( \frac{3}{R_{z10}} \right)^{C_{ZR}}$$

Where:

$$R_z = \frac{R_{z1} + R_{z2}}{2}$$

The peak-to-valley roughness determined for the pinion *R*<sub>z1</sub> and for the wheel *R*<sub>z2</sub> are mean values for the peak-to-valley roughness *R*<sub>z</sub> measured on several tooth flanks (*R*<sub>z</sub> as defined in the reference standard ISO 6336-2:2019).

$$R_{z10} = R_z \sqrt[3]{\frac{10}{\rho_{red}}}$$

relative radius of curvature:

$$\rho_{red} = \frac{\rho_1 \cdot \rho_2}{\rho_1 + \rho_2}$$

Wherein:

$$\rho_{1,2} = 0.5 \cdot d_{b1,2} \cdot \tan \alpha_{tw}$$

(also for internal gears, *d*<sub>b</sub> negative sign)

If the roughness stated is an arithmetic mean roughness, i.e. *R*<sub>a</sub> value (=*CLA* value) (=*AA* value) the following approximate relationship can be applied:

*R*<sub>a</sub>= *CLA* = *AA* = *R*<sub>z</sub> /6

In the range 850 N/mm<sup>2</sup> ≤ *σ*<sub>Hlim</sub> ≤ 1200 N/mm<sup>2</sup>, *C*<sub>ZR</sub> is to be calculated as follows:

$$C_{ZR} = 0.32 - 0.0002 \cdot \sigma_{H\lim}$$

If *σ*<sub>Hlim</sub> < 850 N/mm<sup>2</sup>, take *C*<sub>ZR</sub> = 0.150

If *σ*<sub>Hlim</sub> > 1200 N/mm<sup>2</sup>, take *C*<sub>ZR</sub> = 0.080

### M56.2.11 Hardness ratio factor, *Z*<sub>W</sub>

The hardness ratio factor, *Z*<sub>W</sub>, accounts for the increase of surface durability of a soft steel gear meshing with a significantly harder gear with a smooth surface in the following cases:

a) Surface-hardened pinion with through-hardened wheel

If *HB*< 130

$$Z_W = 1.2 \cdot \left( \frac{3}{R_{zH}} \right)^{0.15}$$

If 130 ≤ *HB* ≤ 470

$$Z_W = \left( 1.2 - \frac{HB - 130}{1700} \right) \cdot \left( \frac{3}{R_{zH}} \right)^{0.15}$$

If *HB* >470

$$Z_W = \left( \frac{3}{R_{zH}} \right)^{0.15}$$

Where:

*HB* = Brinell hardness of the tooth flanks of the softer gear of the pair

*R*<sub>zH</sub> = equivalent roughness, μm

$$R_{zH} = \frac{R_{z1} \cdot (10 / \rho_{red})^{0.33} \cdot (R_{z1} / R_{z2})^{0.66}}{(v \cdot v_{40} / 1500)^{0.33}}$$

If *R*<sub>zH</sub> > 16 then *R*<sub>zH</sub> = 16 μm
If *R*<sub>zH</sub> < 3 then *R*<sub>zH</sub> = 3 μm

*ρ*<sub>red</sub> = relative radius of curvature (see clause 2.10 c)

b) Through-hardened pinion and wheel

When the pinion is substantially harder than the wheel, the work hardening effect increases the load capacity of the wheel flanks. *Z*<sub>W</sub> applies to the wheel only, not to the pinion.

If *HB*<sub>1</sub>/*HB*<sub>2</sub> < 1.2 $\quad Z_W = 1$

If 1.2≤ *HB*<sub>1</sub>/*HB*<sub>2</sub>≤1.7 $\quad Z_W = 1 + \left( 0.00898 \dfrac{HB_1}{HB_2} - 0.00829 \right) \cdot (u - 1)$

If *HB*<sub>1</sub>/*HB*<sub>2</sub>>1.7 $\quad Z_W = 1 + 0.00698 \cdot (u - 1)$

If gear ratio *u*>20 then the value *u*=20 is to be used.

In any case, if calculated *Z*<sub>W</sub> <1 then the value *Z*<sub>W</sub> = 1.0 is to be used.

### M56.2.12 Size factor, *Z*<sub>X</sub>

The size factor, *Z*<sub>X</sub>, accounts for the influence of tooth dimensions on permissible contact stress and reflects the non-uniformity of material properties.

The factor mainly depends on:

- material and heat treatment;
- tooth and gear dimensions;
- ratio of case depth to tooth size;
- ratio of case depth to equivalent radius of curvature.

For through-hardened gears and for surface-hardened gears with adequate casedepth relative to tooth size and radius of relative curvature *Z*<sub>X</sub> = 1. When the casedepth is relatively shallow then a smaller value of *Z*<sub>X</sub> should be chosen.

### M56.2.13 Safety factor for contact stress, *S*<sub>H</sub>

The safety factor for contact stress, *S*<sub>H</sub>, can be assumed by the Society taking into account the type of application.

The following guidance values can be adopted:

- Main propulsion gears:    1.20 to 1.40
- Auxiliary gears:            1.15 to 1.20

For gearing of duplicated independent propulsion or auxiliary machinery, duplicated beyond that required for class, a reduced value can be assumed at the discretion of the Society.

## M56.3 Tooth root bending strength

### M56.3.1 Scope and general remarks

The criterion for tooth root bending strength is the permissible limit of local tensile strength in the root fillet. The root stress *σ*<sub>F</sub> and the permissible root stress *σ*<sub>FP</sub> shall be calculated separately for the pinion and the wheel.

*σ*<sub>F</sub> must not exceed *σ*<sub>FP</sub>.

The following formulae and definitions apply to gears having rim thickness greater than 3.5*m*<sub>n</sub>.

The result of rating calculations made by following this method are acceptable for normal pressure angles up to 25° and reference helix angles up to 30°.

For larger pressure angles and large helix angles, the calculated results should be confirmed by experience as by Method A of the reference standard ISO 6336-3:2019.

### M56.3.2 Basic equations

#### M56.3.2.1 Tooth root bending stress for pinion and wheel

$$\sigma_F = \frac{F_t}{bm_n} Y_F Y_S Y_\beta Y_B Y_{DT} K_A K_\gamma K_v K_{F\alpha} K_{F\beta} \leq \sigma_{FP}$$

where:

| Symbol | Description | Reference |
|---|---|---|
| *Y*<sub>F</sub> | tooth form factor | (see clause 3.3) |
| *Y*<sub>S</sub> | stress correction factor | (see clause 3.4) |
| *Y*<sub>β</sub> | helix angle factor | (see clause 3.5) |
| *Y*<sub>B</sub> | rim thickness factor | (see clause 3.6) |
| *Y*<sub>DT</sub> | deep tooth factor | (see clause 3.7) |
| *F*<sub>t</sub>, *K*<sub>A</sub>, *K*<sub>γ</sub>, *K*<sub>v</sub>, *K*<sub>Fα</sub>, *K*<sub>Fβ</sub> |  | (see Part 1) |
| *b* |  | (see Part 1, clause 1.4) |
| *m*<sub>n</sub> |  | (see Part 1, clause 1.3) |

#### M56.3.2.2 Permissible tooth root bending stress for pinion and wheel

$$\sigma_{FP} = \frac{\sigma_{FE} Y_d Y_N}{S_F} Y_{\delta relT} Y_{RrelT} Y_X$$

where:

*σ*<sub>FE</sub> = bending endurance limit
*Y*<sub>d</sub> = design factor
*Y*<sub>N</sub> = life factor
*Y*<sub>δrelT</sub> = relative notch sensitivity factor
*Y*<sub>RrelT</sub> = relative surface factor
*Y*<sub>X</sub> = size factor
*S*<sub>F</sub> = safety factor for tooth root bending stress

### M56.3.3 Tooth form factor, *Y*<sub>F</sub>

The tooth form factor, *Y*<sub>F</sub>, represents the influence on nominal bending stress of the tooth form with load applied at the outer point of single pair tooth contact. *Y*<sub>F</sub> shall be determined separately for the pinion and the wheel. In the case of helical gears, the form factors for gearing shall be determined in the normal section, i.e. for the virtual spur gear with virtual number of teeth *Z*<sub>n</sub>.

The tooth form factor, *Y*<sub>F</sub>, is to be calculated as follows:

$$Y_F = \frac{6 \dfrac{h_F}{m_n} \cos \alpha_{Fen}}{\left( \dfrac{s_{Fn}}{m_n} \right)^2 \cos \alpha_n}$$

Where:

*h*<sub>F</sub> = bending moment arm for tooth root bending stress
       for application of load at the outer point of single tooth
       pair contact                                                       mm

*s*<sub>Fn</sub> = tooth root normal chord in the critical section           mm

*α*<sub>Fen</sub> = pressure angle at the outer point of single tooth pair
           contact in the normal section                                  °

![Fig. 3.1 Dimensions of h_F, s_Fn and α_Fen for external gear](assets/UR-M56-Rev.4-Corr.3-Sep-2025-CLN/part01-fig-000.png)

**Fig. 3.1 Dimensions of *h*<sub>F</sub>, *s*<sub>Fn</sub> and *α*<sub>Fen</sub> for external gear**

For the calculation of *h*<sub>F</sub>, *s*<sub>Fn</sub> and *α*<sub>Fen</sub>, the procedure outlined in the reference standard ISO 6336-3:2019 (Method B) is to be used.

### M56.3.4 Stress correction factor, *Y*<sub>S</sub>

The stress correction factor *Y*<sub>S</sub>, is used to convert the nominal bending stress to the local tooth root stress, taking into account that not only bending stresses arise at the root.

*Y*<sub>S</sub> applies to the load application at the outer point of single tooth pair contact.

*Y*<sub>S</sub> shall be determined separately for the pinion and for the wheel.
The stress correction factor, *Y*<sub>S</sub>, is to be determined with the following equation (having range of validity: 1≤ *q*<sub>s</sub> ≤ 8 ):

$$Y_S = (1.2 + 0.13 L) q_s^{\left( \dfrac{1}{1.21 + 2.3/L} \right)}$$

Where:

$$q_s = \frac{s_{Fn}}{2 \rho_F}$$

*q*<sub>s</sub>     = notch parameter,

*ρ*<sub>F</sub>    = root fillet radius in the critical section, mm

L = *s*<sub>Fn</sub> /*h*<sub>F</sub>

For *h*<sub>F</sub> and *s*<sub>Fn</sub> see clause 3.1

For the calculation of *ρ*<sub>F</sub> the procedure outlined in the reference standard ISO 6336-3:2019 is to be used.

### M56.3.5 Helix angle factor, *Y*<sub>β</sub>

The helix angle factor, *Y*<sub>β</sub>, converts the stress calculated for a point loaded cantilever beam representing the substitute gear tooth to the stress induced by a load along an oblique load line into a cantilever plate which represents a helical gear tooth.

The helix angle factor, *Y*<sub>β</sub> is to be calculated as follows:

$$Y_\beta = 1 - \varepsilon_\beta \frac{\beta}{120}$$

where:

*β*    =  reference helix angle in degrees.

The value 1.0 is substituted for *ε*<sub>β</sub> when *ε*<sub>β</sub> > 1.0, and 30° is substituted for *β* > 30°.

### M56.3.6 Rim thickness factor, *Y*<sub>B</sub>

The rim thickness factor, *Y*<sub>B</sub>, is a simplified factor used to de-rate thin rimmed gears. For critically loaded applications, this method should be replaced by a more comprehensive analysis. Factor *Y*<sub>B</sub> is to be determined as follows:

a) for external gears:
   if *s*<sub>R</sub> / *h* ≥ 1.2 $\quad Y_B = 1$
   if 0.5 < *s*<sub>R</sub> / *h* < 1.2 $\quad Y_B = 1.6 \cdot \ln \left( 2.242 \dfrac{h}{s_R} \right)$

where:

*s*<sub>R</sub> = rim thickness of external gears, mm
*h* = tooth height, mm

The case *s*<sub>R</sub> / *h* ≤ 0.5 is to be avoided.

b) for internal gears:
   if *s*<sub>R</sub> / *m*<sub>n</sub> ≥ 3.5 $\quad Y_B = 1$
   if 1.75 < *s*<sub>R</sub> / *m*<sub>n</sub> < 3.5 $\quad Y_B = 1.15 \cdot \ln \left( 8.324 \dfrac{m_n}{s_R} \right)$

where:

*s*<sub>R</sub> = rim thickness of internal gears, mm

The case *s*<sub>R</sub> / *m*<sub>n</sub> ≤ 1.75 is to be avoided.

### M56.3.7 Deep tooth factor, *Y*<sub>DT</sub>

The deep tooth factor, *Y*<sub>DT</sub>, adjusts the tooth root stress to take into account high precision gears and contact ratios within the range of virtual contact ratio 2.05 ≤ *ε*<sub>αn</sub> ≤ 2.5 , where:

$$\varepsilon_{\alpha n} = \frac{\varepsilon_\alpha}{\cos^2 \beta_b}$$

Factor *Y*<sub>DT</sub> is to be determined as follows:

if ISO accuracy grade ≤ 4 and *ε*<sub>αn</sub> > 2.5 $\quad Y_{DT} = 0.7$
if ISO accuracy grade ≤4 and 2.05 < *ε*<sub>αn</sub> ≤ 2.5 $\quad Y_{DT} = 2.366 - 0.666 \cdot \varepsilon_{\alpha n}$
in all other cases $\quad Y_{DT} = 1.0$

### M56.3.8 Bending endurance limit, *σ*<sub>FE</sub>

For a given material, *σ*<sub>FE</sub> is the local tooth root stress which can be permanently endured.

According to the reference standard ISO 6336-5:2016 the number of 3x10<sup>6</sup> cycles is regarded as the beginning of the endurance limit.

*σ*<sub>FE</sub> is defined as the unidirectional pulsating stress with a minimum stress of zero (disregarding residual stresses due to heat treatment). Other conditions such as alternating stress or prestressing etc. are covered by the design factor *Y*<sub>d</sub>.

The *σ*<sub>FE</sub> values are to correspond to a failure probability 1% or less.

The endurance limit mainly depends on:

- material composition, cleanliness and defects;
- mechanical properties;
- residual stresses;
- hardening process, depth of hardened zone, hardness gradient;
- material structure (forged, rolled bar, cast).

The bending endurance limit, *σ*<sub>FE</sub> is to be determined, in general, making reference to values indicated in the reference standard ISO 6336-5:2016, for material quality *MQ*.

### M56.3.9 Design factor, *Y*<sub>d</sub>

The design factor, *Y*<sub>d</sub>, takes into account the influence of load reversing and shrinkfit prestressing on the tooth root strength, relative to the tooth root strength with unidirectional load as defined for *σ*<sub>FE</sub>.

The design factor, *Y*<sub>d</sub>, for load reversing, is to be determined as follows:
*Y*<sub>d</sub> = 1.0    in general;
*Y*<sub>d</sub> = 0.9    for gears with occasional part load in reversed direction, such as main wheel in reversing gearboxes;
*Y*<sub>d</sub> = 0.7    for idler gears

### M56.3.10 Life factor, *Y*<sub>N</sub>

The life factor, *Y*<sub>N</sub>, accounts for the higher tooth root bending stress permissible in case a limited life (number of load cycles) is required.

The factor mainly depends on:

- material and heat treatment;
- number of load cycles (service life);
- influence factors (*Y*<sub>δrelT</sub>, *Y*<sub>RrelT</sub>, *Y*<sub>X</sub>).

The life factor, *Y*<sub>N</sub>, is to be determined according to Method B outlined in the reference standard ISO 6336-3:2019.

### M56.3.11 Relative notch sensitivity factor, *Y*<sub>δrelT</sub>

The relative notch sensitivity factor, *Y*<sub>δrelT</sub>, indicates the extent to which the theoretically concentrated stress lies above the fatigue endurance limit. The factor mainly depends on material and relative stress gradient.

The relative notch sensitivity factor, *Y*<sub>δrelT</sub>, is to be determined as follows:

$$Y_{\delta relT} = \frac{1 + \sqrt{0.2 \rho' (1 + 2 q_s)}}{1 + \sqrt{1.2 \rho'}}$$

where:

*q*<sub>s</sub> = notch parameter (see clause 3.4)

*ρ'* = slip-layer thickness, mm, from the following table

| Material |  | *ρ'*, mm |
|---|---|---|
| case hardened steels, flame or induction hardened steels |  | 0.0030 |
| through-hardened steels<sup>1)</sup>, yield point *R*<sub>e</sub>= | 500 N/mm² | 0.0281 |
|  | 600 N/mm² | 0.0194 |
|  | 800 N/mm² | 0.0064 |
|  | 1000 N/mm² | 0.0014 |
| nitrided steels |  | 0.1005 |

<sup>1)</sup>The given values of *ρ'* can be interpolated for values of *R*<sub>e</sub> not stated above

### M56.3.12 Relative surface factor, *Y*<sub>RrelT</sub>

The relative surface factor, *Y*<sub>RrelT</sub>, takes into account the dependence of the root strength on the surface condition in the tooth root fillet, mainly the dependence on the peak to valley surface roughness.

The relative surface factor, *Y*<sub>RrelT</sub> is to be determined as follows:

| *R*<sub>z</sub> < 1 | 1≤ *R*<sub>z</sub> ≤ 40 | Material |
|---|---|---|
| 1.120 | $1.674 - 0.529 (R_z + 1)^{0.1}$ | case hardened steels, through - hardened steels (*σ*<sub>B</sub> ≥ 800 N/mm<sup>2</sup>) |
| 1.070 | $5.306 - 4.203 (R_z + 1)^{0.01}$ | normalised steels (*σ*<sub>B</sub> < 800 N/mm<sup>2</sup>) |
| 1.025 | $4.299 - 3.259 (R_z + 1)^{0.0058}$ | nitrided steels |

Where:

*R*<sub>z</sub>    = mean peak-to-valley roughness of tooth root fillets, μm

*σ*<sub>B</sub>   = tensile strength, N/mm<sup>2</sup>

The method applied here is only valid when scratches or similar defects deeper than 2*R*<sub>z</sub> are not present.

If the roughness stated is an arithmetic mean roughness, i.e. *R*<sub>a</sub> value (=*CLA* value) (=*AA* value) the following approximate relationship can be applied:

*R*<sub>a</sub>= *CLA* = *AA* = *R*<sub>Z</sub> /6

### M56.3.13 Size factor, *Y*<sub>X</sub>

The size factor, *Y*<sub>X</sub>, takes into account the decrease of the strength with increasing size.

The factor mainly depends on:

- material and heat treatment;
- tooth and gear dimensions;
- ratio of case depth to tooth size.

The size factor, *Y*<sub>X</sub>, is to be determined as follows:

| Formula | Range | Material |
|---|---|---|
| *Y*<sub>X</sub> = 1.00 | for *m*<sub>n</sub> ≤ 5 | generally |
| *Y*<sub>X</sub> = 1.03 - 0.06 *m*<sub>n</sub> | for 5 < *m*<sub>n</sub> < 30 | normalised and through-hardened steels |
| *Y*<sub>X</sub> = 0.85 | for *m*<sub>n</sub> ≥ 30 | normalised and through-hardened steels |
| *Y*<sub>X</sub> = 1.05 - 0.010 *m*<sub>n</sub> | for 5 < *m*<sub>n</sub> < 25 | surface hardened steels |
| *Y*<sub>X</sub> = 0.80 | for *m*<sub>n</sub> ≥ 25 | surface hardened steels |

### M56.3.14 Safety factor for tooth root bending stress, *S*<sub>F</sub>

The safety factor for tooth root bending stress, *S*<sub>F</sub>, can be assumed by the Society taking into account the type of application.
The following guidance values can be adopted:

- Main propulsion gears:    1.55 to 2.00
- Auxiliary gears:            1.40 to 1.45

For gearing of duplicated independent propulsion or auxiliary machinery, duplicated beyond that required for class, a reduced value can be assumed at the discretion of the Society.

End of Document

# M57 Use of ammonia as a refrigerant

M57
(1993)

1. Ammonia refrigerating machinery shall be installed in dedicated gastight compartments. Except for small compartments, at least two access doors are to be provided.

2. Compartments containing ammonia machinery (including process vessels) are to be fitted with:

    a) a negative ventilation system independent of ventilation systems serving other ship spaces and having a capacity not less than 30 changes per hour based upon the total volume of the space; other suitable arrangements which ensure an equivalent effectiveness may be considered;

    b) a fixed ammonia detector system with alarms inside and outside the compartment;

    c) water screens above all access doors, operable manually from outside the compartment;

    d) an independent bilge system.

3. At least two sets of breathing apparatus and protective clothings are to be available.

4. Ammonia piping is not to pass through accommodation spaces.

5. In case of ammonia plants of fishing vessels under 55 m in length or other ammonia plants with a quantity of ammonia not greater than 25 kg said plants are allowed to be located in the machinery space.

    The area where the ammonia machinery is installed is to be served by a hood with a negative ventilation system, so as not to permit any leakage of ammonia from dissipating into other areas in the space.

    A water spray system is to be provided for the said area.

    In addition previous items 2 b), 3 and 4 apply.

End of Document

# M58 Charge air coolers

(1994)

Deleted Feb 2015, replaced by UR M72.

End of Document

# M59 Control and Safety Systems for Dual Fuel Diesel Engines

M59
(1996)

Deleted June 2019

End of Document

# Starting Arrangements of Internal Combustion Engines

M61
(Dec 2003)
(Rev.1 Feb 2022)
(Rev.2 July 2023)
(Rev.3 Feb 2024)

## M61.1 Mechanical starting arrangements

M61.1.1 The arrangement for air starting is to be such that the necessary air for the first charge can be produced on board without external aid.

M61.1.2 Where the main engine is arranged for starting by compressed air, two or more air compressors are to be fitted. At least one of the compressors is to be driven independent of the main propulsion unit. The capacity of one of the said independently driven compressors or the combined capacity of independently driven compressors shall not be less than 50 % of the total required.

M61.1.3 The total capacity of air compressors is to be sufficient to supply within one hour the quantity of air needed to satisfy M61.1.5 by charging the receivers from atmospheric pressure. The capacity is to be approximately equally divided between the number of compressors fitted, excluding an emergency compressor which may be installed to satisfy M61.1.1.

M61.1.4 Where the main engine is arranged for starting by compressed air, at least two starting air receivers of about equal capacity are to be fitted which may be used independently.

M61.1.5 The total capacity of air receivers is to be sufficient to provide, without their being replenished, not less than 12 consecutive starts alternating between Ahead and Astern of each main engine of the reversible type, and not less than six starts of each main non-reversible type engine connected to a controllable pitch propeller or other device enabling the start without opposite torque. When other consumers such as auxiliary engines starting systems, low-pressure compressed air systems (see UR M84.2.2), control systems, whistle, etc., are to be connected to starting air receivers, their air consumption is also to be taken into account.

Regardless of the above, for multi-engine installations the number of starts required for each engine may be reduced upon the agreement with the Classification Society depending upon the arrangement of the engines and the transmission of their output to the propellers.

Note:

1. Rev.1 of this Unified Requirement is to be uniformly implemented by IACS Societies on ships contracted for construction on or after 1 January 2023.

2. Rev.2 of this Unified Requirement is to be uniformly implemented by IACS Societies on ships contracted for construction on or after 1 January 2025.

3. Rev.3 of this Unified Requirement is to be uniformly implemented by IACS Societies on ships contracted for construction on or after 1 July 2025.

4. The "contracted for construction" date means the date on which the contract to build the vessel is signed between the prospective owner and the shipbuilder. For further details regarding the date of "contract for construction", refer to IACS Procedural Requirement (PR) No.29.

## M61.2 Electrical starting

M61.2.1 Where the main engine is arranged for electric starting, two separate batteries are to be fitted. The arrangement is to be such that the batteries cannot be connected in parallel. Each battery is to be capable of starting the main engine when in cold and ready to start conditions. The combined capacity of the batteries is to be sufficient without recharging to provide within 30 minutes the number of starts of main engines are required above in case of air starting.

M61.2.2 Electric starting arrangements for auxiliary engines are to have two separate batteries or may be supplied by separate circuits from the main engine batteries when such are provided. In the case of a single auxiliary engine only one battery may be required. The capacity of the batteries for starting the auxiliary engines is to be sufficient for at least three starts for each engine.

M61.2.3 The starting batteries are to be used for starting and the engine's own monitoring purposes only. Provisions are to be made to maintain continuously the stored energy at all times.

End of Document

# M62

## M62 (Feb 2002) Rooms for emergency fire pumps in cargo ships

Deleted June 2014, converted to Rec 135.

End of Document

# Design of integrated cargo and ballast systems on tankers

M64
(April 2003)
(Rev.1 July 2004)

## 1. Application

These requirements are applicable to integrated cargo and ballast systems installed on tankers (i.e. cargo ships constructed or adapted for the carriage of liquid cargoes in bulk) contracted for construction on or after 1 January 2004, irrespective of the size or type of the tanker.

Within the scope of these requirements, integrated cargo and ballast system means any integrated hydraulic and/or electric system used to drive both cargo and ballast pumps (including active control and safety systems and excluding passive components, e.g. piping).

## 2. Functional Requirements

The operation of cargo and/or ballast systems may be necessary, under certain emergency circumstances or during the course of navigation, to enhance the safety of tankers.

As such, measures are to be taken to prevent cargo and ballast pumps becoming inoperative simultaneously due to a single failure in the integrated cargo and ballast system, including its control and safety systems.

## 3. Design features

The following design features are, inter alia, to be fitted:

.1 the emergency stop circuits of the cargo and ballast systems are to be independent from the circuits for the control systems. A single failure in the control system circuits or the emergency stop circuits are not to render the integrated cargo and ballast system inoperative;

.2 manual emergency stops of the cargo pumps are to be arranged in a way that they are not to cause the stop of the power pack making ballast pumps inoperable;

.3 the control systems are to be provided with backup power supply, which may be satisfied by a duplicate power supply from the main switch board. The failure of any power supply is to provide audible and visible alarm activation at each location where the control panel is fitted.

.4 in the event of failure of the automatic or remote control systems, a secondary means of control is to be made available for the operation of the integrated cargo and ballast system. This is to be achieved by manual overriding and/or redundant arrangements within the control systems.

Note:

1. This UR is to be uniformly implemented by all IACS Societies on tankers (as defined in M64.1) contracted for construction on or after 1 January 2004
2. The "contracted for construction" date means the date on which the contract to build the vessel is signed between the prospective owner and the shipbuilder. For further details regarding the date of "contract for construction", refer to IACS Procedural Requirement (PR) No. 29.

END

# M65

## Draining and Pumping Forward Spaces in Bulk Carriers

M65
(Feb 2004)
(Rev.1 July 2004)

### Application

1. This requirement applies to bulk carriers constructed generally with single deck, top-side tanks and hopper side tanks in cargo spaces intended primarily to carry dry cargo in bulk, and includes such types as ore carriers and combination carriers, which are contracted for construction on or after 1 January 2005.

### Dewatering capacity

2. The dewatering system for ballast tanks located forward of the collision bulkhead and for bilges of dry spaces any part of which extends forward of the foremost cargo hold<sup>[1]</sup> is to be designed to remove water from the forward spaces at a rate of not less than 320Am<sup>3</sup>/h, where A is the cross-sectional area in m<sup>2</sup> of the largest air pipe or ventilator pipe connected from the exposed deck to a closed forward space that is required to be dewatered by these arrangements

<sup>[1]</sup>. Reference is made to SOLAS regulation XII/13 and Unified Interpretation SC 179 "Dewatering of forward spaces of bulk carriers".

Note:

1) The "contracted for construction" date means the date on which the contract to build the vessel is signed between the prospective owner and the shipbuilder. For further details regarding the date of "contract for construction", refer to IACS Procedural Requirement (PR) No. 29.

IACS Req. 2004/Rev.1 2004

END

# M67 Type Testing Procedure for Crankcase Oil Mist Detection and Alarm Equipment

M67
(Jan 2005)
(Corr.1 Nov 2005)
(Rev.1 Oct 2006)
(Corr.1 Oct 2007)
(Rev.2 Feb 2015)

## 1. Scope

1.1 To specify the tests required to demonstrate that crankcase oil mist detection and alarm equipment intended to be fitted to diesel engines satisfy classification society requirements.

Note:
This test procedure is also applicable to oil mist detection and alarm equipment intended for gear cases.

## 2. Recognised Standards

2.1 IACS Unified Requirement E10 Test Specification for Type Approval.

## 3. Purpose

3.1 The purpose of type testing crankcase oil mist detection and alarm equipment is seven fold:

3.1.1 To verify the functionality of the system.

3.1.2 To verify the effectiveness of the oil mist detectors.

3.1.3 To verify the accuracy of oil mist detectors.

3.1.4 To verify the alarm set points.

3.1.5 To verify time delays between oil mist leaving the source and alarm activation.

3.1.6 To verify functional failure detection.

3.1.7 To verify the influence of optical obscuration on detection.

Note:

1) Engines are to be fitted with crankcase oil mist detection and alarm equipment complying with this UR when:

    i) an application for certification of an engine is dated on/after 1 January 2007; or

    ii) installed in new ships for which the date of contract for construction is on or after 1 January 2007.

2) Rev.2 of this UR is to be uniformly implemented by IACS Societies from 1 July 2016.

3) The "contracted for construction" date means the date on which the contract to build the vessel is signed between the prospective owner and the shipbuilder. For further details regarding the date of "contract for construction", refer to IACS Procedural Requirement (PR) No. 29.

## 4. Test facilities

4.1 Test houses carrying out type testing of crankcase oil mist detection and alarm equipment are to satisfy the following criteria:

4.1.1 A full range of facilities for carrying out the environmental and functionality tests required by this procedure shall be available and be acceptable to the classification societies.

4.1.2 The test house that verifies the functionality of the equipment is to be equipped so that it can control, measure and record oil mist concentration levels in terms of mg/l to an accuracy of ± 10% in accordance with this procedure.

4.1.3 When verifying the functionality, test houses are to consider the possible hazards associated with the generation of the oil mist required and take adequate precautions. IACS will accept the use of low toxicity, low hazard oils as used in other applications, provided it is demonstrated to have similar properties to SAE 40 monograde mineral oil specified.

## 5. Equipment testing

5.1 The range of tests is to include the following:

5.1.1 For the alarm/monitoring panel:

   (a) Functional tests described in Section 6.

   (b) Electrical power supply failure test.

   (c) Power supply variation test.

   (d) Dry heat test.

   (e) Damp heat test.

   (f) Vibration test.

   (g) EMC test.

   (h) Insulation resistance test.

   (i) High voltage test.

   (j) Static and dynamic inclinations, if moving parts are contained.

5.1.2 For the detectors:

   (a) Functional tests described in Section 6.

   (b) Electrical power supply failure test.

   (c) Power supply variation test.

   (d) Dry heat test.

   (e) Damp heat test.

   (f) Vibration test.

   (g) EMC test where susceptible.

   (h) Insulation resistance test.

   (i) High voltage test.

   (j) Static and dynamic inclinations.

## 6. Functional tests

6.1 All tests to verify the functionality of crankcase oil mist detection and alarm equipment are to be carried out in accordance with 6.2 to 6.6 with an oil mist concentration in air, known in terms of mg/l to an accuracy of ±10%.

6.2 The concentration of oil mist in the test chamber is to be measured in the top and bottom of the chamber and these concentrations are not to differ by more than 10%. See also 8.1.1.1.

6.3 The oil mist detector monitoring arrangements are to be capable of detecting oil mist in air concentrations of between

(a) 0 and 10% of the lower explosive limit (LEL) or

(b) between 0 and a percentage of weight of oil in air determined by the Manufacturer based on the sensor measurement method (e.g. obscuration or light scattering) that is acceptable to the Society taking into account the alarm level specified in 6.4.

Note: The LEL corresponds to an oil mist concentration of approximately 50mg/l (~4.1% weight of oil in air mixture).

6.4 The alarm set point for oil mist concentration in air is to provide an alarm at a maximum level corresponding to not more than 5% of the LEL or approximately 2.5mg/l.

6.5 Where alarm set points can be altered, the means of adjustment and indication of set points are to be verified against the equipment manufacturer's instructions.

6.6 The performance of the oil mist detector in mg/l is to be demonstrated. This is to include the following:

- range (oil mist detector)
- resolution (oil mist detector)
- sensitivity (oil mist detector)

Note:
Sensitivity of a measuring system: quotient of the change in an indication of a measuring system and the corresponding change in a value of a quantity being measured.

Resolution: smallest change in a quantity being measured that causes a perceptible change in the corresponding indication.

6.7 Where oil mist is drawn into a detector via piping arrangements, the time delay between the sample leaving the crankcase and operation of the alarm is to be determined for the longest and shortest lengths of pipes recommended by the manufacturer. The pipe arrangements are to be in accordance with the manufacturer's instructions/recommendations. Piping is to be arranged to prevent pooling of oil condensate which may cause a blockage of the sampling pipe over time.

6.8 It is to be demonstrated that the openings of detector equipment does not become occluded or blocked under continuous splash and spray of engine lubricating oil, as may occur in the crankcase atmosphere. Testing is to be in accordance with arrangements proposed by the manufacturer and agreed by the classification society. The temperature, quantity and angle of impact of the oil to be used is to be declared and their selection justified by the manufacturer.

6.9 Detector equipment may be exposed to water vapour from the crankcase atmosphere which may affect the sensitivity of the equipment and it is to be demonstrated that exposure to such conditions will not affect the functional operation of the detector equipment. Where exposure to water vapour and/or water condensation has been identified as a possible source of equipment malfunctioning, testing is to demonstrate that any mitigating arrangements such as heating are effective. Testing is to be in accordance with arrangements proposed by the manufacturer and agreed by the classification society.

Note:
This testing is in addition to that required by 5.1.2(e) and is concerned with the effects of condensation caused by the detection equipment being at a lower temperature than the crankcase atmosphere.

6.10 It is to be demonstrated that an indication is given where lenses fitted in the equipment and used in determination of the oil mist level have been partially obscured to a degree that will affect the reliability of the information and alarm indication as required by M10.16.

## 7. Detectors and alarm equipment to be tested

7.1 The detectors and alarm equipment selected for the type testing are to be selected from the manufacturer's normal production line by the classification society witnessing the tests.

7.2 Two detectors are to be tested. One is to be tested in clean condition and the other in a condition representing the maximum level of lens obscuration specified by the manufacturer.

## 8. Method

8.1 The following requirements are to be satisfied at type testing:

8.1.1 Oil mist generation is to satisfy 8.1.1.1 to 8.1.1.5.

8.1.1.1 The ambient temperature in and around the test chamber is to be at the standard atmospheric conditions defined in IACS Unified Requirement E10 Test Specification for Type Approval before any test run is started.

8.1.1.2 Oil mist is to be generated with suitable equipment using an SAE 40 monograde mineral oil or equivalent and supplied to a test chamber. The selection of the oil to be used is to take into consideration risks to health and safety, and the appropriate controls implemented. A low toxicity, low flammability oil of similar viscosity may be used as an alternative. The oil mist produced is to have an average (or arithmetic mean) droplet size not exceeding 5 µm. The oil droplet size is to be checked using the sedimentation method or an equivalent method to a relevant international or national standard. If the sedimentation method is chosen, the test chamber is to have a minimum height of 1m and volume of not less than 1m<sup>3</sup>.

Note:
The calculated oil droplet size using the sedimentation method represents the average droplet size.

8.1.1.3 The oil mist concentrations used are to be ascertained by the gravimetric deterministic method or equivalent. Where an alternative technique is used its equivalence is to be demonstrated.

Note:
For this test, the gravimetric deterministic method is a process where the difference in weight of a 0.8 µm pore size membrane filter is ascertained from weighing the filter before and after drawing 1 litre of oil mist through the filter from the oil mist test chamber. The oil mist chamber is to be fitted with a recirculating fan.

8.1.1.4 Samples of oil mist are to be taken at regular intervals and the results plotted against the oil mist detector output. The oil mist detector is to be located adjacent to where the oil mist samples are drawn off.

8.1.1.5 The results of a gravimetric analysis are considered invalid and are to be rejected if the resultant calibration curve has an increasing gradient with respect to the oil mist detection reading. This situation occurs when insufficient time has been allowed for the oil mist to become homogeneous. Single results that are more than 10% below the calibration curve are to be rejected. This situation occurs when the integrity of the filter unit has been compromised and not all of the oil is collected on the filter paper.

8.1.1.6 The filters require to be weighed to a precision of 0.1mg and the volume of air/oil mist sampled to 10ml.

8.1.2 For type approval by a classification society the testing is to be witnessed by authorised personnel from the classification society.

8.1.3 Oil mist detection equipment is to be tested in the orientation (vertical, horizontal or inclined) in which it is intended to be installed on an engine or gear case as specified by the equipment manufacturer.

8.1.4 Type testing is to be carried out for each type of oil mist detection and alarm equipment for which a manufacturer seeks classification approval. Where sensitivity levels can be adjusted, testing is to be carried out at the extreme and mid-point level settings.

## 9. Assessment

9.1 Assessment of oil mist detection equipment after testing is to address the following:

9.1.1 The equipment to be tested is to have evidence of design appraisal/approval by the classification society witnessing tests.

9.1.2 Details of the detection equipment to be tested are to be recorded and are to include:

- name of manufacturer;
- type designation;
- oil mist concentration assessment capability and alarm settings;
- The maximum percentage level of lens obscuration used in 7.2.

9.1.3 After completing the tests, the detection equipment is to be examined and the condition of all components ascertained and documented. Photographic records of the monitoring equipment condition are to be taken and included in the report.

## 10. Design series qualification

10.1 The approval of one type of detection equipment may be used to qualify other devices having identical construction details. Proposals are to be submitted for consideration.

## 11. The report

11.1 The test house is to provide a full report which includes the following information and documents:

11.1.1 Test specification.

11.1.2 Details of equipment tested.

11.1.3 Results of tests.

To include a declaration by the manufacturer of the oil mist detector of its:

- Performance, in mg/L;
- Accuracy, of oil mist concentration in air;
- Precision, of oil mist concentration in air;
- Range, of oil mist detector;
- Resolution, of oil mist detector;
- Response time, of oil mist detector;
- Sensitivity, of oil mist detector;
- Obscuration of sensor detection, declared as percentage of obscuration. 0% totally clean, 100% totally obscure;
- Detector failure alarm;

## 12. Acceptance

12.1 Acceptance of crankcase oil mist detection equipment is at the discretion of individual classification societies based on the appraisal plans and particulars and the test house report of the results of type testing.

12.2 The following information is to be submitted to classification societies for acceptance of oil mist detection equipment and alarm arrangements:

12.2.1 Description of oil mist detection equipment and system including alarms.

12.2.2 Copy of the test house report identified in 11.

12.2.3 Schematic layout of engine oil mist detection arrangements showing location of detectors/sensors and piping arrangements and dimensions.

12.2.4 Maintenance and test manual which is to include the following information:

   (a) Intended use of equipment and its operation.

   (b) Functionality tests to demonstrate that the equipment is operational and that any faults can be identified and corrective actions notified.

   (c) Maintenance routines and spare parts recommendations.

   (d) Limit setting and instructions for safe limit levels.

   (e) Where necessary, details of configurations in which the equipment is and is not to be used.

End of Document

# M69

## Qualitative Failure Analysis for Propulsion and Steering on Passenger Ships

M69
(June 2008)
(Rev.1 Feb 2021)

Deleted in Mar 2022.

End of Document

# M71 Type Testing of I.C. Engines

(Feb 2015)
(Corr.1 June 2016)

## 1. General

1.1 Type approval of I.C. engine types consists of drawing approval, specification approval, conformity of production, approval of type testing programme, type testing of engines, review of the obtained results, and the issuance of the Type Approval Certificate. The maximum period of validity of a Type Approval Certificate is 5 years. The requirements for drawing approval and specification approval of engines and components are specified in separate URs.

1.2 For the purpose of this UR, the following definitions apply:

*Low-Speed Engines* means diesel engines having a rated speed of less than 300 rpm.

*Medium-Speed Engines* means diesel engines having a rated speed of 300 rpm and above, but less than 1400 rpm.

*High-Speed Engines* means diesel engines having a rated speed of 1400 rpm or above.

## 2. Objectives

2.1 The type testing, documented in this UR, is to be arranged to represent typical foreseen service load profiles, as specified by the engine builder, as well as to cover for required margins due to fatigue scatter and reasonably foreseen in-service deterioration.

2.2 This applies to:

- Parts subjected to high cycle fatigue (HCF) such as connecting rods, cams, rollers and spring tuned dampers where higher stresses may be provided by means of elevated injection pressure, cylinder maximum pressure, etc.

- Parts subjected to low cycle fatigue (LCF) such as "hot" parts when load profiles such as idle - full load - idle (with steep ramps) are frequently used.

- Operation of the engine at limits as defined by its specified alarm system, such as running at maximum permissible power with the lowest permissible oil pressure and/or highest permissible oil inlet temperature.

Notes:

1. The requirements of UR M71 are to be uniformly implemented by IACS Societies for engines for which the date of application for type approval certification is dated on or after 1 July 2016.

2. The "date of application for type approval" is the date of the document accepted by the Classification Society as request for type approval certification of a new engine type or of an engine type that has undergone substantive modifications in respect of the one previously type approved, or for renewal of an expired type approval certificate.

## 3. Validity

3.1 Type testing is required for every new engine type intended for installation onboard ships subject to classification.

3.2 A type test carried out for a particular type of engine at any place of manufacture will be accepted for all engines of the same type built by licensees or the licensor, subject to each place of manufacture being found to be acceptable to the Society.

3.3 A type of engine is defined by:

- bore and stroke

- injection method (direct or indirect)

- valve and injection operation (by cams or electronically controlled)

- kind of fuel (liquid, dual-fuel, gaseous)

- working cycle (4-stroke, 2-stroke)

- turbo-charging system (pulsating or constant pressure)

- the charging air cooling system (e.g. with or without intercooler)

- cylinder arrangement (in-line or V) <sup>1)</sup>

- cylinder power, speed and cylinder pressures <sup>2)</sup>

Notes:

<sup>1)</sup> One type test will be considered adequate to cover a range of different numbers of cylinders. However, a type test of an in-line engine may not always cover the V-version. Subject to the individual Societies' discretion, separate type tests may be required for the V-version. On the other hand, a type test of a V-engine covers the in-line engines, unless the bmep is higher.

Items such as axial crankshaft vibration, torsional vibration in camshaft drives, and crankshafts, etc. may vary considerably with the number of cylinders and may influence the choice of engine to be selected for type testing.

<sup>2)</sup> The engine is type approved up to the tested ratings and pressures (100% corresponding to MCR).

Provided documentary evidence of successful service experience with the classified rating of 100% is submitted, an increase (if design approved*) may be permitted without a new type test if the increase from the type tested engine is within:

- 5% of the maximum combustion pressure, or
- 5% of the mean effective pressure, or
- 5% of the rpm

Providing maximum power is not increased by more than 10%, an increase of maximum approved power may be permitted without a new type test provided engineering analysis and evidence of successful service experience in similar field applications (even if the application is not classified) or documentation of internal testing are submitted if the increase from the type tested engine is within:

- 10% of the maximum combustion pressure, or
- 10% of the mean effective pressure, or
- 10% of the rpm

\* Only crankshaft calculation and crankshaft drawings, if modified.

### De-rated engine

If an engine has been design approved, and internal testing per Stage A is documented to a rating higher than the one type tested, the Type Approval may be extended to the increased power/mep/rpm upon submission of an Extended Delivery Test Report at:

- Test at over speed (only if nominal speed has increased)
- Rated power, i.e. 100% output at 100% torque and 100% speed corresponding to load point 1., 2 measurements with one running hour in between
- Maximum permissible torque (normally 110%) at 100% speed corresponding to load point 3 or maximum permissible power (normally 110%) and speed according to nominal propeller curve corresponding to load point 3a., ½ hour
- 100% power at maximum permissible speed corresponding to load point 2, ½ hour

### Integration Test

An integration test demonstrating that the response of the complete mechanical, hydraulic and electronic system is as predicted maybe carried out for acceptance of sub-systems (Turbo Charger, Engine Control System, Dual Fuel, Exhaust Gas treatment…) separately approved. The scope of these tests shall be proposed by the designer/licensor taking into account of impact on engine.

## 4. Safety precautions

4.1 Before any test run is carried out, all relevant equipment for the safety of attending personnel is to be made available by the manufacturer/shipyard and is to be operational, and its correct functioning is to be verified.

4.2 This applies especially to crankcase explosive conditions protection, but also overspeed protection and any other shut down function.

4.3 The inspection for jacketing of high-pressure fuel oil lines and proper screening of pipe connections (as required in M71.8.9 fire measures) is also to be carried out before the test runs.

4.4 Interlock test of turning gear is to be performed when installed.

## 5. Test programme

5.1 The type testing is divided into 3 stages:

1. Stage A - internal tests.
    This includes some of the testing made during the engine development, function testing, and collection of measured parameters and records of testing hours. The results of testing required by the Society or stipulated by the designer are to be presented to the Society before starting stage B.

2. Stage B - witnessed tests.
    This is the testing made in the presence of Classification Society personnel.

3. Stage C - component inspection.
    This is the inspection of engine parts to the extent as required by the Society.

5.2 The complete type testing program is subject to approval by the Society. The extent the Surveyor's attendance is to be agreed in each case, but at least during stage B and C.

5.3 Testing prior to the witnessed type testing (stage B and C), is also considered as a part of the complete type testing program.

5.4 Upon completion of complete type testing (stage A through C), a type test report is to be submitted to the Society for review. The type test report is to contain:

- overall description of tests performed during stage A. Records are to be kept by the builders QA management for presentation to the Classification Society.

- detailed description of the load and functional tests conducted during stage B.

- inspection results from stage C.

5.5 As required in M71.2 the type testing is to substantiate the capability of the design and its suitability for the intended operation. Special testing such as LCF and endurance testing will normally be conducted during stage A.

5.6 High speed engines for marine use are normally to be subjected to an endurance test of 100 hours at full load. Omission or simplification of the type test may be considered for the type approval of engines with long service experience from non-marine fields or for the extension of type approval of engines of a well-known type, in excess of the limits given in M71.3.

Propulsion engines for high speed vessels that may be used for frequent load changes from idle to full are normally to be tested with at least 500 cycles (idle - full load - idle) using the steepest load ramp that the control system (or operation manual if not automatically controlled) permits. The duration at each end is to be sufficient for reaching stable temperatures of the hot parts.

## 6. Measurements and recordings

6.1 During all testing the ambient conditions (air temperature, air pressure and humidity) are to be recorded.

6.2 As a minimum, the following engine data are to be measured and recorded:

- Engine r.p.m.

- Torque

- Maximum combustion pressure for each cylinder <sup>1)</sup>

- Mean indicated pressure for each cylinder <sup>1)</sup>

- Charging air pressure and temperature

- Exhaust gas temperature

- Fuel rack position or similar parameter related to engine load

- Turbocharger speed

- All engine parameters that are required for control and monitoring for the intended use (propulsion, auxiliary, emergency).

Notes:

<sup>1)</sup> For engines where the standard production cylinder heads are not designed for such measurements, a special cylinder head made for this purpose may be used. In such a case, the measurements may be carried out as part of Stage A and are to be properly documented. Where deemed necessary e.g. for dual fuel engines, the measurement of maximum combustion pressure and mean indicated pressure may be carried out by indirect means, provided the reliability of the method is documented.

Calibration records for the instrumentation used to collect data as listed above are to be presented to - and reviewed by the attending Surveyor.

Additional measurements may be required in connection with the design assessment.

## 7. Stage A - internal tests

7.1 During the internal tests, the engine is to be operated at the load points important for the engine designer and the pertaining operating values are to be recorded. The load conditions to be tested are also to include the testing specified in the applicable type approval programme.

7.2 At least the following conditions are to be tested:

- Normal case:

    The load points 25%, 50%, 75%, 100% and 110% of the maximum rated power for continuous operation, to be made along the normal (theoretical) propeller curve and at constant speed for propulsion engines (if applicable mode of operation i.e. driving controllable pitch propellers), and at constant speed for engines intended for generator sets including a test at no load and rated speed.

- The limit points of the permissible operating range. These limit points are to be defined by the engine manufacturer.

- For high speed engines, the 100 hr full load test and the low cycle fatigue test apply as required in connection with the design assessment.

- Specific tests of parts of the engine, required by the Society or stipulated by the designer.

## 8. Stage B - witnessed tests

8.1 The tests listed below are to be carried out in the presence of a Surveyor. The achieved results are to be recorded and signed by the attending Surveyor after the type test is completed.

8.2 The over-speed test is to be carried out and is to demonstrate that the engine is not damaged by an actual engine overspeed within the overspeed shutdown system set-point. This test may be carried out at the manufacturer's choice either with or without load during the speed overshoot.

8.3 Load points

The engine is to be operated according to the power and speed diagram (see Figure 1). The data to be measured and recorded when testing the engine at the various load points have to include all engine parameters listed in M71.6. The operating time per load point depends on the engine size (achievement of steady state condition) and on the time for collection of the operating values. Normally, an operating time of 0.5 hour can be assumed per load point, however sufficient time should be allowed for visual inspection by the Surveyor.

8.4 The load points are:

- Rated power (MCR), i.e. 100% output at 100% torque and 100% speed corresponding to load point 1, normally for 2 hours with data collection with an interval of 1 hour. If operation of the engine at limits as defined by its specified alarm system (e.g. at alarm levels of lub oil pressure and inlet temperature) is required, the test should be made here.

- 100% power at maximum permissible speed corresponding to load point 2.

- Maximum permissible torque (at least and normally 110%) at 100% speed corresponding to load at point 3, or maximum permissible power (at least and normally 110%) and 103.2% speed according to the nominal propeller curve corresponding to load point 3a. Load point 3a applies to engines only driving fixed pitch propellers or water jets. Load point 3 applies to all other purposes.
    Load point 3 (or 3a as applicable) is to be replaced with a load that corresponds to the specified overload and duration approved for intermittent use. This applies where such overload rating exceeds 110% of MCR. Where the approved intermittent overload rating is less than 110% of MCR, subject overload rating has to replace the load point at 100% of MCR. In such case the load point at 110% of MCR remains.

- Minimum permissible speed at 100% torque, corresponding to load point 4.

- Minimum permissible speed at 90% torque corresponding to load point 5. (Applicable to propulsion engines only).

- Part loads e.g. 75%, 50% and 25% of rated power and speed according to nominal propeller curve (i.e. 90.8%, 79.3% and 62.9% speed) corresponding to points 6, 7 and 8 or at constant rated speed setting corresponding to points 9, 10 and 11, depending on the intended application of the engine.

- Crosshead engines not restricted for use with C.P. propellers are to be tested with no load at the associated maximum permissible engine speed.

8.5 During all these load points, engine parameters are to be within the specified and approved values.

![Figure 1 Load points - power vs speed diagram showing load points 1-11 with regions of continuous operation, intermitted operation, and short-time overload operation](assets/ur-m71corr1/part01-fig-000.png)

Figure 1 Load points

① = range of continuous operation

② = range of intermitted operation

③ = range of short-time overload operation

8.6 Operation with damaged turbocharger

For 2-stroke propulsion engines, the achievable continuous output is to be determined in the case of turbocharger damage.

Engines intended for single propulsion with a fixed pitch propeller are to be able to run continuously at a speed (r.p.m.) of 40% of full speed along the theoretical propeller curve when one turbocharger is out of operation. (The test can be performed by either by-passing the turbocharger, fixing the turbocharger rotor shaft or removing the rotor.)

8.7 Functional tests

- Verification of the lowest specified propulsion engine speed according to the nominal propeller curve as specified by the engine designer (even though it works on a water-brake). During this operation, no alarm shall occur.

- Starting tests, for non-reversible engines and/or starting and reversing tests, for reversible engines, for the purpose of determining the minimum air pressure and the consumption for a start.

- Governor tests: tests for compliance with UR M3.1 and M3.2 are to be carried out.

8.8 Integration test

For electronically controlled diesel engines, integration tests are to verify that the response of the complete mechanical, hydraulic and electronic system is as predicted for all intended operational modes. The scope of these tests is to be agreed with the Society for selected cases based on the FMEA required in UR M44.

8.9 Fire protection measures

Verification of compliance with requirements for jacketing of high-pressure fuel oil lines, screening of pipe connections in piping containing flammable liquids and insulation of hot surfaces:

- The engine is to be inspected for jacketing of high-pressure fuel oil lines, including the system for the detection of leakage, and proper screening of pipe connections in piping containing flammable liquids.

- Proper insulation of hot surfaces is to be verified while running the engine at 100% load, alternatively at the overload approved for intermittent use. Readings of surface temperatures are to be done by use of Infrared Thermoscanning Equipment. Equivalent measurement equipment may be used when so approved by the Society. Readings obtained are to be randomly verified by use of contact thermometers.

## 9. Stage C - Opening up for Inspections

9.1 The crankshaft deflections are to be measured in the specified (by designer) condition (except for engines where no specification exists).

9.2 High speed engines for marine use are normally to be stripped down for a complete inspection after the type test.

9.3 For all the other engines, after the test run the components of one cylinder for in-line engines and two cylinders for V-engines are to be presented for inspection as follows (engines with long service experience from non-marine fields can have a reduced extent of opening):

- piston removed and dismantled

- crosshead bearing dismantled

- guide planes

- connecting rod bearings (big and small end) dismantled (special attention to serrations and fretting on contact surfaces with the bearing backsides)

- main bearing dismantled

- cylinder liner in the installed condition

- cylinder head, valves disassembled

- cam drive gear or chain, camshaft and crankcase with opened covers. (The engine must be turnable by turning gear for this inspection.)

9.4 For V-engines, the cylinder units are to be selected from both cylinder banks and different crank throws.

9.5 If deemed necessary by the surveyor, further dismantling of the engine may be required.

End of Document

