# M56 Marine gears – load capacity of involute parallel axis spur and helical gears

## M56.1 Basic principles - introduction and general influence factors

### M56.1.1 Introduction

The following definitions are mainly based on the ISO 6336 series standard (hereinafter called "reference standard") for the calculation of load capacity of spur and helical gears.

### M56.1.2 Scope and field of application

These requirements apply to enclosed gears, both intended for main propulsion and for essential auxiliary services, which accumulate a large number of load cycles (several millions), whose gear set is intended to transmit a maximum continuous power equal to, or greater than:

- 220 kW for gears intended for main propulsion
- 110 kW for gears intended for essential auxiliary services

These requirements, however, may be applied to the enclosed gears, whose gear set is intended to transmit a maximum continuous power less than those specified above at the request of the individual society.

**Notes:**

1. The requirements of UR M56 Rev.2 are to be uniformly implemented from 1 January 2015 by all IACS Societies to any marine gear subject to approval and to any Type Approved marine gear from the date of the first renewal after 1 January 2015. For a marine gear approved prior to 1 January 2015 where no failure has occurred, and no changes in design / scantlings of the gear meshes or materials or declared load capacity data has taken place the requirements of UR M56 Rev.2 may be waived.
2. The requirements of UR M56 Rev.3 are to be uniformly implemented from 1 January 2017 by all IACS Societies to any marine gear subject to approval and to any Type Approved marine gear from the date of the first renewal after 1 January 2017. For a marine gear approved prior to 1 January 2017 where no failure has occurred, and no changes in design / scantlings of the gear meshes or materials or declared load capacity data has taken place the requirements of UR M56 Rev.3 may be waived.
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
| :--- | :--- | :--- |
| $$a$$ | centre distance | mm |
| $$b$$ | common face width | mm |
| $$b_{1,2}$$ | face width of pinion, wheel | mm |
| $$d$$ | reference diameter | mm |
| $$d_{1,2}$$ | reference diameter of pinion, wheel | mm |
| $$d_{a1,2}$$ | tip diameter of pinion, wheel | mm |
| $$d_{b1,2}$$ | base diameter of pinion, wheel | mm |
| $$d_{f1,2}$$ | root diameter of pinion, wheel | mm |
| $$d_{w1,2}$$ | working diameter of pinion, wheel | mm |
| $$F_t$$ | nominal tangential load | N |
| $$F_{bt}$$ | nominal tangential load on base cylinder in the transverse section | N |
| $$h$$ | tooth depth | mm |
| $$m_n$$ | normal module | mm |
| $$m_t$$ | transverse module | mm |
| $$n_{1,2}$$ | rotational speed of pinion, wheel | revs/min (rpm) |
| $$P$$ | maximum continuous power transmitted by the gear set | kW |
| $$T_{1,2}$$ | torque in way of pinion, wheel | Nm |
| $$u$$ | gear ratio | |
| $$v$$ | linear velocity at pitch diameter | m/s |
| $$x_{1,2}$$ | addendum modification coefficient of pinion, wheel | |
| $$z$$ | number of teeth | |
| $$z_{1,2}$$ | number of teeth of pinion, wheel | |
| $$z_n$$ | virtual number of teeth | |
| $$\alpha_n$$ | normal pressure angle at reference cylinder | ° |
| $$\alpha_t$$ | transverse pressure angle at ref. cylinder | ° |
| $$\alpha_{tw}$$ | transverse pressure angle at working pitch cylinder | ° |
| $$\beta$$ | helix angle at reference cylinder | ° |
| $$\beta_b$$ | helix angle at base cylinder | ° |
| $$\epsilon_\alpha$$ | transverse contact ratio | |
| $$\epsilon_\beta$$ | overlap ratio | |
| $$\epsilon_\gamma$$ | total contact ratio | |

### M56.1.4 Geometrical definitions

For internal gearing $$z_2, a, d_2, d_{a2}, d_{b2}$$ and $$d_{w2}$$ are negative. The pinion is defined as the gear with the smaller number of teeth, therefore the absolute value of the gear ratio, defined as follows, is always greater or equal to the unity:

$$ u = z_2 / z_1 = d_{w2} / d_{w1} = d_2 / d_1 $$

For external gears $$u$$ is positive, for internal gears $$u$$ is negative.

In the equation of surface durability $$b$$ is the common face width on the pitch diameter.

In the equation of tooth root bending stress $$b_1$$ or $$b_2$$ are the face widths at the respective tooth roots. In any case, $$b_1$$ and $$b_2$$ are not to be taken as greater than $$b$$ by more than one module ($$m_n$$) on either side.

The common face width $$b$$ may be used also in the equation of teeth root bending stress if significant crowning or end relief have been adopted.

$$ \tan \alpha_t = \frac{\tan \alpha_n}{\cos \beta} $$

$$ \tan \beta_b = \tan \beta \cdot \cos \alpha_t $$

$$ d_{1,2} = \frac{z_{1,2} m_n}{\cos \beta} $$

$$ d_{b1,2} = d_{1,2} \cos \alpha_t $$

$$ \begin{cases} d_{w1} = \frac{2a}{u+1} \\ d_{w2} = \frac{2au}{u+1} \end{cases} \text{where } a = 0.5(d_{w1} + d_{w2}) $$

$$ z_{n1,2} = \frac{z_{1,2}}{\cos^2 \beta_b \cdot \cos \beta} $$

$$ m_t = \frac{m_n}{\cos \beta} $$

$$ \text{inv } \alpha = \tan \alpha - \frac{\pi \alpha}{180}; \alpha [°] $$

$$ \text{inv } \alpha_{tw} = \text{inv } \alpha_t + 2 \tan \alpha_n \frac{x_1 + x_2}{z_1 + z_2} \text{ or } \cos \alpha_{tw} = \frac{m_t (z_1 + z_2)}{2a} \cos \alpha_t $$

$$ \epsilon_\alpha = \frac{0.5 \sqrt{d_{a1}^2 - d_{b1}^2} \pm 0.5 \sqrt{d_{a2}^2 - d_{b2}^2} - a \cdot \sin \alpha_{tw}}{\pi \cdot m_t \cdot \cos \alpha_t} $$
(the positive sign is used for external gears, the negative sign for internal gears)

$$ \epsilon_\beta = \frac{b \cdot \sin \beta}{\pi \cdot m_n} $$
(for double helix, $$b$$ is to be taken as the width of one helix)

$$ \epsilon_\gamma = \epsilon_\alpha + \epsilon_\beta $$

$$ v = \pi \cdot d_{1,2} n_{1,2} / (60 \cdot 10^3) $$

### M56.1.5 Nominal tangential load, $$F_t$$

The nominal tangential load, $$F_t$$, tangential to the reference cylinder and perpendicular to the relevant axial plane, is calculated directly from the maximum continuous power transmitted by the gear set by means of the following equations:

$$ T_{1,2} = \frac{30 \cdot 10^3 P}{\pi \cdot n_{1,2}} $$

$$ F_t = 2000 \cdot T_{1,2} / d_{1,2} $$

### M56.1.6 General influence factors

#### M56.1.6.1 Application factor, $$K_A$$

The application factor, $$K_A$$, accounts for dynamic overloads from sources external to the gearing.

$$K_A$$, for gears designed for infinite life is defined as the ratio between the maximum repetitive cyclic torque applied to the gear set and the nominal rated torque.

The nominal rated torque is defined by the rated power and speed and is the torque used in the rating calculations.

The factor mainly depends on:
- characteristics of driving and driven machines;
- ratio of masses;
- type of couplings;
- operating conditions (overspeeds, changes in propeller load conditions, ...).

When operating near a critical speed of the drive system, a careful analysis of conditions must be made.

The application factor, $$K_A$$, should be determined by measurements or by system analysis acceptable to the Society. Where a value determined in such a way cannot be supplied, the following values can be considered.

a) Main propulsion
- diesel engine with hydraulic or electromagnetic slip coupling : 1.00
- diesel engine with high elasticity coupling : 1.30
- diesel engine with other couplings : 1.50

$$^1)$$ Where the vessel, on which the reduction gear is being used, is receiving an Ice Class notation, the Application Factor or the Nominal Tangential Force should be adjusted to reflect the ice load associated with the requested Ice Class, i.e. applying the design approach in UR I3 when applicable.

b) Auxiliary gears
- electric motor, diesel engine with hydraulic or electromagnetic slip coupling : 1.00
- diesel engine with high elasticity coupling : 1.20
- diesel engine with other couplings : 1.40

#### M56.1.6.2 Load sharing factor, $$K_\gamma$$

The load sharing factor, $$K_\gamma$$ accounts for the maldistribution of load in multiple path transmissions (dual tandem, epicyclic, double helix, etc.)

$$K_\gamma$$ is defined as the ratio between the maximum load through an actual path and the evenly shared load. The factor mainly depends on accuracy and flexibility of the branches.

The load sharing factor, $$K_\gamma$$, should be determined by measurements or by system analysis. Where a value determined in such a way cannot be supplied, the following values can be considered for epicyclic gears:

- up to 3 planetary gears : 1.00
- 4 planetary gears : 1.20
- 5 planetary gears : 1.30
- 6 planetary gears and over : 1.40

#### M56.1.6.3 Internal dynamic factor, $$K_v$$

The internal dynamic factor, $$K_v$$, accounts for internally generated dynamic loads due to vibrations of pinion and wheel against each other.

$$K_v$$ is defined as the ratio between the maximum load which dynamically acts on the tooth flanks and the maximum externally applied load ($$F_t K_A K_\gamma$$).

The factor mainly depends on:
- transmission errors (depending on pitch and profile errors);
- masses of pinion and wheel;
- gear mesh stiffness variation as the gear teeth pass through the meshing cycle;
- transmitted load including application factor;
- pitch line velocity;
- dynamic unbalance of gears and shaft;
- shaft and bearing stiffnesses;
- damping characteristics of the gear system.

The dynamic factor, $$K_v$$, is to be calculated as follows:

This method may be applied only to cases where all the following conditions are satisfied:
- running velocity in the subcritical range, i.e.:
  $$ \frac{v z_1}{100} \sqrt{\frac{u^2}{1 + u^2}} < 10 \text{ m/s} $$
- spur gears ($$\beta = 0°$$) and helical gears with $$\beta \le 30°$$
- pinion with relatively low number of teeth, $$z_1 < 50$$
- solid disc wheels or heavy steel gear rim

This method may be applied to all types of gears if $$\frac{v z_1}{100} \sqrt{\frac{u^2}{1 + u^2}} < 3 \text{ m/s}$$, as well as to helical gears where $$\beta > 30°$$.

For gears other than the above, reference is to be made to Method B outlined in the reference standard ISO 6336-1:2019.

a) For spur gears and for helical gears with overlap ratio $$\epsilon_\beta \ge 1$$

$$ K_v = 1 + \left( \frac{K_1}{\frac{K_A F_t}{b}} + K_2 \right) \cdot \frac{v z_1}{100} K_3 \sqrt{\frac{u^2}{1 + u^2}} $$

If $$K_A F_t/b$$ is less than 100 N/mm, this value is assumed to be equal to 100 N/mm.

Numerical values for the factor $$K_1$$ are to be as specified in the Table 1.1

**Table 1.1 Values of the factor $$K_1$$ for the calculation of $$K_v$$**

| | ISO accuracy grades$$^2)$$ | | | | | |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| | **3** | **4** | **5** | **6** | **7** | **8** |
| spur gears | 2.1 | 3.9 | 7.5 | 14.9 | 26.8 | 39.1 |
| helical gears | 1.9 | 3.5 | 6.7 | 13.3 | 23.9 | 34.8 |

For all accuracy grades the factor $$K_2$$ is to be in accordance with the following:
- for spur gears, $$K_2 = 0.0193$$
- for helical gears, $$K_2 = 0.0087$$

Factor $$K_3$$ is to be in accordance with the following:

If $$\frac{v z_1}{100} \sqrt{\frac{u^2}{1 + u^2}} \le 0.2$$ then $$K_3 = 2.0$$

If $$\frac{v z_1}{100} \sqrt{\frac{u^2}{1 + u^2}} > 0.2$$ then $$K_3 = 2.071 - 0.357 \cdot \frac{v z_1}{100} \sqrt{\frac{u^2}{1 + u^2}}$$

b) For helical gears with overlap ratio $$\epsilon_\beta < 1$$ the value $$K_v$$ is determined by linear interpolation between values determined for spur gears ($$K_{v\alpha}$$) and helical gears ($$K_{v\beta}$$) in accordance with:

$$ K_v = K_{v\alpha} - \epsilon_\beta (K_{v\alpha} - K_{v\beta}) $$

Where:
$$K_{v\alpha}$$ is the $$K_v$$ value for spur gears, in accordance with a);
$$K_{v\beta}$$ is the $$K_v$$ value for helical gears, in accordance with a).

$$^2)$$ ISO accuracy grades according to ISO 1328-1:2013. In case of mating gears with different accuracy grades, the grade corresponding to the lower accuracy should be used.

#### M56.1.6.4 Face load distribution factors, $$K_{H\beta}$$ and $$K_{F\beta}$$

The face load distribution factors, $$K_{H\beta}$$ for contact stress, $$K_{F\beta}$$ for tooth root bending stress, account for the effects of non-uniform distribution of load across the face width.

$$K_{H\beta}$$ is defined as follows:
$$ K_{H\beta} = \frac{\text{maximum load per unit face width}}{\text{mean load per unit face width}} $$

$$K_{F\beta}$$ is defined as follows:
$$ K_{F\beta} = \frac{\text{maximum bending stress at tooth root per unit face width}}{\text{mean bending stress at tooth root per unit face width}} $$

The mean bending stress at tooth root relates to the considered face width $$b_1$$ resp. $$b_2$$.

$$K_{F\beta}$$ can be expressed as a function of the factor $$K_{H\beta}$$.

The factors $$K_{H\beta}$$ and $$K_{F\beta}$$ mainly depend on:
- gear tooth manufacturing accuracy;
- errors in mounting due to bore errors;
- bearing clearances;
- wheel and pinion shaft alignment errors;
- elastic deflections of gear elements, shafts, bearings, housing and foundations which support the gear elements;
- thermal expansion and distortion due to operating temperature;
- compensating design elements (tooth crowning, end relief, etc.).

The face load distribution factors, $$K_{H\beta}$$ for contact stress, and $$K_{F\beta}$$ for tooth root bending stress, are to be determined according to the Method C outlined in the reference standard ISO 6336-1:2019.

Alternative methods acceptable to the Society may be applied.

a) In case the hardest contact is at the end of the face width $$K_{F\beta}$$ is given by the following equations:

$$ K_{F\beta} = K_{H\beta}^N $$

$$ N = \frac{(b/h)^2}{1 + (b/h) + (b/h)^2} $$

$$(b/h)$$ = face width/tooth height ratio, the minimum of $$b_1/h_1$$ or $$b_2/h_2$$.
For double helical gears, the face width of only one helix is to be used.
When $$b/h < 3$$ the value $$b/h = 3$$ is to be used.

b) In case of gears where the ends of the face width are lightly loaded or unloaded (end relief or crowning):

$$ K_{F\beta} = K_{H\beta} $$

#### M56.1.6.5 Transverse load distribution factors, $$K_{H\alpha}$$ and $$K_{F\alpha}$$

The transverse load distribution factors, $$K_{H\alpha}$$ for contact stress and $$K_{F\alpha}$$ for tooth root bending stress, account for the effects of pitch and profile errors on the transversal load distribution between two or more pairs of teeth in mesh.

The factors $$K_{H\alpha}$$ and $$K_{F\alpha}$$ mainly depend on:
- total mesh stiffness;
- total tangential load $$F_t, K_A, K_\gamma, K_v, K_{H\beta}$$;
- base pitch error;
- tip relief;
- running-in allowances.

The transverse load distribution factors, $$K_{H\alpha}$$ for contact stress and $$K_{F\alpha}$$ for tooth root bending stress, are to be determined according to Method B outlined in the reference standard ISO 6336-1:2019.

## M56.2 Surface durability (pitting)

### M56.2.1 Scope and general remarks

The criterion for surface durability is based on the Hertz pressure on the operating pitch point or at the inner point of single pair contact. The contact stress $$\sigma_H$$ must be equal to or less than the permissible contact stress $$\sigma_{HP}$$.

### M56.2.2 Basic equations

#### M56.2.2.1 Contact stress

$$ \sigma_H = \sigma_{H0} \sqrt{K_A \cdot K_\gamma \cdot K_v \cdot K_{H\alpha} \cdot K_{H\beta}} \le \sigma_{HP} $$

where:

$$\sigma_{H0}$$ = basic value of contact stress for pinion and wheel

$$ \sigma_{H0} = Z_B \cdot Z_H \cdot Z_E \cdot Z_\epsilon \cdot Z_\beta \sqrt{\frac{F_t}{d_1 \cdot b} \frac{(u+1)}{u}} \text{ for pinion} $$

$$ \sigma_{H0} = Z_D \cdot Z_H \cdot Z_E \cdot Z_\epsilon \cdot Z_\beta \sqrt{\frac{F_t}{d_1 \cdot b} \frac{(u+1)}{u}} \text{ for wheel} $$

where:

$$Z_B$$ = single pair tooth contact factor for pinion (see clause 2.3)
$$Z_D$$ = single pair tooth contact factor for wheel (see clause 2.3)
$$Z_H$$ = zone factor (see clause 2.4)
$$Z_E$$ = elasticity factor (see clause 2.5)
$$Z_\epsilon$$ = contact ratio factor (see clause 2.6)
$$Z_\beta$$ = helix angle factor (see clause 2.7)
$$F_t$$ = nominal tangential load at reference cylinder in the transverse section (see Part 1)
$$b$$ = common face width
$$d_1$$ = reference diameter of pinion
$$u$$ = gear ratio (for external gears $$u$$ is positive, for internal gears $$u$$ is negative)

Regarding factors $$K_A, K_\gamma, K_v, K_{H\alpha}$$ and $$K_{H\beta}$$, see Part 1.

#### M56.2.2.2 Permissible contact stress

The permissible contact stress $$\sigma_{HP}$$ is to be evaluated separately for pinion and wheel:

$$ \sigma_{HP} = \frac{\sigma_{H\text{lim}} \cdot Z_N}{S_H} \cdot Z_L \cdot Z_v \cdot Z_R \cdot Z_W \cdot Z_X $$

where:

$$\sigma_{H\text{lim}}$$ = endurance limit for contact stress (see clause 2.8)
$$Z_N$$ = life factor for contact stress (see clause 2.9)
$$Z_L$$ = lubrication factor (see clause 2.10)
$$Z_v$$ = velocity factor (see clause 2.10)
$$Z_R$$ = roughness factor (see clause 2.10)
$$Z_W$$ = hardness ratio factor (see clause 2.11)
$$Z_X$$ = size factor for contact stress (see clause 2.12)
$$S_H$$ = safety factor for contact stress (see clause 2.13)

### M56.2.3 Single pair tooth contact factors, $$Z_B$$ and $$Z_D$$

The single pair tooth contact factors, $$Z_B$$ for pinion and $$Z_D$$ for wheel, account for the influence of the tooth flank curvature on contact stresses at the inner point of single pair contact in relation to $$Z_H$$.

The factors transform the contact stresses determined at the pitch point to contact stresses considering the flank curvature at the inner point of single pair contact.

The single pair tooth contact factors, $$Z_B$$ for pinions and $$Z_D$$ for wheels, are to be determined as follows:

For spur gears, $$\epsilon_\beta = 0$$

$$Z_B = M_1$$ or 1 whichever is the larger value
$$Z_D = M_2$$ or 1 whichever is the larger value

$$ M_1 = \frac{\tan \alpha_{tw}}{\sqrt{\left[ \sqrt{\frac{d_{a1}^2}{d_{b1}^2} - 1} - \frac{2\pi}{z_1} \right] \left[ \sqrt{\frac{d_{a2}^2}{d_{b2}^2} - 1} - (\epsilon_\alpha - 1) \frac{2\pi}{z_2} \right]}} $$

$$ M_2 = \frac{\tan \alpha_{tw}}{\sqrt{\left[ \sqrt{\frac{d_{a2}^2}{d_{b2}^2} - 1} - \frac{2\pi}{z_2} \right] \left[ \sqrt{\frac{d_{a1}^2}{d_{b1}^2} - 1} - (\epsilon_\alpha - 1) \frac{2\pi}{z_1} \right]}} $$

For helical gears when $$\epsilon_\beta \ge 1$$

$$Z_B = 1$$
$$Z_D = 1$$

For helical gears when $$\epsilon_\beta < 1$$ the values $$Z_B$$ and $$Z_D$$ are determined by linear interpolation between $$Z_B$$ and $$Z_D$$ for spur gears and $$Z_B$$ and $$Z_D$$ for helical gears having $$\epsilon_\beta \ge 1$$.

Thus:
$$Z_B = M_1 - \epsilon_\beta (M_1 - 1)$$ and $$Z_B \ge 1$$
$$Z_D = M_2 - \epsilon_\beta (M_2 - 1)$$ and $$Z_D \ge 1$$

For internal gears, $$Z_D$$ shall be taken as equal to 1.

### M56.2.4 Zone factor, $$Z_H$$

The zone factor, $$Z_H$$, accounts for the influence on the Hertzian pressure of tooth flank curvature at pitch point and transforms the tangential load at the reference cylinder to the normal load at the pitch cylinder.

The zone factor, $$Z_H$$, is to be calculated as follows:

$$ Z_H = \sqrt{\frac{2 \cos \beta_b}{\cos^2 \alpha_t \tan \alpha_{tw}}} $$

### M56.2.5 Elasticity factor, $$Z_E$$

The elasticity factor, $$Z_E$$, accounts for the influence of the material properties $$E$$ (modulus of elasticity) and $$\nu$$ (Poisson's ratio) on the contact stress.

The elasticity factor, $$Z_E$$, for steel gears ($$E= 206,000$$ N/mm², $$\nu= 0.3$$) is equal to:

$$ Z_E = 189.8 \sqrt{\text{N/mm}^2} $$

In other cases, reference is to be made to the reference standard ISO 6336-2:2019.

### M56.2.6 Contact ratio factor, $$Z_\epsilon$$

The contact ratio factor, $$Z_\epsilon$$, accounts for the influence of the transverse contact ratio and the overlap ratio on the specific surface load of gears.

The contact ratio factor, $$Z_\epsilon$$, is to be calculated as follows:

Spur gears:
$$ Z_\epsilon = \sqrt{\frac{4 - \epsilon_\alpha}{3}} $$

Helical gears:
- for $$\epsilon_\beta < 1$$
  $$ Z_\epsilon = \sqrt{\frac{4 - \epsilon_\alpha}{3} (1 - \epsilon_\beta) + \frac{\epsilon_\beta}{\epsilon_\alpha}} $$
- for $$\epsilon_\beta \ge 1$$
  $$ Z_\epsilon = \sqrt{\frac{1}{\epsilon_\alpha}} $$

### M56.2.7 Helix angle factor, $$Z_\beta$$

The helix angle factor, $$Z_\beta$$, accounts for the influence of helix angle on surface durability, allowing for such variables as the distribution of load along the lines of contact. $$Z_\beta$$ is dependent only on the helix angle.

The helix angle factor, $$Z_\beta$$, is to be calculated as follows:

$$ Z_\beta = \sqrt{\frac{1}{\cos \beta}} $$

Where $$\beta$$ is the reference helix angle.

### M56.2.8 Endurance limit for contact stress, $$\sigma_{H\text{lim}}$$

For a given material, $$\sigma_{H\text{lim}}$$ is the limit of repeated contact stress which can be permanently endured. The value of $$\sigma_{H\text{lim}}$$ can be regarded as the level of contact stress which the material will endure without pitting for at least $$5 \times 10^7$$ load cycles.

For this purpose, pitting is defined by:
- for not surface hardened gears:
  pitted area > 2% of total active flank area
- for surface hardened gears:
  pitted area > 0.5% of total active flank area, or
  > 4% of one particular tooth flank area.

The $$\sigma_{H\text{lim}}$$ values are to correspond to a failure probability of 1% or less.

The endurance limit mainly depends on:
- material composition, cleanliness and defects;
- mechanical properties;
- residual stresses;
- hardening process, depth of hardened zone, hardness gradient;
- material structure (forged, rolled bar, cast).

The endurance limit for contact stress $$\sigma_{H\text{lim}}$$, is to be determined, in general, making reference to values indicated in the standard ISO 6336-5:2016, for material quality MQ.

### M56.2.9 Life factor, $$Z_N$$

The life factor $$Z_N$$, accounts for the higher permissible contact stress in case a limited life (number of cycles) is required.

The factor mainly depends on:
- material and heat treatment;
- number of cycles;
- influence factors ($$Z_R, Z_v, Z_L, Z_W, Z_X$$).

The life factor, $$Z_N$$, is to be determined according to Method B outlined in the reference standard ISO 6336-2:2019.

### M56.2.10 Influence factors of lubrication film on contact stress, $$Z_L, Z_v$$ and $$Z_R$$

The lubricant factor, $$Z_L$$, accounts for the influence of the type of lubricant and its viscosity. The velocity factor, $$Z_v$$, accounts for the influence of the pitch line velocity. The roughness factor, $$Z_R$$, accounts for the influence of the surface roughness on the surface endurance capacity.

The factors may be determined for the softer material where gear pairs are of different hardness.

The factors mainly depend on:
- viscosity of lubricant in the contact zone;
- the sum of the instantaneous velocities of the tooth surfaces;
- load;
- relative radius of curvature at the pitch point;
- surface roughness of teeth flanks;
- hardness of pinion and gear.

The lubricant factor, $$Z_L$$, the velocity factor, $$Z_v$$, and the roughness factor $$Z_R$$ are to be calculated as follows:

a) Lubricant factor, $$Z_L$$

The factor, $$Z_L$$, is to be calculated from the following equation:

$$ Z_L = C_{ZL} + \frac{4(1 - C_{ZL})}{\left( 1.2 + \frac{134}{\nu_{40}} \right)^2} $$

In the range $$850 \text{ N/mm}^2 \le \sigma_{H\text{lim}} \le 1200 \text{ N/mm}^2$$, $$C_{ZL}$$ is to be calculated as follows:

$$ C_{ZL} = \left( 0.08 \frac{\sigma_{H\text{lim}} - 850}{350} \right) + 0.83 $$

If $$\sigma_{H\text{lim}} < 850 \text{ N/mm}^2$$, take $$C_{ZL} = 0.83$$
If $$\sigma_{H\text{lim}} > 1200 \text{ N/mm}^2$$, take $$C_{ZL} = 0.91$$

Where:
$$\nu_{40}$$ = nominal kinematic viscosity of the oil at 40°C, mm²/s

b) Velocity factor, $$Z_v$$

The velocity factor, $$Z_v$$, is to be calculated from the following equations:

$$ Z_v = C_{ZV} + \frac{2(1 - C_{ZV})}{\sqrt{0.8 + \frac{32}{v}}} $$

In the range $$850 \text{ N/mm}^2 \le \sigma_{H\text{lim}} \le 1200 \text{ N/mm}^2$$, $$C_{ZV}$$ is to be calculated as follows:

$$ C_{ZV} = C_{ZL} + 0.02 $$

c) Roughness factor, $$Z_R$$

The roughness factor, $$Z_R$$, is to be calculated from the following equations:

$$ Z_R = \left( \frac{3}{R_{z10}} \right)^{C_{ZR}} $$

Where:
$$ R_z = \frac{R_{z1} + R_{z2}}{2} $$

The peak-to-valley roughness determined for the pinion $$R_{z1}$$ and for the wheel $$R_{z2}$$ are mean values for the peak-to-valley roughness $$R_z$$ measured on several tooth flanks ($$R_z$$ as defined in the reference standard ISO 6336-2:2019).

$$ R_{z10} = R_z \sqrt[3]{\frac{10}{\rho_{red}}} $$

relative radius of curvature:
$$ \rho_{red} = \frac{\rho_1 \cdot \rho_2}{\rho_1 + \rho_2} $$

Wherein:
$$ \rho_{1,2} = 0.5 \cdot d_{b1,2} \cdot \tan \alpha_{tw} $$
(also for internal gears, $$d_b$$ negative sign)

If the roughness stated is an arithmetic mean roughness, i.e. $$R_a$$ value (=CLA value) (=AA value) the following approximate relationship can be applied:

$$ R_a = \text{CLA} = \text{AA} = R_z / 6 $$

In the range $$850 \text{ N/mm}^2 \le \sigma_{H\text{lim}} \le 1200 \text{ N/mm}^2$$, $$C_{ZR}$$ is to be calculated as follows:

$$ C_{ZR} = 0.32 - 0.0002 \cdot \sigma_{H\text{lim}} $$

If $$\sigma_{H\text{lim}} < 850 \text{ N/mm}^2$$, take $$C_{ZR} = 0.150$$
If $$\sigma_{H\text{lim}} > 1200 \text{ N/mm}^2$$, take $$C_{ZR} = 0.080$$

### M56.2.11 Hardness ratio factor, $$Z_W$$

The hardness ratio factor, $$Z_W$$, accounts for the increase of surface durability of a soft steel gear meshing with a significantly harder gear with a smooth surface in the following cases:

a) Surface-hardened pinion with through-hardened wheel

If $$HB < 130$$
$$ Z_W = 1.2 \cdot \left( \frac{3}{R_{zH}} \right)^{0.15} $$

If $$130 \le HB \le 470$$
$$ Z_W = \left[ 1.2 - \left( \frac{HB - 130}{1700} \right) \right] \cdot \left( \frac{3}{R_{zH}} \right)^{0.15} $$

If $$HB > 470$$
$$ Z_W = \left( \frac{3}{R_{zH}} \right)^{0.15} $$

Where:
$$HB$$ = Brinell hardness of the tooth flanks of the softer gear of the pair
$$R_{zH}$$ = equivalent roughness, μm

$$ R_{zH} = \frac{R_{z1} \cdot (10 / \rho_{red})^{0.33} \cdot (R_{z1} / R_{z2})^{0.66}}{(v \cdot \nu_{40} / 1500)^{0.33}} $$

If $$R_{zH} > 16$$ then $$R_{zH} = 16 \text{ µm}$$
If $$R_{zH} < 3$$ then $$R_{zH} = 3 \text{ µm}$$

$$\rho_{red}$$ = relative radius of curvature (see clause 2.10 c)

b) Through-hardened pinion and wheel

When the pinion is substantially harder than the wheel, the work hardening effect increases the load capacity of the wheel flanks. $$Z_W$$ applies to the wheel only, not to the pinion.

If $$HB_1/HB_2 < 1.2$$, $$Z_W = 1$$
If $$1.2 \le HB_1/HB_2 \le 1.7$$, $$Z_W = 1 + \left( 0.00898 \frac{HB_1}{HB_2} - 0.00829 \right) \cdot (u - 1)$$
If $$HB_1/HB_2 > 1.7$$, $$Z_W = 1 + 0.00698 \cdot (u - 1)$$

If gear ratio $$u > 20$$ then the value $$u = 20$$ is to be used.

In any case, if calculated $$Z_W < 1$$ then the value $$Z_W = 1.0$$ is to be used.

### M56.2.12 Size factor, $$Z_X$$

The size factor, $$Z_X$$, accounts for the influence of tooth dimensions on permissible contact stress and reflects the non-uniformity of material properties.

The factor mainly depends on:
- material and heat treatment;
- tooth and gear dimensions;
- ratio of case depth to tooth size;
- ratio of case depth to equivalent radius of curvature.

For through-hardened gears and for surface-hardened gears with adequate casedepth relative to tooth size and radius of relative curvature $$Z_X = 1$$. When the casedepth is relatively shallow then a smaller value of $$Z_X$$ should be chosen.

### M56.2.13 Safety factor for contact stress, $$S_H$$

The safety factor for contact stress, $$S_H$$, can be assumed by the Society taking into account the type of application.

The following guidance values can be adopted:
- Main propulsion gears: 1.20 to 1.40
- Auxiliary gears: 1.15 to 1.20

For gearing of duplicated independent propulsion or auxiliary machinery, duplicated beyond that required for class, a reduced value can be assumed at the discretion of the Society.

## M56.3 Tooth root bending strength

### M56.3.1 Scope and general remarks

The criterion for tooth root bending strength is the permissible limit of local tensile strength in the root fillet. The root stress $$\sigma_F$$ and the permissible root stress $$\sigma_{FP}$$ shall be calculated separately for the pinion and the wheel.

$$\sigma_F$$ must not exceed $$\sigma_{FP}$$.

The following formulae and definitions apply to gears having rim thickness greater than $$3.5 m_n$$.

The result of rating calculations made by following this method are acceptable for normal pressure angles up to 25° and reference helix angles up to 30°.

For larger pressure angles and large helix angles, the calculated results should be confirmed by experience as by Method A of the reference standard ISO 6336-3:2019.

### M56.3.2 Basic equations

#### M56.3.2.1 Tooth root bending stress for pinion and wheel

$$ \sigma_F = \frac{F_t}{b m_n} Y_F Y_S Y_\beta Y_B Y_{DT} K_A K_\gamma K_v K_{F\alpha} K_{F\beta} \le \sigma_{FP} $$

where:
$$Y_F$$ = tooth form factor (see clause 3.3)
$$Y_S$$ = stress correction factor (see clause 3.4)
$$Y_\beta$$ = helix angle factor (see clause 3.5)
$$Y_B$$ = rim thickness factor (see clause 3.6)
$$Y_{DT}$$ = deep tooth factor (see clause 3.7)
$$F_t, K_A, K_\gamma, K_v, K_{F\alpha}, K_{F\beta}$$ (see Part 1)
$$b$$ (see Part 1, clause 1.4)
$$m_n$$ (see Part 1, clause 1.3)

#### M56.3.2.2 Permissible tooth root bending stress for pinion and wheel

$$ \sigma_{FP} = \frac{\sigma_{FE} Y_d Y_N}{S_F} Y_{\delta \text{relT}} Y_{R\text{relT}} Y_X $$

where:
$$\sigma_{FE}$$ = bending endurance limit
$$Y_d$$ = design factor
$$Y_N$$ = life factor
$$Y_{\delta \text{relT}}$$ = relative notch sensitivity factor
$$Y_{R\text{relT}}$$ = relative surface factor
$$Y_X$$ = size factor
$$S_F$$ = safety factor for tooth root bending stress

### M56.3.3 Tooth form factor, $$Y_F$$

The tooth form factor, $$Y_F$$, represents the influence on nominal bending stress of the tooth form with load applied at the outer point of single pair tooth contact. $$Y_F$$ shall be determined separately for the pinion and the wheel. In the case of helical gears, the form factors for gearing shall be determined in the normal section, i.e. for the virtual spur gear with virtual number of teeth $$z_n$$.

The tooth form factor, $$Y_F$$, is to be calculated as follows:

$$ Y_F = \frac{6 \frac{h_F}{m_n} \cos \alpha_{Fen}}{\left( \frac{s_{Fn}}{m_n} \right)^2 \cos \alpha_n} $$

Where:
$$h_F$$ = bending moment arm for tooth root bending stress for application of load at the outer point of single tooth pair contact (mm)
$$s_{Fn}$$ = tooth root normal chord in the critical section (mm)
$$\alpha_{Fen}$$ = pressure angle at the outer point of single tooth pair contact in the normal section (°)

![Figure 3.1: Dimensions of hF, sFn and alpha_Fen for external gear](Dimensions of hF, sFn and alpha_Fen for external gear)

For the calculation of $$h_F$$, $$s_{Fn}$$ and $$\alpha_{Fen}$$, the procedure outlined in the reference standard ISO 6336-3:2019 (Method B) is to be used.

### M56.3.4 Stress correction factor, $$Y_S$$

The stress correction factor $$Y_S$$, is used to convert the nominal bending stress to the local tooth root stress, taking into account that not only bending stresses arise at the root.

$$Y_S$$ applies to the load application at the outer point of single tooth pair contact.

$$Y_S$$ shall be determined separately for the pinion and for the wheel.
The stress correction factor, $$Y_S$$, is to be determined with the following equation (having range of validity: $$1 \le q_s \le 8$$):

$$ Y_S = (1.2 + 0.13 L) q_s^{\left( \frac{1}{1.21 + 2.3/L} \right)} $$

Where:
$$ q_s = \frac{s_{Fn}}{2 \rho_F} $$

$$q_s$$ = notch parameter,
$$\rho_F$$ = root fillet radius in the critical section, mm
$$L = s_{Fn} / h_F$$

For $$h_F$$ and $$s_{Fn}$$ see clause 3.1

For the calculation of $$\rho_F$$ the procedure outlined in the reference standard ISO 6336-3:2019 is to be used.

### M56.3.5 Helix angle factor, $$Y_\beta$$

The helix angle factor, $$Y_\beta$$, converts the stress calculated for a point loaded cantilever beam representing the substitute gear tooth to the stress induced by a load along an oblique load line into a cantilever plate which represents a helical gear tooth.

The helix angle factor, $$Y_\beta$$ is to be calculated as follows:

$$ Y_\beta = 1 - \epsilon_\beta \frac{\beta}{120} $$

where:
$$\beta$$ = reference helix angle in degrees.

The value 1.0 is substituted for $$\epsilon_\beta$$ when $$\epsilon_\beta > 1.0$$, and 30° is substituted for $$\beta > 30°$$.

### M56.3.6 Rim thickness factor, $$Y_B$$

The rim thickness factor, $$Y_B$$, is a simplified factor used to de-rate thin rimmed gears. For critically loaded applications, this method should be replaced by a more comprehensive analysis. Factor $$Y_B$$ is to be determined as follows:

a) for external gears:
if $$s_R / h \ge 1.2$$, $$Y_B = 1$$
if $$0.5 < s_R / h < 1.2$$, $$Y_B = 1.6 \cdot \ln \left( 2.242 \frac{h}{s_R} \right)$$

where:
$$s_R$$ = rim thickness of external gears, mm
$$h$$ = tooth height, mm

The case $$s_R / h \le 0.5$$ is to be avoided.

b) for internal gears:
if $$s_R / m_n \ge 3.5$$, $$Y_B = 1$$
if $$1.75 < s_R / m_n < 3.5$$, $$Y_B = 1.15 \cdot \ln \left( 8.324 \frac{m_n}{s_R} \right)$$

where:
$$s_R$$ = rim thickness of internal gears, mm

The case $$s_R / m_n \le 1.75$$ is to be avoided.

### M56.3.7 Deep tooth factor, $$Y_{DT}$$

The deep tooth factor, $$Y_{DT}$$, adjusts the tooth root stress to take into account high precision gears and contact ratios within the range of virtual contact ratio $$2.05 \le \epsilon_{\alpha n} \le 2.5$$, where:

$$ \epsilon_{\alpha n} = \frac{\epsilon_\alpha}{\cos^2 \beta_b} $$

Factor $$Y_{DT}$$ is to be determined as follows:

if ISO accuracy grade $$\le 4$$ and $$\epsilon_{\alpha n} > 2.5$$, $$Y_{DT} = 0.7$$
if ISO accuracy grade $$\le 4$$ and $$2.05 < \epsilon_{\alpha n} \le 2.5$$, $$Y_{DT} = 2.366 - 0.666 \cdot \epsilon_{\alpha n} $$

in all other cases $$Y_{DT} = 1.0$$

### M56.3.8 Bending endurance limit, $$\sigma_{FE}$$

For a given material, $$\sigma_{FE}$$ is the local tooth root stress which can be permanently endured.

According to the reference standard ISO 6336-5:2016 the number of $$3 \times 10^6$$ cycles is regarded as the beginning of the endurance limit.

$$\sigma_{FE}$$ is defined as the unidirectional pulsating stress with a minimum stress of zero (disregarding residual stresses due to heat treatment). Other conditions such as alternating stress or prestressing etc. are covered by the design factor $$Y_d$$.

The $$\sigma_{FE}$$ values are to correspond to a failure probability of 1% or less.

The endurance limit mainly depends on:
- material composition, cleanliness and defects;
- mechanical properties;
- residual stresses;
- hardening process, depth of hardened zone, hardness gradient;
- material structure (forged, rolled bar, cast).

The bending endurance limit, $$\sigma_{FE}$$ is to be determined, in general, making reference to values indicated in the reference standard ISO 6336-5:2016, for material quality MQ.

### M56.3.9 Design factor, $$Y_d$$

The design factor, $$Y_d$$, takes into account the influence of load reversing and shrinkfit prestressing on the tooth root strength, relative to the tooth root strength with unidirectional load as defined for $$\sigma_{FE}$$.

The design factor, $$Y_d$$, for load reversing, is to be determined as follows:
- $$Y_d = 1.0$$ in general;
- $$Y_d = 0.9$$ for gears with occasional part load in reversed direction, such as main wheel in reversing gearboxes;
- $$Y_d = 0.7$$ for idler gears

### M56.3.10 Life factor, $$Y_N$$

The life factor, $$Y_N$$, accounts for the higher tooth root bending stress permissible in case a limited life (number of cycles) is required.

The factor mainly depends on:
- material and heat treatment;
- number of load cycles (service life);
- influence factors ($$Y_{\delta \text{relT}}, Y_{R\text{relT}}, Y_X$$).

The life factor, $$Y_N$$, is to be determined according to Method B outlined in the reference standard ISO 6336-3:2019.

### M56.3.11 Relative notch sensitivity factor, $$Y_{\delta \text{relT}}$$

The relative notch sensitivity factor, $$Y_{\delta \text{relT}}$$, indicates the extent to which the theoretically concentrated stress lies above the fatigue endurance limit. The factor mainly depends on material and relative stress gradient.

The relative notch sensitivity factor, $$Y_{\delta \text{relT}}$$, is to be determined as follows:

$$ Y_{\delta \text{relT}} = \frac{1 + \sqrt{0.2 \rho' (1 + 2 q_s)}}{1 + \sqrt{1.2 \rho'}} $$

where:
$$q_s$$ = notch parameter (see clause 3.4)
$$\rho'$$ = slip-layer thickness, mm, from the following table

| Material | $$\rho'$$, mm |
| :--- | :---: |
| case hardened steels, flame or induction hardened steels | 0.0030 |
| through-hardened steels$$^1)$$, yield point $$R_e =$$ | |
| 500 N/mm² | 0.0281 |
| 600 N/mm² | 0.0194 |
| 800 N/mm² | 0.0064 |
| 1000 N/mm² | 0.0014 |
| nitrided steels | 0.1005 |

$$^1)$$ The given values of $$\rho'$$ can be interpolated for values of $$R_e$$ not stated above

### M56.3.12 Relative surface factor, $$Y_{R\text{relT}}$$

The relative surface factor, $$Y_{R\text{relT}}$$, takes into account the dependence of the root strength on the surface condition in the tooth root fillet, mainly the dependence on the peak to valley surface roughness.

The relative surface factor, $$Y_{R\text{relT}}$$ is to be determined as follows:

| $$R_z < 1$$ | $$1 \le R_z \le 40$$ | Material |
| :--- | :--- | :--- |
| 1.120 | $$1.674 - 0.1529 (R_z + 1)^{0.1}$$ | case hardened steels, through - hardened steels ($$\sigma_B \ge 800 \text{ N/mm}^2$$) |
| 1.070 | $$5.306 - 4.203 (R_z + 1)^{0.01}$$ | normalised steels ($$\sigma_B < 800 \text{ N/mm}^2$$) |
| 1.025 | $$4.299 - 3.259 (R_z + 1)^{0.0058}$$ | nitrided steels |

Where:
$$R_z$$ = mean peak-to-valley roughness of tooth root fillets, μm
$$\sigma_B$$ = tensile strength, N/mm²

The method applied here is only valid when scratches or similar defects deeper than $$2 R_z$$ are not present.

If the roughness stated is an arithmetic mean roughness, i.e. $$R_a$$ value (=CLA value) (=AA value) the following approximate relationship can be applied:

$$ R_a = \text{CLA} = \text{AA} = R_z / 6 $$

### M56.3.13 Size factor, $$Y_X$$

The size factor, $$Y_X$$, takes into account the decrease of the strength with increasing size.

The factor mainly depends on:
- material and heat treatment;
- tooth and gear dimensions;
- ratio of case depth to tooth size.

The size factor, $$Y_X$$, is to be determined as follows:

| $$Y_X$$ | for $$m_n$$ | Description |
| :--- | :--- | :--- |
| $$Y_X = 1.00$$ | for $$m_n \le 5$$ | generally |
| $$Y_X = 1.03 - 0.06 m_n$$ | for $$5 < m_n < 30$$ | normalised and through-hardened steels |
| $$Y_X = 0.85$$ | for $$m_n \ge 30$$ | normalised and through-hardened steels |
| $$Y_X = 1.05 - 0.010 m_n$$ | for $$5 < m_n < 25$$ | surface hardened steels |
| $$Y_X = 0.80$$ | for $$m_n \ge 25$$ | surface hardened steels |

### M56.3.14 Safety factor for tooth root bending stress, $$S_F$$

The safety factor for tooth root bending stress, $$S_F$$, can be assumed by the Society taking into account the type of application.
The following guidance values can be adopted:
- Main propulsion gears: 1.55 to 2.00
- Auxiliary gears: 1.40 to 1.45

For gearing of duplicated independent propulsion or auxiliary machinery, duplicated beyond that required for class, a reduced value can be assumed at the discretion of the Society.

**End of Document**
