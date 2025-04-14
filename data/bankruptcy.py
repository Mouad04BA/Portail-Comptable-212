"""
Bankruptcy filing process and FAQ data for Morocco
"""

def get_filing_process():
    """
    Returns the bankruptcy filing process steps
    """
    filing_process = [
        {
            "step": 1,
            "title": "Assess Financial Situation",
            "description": "Conduct a thorough assessment of the company's financial situation to determine if bankruptcy is the appropriate solution.",
            "details": """
                <p>Before initiating bankruptcy proceedings, it's essential to perform a comprehensive assessment of the company's financial health. This involves:</p>
                <ul>
                    <li>Reviewing all financial statements (balance sheet, income statement, cash flow)</li>
                    <li>Analyzing debt structure and repayment capabilities</li>
                    <li>Evaluating potential for financial recovery</li>
                    <li>Consulting with financial advisors and legal counsel</li>
                </ul>
                <p>This assessment will help determine whether bankruptcy is necessary or if alternative solutions might be viable, such as restructuring, debt negotiation, or merger opportunities.</p>
            """
        },
        {
            "step": 2,
            "title": "Select Appropriate Procedure",
            "description": "Determine the most suitable bankruptcy procedure based on the company's situation: safeguard procedure, judicial reorganization, or judicial liquidation.",
            "details": """
                <p>Under Moroccan law, there are three main bankruptcy procedures:</p>
                <ol>
                    <li><strong>Safeguard Procedure (Procédure de Sauvegarde):</strong> For companies that are not yet in payment default but facing difficulties that they cannot overcome alone. This preventive measure allows the business to continue operations while restructuring debt.</li>
                    <li><strong>Judicial Reorganization (Redressement Judiciaire):</strong> For companies that are unable to pay their debts but whose situation is not irreversibly compromised. This procedure aims to enable the continuation of business activities, maintain employment, and settle liabilities.</li>
                    <li><strong>Judicial Liquidation (Liquidation Judiciaire):</strong> For companies whose situation is irreversibly compromised. This procedure entails ceasing business activities and selling assets to pay creditors.</li>
                </ol>
                <p>The choice between these procedures depends on the company's financial situation, viability prospects, and specific circumstances.</p>
            """
        },
        {
            "step": 3,
            "title": "File a Petition",
            "description": "Prepare and submit the bankruptcy petition to the Commercial Court in the company's jurisdiction.",
            "details": """
                <p>Filing a bankruptcy petition requires careful preparation of specific documents:</p>
                <ul>
                    <li>Formal petition request signed by the legal representative or authorized agent</li>
                    <li>Certificate of registration in the Commercial Register (less than 3 months old)</li>
                    <li>Copy of company bylaws and amendments</li>
                    <li>Financial statements for the last three fiscal years</li>
                    <li>Statement of assets and liabilities</li>
                    <li>Cash flow statement for the last six months</li>
                    <li>List of creditors with amounts owed and payment due dates</li>
                    <li>List of employees with their positions and seniority</li>
                    <li>Inventory of company property and assets</li>
                    <li>Detailed explanation of the financial difficulties and their causes</li>
                </ul>
                <p>The petition must be filed with the clerk of the Commercial Court in the jurisdiction where the company's headquarters is located. The filing fee must be paid at the time of submission.</p>
            """
        },
        {
            "step": 4,
            "title": "Court Examination",
            "description": "The Commercial Court examines the petition and decides whether to open bankruptcy proceedings.",
            "details": """
                <p>After the petition is filed, the court examines it to determine if the company meets the legal criteria for bankruptcy proceedings:</p>
                <ol>
                    <li>The court will schedule an initial hearing, typically within 15 days of filing</li>
                    <li>During this hearing, the company's representative must appear before the judge to explain the financial situation</li>
                    <li>The judge may request additional information or documents to properly assess the case</li>
                    <li>The court will verify that the company is indeed in a state of cessation of payments or facing insurmountable difficulties</li>
                    <li>Based on this assessment, the court will decide whether to open bankruptcy proceedings and which procedure is appropriate</li>
                </ol>
                <p>If the court opens proceedings, it will issue a judgment that specifies the type of procedure (safeguard, reorganization, or liquidation) and appoint the necessary officials to oversee the process.</p>
            """
        },
        {
            "step": 5,
            "title": "Appointment of Officials",
            "description": "The court appoints an insolvency judge, a trustee, and possibly a creditors' representative.",
            "details": """
                <p>When bankruptcy proceedings are opened, the court appoints several officials to manage the process:</p>
                <ul>
                    <li><strong>Insolvency Judge (Juge-Commissaire):</strong> Oversees the proceedings, ensures compliance with legal requirements, and resolves disputes that may arise during the process</li>
                    <li><strong>Trustee (Syndic):</strong> Manages the company's operations during the proceedings, prepares an inventory of assets, verifies creditors' claims, and implements the recovery plan or liquidation</li>
                    <li><strong>Creditors' Representative (Représentant des Créanciers):</strong> In larger cases, represents the interests of creditors throughout the proceedings</li>
                    <li><strong>Employee Representative (Représentant des Salariés):</strong> May be appointed to represent employee interests, particularly regarding unpaid wages and potential layoffs</li>
                </ul>
                <p>These officials play crucial roles in ensuring the bankruptcy process is conducted fairly and in accordance with legal requirements, while balancing the interests of all stakeholders.</p>
            """
        },
        {
            "step": 6,
            "title": "Observation Period",
            "description": "In case of judicial reorganization, an observation period begins to assess the company's viability and prepare a recovery plan.",
            "details": """
                <p>The observation period is a critical phase in judicial reorganization proceedings, typically lasting 4 months initially, with possible extensions up to 12 months in total. During this period:</p>
                <ol>
                    <li>The trustee conducts a thorough analysis of the company's economic, social, and environmental situation</li>
                    <li>The business continues to operate under supervision, with certain restrictions on management actions</li>
                    <li>An inventory of assets and verification of creditors' claims is performed</li>
                    <li>Debts incurred prior to the opening of proceedings are frozen (stay of proceedings)</li>
                    <li>New financing may be sought to support operations during this period</li>
                    <li>A recovery plan is developed, which may include:
                        <ul>
                            <li>Business restructuring measures</li>
                            <li>Debt rescheduling or reduction</li>
                            <li>Potential sale of certain assets</li>
                            <li>Staffing adjustments</li>
                        </ul>
                    </li>
                </ol>
                <p>At the end of the observation period, the court will decide whether to approve a recovery plan, convert the proceedings to liquidation, or terminate the proceedings if the company's situation has sufficiently improved.</p>
            """
        },
        {
            "step": 7,
            "title": "Creditors' Claims",
            "description": "Creditors must submit their claims within two months of the publication of the judgment.",
            "details": """
                <p>The claims submission process is strictly regulated and time-sensitive:</p>
                <ul>
                    <li>All creditors must submit their claims to the trustee within two months from the publication of the judgment in the official bulletin (for local creditors) or four months (for foreign creditors)</li>
                    <li>Claims must be submitted using official forms and include supporting documentation</li>
                    <li>Required information includes:
                        <ul>
                            <li>Creditor's identity and contact information</li>
                            <li>Amount of the claim</li>
                            <li>Due date</li>
                            <li>Any securities or guarantees attached to the claim</li>
                            <li>Supporting documents (contracts, invoices, etc.)</li>
                        </ul>
                    </li>
                    <li>The trustee verifies each claim and may accept it, reject it, or classify it as disputed</li>
                    <li>A list of accepted claims is prepared and submitted to the insolvency judge</li>
                    <li>Disputed claims are subject to court resolution</li>
                    <li>Creditors whose claims are rejected can file an appeal within 30 days</li>
                </ul>
                <p>Failure to submit claims within the prescribed timeframe may result in creditors being barred from participating in the distribution of assets, except in cases where the court grants relief from the deadline for valid reasons.</p>
            """
        },
        {
            "step": 8,
            "title": "Recovery Plan or Liquidation",
            "description": "The court decides whether to approve a recovery plan or proceed with liquidation.",
            "details": """
                <p>Based on the analysis conducted during the observation period, the court will make one of the following decisions:</p>
                
                <h4>Recovery Plan (Plan de Continuation)</h4>
                <p>If the company is deemed viable, a recovery plan may be approved, which typically includes:</p>
                <ul>
                    <li>Restructuring measures to restore profitability</li>
                    <li>Debt repayment schedule, potentially with reductions in amounts</li>
                    <li>Operating changes to improve efficiency</li>
                    <li>Employment adjustments</li>
                    <li>Monitoring mechanisms to ensure plan implementation</li>
                </ul>
                <p>The plan typically spans 3-10 years and is binding on all creditors.</p>
                
                <h4>Liquidation</h4>
                <p>If recovery is not possible, the court will order judicial liquidation, which involves:</p>
                <ul>
                    <li>Cessation of business operations</li>
                    <li>Sale of all company assets</li>
                    <li>Distribution of proceeds to creditors according to their rank</li>
                    <li>Dissolution of the company</li>
                </ul>
                
                <h4>Partial Transfer Plan (Plan de Cession)</h4>
                <p>In some cases, the court may approve a partial transfer plan, where:</p>
                <ul>
                    <li>Part of the business is sold to a third party as a going concern</li>
                    <li>The proceeds are used to pay creditors</li>
                    <li>The remainder of the business may be liquidated</li>
                </ul>
                
                <p>The court's decision is based on which option provides the best outcome for preserving employment, satisfying creditors, and maintaining economic activity.</p>
            """
        },
        {
            "step": 9,
            "title": "Implementation and Monitoring",
            "description": "Implementation of the recovery plan or liquidation process, with monitoring by court-appointed officials.",
            "details": """
                <p>Once the court has decided on recovery or liquidation, the implementation phase begins:</p>
                
                <h4>For Recovery Plans</h4>
                <ul>
                    <li>The trustee or a court-appointed administrator oversees implementation</li>
                    <li>Regular reports must be submitted to the court on plan progress</li>
                    <li>Creditors receive payments according to the approved schedule</li>
                    <li>The company must adhere to all operational changes specified in the plan</li>
                    <li>Failure to comply with the plan may result in its termination and conversion to liquidation</li>
                    <li>Successful implementation leads to the company returning to normal operations</li>
                </ul>
                
                <h4>For Liquidation</h4>
                <ul>
                    <li>The liquidator catalogs and values all company assets</li>
                    <li>Assets are sold through public auctions or private sales as authorized by the court</li>
                    <li>Proceeds are distributed to creditors according to the legally established priority:
                        <ol>
                            <li>Secured creditors (for the assets on which they hold security)</li>
                            <li>Employee claims for unpaid wages (limited to last 6 months)</li>
                            <li>Court costs and expenses related to the proceedings</li>
                            <li>Tax authorities</li>
                            <li>Social security institutions</li>
                            <li>Unsecured creditors</li>
                        </ol>
                    </li>
                    <li>Final accounts are prepared and submitted to the court</li>
                    <li>The court issues a judgment closing the liquidation</li>
                </ul>
                
                <p>Throughout implementation, the insolvency judge continues to oversee the process and resolve any disputes that arise.</p>
            """
        },
        {
            "step": 10,
            "title": "Closure of Proceedings",
            "description": "The bankruptcy proceedings are closed either upon successful implementation of the recovery plan or completion of liquidation.",
            "details": """
                <p>The bankruptcy proceedings are formally concluded through a court judgment in one of the following scenarios:</p>
                
                <h4>For Recovery Plans</h4>
                <ul>
                    <li>When all obligations under the plan have been fulfilled</li>
                    <li>When the plan period has concluded (typically 3-10 years)</li>
                    <li>The judgment closing the proceedings removes court supervision</li>
                    <li>The company returns to normal operations</li>
                </ul>
                
                <h4>For Liquidation</h4>
                <ul>
                    <li>When all assets have been realized and distributed</li>
                    <li>When further proceedings are not possible due to insufficient assets</li>
                    <li>The judgment includes the dissolution of the company</li>
                    <li>Corporate registration is canceled</li>
                </ul>
                
                <h4>Legal Consequences of Closure</h4>
                <ul>
                    <li>Debts not discharged during the proceedings may remain enforceable against the debtor, depending on the circumstances</li>
                    <li>If the court determines mismanagement contributed to the bankruptcy, directors may face personal liability</li>
                    <li>In cases of fraudulent bankruptcy, criminal penalties may apply</li>
                    <li>Records of the bankruptcy proceedings remain in public registries for a period determined by law</li>
                </ul>
                
                <p>The closure judgment marks the end of the collective proceedings, though individual legal actions may continue in certain cases, particularly if fraud or mismanagement is discovered after the proceedings have closed.</p>
            """
        }
    ]
    
    return filing_process

def get_faq():
    """
    Returns frequently asked questions about bankruptcy in Morocco
    """
    faq = [
        {
            "question": "What is the difference between safeguard procedure, judicial reorganization, and judicial liquidation?",
            "answer": """
                <p>The three main bankruptcy procedures in Morocco differ primarily in the financial condition of the company and the objectives:</p>
                <ul>
                    <li><strong>Safeguard Procedure (Procédure de Sauvegarde):</strong> A preventive measure for companies facing difficulties but not yet in default. The company continues normal operations while reorganizing debts. Management remains in place, supervised by a court-appointed administrator.</li>
                    <li><strong>Judicial Reorganization (Redressement Judiciaire):</strong> For companies unable to pay debts but with potential for recovery. Business continues under supervision with the aim of implementing a recovery plan. Management may be restricted or replaced.</li>
                    <li><strong>Judicial Liquidation (Liquidation Judiciaire):</strong> For companies with irreversibly compromised situations. Operations cease, assets are sold, and proceeds are distributed to creditors according to priority rules.</li>
                </ul>
                <p>The key difference is that safeguard is initiated before payment default, while reorganization and liquidation occur after payment default, with reorganization focusing on recovery and liquidation on asset distribution.</p>
            """
        },
        {
            "question": "Who can initiate bankruptcy proceedings in Morocco?",
            "answer": """
                <p>Bankruptcy proceedings in Morocco can be initiated by several parties:</p>
                <ul>
                    <li><strong>The Company:</strong> Through its legal representative (typically the manager or board of directors)</li>
                    <li><strong>Creditors:</strong> Any creditor can request judicial reorganization or liquidation for a debtor in default</li>
                    <li><strong>The Public Prosecutor:</strong> If public interest requires it</li>
                    <li><strong>The Court:</strong> The Commercial Court can initiate proceedings on its own motion in certain circumstances</li>
                </ul>
                <p>It's important to note that only the company itself can initiate safeguard procedures, while judicial reorganization or liquidation can be initiated by any of the parties listed above.</p>
                <p>The legal representative of a company is legally obligated to file for bankruptcy within 30 days of cessation of payments. Failure to do so can result in personal liability.</p>
            """
        },
        {
            "question": "What is the timeframe for bankruptcy proceedings in Morocco?",
            "answer": """
                <p>The duration of bankruptcy proceedings varies depending on the procedure and complexity:</p>
                <ul>
                    <li><strong>Initial Court Decision:</strong> Typically within 15-30 days of filing</li>
                    <li><strong>Observation Period (for reorganization):</strong> Initially 4 months, extendable up to 12 months in total</li>
                    <li><strong>Claims Submission:</strong> 2 months for local creditors, 4 months for foreign creditors</li>
                    <li><strong>Recovery Plan Implementation:</strong> Usually spans 3-10 years</li>
                    <li><strong>Liquidation:</strong> Typically 1-3 years, but can take longer for complex cases</li>
                </ul>
                <p>Several factors can affect the duration, including the company size, number of creditors, complexity of assets, and whether litigation arises during the proceedings. Courts generally aim to process cases efficiently, but the primary goal is to ensure proper treatment of all stakeholders' interests.</p>
            """
        },
        {
            "question": "How are employees affected by bankruptcy proceedings?",
            "answer": """
                <p>Employees have special protections during bankruptcy proceedings in Morocco:</p>
                <ul>
                    <li><strong>Priority Claims:</strong> Unpaid wages for the last six months have priority in payment over most other creditors</li>
                    <li><strong>Employment Contracts:</strong> 
                        <ul>
                            <li>In safeguard and reorganization, employment contracts continue unless specifically modified as part of the recovery plan</li>
                            <li>In liquidation, contracts are terminated, but with specific protections and notice requirements</li>
                        </ul>
                    </li>
                    <li><strong>Representation:</strong> An employee representative may be appointed to participate in proceedings</li>
                    <li><strong>Social Insurance Fund:</strong> The CNSS (Caisse Nationale de Sécurité Sociale) may provide compensation for certain unpaid wages when the company cannot pay</li>
                    <li><strong>Consultation Requirements:</strong> Any mass layoffs must follow specific legal procedures, including consultation with employee representatives</li>
                </ul>
                <p>Employees should promptly submit claims for any unpaid wages through the designated trustee to ensure their rights are protected.</p>
            """
        },
        {
            "question": "Can directors and managers be held personally liable in bankruptcy cases?",
            "answer": """
                <p>Yes, directors and managers can face personal liability in certain bankruptcy situations:</p>
                <ul>
                    <li><strong>Action for Liability of Assets (Action en Responsabilité pour Insuffisance d'Actif):</strong> If mismanagement contributed to insufficient assets, directors may be ordered to pay all or part of the company's debts</li>
                    <li><strong>Extension of Proceedings:</strong> Courts can extend bankruptcy proceedings to directors who have:
                        <ul>
                            <li>Used company assets as personal property</li>
                            <li>Conducted business in their personal interest under the company name</li>
                            <li>Diverted company assets or artificially increased liabilities</li>
                        </ul>
                    </li>
                    <li><strong>Prohibition from Managing:</strong> Directors found responsible for company failure may be prohibited from managing any commercial enterprise for up to 15 years</li>
                    <li><strong>Criminal Liability:</strong> In cases of fraudulent bankruptcy, directors may face criminal charges with penalties including imprisonment and fines</li>
                </ul>
                <p>Proper documentation of decision-making processes and strict compliance with legal obligations are essential for directors to protect themselves from personal liability.</p>
            """
        },
        {
            "question": "What happens to ongoing contracts when a company enters bankruptcy?",
            "answer": """
                <p>The treatment of ongoing contracts depends on the type of bankruptcy procedure:</p>
                <ul>
                    <li><strong>Automatic Continuation:</strong> Generally, ongoing contracts continue despite the opening of bankruptcy proceedings, unless specific termination clauses apply</li>
                    <li><strong>Trustee's Option:</strong> The court-appointed trustee has the right to:
                        <ul>
                            <li>Request the continuation of contracts deemed necessary for company operations</li>
                            <li>Terminate contracts if continuation is not in the company's interest</li>
                        </ul>
                    </li>
                    <li><strong>Protections Against Termination:</strong> Contractual clauses that automatically terminate contracts due to bankruptcy filing are generally unenforceable</li>
                    <li><strong>Special Contracts:</strong> Some contracts have specific treatment:
                        <ul>
                            <li>Employment contracts (as discussed in a previous question)</li>
                            <li>Lease agreements have special continuation rights</li>
                            <li>Public procurement contracts may have specific provisions</li>
                        </ul>
                    </li>
                </ul>
                <p>Counterparties to contracts with a company in bankruptcy should seek legal advice regarding their rights and obligations, as improper termination or continuation may have legal consequences.</p>
            """
        },
        {
            "question": "How are secured creditors treated in Moroccan bankruptcy proceedings?",
            "answer": """
                <p>Secured creditors receive preferential treatment in Moroccan bankruptcy proceedings:</p>
                <ul>
                    <li><strong>Priority in Payment:</strong> Secured creditors have priority over unsecured creditors for the assets on which they hold security</li>
                    <li><strong>Types of Security:</strong> Recognized securities include:
                        <ul>
                            <li>Mortgages on real estate</li>
                            <li>Pledges on business assets</li>
                            <li>Pledges on specific equipment</li>
                            <li>Security interests in receivables</li>
                        </ul>
                    </li>
                    <li><strong>During Observation Period:</strong> 
                        <ul>
                            <li>Enforcement of security is suspended (stay of proceedings)</li>
                            <li>Interest continues to accrue on secured debts (unlike unsecured debts)</li>
                        </ul>
                    </li>
                    <li><strong>In Recovery Plans:</strong> Secured creditors may receive more favorable treatment than unsecured creditors</li>
                    <li><strong>In Liquidation:</strong> Secured creditors are paid from the proceeds of their collateral before unsecured creditors</li>
                </ul>
                <p>Despite these protections, secured creditors must still file their claims within the legal timeframe and participate in the proceedings to preserve their rights.</p>
            """
        },
        {
            "question": "Can a bankruptcy filing be rejected by the court?",
            "answer": """
                <p>Yes, a bankruptcy filing can be rejected by the court for several reasons:</p>
                <ul>
                    <li><strong>Insufficient Evidence of Cessation of Payments:</strong> For judicial reorganization or liquidation, the court must verify that the company is actually unable to pay its debts as they become due</li>
                    <li><strong>Incomplete Documentation:</strong> If the required documents are not provided or are insufficient</li>
                    <li><strong>Bad Faith Filing:</strong> If the court determines the filing is primarily to evade obligations rather than address genuine financial difficulties</li>
                    <li><strong>Insufficient Assets:</strong> In some cases, if the company has virtually no assets to cover even the basic costs of proceedings</li>
                    <li><strong>For Safeguard Procedures:</strong> If the company is already in default on payments (in which case judicial reorganization would be appropriate instead)</li>
                </ul>
                <p>If a filing is rejected, the company or creditor may appeal the decision or file a new petition addressing the deficiencies identified by the court. It's crucial to prepare thorough documentation and demonstrate genuine financial distress to avoid rejection.</p>
            """
        },
        {
            "question": "What is the role of the trustee in bankruptcy proceedings?",
            "answer": """
                <p>The trustee (syndic) plays a central role in Moroccan bankruptcy proceedings:</p>
                <ul>
                    <li><strong>Company Management:</strong> 
                        <ul>
                            <li>In safeguard procedures, supervises management actions</li>
                            <li>In judicial reorganization, may be granted partial or complete management authority</li>
                            <li>In liquidation, replaces management entirely</li>
                        </ul>
                    </li>
                    <li><strong>Asset Inventory:</strong> Creates a comprehensive inventory of all company assets</li>
                    <li><strong>Creditor Claims:</strong> 
                        <ul>
                            <li>Receives and verifies creditor claims</li>
                            <li>Creates the list of admitted and rejected claims</li>
                            <li>Participates in resolution of disputed claims</li>
                        </ul>
                    </li>
                    <li><strong>Recovery Plan:</strong> 
                        <ul>
                            <li>Assists in developing feasible recovery plans</li>
                            <li>Reports on company viability</li>
                            <li>Monitors implementation of approved plans</li>
                        </ul>
                    </li>
                    <li><strong>Liquidation:</strong> Manages the sale of assets and distribution of proceeds</li>
                    <li><strong>Reporting:</strong> Provides regular reports to the court on proceedings status</li>
                    <li><strong>Legal Actions:</strong> May initiate legal actions to void fraudulent transactions or recover assets</li>
                </ul>
                <p>The trustee is an independent professional, typically an accountant or lawyer, appointed by the court. Their fees are paid from the company's assets as priority expenses of the proceedings.</p>
            """
        },
        {
            "question": "Can transactions made before bankruptcy be canceled?",
            "answer": """
                <p>Yes, certain transactions made before bankruptcy can be voided or "clawed back" through legal actions:</p>
                <ul>
                    <li><strong>Suspect Period (Période Suspecte):</strong> Transactions made during the period between the date of cessation of payments (as determined by the court) and the judgment opening proceedings are subject to greater scrutiny</li>
                    <li><strong>Automatically Void Transactions:</strong> Regardless of the counterparty's knowledge, the following are automatically void:
                        <ul>
                            <li>Gratuitous transfers of assets</li>
                            <li>Contracts with significantly imbalanced obligations favoring the counterparty</li>
                            <li>Payments for debts not yet due</li>
                            <li>Payments made through unusual means (not in the ordinary course of business)</li>
                            <li>Security interests granted for previously unsecured debts</li>
                        </ul>
                    </li>
                    <li><strong>Optionally Void Transactions:</strong> The court may void other transactions if the counterparty knew of the company's cessation of payments</li>
                    <li><strong>Extended Lookback Period:</strong> Certain transactions can be challenged up to 18 months before the bankruptcy filing</li>
                </ul>
                <p>These provisions aim to ensure fair treatment of all creditors and prevent preferential treatment or asset dissipation before bankruptcy. Parties who received payments or assets that are subsequently voided must return them to the company's estate.</p>
            """
        }
    ]
    
    return faq
