**Requirements: Production Operations Control System**

**1. Core Problem**

Production teams manage multiple concurrent orders across various suppliers. Dependencies span product approvals, packaging, materials, quality inspections, production timelines, and logistics. Currently, this information is distributed across static trackers and disjointed communications, causing teams to react to bottlenecks only after they have already impacted the timeline.

**2. Core Objective**

Answer questions instantly: 

1. What is at risk?
2. Why is it at risk?
3. What needs action now?

**3. Target Users & Needs**

- Production Coordinator: "What specific actions do I need to chase today?" (Focus: Daily task execution)

- Production Manager: "Which orders are at risk and why?" (Focus: Bottleneck resolution and supplier management)

- Leadership: "What is the overall production health and exposure?" (Focus: Macro risk and volume at risk)

**4. Key Features & Business Logic**

The system will shift from status tracking to active decision-support using a rule-based risk engine.

**Risk Drivers & Weighting:**

*   Inspection failed: +40
*   Material late: +30
*   Approval overdue: +25
*   Production behind schedule: +20
*   Packaging incomplete: +15
*   Shipment unbooked: +10

**Risk Categories:**

* CRITICAL (80–100):** Immediate intervention required; high probability of missed ex-factory date.
* HIGH (50–79):** Significant delay risk; requires manager visibility and mitigation plan.
* MEDIUM (25–49):** Early warning indicators; coordinator must chase dependencies.
* LOW (0–24):** On track; standard monitoring.

**5. Required Outputs**

1.  Prioritized Action Queue: An automated, ranked list of orders requiring intervention, including the specific risk reason and assigned action owner.
2.  Operations Dashboard: A visual interface showing total active orders, units at risk, risk by supplier, and risk by operational stage.

**6. Out of Scope (V1)**

*   Predictive machine learning models.
*   Live API connections to supplier ERPs (using flat-file data ingestion for V1).
*   Automated email alerts.
