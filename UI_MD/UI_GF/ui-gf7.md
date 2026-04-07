# GF7 External surface area of the tank for determining sizing of pressure relief valve
(Dec 2017)

The International Code of Safety for Ships Using Gases or Other Low-Flashpoint Fuels (IGF Code), MSC Res.391(95), paragraph 6.7.3.1.1.2 and figure 6.7.1;

Paragraph 6.7.3.1.1.2 states:

vapours generated under fire exposure computed using the following formula:

Q = FGA<sup>0.82</sup> (m³/s),

where:

*   **Q** = minimum required rate of discharge of air at standard conditions of 273.15 Kelvin (K) and 0.1013 MPa.
*   **F** = fire exposure factor for different liquefied gas fuel types:
    *   **F** = 1.0 for tanks without insulation located on deck;
    *   **F** = 0.5 for tanks above the deck when insulation is approved by the Administration. (Approval will be based on the use of a fireproofing material, the thermal conductance of insulation and its stability under fire exposure);
    *   **F** = 0.5 for uninsulated independent tanks installed in holds;
    *   **F** = 0.2 for insulated independent tanks in holds (or uninsulated independent tanks in insulated holds);
    *   **F** = 0.1 for insulated independent tanks in inerted holds (or uninsulated independent tanks in inerted, insulated holds); and
    *   **F** = 0.1 for membrane tanks.
    *   For independent tanks partly protruding through the weather decks, the fire exposure factor shall be determined on the basis of the surface areas above and below deck.
*   **G** = gas factor according to formula:

    ```
    G = 12.4 * Z * T
        -----------
         L * D * M
    ```

    where:

(Cont)

*   **T** = temperature in Kelvin at relieving conditions, i.e. 120% of the pressure at which the pressure relief valve is set;
*   **L** = latent heat of the material being vaporized at relieving conditions, in kJ/kg;
*   **D** = a constant based on relation of specific heats k and is calculated as follows:

    ```
    D = k * ( (2 / (k+1))^( (k+1) / (k-1) ) )^(1/2)
    ```

    where:
    *   **k** = ratio of specific heats at relieving conditions, and the value of which is between 1.0 and 2.2. If k is not known, D = 0.606 shall be used;
*   **Z** = compressibility factor of the gas at relieving conditions; if not known, Z = 1.0 shall be used;
*   **M** = molecular mass of the product.

The gas factor of each liquefied gas fuel to be carried is to be determined and the highest value shall be used for PRV sizing.

*   **A** = external surface area of the tank (m²), as for different tank types, as shown in figure 6.7.1.

Image description: Diagrams illustrating various tank types, including cylindrical tanks with spherically dished, hemispherical or semi-ellipsoidal heads, or spherical tanks, and prismatic tanks.

Image description: Diagrams illustrating various tank types for Figure 6.7.1, including Bilobe tanks and Horizontal cylindrical tanks arrangement.

**Figure 6.7.1**

## Interpretation

### For prismatic tanks

1.  Lmin, for non-tapered tanks, is the smaller of the horizontal dimensions of the flat bottom of the tank. For tapered tanks, as would be used for the forward tank, Lmin is the smaller of the length and the average width.
2.  For prismatic tanks whose distance between the flat bottom of the tank and bottom of the hold space is equal to or less than Lmin/10:
    **A = external surface area minus flat bottom surface area.**
3.  For prismatic tanks whose distance between the flat bottom of the tank and bottom of the hold space is greater than Lmin/10:
    **A = external surface area.**

Note:

1.  This Unified Interpretation is to be uniformly implemented by IACS Societies on ships contracted for construction on or after 1 January 2018.
2.  The "contracted for construction" date means the date on which the contract to build the vessel is signed between the prospective owner and the shipbuilder. For further details regarding the date of "contract for construction", refer to IACS Procedural Requirement (PR) No. 29.

End of Document