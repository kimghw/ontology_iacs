
# K3 Keyless Fitting of Propellers without Ice Strengthening

**K3**
(1978)
(Corr. 1 April 1998)
(Corr. 2 June 1998)

### K3.1 Requirements to be satisfied

The formulae, etc., given herein are not applicable for propellers where a sleeve is introduced between shaft and boss.

The taper of the propeller shaft cone should not exceed $$1/15$$.

Prior to final pull-up, the contact area between the mating surfaces is to be checked and should not be less than 70% of the theoretical contact area (100%). Non-contact bands extending circumferentially around the boss or over the full length of the boss are not acceptable.

After final pull-up, the propeller is to be secured by a nut on the propeller shaft. The nut should be secured to the shaft.

The factor of safety against friction slip at 35°C is not to be less than 2,8 under the action of rated torque (based on rated power r.p.m.) plus torque due to torsionals as defined in K3.4.

For the oil injection method the coefficient of friction should be 0,13 for bosses made in copper-based alloy and steel.

The maximum equivalent uniaxial stress in the boss at 0°C based on the Mises-Hencky criterion ($$\sigma_E$$) should not exceed 70% of the yield point or 0.2% proof-stress (0,2% offset yield strength) for the propeller material based on the test piece value. For cast iron the value should not exceed 30% of the nominal tensile strength.

### K3.2 Material constants

| Modulus of elasticity | |
| :--- | :--- |
| Cast and forged steel | $$2,1 \times 10^4 \text{ kgf/mm}^2$$ |
| Cast iron | $$1,0 \times 10^4 \text{ kgf/mm}^2$$ |
| Copper based alloys, Cu 1 and Cu 2 | $$1,1 \times 10^4 \text{ kgf/mm}^2$$ |
| Copper based alloys, Cu 3 and Cu 4 | $$1,2 \times 10^4 \text{ kgf/mm}^2$$ |

| Poisson's ratio | |
| :--- | :--- |
| Cast and forged steel | 0,29 |
| Cast iron | 0,26 |
| All copper-based alloys | 0,33 |

| Coefficient of linear expansion | |
| :--- | :--- |
| Cast and forged steel and cast iron | $$12,0 \times 10^{-6} \text{ mm/mm}^\circ\text{C}$$ |
| All copper-based alloys | $$17,5 \times 10^{-6} \text{ mm/mm}^\circ\text{C}$$ |

---

### K3.3 Formulae used

The formulae given below, for the ahead condition, will also give sufficient safety in the astern condition.

The formulae are applicable for solid shafts only.

**Minimum required surface pressure at 35°C**
$$P_{35} = \frac{ST}{AB} \left[ -S\theta + \sqrt{\mu^2 + B \left( \frac{F_v}{T} \right)^2} \right]$$
where $$B = \mu^2 - S^2 \theta^2$$

**Corresponding minimum pull-up length at 35°C**
$$\delta_{35} = P_{35} \frac{D_s}{2\theta} \left[ \frac{1}{E_b} \left( \frac{K^2 + 1}{K^2 - 1} + \nu_b \right) + \frac{1}{E_s} (1 - \nu_s) \right]$$

**Minimum pull-up length at temperature $$t$$ ($$t < 35^\circ\text{C}$$)**
$$\delta_t = \delta_{35} + \frac{D_s}{2\theta} (\alpha_b - \alpha_s)(35 - t)$$

**Corresponding minimum surface pressure at temperature $$t$$**
$$P_t = P_{35} \frac{\delta_t}{\delta_{35}}$$

**Minimum push-up load at temperature $$t$$**
$$W_t = A P_t (\mu + \theta)$$

**Maximum permissible surface pressure at 0°C**
$$P_{max} = \frac{0,7 \sigma_y (K^2 - 1)}{\sqrt{3K^4 + 1}}$$

**Corresponding maximum permissible pull-up length at 0°C**
$$\delta_{max} = \frac{P_{max}}{P_{35}} \delta_{35}$$

**Shear force at interface**
$$F_v = \frac{2cQ}{D_s}$$

**Rated thrust developed for free running vessels (if not given)**
$$T = 132 \frac{H}{V_s} \text{ or } T = 4,3 \cdot 10^6 \frac{H}{PN}$$

---

### K3.4 Nomenclature

*   **$$A$$** = 100% theoretical contact area ($$\text{mm}^2$$) between boss and shaft, as read from drawings and disregarding oil grooves
*   **$$D_s$$** = diameter (mm) of propeller shaft at the midpoint of the taper in the axial direction
*   **$$D_b$$** = mean outer diameter (mm) of propeller boss at the axial position corresponding to $$D_s$$
*   **$$K$$** = $$D_b / D_s$$
*   **$$F_v$$** = shear force at interface = $$2cQ/D_s$$ (kgf)
*   **$$Q$$** = rated torque (kgf•mm) transmitted according to rated horsepower, $$H$$, and speed of propeller shaft
*   **$$T$$** = rated thrust (kgf)
*   **$$c$$** = constant,
    *   $$c = 1,0$$ for turbines, geared diesel drives, electric drives and for direct diesel drives with a hydraulic or an electromagnetic or high elasticity coupling
    *   $$c = 1,2$$ for a direct diesel drive.
    The Classification Society reserves the right to increase the $$c$$ constant if the shrinkage has to absorb an extreme high pulsating torque.
*   **$$H$$** = rated brake horsepower (PS)
*   **$$P$$** = mean propeller pitch (mm)
*   **$$N$$** = propeller speed (r.p.m.) at rated brake horsepower
*   **$$V_s$$** = ship speed (knots) at rated horsepower
*   **$$S$$** = factor of safety against friction slip at 35°C
*   **$$\theta$$** = half taper of propeller shaft, e.g. taper = 1/15. $$\theta = 1/30$$
*   **$$\mu$$** = coefficient of friction between mating surfaces
*   **$$P_{35}$$** = surface pressure ($$\text{kgf/mm}^2$$) between mating surfaces at 35°C
*   **$$P_t$$** = surface pressure ($$\text{kgf/mm}^2$$) between mating surfaces at temperature $$t^\circ\text{C}$$
*   **$$P_0$$** = surface pressure ($$\text{kgf/mm}^2$$) between mating surfaces at temperature 0°C
*   **$$P_{max}$$** = maximum allowable surface pressure ($$\text{kgf/mm}^2$$) at 0°C
*   **$$\delta_{35}$$** = pull-up length (mm) at temperature 35°C
*   **$$\delta_t$$** = pull-up length (mm) at temperature $$t^\circ\text{C}$$
*   **$$\delta_{max}$$** = maximum allowable pull-up length (mm) at temperature 0°C
*   **$$W_t$$** = push-up load (kgf) at temperature $$t^\circ\text{C}$$
*   **$$\sigma_E$$** = equivalent uniaxial stress ($$\text{kgf/mm}^2$$) in the boss according to the Mises-Hencky criterion
*   **$$\alpha_s$$** = coefficient of linear expansion ($$\text{mm/mm}^\circ\text{C}$$) of shaft material
*   **$$\alpha_b$$** = coefficient of linear expansion ($$\text{mm/mm}^\circ\text{C}$$) of boss material
*   **$$E_s$$** = modulus of elasticity ($$\text{kgf/mm}^2$$) of shaft material
*   **$$E_b$$** = modulus of elasticity ($$\text{kgf/mm}^2$$) of boss material
*   **$$\nu_s$$** = Poisson's ratio for shaft material
*   **$$\nu_b$$** = Poisson's ratio for boss material
*   **$$\sigma_y$$** = yield point or 0,2% proof stress (0,2% offset yield strength) of propeller material ($$\text{kgf/mm}^2$$)


