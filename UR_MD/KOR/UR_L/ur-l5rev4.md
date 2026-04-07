# L5 Computer Software for Onboard Stability Calculations

**(May 04)**
**(Rev.1 Feb 2005)**
**(Rev.2 Sep 2006)**
**(Corr.1 Nov 2006)**
**(Rev.3 June 2017)**
**(Rev.4 June 2020)**

### Application

This Unified Requirement is applicable to software which calculates the stability of actual loading conditions and which is installed on ships and on units subject to compliance with the 1966 Load Line Convention or the 1988 Protocol to the Load Line Convention, as amended, the IMO MODU Code and/or the 2008 IS Code.

The use of onboard computers for stability calculations is not a requirement of class.

Stability software installed onboard shall cover all mandatory class and statutory intact and damage stability requirements applicable to the ship. This UR, requires approval of software installed on onboard computers which is capable of performing stability calculations.

Active and passive systems are defined in paragraph 2. This UR covers passive systems and the off-line operation mode of active systems only.

The requirements in this UR apply to stability software on ships contracted for construction on or after 1 July 2005.

### 1. General

- The scope of a stability calculation software shall be in accordance with the stability information as approved by the administration and shall at least include all information and perform all calculations or checks as necessary to ensure compliance with the applicable stability requirements.
- Approved stability software is not a substitute for the approved stability information, and is used as a supplement to the approved stability information to facilitate stability calculations.
- The input/output information shall be easily comparable with approved stability information so as to avoid confusion and possible misinterpretation by the operator relative to the approved stability information.

**Note:**

1. The "contracted for construction" date means the date on which the contract to build the vessel is signed between the prospective owner and the shipbuilder. For further details regarding the date of "contract for construction", refer to IACS Procedural Requirement (PR) No.29.
2. Changes introduced in Rev.2 of this UR are to be uniformly applied by IACS Societies on ships contracted for construction on or after 1 January 2007.
3. Changes introduced in Rev.3 of this UR are to be uniformly applied by IACS Societies on ships contracted for construction on or after 1 July 2018.
4. Changes introduced in Rev.4 of this UR are to be uniformly applied by IACS Societies on ships contracted for construction on or after 1 July 2021.

---

- An operation manual is to be provided for the onboard computer stability software.
- The language in which the stability information is displayed and printed out as well as the operation manual written shall be the same as used in the ship's approved stability information. The society may require a translation into a language considered appropriate.
- The onboard computer software for stability calculations is to be ship specific and the results of the calculations are to be only applicable to the ship for which it has been approved.
- In case of modifications implying changes in the main data or internal arrangement of the ship, the specific approval of any original stability calculation software is no longer valid. The software is to be modified accordingly and re-approved.

### 2. Calculation Systems

A passive system requires manual data entry;

an active system replaces the manual entry with sensors reading and entering the contents of tanks, etc.; and

a third system, an integrated system, controls or initiates actions based on the sensor-supplied inputs and is not within the scope of this UR.

### 3. Types of Stability Software

Four types of calculations performed by stability software are acceptable depending upon a vessel's stability requirements:

**Type 1**
Software calculating intact stability only (for vessels not required to meet a damage stability criterion).

**Type 2**
Software calculating intact stability and checking damage stability on basis of a limit curve (e.g. for vessels applicable to SOLAS Part B-1 damage stability calculations, etc.) or checking all the stability requirements (intact and damage stability) on the basis of a limit curve.

**Type 3**
Software calculating intact stability and damage stability by direct application of pre-programmed damage cases based on the relevant Conventions or Codes for each loading condition (for some tankers etc.).

**Type 4**
Software calculating damage stability associated with an actual loading condition and actual flooding case, using direct application of user defined damage, for the purpose of providing operational information for safe return to port (SRtP).

Damage stability of both Type 3 and Type 4 stability software shall be based on a hull form model, that is, directly calculated from a full three-dimensional geometric model.

### 4. Functional requirements:

#### 4.1 General requirements for any type of stability software

4.1.1 The calculation program shall present relevant parameters of each loading condition in order to assist the Master in his judgement on whether the ship is loaded within the approval limits. The following parameters shall be presented for a given loading condition:
- deadweight data;
- lightship data;
- trim;
- draft at the draft marks and perpendiculars;
- summary of loading condition displacement, VCG, LCG and, if applicable, TCG;
- downflooding angle and corresponding downflooding opening (not applicable for Type 2 software which uses limit curve for checking all the stability requirements. However, if intact stability criteria are given in addition to the limit curve, downflooding angle and the corresponding downflooding opening shall be indicated);
- compliance with stability criteria: Listing of all calculated stability criteria, the limit values, the obtained values and the conclusions (criteria fulfilled or not fulfilled) (not applicable for Type 2 software which uses limit curve for checking all the stability requirements. However, if intact stability criteria are given in addition to the limit curve, the limit values, the obtained values and the conclusion shall be indicated).

4.1.2 A clear warning shall be given on screen and in hard copy printout if any of the loading limitations are not complied with.
Loading limitations shall include, but may not be limited to:
- Trim, draught, liquid densities, tank filling levels, initial heel;
- Use of limit KG/GM curves in conjunction with above for Type 2;
- Restrictions to the stowage height for timber where timber load lines are assigned.

4.1.3 Type 3 software is to include pre-defined relevant damage cases for both sides of the ship according to the applicable rules for automatic check of a given loading condition.

4.1.4 The date and time of a saved calculation shall be part of the screen display and hard copy printout.

4.1.5 Each hard copy printout shall contain identification of the calculation program including version number.

4.1.6 Units of measurement are to be clearly identified and used consistently within a loading calculation.

4.1.7 For Type 3 and Type 4 software, the system shall be pre-loaded with a detailed computer model of the complete hull, including appendages, all compartments, tanks and the relevant parts of the superstructure considered in the damage stability calculation, wind profile, down-flooding and up-flooding openings, cross-flooding arrangements, internal compartment connections and escape routes, as applicable and according to the type of stability software.

4.1.8 For Type 1 and Type 2 software, in case a full three dimensional model is used for stability calculations, the requirements of the computer model are to be as per paragraph 4.1.7 above to the extent as applicable and according to the type of stability software.

#### 4.2 Further requirements for Type 4 stability software

4.2.1 The normal (Type 1, 2 and 3) and SRtP (Type 4) software need not be "totally separated". Where the normal and SRtP software are not totally separated:
- the function of switching between normal software and Type 4 software shall be provided.
- the actual intact loading condition is to be the same for both functions (normal operation and SRtP); and
- the SRtP module needs only to be activated in case of an incident.

Approval of Type 4 (SRtP) software is for stability only.

4.2.2 In passenger ships which are subject to SRtP and have an onboard stability computer and shore-based support, such software need not be identical.

4.2.3 Each internal space shall be assigned its permeability as shown below, unless a more accurate permeability has been reflected in the approved stability information.

| Spaces | Default | Full | Partially filled | Empty |
| :--- | :---: | :---: | :---: | :---: |
| Container Spaces | 0.95 | 0.70 | 0.80 | 0.95 |
| Dry Cargo spaces | 0.95 | 0.70 | 0.80 | 0.95 |
| Ro-Ro spaces | 0.95 | 0.90 | 0.90 | 0.95 |
| Cargo liquids | 0.95 | 0.70 | 0.80 | 0.95 |
| Intended for consumable liquids | 0.95 | 0.95 | 0.95 | 0.95 |
| Stores | 0.95 | 0.60 | (0.60) | 0.95 |
| Occupied by machinery | | | 0.85 | |
| Void spaces | | | 0.95 | |
| Occupied by accommodation | | | 0.95 | |

4.2.4 The system shall be capable of accounting for applied moments such as wind, lifeboat launching, cargo shifts and passenger relocation.

4.2.5 The system shall account for the effect of wind by using the method in SOLAS regulation II-1/7-2.4.1.2 as the default, but allow for manual input of the wind speed/pressure if the on-scene pressure is significantly different ($$P = 120 \text{ N/m}^2$$ equates to Beaufort 6; approximately 13.8 m/s or 27 knots).

4.2.6 The system shall be capable of assessing the impact of open main watertight doors on stability (e.g. for each damage case provided for verification, additional damage stability calculation shall be done and presented, taking into account any watertight door located within the damaged compartment(s)).

4.2.7 The system shall utilize the latest approved lightship weight and centre of gravity information.

4.2.8 The output of the software is to be such that it provides the master with sufficient clear unambiguous information to enable quick and accurate assessment of the stability of the vessel for any actual damage, the impact of flooding on the means of escape and the controls of devices necessary for managing and/or controlling the stability of the ship.

When the actual loading condition is input in the SRtP software, the following output (intact stability) shall be available:
- deadweight data;
- lightship data;
- trim;
- heel;
- draft at the draft marks and perpendiculars;
- summary of loading condition displacement, VCG, LCG and, if applicable, TCG;
- downflooding angle and corresponding downflooding opening;
- free surfaces;
- GM value;
- GZ values relevant to an adequate range of heeling (not less than 60°) available indicatively at the following intervals: 0 5 10 15 20 25 30 40 50 60 deg;
- compliance with relevant intact stability criteria (i.e. 2008 IS Code): listing of all calculated intact stability criteria, the limiting values, the obtained values and the evaluation (criteria fulfilled or not fulfilled);
- GM/KG limiting curve according to SOLAS, Ch II-1, Regulation 5-1.

When the actual loading condition is associated to the actual damage case(s) due to the casualty, the following output (damage stability) shall be available:
- trim;
- heel;
- draft at the draft marks and perpendiculars;
- progressive flooding angle and corresponding progressive flooding openings;
- GM value;
- GZ values relevant to an adequate range of heeling (not less than 60°) available indicatively at the following intervals: 0 5 10 15 20 25 30 40 50 60 deg;
- compliance with stability criteria: listing of all calculated stability criteria, the limit values, the obtained values and the conclusions (criteria fulfilled or not fulfilled);
- the survivability criteria for Type 4 software (SRtP) are left to the discretion of the Administration;
- relevant flooding points (unprotected or weathertight) with the distance from the damage waterline to each point;
- list of all flooded compartments with the permeability considered;
- amount of water in each flooded compartment;
- escape route immersion angles;
- a profile view, deck views and cross-sections of the ship indicating the flooded water plane and the damaged compartments.

4.2.9 For ro-ro passenger ships there shall be algorithms in the software for estimating the effect of water accumulation on deck (WOD) (e.g. 1. In addition to the predefined significant wave height taken from the approved stability document, there shall be possibility for the crew to input manually the significant wave height of the ship navigation area in the system, 2. In addition to the predefined significant wave height taken from the approved stability document, calculations with two additional significant wave heights shall be submitted for checking the correctness of the algorithms in the software for estimating the effect of WOD).*

\* This paragraph applies to Ro-Ro Passenger ships subject to the Stockholm Agreement (IMO Circular Letter No. 1891)

### 5. Acceptable Tolerances

Depending on the type and scope of programs, the acceptable tolerances are to be determined differently, according to 5.1 or 5.2. Deviation from these tolerances shall not be accepted unless the Society considers that there is a satisfactory explanation for the difference and that there will be no adverse effect on the safety of the ship.

Examples of pre-programmed input data include the following:
- **Hydrostatic data:** Displacement, LCB, LCF, VCB, KMt and MCT versus draught.
- **Stability data:** KN or MS values at appropriate heel/ trim angles versus displacement, stability limits.
- **Compartment data:** Volume, LCG, VCG, TCG and FSM/ Grain heeling moments vs level of the compartment's contents.

Examples of output data include the following:
- **Hydrostatic data:** Displacement, LCB, LCF, VCB, KMt and MCT versus draught as well as actual draughts, trim.
- **Stability data:** FSC (free surface correction), GZ-values, KG, GM, KG/GM limits, allowable grain heeling moments, derived stability criteria, e.g. areas under the GZ curve, weather criteria.
- **Compartment data:** Calculated Volume, LCG, VCG, TCG and FSM/ Grain heeling moments vs level of the compartment's contents.

The computational accuracy of the calculation program results shall be within the acceptable tolerances, specified in 5.1 or 5.2, of the results using an independent program or the approved stability information with identical input.

5.1 Programs which use only pre-programmed data from the approved stability information as the basis for stability calculations, shall have zero tolerances for the printouts of input data.

Output data tolerances are to be close to zero, however, small differences associated with calculation rounding or abridged input data are acceptable.

Additionally differences associated with the use of hydrostatic and stability data for trims that differ from those in the approved stability information, are acceptable subject to review by the individual Society.

5.2 Programs which use hull form models as their basis for stability calculations, shall have tolerances for the printouts of basic calculated data established against either data from the approved stability information or data obtained using the approval authority's model. Acceptable tolerances shall be in accordance with Table 1.

#### Table 1

| Hull Form Dependent | |
| :--- | :--- |
| Displacement | +/- 2% |
| Longitudinal center of buoyancy, from AP | +/- 1% / 50 cm |
| Vertical center of buoyancy | +/- 1% / 5 cm |
| Transverse center of buoyancy | +/- 0.5% of B / 5 cm |
| Longitudinal center of flotation, from AP | +/- 1% / 50 cm |
| Moment to trim 1 cm | +/- 2% |
| Transverse metacentric height | +/- 1% / 5 cm |
| Longitudinal metacentric height | +/- 1% / 50 cm |
| Cross curves of stability | +/- 5 cm |
| **Compartment dependent** | |
| Volume or deadweight | +/- 2% |
| Longitudinal center of gravity, from AP | +/- 1% / 50 cm |
| Vertical centre of gravity | +/- 1% / 5 cm |
| Transverse center of gravity | +/- 0.5% of B / 5 cm |
| Free surface moment | +/- 2% |
| Shifting moment | +/- 5% |
| Level of contents | +/- 2% |
| **Trim and stability** | |
| Draughts (forward, aft, mean) | +/- 1% / 5 cm |
| GMt (both solid and corrected for free surfaces) | +/- 1% / 5 cm |
| GZ values | +/- 5% / 5 cm |
| Downflooding angle | +/- 2° |
| Equilibrium angles | +/- 1° |
| Distance from WL to unprotected and weathertight openings, or other relevant point, if applicable | +/- 5% / 5 cm |
| Areas under righting arm curve | +/- 5% / 0.0012 mrad |

**Notes:**

1. $$\text{Deviation in \%} = \left\{ \frac{\text{base value} - \text{applicant's value}}{\text{base value}} \right\} \times 100$$
   Where the "base value" may be from the approved stability information or the society's computer model.
2. When applying the tolerances in Table 1 having two values, the allowable tolerance is the greater of the two values.
3. Where differences in calculation methodology exist between the programs used in the comparison, this may be a basis for accepting deviations greater than that specified in Table 1 provided a software examination is carried out in sufficient detail to clearly document that such differences are technically justifiable.
4. Deviation from these tolerances shall not be accepted unless the Society considers that there is a satisfactory explanation for the difference and that it is clearly evident from the Society's stability calculations that the deviation does not impact compliance with the required stability criteria for the ship under consideration.

### 6. Approval Procedure

**Conditions of approval of the onboard software for stability calculations**

The onboard software used for stability calculations is subject to approval, which is to include;
- verification of type approval, if any;
- verification that the data used is consistent with the current condition of the ship. (Refer to paragraph 6.2);
- verification and approval of the test conditions;
- verification that the software is appropriate for the type of ship and stability calculations required;
- verification of functional requirements under paragraph 4.1.2.

The satisfactory operation of the software with the onboard computer(s) for stability calculations is to be verified by testing upon installation. (Refer to paragraph 8). A copy of the approved test conditions and the operation manual for the computer/ software are to be available on board.

#### 6.1 General Approval (optional):

Upon application to the Society for general approval of the calculation program, the Society may provide the applicant with test data consisting of two or more design data sets, each of which is to include a ship's hull form data, compartmentation data, lightship characteristics and deadweight data, in sufficient detail to accurately define the ship and it's loading condition. Acceptable hull form and compartmentation data may be in the form of surface coordinates for modeling the hull form and compartment boundaries, e.g: a table of offsets, or in the form of pre-calculated tabular data, e.g: hydrostatic tables, capacity tables, etc., depending upon the form of data used by the software being submitted for approval. Alternatively, the general approval may be given based on at least two test ships agreed upon between the society and the applicant.

In general, the software is to be tested for two types of ships for which approval is requested, with at least one design data set for each of the two types. Where approval is requested for only one type of ship, a minimum of two data sets for different hull forms of that type of ship are required to be tested. For calculation software which is based on the input of hull form data, design data sets shall be provided for three types of ships for which the software is to be approved, or a minimum of three data sets for different hull forms, if approval is requested for only one type of ship. Representative ship types which require different design data sets due to their hull forms, typical arrangements, and nature of cargo include: tanker, bulk carrier, container ship, and other dry cargo and passenger ships. The test data sets shall be used by the applicant to run the calculation program for the test ships. The results obtained (together with the hydrostatic data and cross-curve data developed by the program, if appropriate) shall be submitted to the Society for the assessment of the program's computational accuracy. The Society shall perform parallel calculations using the same data sets and a comparison of these results will be made against the applicant's submitted program's results.

#### 6.2 Specific Approval:

- The Society shall verify the accuracy of the computational results and actual ship data used by the calculation program for the particular ship on which the program will be installed.
- Upon application to the Society for data verification, the Society and the applicant shall agree on a minimum of four loading conditions, taken from the ship's approved stability information, which are to be used as the test conditions. For ships carrying liquids in bulk, at least one of the conditions shall include partially filled tanks. For ships carrying grain in bulk, one of the grain loading conditions shall include a partially filled grain compartment. Within the test conditions each compartment shall be loaded at least once. The test conditions normally are to cover the range of load draughts from the deepest envisaged loaded condition to the light ballast condition and shall include at least one departure and one arrival condition.

For Type 4 stability software for SRtP, the Society shall examine at least three damage cases, each of them associated with at least three loading conditions taken from the ship's approved stability information. Output of the software is to be compared with results of corresponding load / damage case in the approved damage stability booklet or an alternative independent software source.

- The Society is to verify that the following data, submitted by the applicant, is consistent with arrangements and most recently approved lightship characteristics of the ship according to current plans and documentation on file with the Society, subject to possible further verification on board:
  - Identification of the calculation program including version number;
  - Main dimensions, hydrostatic particulars and, if applicable, the ship profile;
  - The position of the forward and after perpendiculars, and if appropriate, the calculation method to derive the forward and after draughts at the actual position of the ship's draught marks;
  - Ship lightweight and centre of gravity derived from the most recently approved inclining experiment or light weight check;
  - Lines plan, offset tables or other suitable presentation of hull form data if necessary for the Society to model the ship;
  - Compartment definitions, including frame spacing, and centres of volume, together with capacity tables (sounding/ullage tables), free surface corrections, if appropriate;
  - Cargo and Consumables distribution for each loading condition.

Verification by the Society does not absolve the applicant and shipowner of responsibility for ensuring that the information programmed into the onboard computer software is consistent with the current condition of the ship.

### 7. Operation Manual

A simple and straightforward operation manual is to be provided, containing descriptions and instructions, as appropriate, for at least the following:
- installation
- function keys
- menu displays
- input and output data
- required minimum hardware to operate the software
- use of the test loading conditions
- computer-guided dialogue steps
- list of warnings

### 8. Installation Testing

To ensure correct working of the computer after the final or updated software has been installed, it is the responsibility of the ship's Master to have test calculations carried out according to the following pattern in the presence of a Society surveyor:

From the approved test conditions at least one load case (other than light ship) shall be calculated. Note: Actual loading condition results are not suitable for checking the correct working of the computer.

Normally, the test conditions are permanently stored in the computer.

Steps to be performed:
- Retrieve the test load case and start a calculation run; compare the stability results with those in the documentation.
- Change several items of deadweight (tank weights and the cargo weight) sufficiently to change the draught or displacement by at least 10%. The results are to be reviewed to ensure that they differ in a logical way from those of the approved test condition.
- Revise the above modified load condition to restore the initial test condition and compare the results. Confirm that the relevant input and output data of the approved test condition have been replicated.
- Alternatively, one or more test conditions shall be selected and the test calculation performed by entering all deadweight data for each selected test condition into the program as if it were a proposed loading. The results shall be verified as identical to the results in the approved copy of the test conditions.

### 9. Periodical Testing

It is the responsibility of the ship's master to check the accuracy of the onboard computer for stability calculations at each Annual Survey by applying at least one approved test condition. If a Society surveyor is not present for the computer check, a copy of the test condition results obtained by the computer check is to be retained on board as documentation of satisfactory testing for the surveyor's verification.

At each Special Survey this checking for all approved test loading conditions is to be done in presence of the surveyor.

The testing procedure shall be carried out in accordance with paragraph 8.

### 10. Other Requirements

Protection against unintentional or unauthorised modification of programs and data shall be provided.

The program shall monitor operation and activate an alarm when the program is incorrectly or abnormally used.

The program and any data stored in the system shall be protected from corruption by loss of power.

Error messages with regard to limitations such as filling a compartment beyond capacity, or exceeding the assigned load line, etc. shall be included.

**End of Document**
