# GC7 Carriage of products not covered by the code

(1986)
(Rev.1
June
2016)

Section 4.23.1.2 of the IMO INTERNATIONAL CODE FOR THE CONSTRUCTION AND EQUIPMENT OF SHIPS CARRYING LIQUEFIED GASES IN BULK (MSC.370(93)) reads:

"4.23.1.2 The design vapour pressure shall not be less than:

$$ P_v = 0.2 + AC(p_r)^{1.5} \text{ (MPa)} $$

where:

$$ A = 0.00185 \sqrt{\frac{\sigma_m}{\Delta \sigma_A}} $$

with:
*   $ \sigma_m $ = design primary membrane stress;
*   $ \Delta \sigma_A $ = allowable dynamic membrane stress (double amplitude at probability level Q = 10°) and equal to:
    *   55 N/mm² for ferritic-perlitic, martensitic and austenitic steel;
    *   25 N/mm² for aluminium alloy (5083-0);
*   C = a characteristic tank dimension to be taken as the greatest of the following:
    *   h, 0.75b or 0.45l,
    with:
    *   h = height of tank (dimension in ship's vertical direction) (m);
    *   b = width of tank (dimension in ship's transverse direction)(m);
    *   l = length of tank (dimension in ship's longitudinal direction) (m);
    *   $ p_r $ = the relative density of the cargo ($ p_r $ = 1 for fresh water) at the design temperature.

When a specified design life of the tank is longer than 10⁸ wave encounters, $ \Delta \sigma_A $ shall be modified to give equivalent crack propagation corresponding to the design life."

Note:
1.  Rev.1 of this UI is to be uniformly implemented by IACS Societies on ships the keels of which are laid or which are at a similar stage of construction on or after 1 July 2016.

---

# GC7 (cont) Interpretation

1.  If the carriage of products not covered by the Code* is intended, it should be verified that the double amplitude of the primary membrane stress $ \Delta \sigma_m $ created by the maximum dynamic pressure differential $ \Delta P $ does not exceed the allowable double amplitude of the dynamic membrane stress $ \Delta \sigma_A $ as specified in paragraph 4.23.1.2 of the Code, ie:

    $$ \Delta \sigma_m \le \Delta \sigma_A $$

2.  The dynamic pressure differential $ \Delta P $ in MPa should be calculated as follows:

    $$ \Delta P = \frac{\rho}{1.02 \cdot 10^5} (\alpha_{\beta 1} Z_{\beta 1} - \alpha_{\beta 2} Z_{\beta 2}) $$

    where:
    *   $ \rho $ is maximum liquid cargo density in kg/m³ at the design temperature
    *   $ \alpha_{\beta} $, $ Z_{\beta} $ are as defined in 4.28.1.2 of the Code, see also Figure below
    *   $ \alpha_{\beta 1} $, $ Z_{\beta 1} $ are the $ \alpha_{\beta} $ and $ Z_{\beta} $ values giving the maximum liquid pressure ($ P_{gd} $)$ _{max} $
    *   $ \alpha_{\beta 2} $, $ Z_{\beta 2} $ are the $ \alpha_{\beta} $ and $ Z_{\beta} $ values giving the minimum liquid pressure ($ P_{gd} $)$ _{min} $

    In order to evaluate the maximum pressure differential $ \Delta P $, pressure differentials should be evaluated over the full range of the acceleration ellipse as shown in the sketches given below.

*Image: A diagram showing an acceleration ellipse and two corresponding pressure point diagrams.
    - The acceleration ellipse has axes labeled 1.0 (vertical) and some horizontal extent. Points $ \alpha_{b2} $ and $ \alpha_{b1} $ are marked on the ellipse.
    - Two pressure point diagrams are shown next to the ellipse.
    - The first diagram (top of tank when b=b2) shows a vector from the tank top to $ \alpha_{b2} $ labeled $ Z_{b2} $.
    - The second diagram (top of tank when b=b1) shows a vector from the tank top to $ \alpha_{b1} $ labeled $ Z_{b1} $.
    - A note below the diagrams states: "NOTE: *The outlined procedure is only applicable to products having a relative density exceeding 1,0."*

End of Document
