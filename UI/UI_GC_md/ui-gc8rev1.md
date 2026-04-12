<!-- markdownlint-disable-file MD013 MD033 MD036 MD026 MD041 MD024 MD029 MD060 MD007 -->
# GC8 Permissible stresses in way of supports of type C cargo tanks

GC8
(1986)
(Rev.1 June 2016)

Section 4.23.3.1 of the IMO INTERNATIONAL CODE FOR THE CONSTRUCTION AND EQUIPMENT OF SHIPS CARRYING LIQUEFIED GASES IN BULK (MSC.370(93)) reads:

*"4.23.3.1 Plastic deformation*

*For type C independent tanks, the allowable stresses shall not exceed:*

$$\sigma_m \leq f$$

$$\sigma_L \leq 1.5f$$

$$\sigma_b \leq 1.5f$$

$$\sigma_L + \sigma_b \leq 1.5f$$

$$\sigma_m + \sigma_b \leq 1.5f$$

$$\sigma_m + \sigma_b + \sigma_g \leq 3.0f$$

$$\sigma_L + \sigma_b + \sigma_g \leq 3.0f,$$

*where:*

- *σ<sub>m</sub> = equivalent primary general membrane stress;*
- *σ<sub>L</sub> = equivalent primary local membrane stress;*
- *σ<sub>b</sub> = equivalent primary bending stress;*
- *σ<sub>g</sub> = equivalent secondary stress; and*
- *f = the lesser of R<sub>m</sub> /A or R<sub>e</sub> /B,*

*with R<sub>m</sub> and R<sub>e</sub> as defined in 4.18.1.3. With regard to the stresses σ<sub>m</sub>, σ<sub>L</sub>, σ<sub>b</sub> and σ<sub>g</sub>, the definition of stress categories in 4.28.3 are referred. The values A and B shall be shown on the International Certificate of Fitness for the Carriage of Liquefied Gases in Bulk and shall have at least the following minimum values:*

|   | *Nickel steels and carbon-manganese steels* | *Austenitic steels* | *Aluminium alloys* |
|---|---|---|---|
| *A* | *3* | *3.5* | *4* |
| *B* | *1.5* | *1.5* | *1.5* |

*"*

Note:

1. Rev.1 of this UI is to be uniformly implemented by IACS Societies on ships the keels of which are laid or which are at a similar stage of construction on or after 1 July 2016.

## Interpretation

The circumferential stresses at supports shall be calculated by a procedure acceptable to the Classification Society for a sufficient number of load cases.

### 1. Permissible stresses in stiffening rings:

For horizontal cylindrical tanks made of C-Mn steel supported in saddles, the equivalent stress in the stiffening rings shall not exceed the following values if calculated using finite element method:

$$\sigma_e \leq \sigma_{all}$$

where:

$$\sigma_{all} = \min(0.57 R_m; 0.85 R_e)$$

$$\sigma_e = \sqrt{(\sigma_n + \sigma_b)^2 + 3\tau^2}$$

- σ<sub>e</sub> = von Mises equivalent stress in N/mm<sup>2</sup>
- σ<sub>n</sub> = normal stress in N/mm<sup>2</sup> in the circumferential direction of the stiffening ring
- σ<sub>b</sub> = bending stress in N/mm<sup>2</sup> in the circumferential direction of the stiffening ring
- τ = shear stress in N/mm<sup>2</sup> in the stiffening ring

R<sub>m</sub> and R<sub>e</sub> as defined in 4.18.1.3 of the Code.

Equivalent stress values σ<sub>e</sub> should be calculated over the full extent of the stiffening ring by a procedure acceptable to the Classification Society, for a sufficient number of load cases.

### 2. The following assumptions should be made for the stiffening rings:

2.1 The stiffening ring should be considered as a circumferential beam formed by web, face plate, doubler plate, if any, and associated shell plating.

The effective width of the associated plating should be taken as:

- .1 For cylindrical shells:

    an effective width (mm) not greater than $0.78 \sqrt{rt}$ on each side of the web. A doubler plate, if any, may be included within that distance.

    where:

    - r = mean radius of the cylindrical shell (mm)
    - t = shell thickness (mm)

- .2 For longitudinal bulkheads (in the case of lobe tanks):

    the effective width should be determined according to established standards. A value of 20 t<sub>b</sub> on each side of the web may be taken as a guidance value.

    where:

    - t<sub>b</sub> = bulkhead thickness (mm).

2.2 The stiffening ring should be loaded with circumferential forces, on each side of the ring, due to the shear stress, determined by the bi-dimensional shear flow theory from the shear force of the tank.

### 3. For calculation of reaction forces at the supports, the following factors should be taken into account:

3.1 Elasticity of support material (intermediate layer of wood or similar material).

3.2 Change in contact surface between tank and support, and of the relevant reactions, due to:

- thermal shrinkage of tank.
- elastic deformations of tank and support material.

The final distribution of the reaction forces at the supports should not show any tensile forces.

### 4. The buckling strength of the stiffening rings should be examined.

End of Document
