import re


# ============================================================================================== #
# -------------------------------------- General feature --------------------------------------- #

TOKEN = r"(\S+)"
NOT = r"(\b(not|n't)_\S+)"
BE = r"(\b(am|is|are|was|were|be|being|been| 'm| 're)_\S+)"
LINKING_V = rf"({BE}|\b(become|became|becoming|seem|grow|grew|grown|look|prove|proving|remain|smell|sound|taste|tasting|turn|get|got|gotten|getting|appear|feel|felt)(s|end|ing)?_\S+)"
HAVE = r"(\b(have|has|had|having| 've| 'd|hath)_\S+)"
DO = r"(\b(do|does|did)_\S+)"
MODAL = r"(\S+_MD)"
AUX = rf"({BE}|{HAVE}|{DO}|{MODAL}| 's_VB\S?)"
ADV = r"(\S+_RB)"
ADJ = r"(\S+_JJ\S?)"
VERB = r"(\S+_VB\S?)"
NOUN = r"(\S+_NN\S?\S?)"
DEM = r"(\b(this|those|these)_\S+|that_DT)"
ART = r"\b(an?_\S+|the_\S+)"
NMOD = rf"(\S+_P?DT|\S+PRP$|\S+JJ\S?|\S+CD|{ART})"
QUANPRP = r"(\b(everybody|somebody|anybody|everyone|someone|anyone|everything|something|anything)_\S+)"
SUBPRP = rf"(\b(i|we|he|she|they|you|it)_\S+|{DEM})"
OBJPRP = rf"(\b(me|us|him|her|them|you|it)_\S+|{DEM})"
SUBJ = rf"({ART}?\s?{NMOD}?\s?{NOUN}|{SUBPRP})"
OBJ = rf"({ART}?\s?{NMOD}?\s?{NOUN}|{OBJPRP})"
CC = r"(\b(and|or)_\S+)"
WHP = rf"(\b(who|whom|which|whose_\S+ {NMOD}?\s?{NOUN})_\S+)"
WHO = r"(\b(what|where|when|how|whether|why|whoever|whomever|whichever|wherever|whenever|whatever|however)_\S+)"
PREP = r"(\b(against|amid|amidst|among|amongst|at|besides|between|by|despite|during|except|for|from|in|into|minus|notwithstanding|of|off|on|onto|opposite|out|per|plus|pro| re|than|through|throughout|thru|toward|towards|upon|versus|via|with|within|without)_\S+|to_IN)"

# -------------------------------------- Structural pattern --------------------------------------- #
SIX_LETTER_WORD_N_LONGER = r"(\S{6,}(?=_\S+))"


# ------------------------------------ Conversational pattern ------------------------------------- #
CONTRACTION = r"(n't| '\S\S?)_[^P]\S+"


# --------------------------------------- Sentential pattern ---------------------------------------- #
# passive voice
BY_PASSIVE = rf"({BE}| 's_V\S+) ({NOT}|{ADV})?\s?{SUBJ}?\s?({ADV}|{NOT})?\s?(\S+_VBN) by_\S+"
AGENTLESS_PASSIVE = rf"{BE} ({NOT}|{ADV})?\s?{SUBJ}?\s?({ADV}|{NOT})?\s?(\S+_VBN)(?= \b(?:(?!by_)\S)+)"

# Tense
PAST_TENSE = r"(\S+_VBD)"
PERFECT_ASPECT = rf"{HAVE} ({NOT}|{ADV})?\s?{SUBJ}?\s?({NOT}|{ADV})?\s?\S+_VB[ND]"
NON_PAST_TENSE = r"( \S+_VB[PZ]?)"
PROGESSIVE_TENSE = rf"({BE}| 's_V\S+) ({NOT}|{ADV})?\s?{SUBJ}?\s?({NOT}|{ADV})?\s?(\S+_VBG)"


# Split structure
SPLIT_AUX = rf"{AUX} {NOT}?\s?{ADV} {ADV}?\s?{VERB}"

# Coordination
PHRASAL_COORD = rf"{ADJ}(=? {CC} {ADJ})|{NOUN}(?= {CC} {NOUN})|{VERB}(?= {CC} {VERB})|{ADV}(?= {CC} {ADV})"
IND_CLAUSE_COORD = fr"{CC} ({ADV}|\S+_IN)?\s?({SUBPRP}|\S+_EX|{WHO}|{WHP}) ({ADV})?\s?({AUX}\s?{NOT}?|{ADV})?\s?({AUX}|{VERB})"

# WH structure
WH_QUESTION = rf"{WHO} {AUX} ({NOT}|{ADV})?\s?({NOT}|{ADV})?\s?{SUBJ}"
WH_CLAUSE = rf"{WHO} (?:(?!{AUX})\S)+|what_\S+ ({AUX}\s?{NOT}?|{ADV})?\s?{ADV}?\s?{VERB} {NOT}?\s?\b(?:(?!{SUBJ})\S)+"

# Nominal postmodifying clause
THAT_RELATIVE = rf"({NOUN} that_\S+ ({AUX}\s?{NOT}?|{ADV})?\s?({AUX}|{VERB})|{NOUN} that_\S+ {SUBJ})"
WH_RELATIVE_SUB = rf" (?:(?!((ask|tell|told)(s|ed|ing)?_\S+|told_\S+))\S)+ \S+ ({NOUN}|\S+_PRP) {WHP} ({AUX}\s?{NOT}?|{ADV})?\s?({AUX}|{VERB})"
WH_RELATIVE_OBJ = rf" (?:(?!((ask|tell)(s|ed|ing)?_\S+|told_\S+))\S)+ \S+ ({NOUN}|\S+_PRP) {WHP} (?:(?!{AUX}|{VERB}|{ADV}|{NOT})\S)+"
PREP_WH_RELATIVE = rf"{PREP} (who|whom|which|whose)_\S+"
PAST_PARTI_POST_NOMINAL_CLAUSE = rf"({NOUN}|{QUANPRP}) \S+VBN ({PREP}|{BE}|{ADV})"

# "To" clause preceded by
SPEECH_ACT_V_PLUS_TO = r"(ask|advise|begg?|beseech|besought|call|claim|challenge|command|convince|decline|heard|invite|offer|pray|promise|prove|remind|report|request|say|said|show|teach|taught|tell|told|urge|warn)(s|d|ed|ing)?_\S+ to_TO"
COGNITION_V_PLUS_TO = r"(assume|believe|consider|estimate|expect|felt|find|found|forget|forgot|forgotten|hear|imagine|judge|know|knew|known|learn|learnt|presume|pretend|remember|see|suppose|take|token|taken|trust|understand|watch)(s|d|ed|ing)?_\S+ to_TO"
DESIRE_V_PLUS_TO = r"(aim|agree|bear|bore|care|choose|chose|consent|dare|decide|design|desire|dread|hate|hesitate|hope|intend|like|look|love|long|mean|need|plan|prefer|prepare|refuse|regret|resolve|schedule|stand|threaten|volunteer|wait|want|wish)(s|d|ed|ing)?_\S+ to_TO"
MODALITY_V_PLUS_TO = r"(afford|allow|appoint|arrange|assist|attempt|authorize|bother|cause|counsell?|compell?|defy|defied|deserve|drive|elect|enable|encourage|endeavor|entitle|fail|forbid|forbidden|force|get|got|gotten|help|inspire|instruct|lead|led|leave|left|manage|oblige|order|permit|persuade|prompt|require|raise|seek|sought|strive|struggle|summon|tempt|try|tried|venture)(s|d|ed|ing)?_\S+ to_TO"
PROBABILITY_V_PLUS_TO = r"(appear|happen|seem|tend)(s|d|ed|ing)?_\S+ to_TO"
CERTAINTY_ADJ_PLUS_TO = r"(apt|certain|due|guaranteed|liable|likely|prone|unlikely|sure)_\S+ to_TO"
ABILITY_ADJ_PLUS_TO = r"(able|anxious|bound|careful|competent|determined|disposed|doomed|eager|eligible|fit|greedy|hesitant|inclined|insufficient|keen|loath|obliged|prepared|quick|ready|reluctant|set|slow|sufficient|unable|unwilling|welcome|willing)_\S+ to_TO"
AFFECT_ADJ_PLUS_TO = r"(afraid|amazed|angry|annoyed|ashamed|astonished|concerned|content|curious|delighted|disappointed|disgusted|embarrassed|free|furious|glad|grateful|happy|impatient|indignant|nervous|perturbed|pleased|proud|puzzled|relieved|sorry|surprised|worried)_\S+ to_TO"
EASE_HARD_ADJ_PLUS_TO = r"(difficult|easier|easy|hard|harder|impossible|pleasant|possible|tough|tougher|unpleasant)_\S+ to_TO"
EVALUATIVE_ADJ_PLUS_TO = r"(awkward|appropriate|bad|best|better|brave|careless|convenient|crazy|criminal|cumbersome|desirable|dreadful|essential|expensive|foolhardy|fruitless|good|important|improper|inappropriate|interesting|logical|lucky|mad|necessary|nice|reasonable|right|safe|sick|silly|smart|stupid|surprising|useful|useless|unreasonable|unseemly|unwise|vital|wise|wonderful|worse|wrong)_\S+ to_TO"
CONTROL_NOUN_PLUS_TO = r"(agreement|authority|commitment|confidence|decision|desire|determination|duty|failure|inclination|intention|obligation|opportunity|plan|potential|promise|proposal|readiness|reluctance|responsibility|right|scheme|temptation|tendency|threat|wish|willingness)(s|es)?_\S+ to_TO"

# "That" clause preceded by
NONFACTIVE_N_PLUS_THAT = r"(comment|news|proposal|proposition|remark|report|requirement)(s|es)?_\S+ that_\S+"
ATTITUDINAL_N_PLUS_THAT = r"(ground|hope|reason|view|thought)(s|es)?_\S+ that_\S+"
FACTIVE_N_PLUS_THAT = r"(assertion|conclusion|conviction|discover|doubt|fact|knowledge|observation|principle|realization|result|statement)(s|es)?_\S+ that_\S+"
LIKELIHOOD_N_PLUS_THAT = r"(assumption|belief|claim|contention|expectation|feeling|hypothesis|idea|implication|impression|indication|notion|opinion|possibility|presumption|probability|rumor|sign|suggestion|suspicion|thesis)(s|es)?_\S+ that_\S+"
NONFACTIVE_V_PLUS_THAT = r"(add|announce|advise|answer|argue|allege|ask|assert|assure|charge|claim|confide|confess|contend|convey|convince|declare|demand|deny|emphasize|explain|express|forewarn|grant|hear|hint|hold|imply|inform|insist|maintain|mention|mutter|notify|notified|order|persuade|petition|phone|pray|proclaim|promise|propose|protest|reassure|recommend|remark|reply|replied|report|respond|reveal|say|said|shout|state|stress|suggest|swear|sworn|teach|taught|telephone|tell|told|urge|vow|warn|whisper|wire|write|wrote|written)(s|d|ed|ing)?_\S+ that_\S+"
ATTITUDINAL_V_PLUS_THAT = r"(accept|admit|agree|anticipate|boast|complain|concede|cry|cried|dream|ensure|expect|fancy|fear|feel|forget|foresee|foresaw|forseen|guarantee|hope|mind|prefer|pretend|reflect|require|resolve|trust|wish|worry|worried)(s|d|ed|ing)?_\S+ that_\S+"
FACTIVE_V_PLUS_THAT = r"(acknowledge|affirm|ascertain|calculate|certify|certified|check|conclude|confirm|decide|deem|demonstrate|determine|discover|find|know|learn|mean|meant|note|notice|observe|prove|realize|recall|recognize|recollect|record|remember|see|show|signify|submit|testify|understand)(s|d|ed|ing)?_\S+ that_\S+"
LIKELIHOOD_V_PLUS_THAT = r"(appear|assume|believe|bet|conceive|consider|deduce|detect|doubt|estimate|figure|gather|guess|hypothesize|imagine|indicate|intend|perceive|postulate|predict|presuppose|presume|reckon|seem|sense|speculate|suppose|suspect|think|thought|wager)(s|d|ed|ing)?_\S+ that_\S+"
LIKELIHOOD_ADJ_PLUS_THAT = r"(doubtful|likely|possible|probable|unlikely)_\S+ that_\S+"
ATTITUDINAL_ADJ_PLUS_THAT = r"(acceptable|adamant|advisable|afraid|alarmed|amazed|amazing|amused|angry|annoyed|annoying|anomalous|appropriate|astonished|aware|awful|careful|concerned|conceivable|critical|crucial|curious|depressed|desirable|disappointed|dissatisfied|distressed|disturbed|dreadful|embarrassing|encouraged|essential|extraordinary|fitting|fortunate|frightened|funny|glad|good|grateful|great|happy|hopeful|horrible|hurt|imperative|incidental|inconceivable|incredible|indisputable|interesting|ironic|irritated|lucky|mad|natural|neat|necessary|nice|notable|noteworthy|noticeable|obligatory|odd|okay|paradoxical|peculiar|pleased|preferable|reassured|relieved|ridiculous|sad|satisfied|sensible|shocked|shocking|silly|sorry|strange|stupid|sufficient|surprised|surprising|thankful|tragic|typical|unacceptable|unaware|uncomfortable|understandable|unfair|unfortunate|unhappy|unlucky|unthinkable|untypical|unusual|upset|upsetting|vital|wonderful|worried)_\S+ that_\S+"


# -------------------------------------- Lexical pattern --------------------------------------- #
PART_OF_SPEECH = [NOUN, VERB, NOUN, NMOD, ART, MODAL, NOT, PREP]

# pronoun subcategories
r"(i|me|my|myself)_\S+"
FIRST_PRP_SING = r"(i|me|my|myself)_\S+"
FIRST_PRP_PLURAL = r"(us|let_\S+ 's|we|our|ourselves)_\S+"
SECOND_PRP = r"(you|your|yourself|yourselves|thy|thee|thyself|thou)_\S+"
THIRD_PRP = r"(s?he|they|her|him|them|his|their|himself|herself|themselves)_\S+"
IT_PRP = r"(it|its|itself)_\S+"
DEMONSTRATIVE_PRP = rf"{DEM} ({AUX}|\S+VB[PZD]?\b|{WHP}|\S+_CC|\S+_IN)"
INDEFINITE_PRP = r"((anybody|anyone|anything|everybody|everyone|everything|nobody|none|nothing|nowhere|somebody|someone|something)_\S+)"

# noun subcategories
NOMINALIZATION = r"\S+(tions?|ments?|ness|nesses|ity|ities)_NN"
ANIMATE_N = r"(family|guy|individual|kid|man|manager|member|parent|teacher|child|people|person|student|woman|animal|applicant|author|baby|boy|client|consumer|critic|customer|doctor|employee|employer|father|female|friend|girl|god|historian|husband|American|Indian|instructor|king|leader|male|mother|owner|president|professor|researcher|scholar|speaker|species|supplier|undergraduate|user|wife|worker|writer|accountant|adult|adviser|agent|aide|ancestor|anthropologist|archaeologist|artist|artiste|assistant|associate|attorney|audience|auditor|bachelor|bird|boss|brother|Buddha|buyer|candidate|cat|citizen|colleague|collector|competitor|counselor|daughter|deer|defendant|designer|developer|director|dog|driver|economist|engineer|executive|expert|farmer|officer|official|participant|partner|patient|personnel|peer|physician|plaintiff|player|poet|police|processor|professional|provider|psychologist|resident|respondent|schizophrenic|scientist|feminist|freshman|ecologist|hero|host|hunter|immigrant|infant|investor|Jew|judge|lady|lawyer|learner|listener|maker|manufacturer|miller|minister|mom|monitor|monkey|neighbor|observer|secretary|server|shareholder|Sikh|sister|slave|son|spouse|supervisor|theorist|tourist|victim|faculty|dean|engineer|reader|couple|graduate)(s|es)?_NN\S?\S?"
COGNITIVE_N = r"(analysis|decision|experience|assessment|calculation|conclusion|consequence|consideration|evaluation|examination|expectation|observation|recognition|relation|understanding|hypothesis|ability|assumption|attention|attitude|belief|concentration|concern|consciousness|concept|fact|idea|knowledge|look|need|reason|sense|view|theory|desire|emotion|feeling|judgment|memory|notion|opinion|perception|perspective|possibility|probability|responsibility|thought)(s|es)?_NN\S?\S?"
CONCRETE_N = r"(tank|stick|target|strata|telephone|string|telescope|sugar|ticket|syllabus|tip|salt|tissue|screen|tooth|sculpture|sphere|seawater|spot|ship|steam|silica|steel|slide|stem|snow|sodium|mud|solid|mushroom|gift|muscle|glacier|tube|gun|nail|handbook|newspaper|handout|node|instrument|notice|knot|novel|lava|page|food|transcript|leg|eye|lemon|brain|magazine|device|magnet|oak|manual|package|marker|peak|match|pen|metal|pencil|block|pie|board|pipe|heart|load|paper|transistor|modem|book|mole|case|motor|computer|mound|dollar|mouth|hand|movie|flower|object|foot|table|frame|water|vessel|arm|visa|bar|grain|bed|hair|body|head|box|ice|car|item|card|journal|chain|key|chair|window|vehicle|leaf|copy|machine|document|mail|door|map|dot|phone|drug|picture|truck|piece|tape|note|liquid|wire|equipment|wood|fiber|plant|fig|resistor|film|sand|file|score|seat|belt|sediment|boat|seed|bone|soil|bubble|solution|bud|water|bulb|portrait|bulletin|step|shell|stone|cake|tree|camera|video|face|wall|acid|alcohol|cap|aluminum|clay|artifact|clock|rain|clothing|asteroid|club|automobile|comet|award|sheet|bag|branch|ball|copper|banana|counter|band|cover|wheel|crop|drop|crystal|basin|cylinder|bell|desk|dinner|pole|button|pot|disk|pottery|drain|radio|drink|reactor|drawing|retina|dust|ridge|edge|ring|engine|ripple|plate|game|cent|post|envelope|rock|filter|root|finger|slope|fish|space|fruit|statue|furniture|textbook|gap|tool|gate|train|gel|deposit|chart|mixture)(s|es)?_NN\S?\S?"
TECHNICAL_N = r"(cell|unit|gene|wave|ion|bacteria|electron|chromosome|element|cloud|sample|isotope|schedule|neuron|software|nuclei|solution|nucleus|atom|ray|margin|virus|mark|hydrogen|mineral|internet|molecule|mineral|organism|message|oxygen|paragraph|particle|sentence|play|star|poem|thesis|proton|unit|web|layer|center|matter|chapter|square|data|circle|equation|compound|exam|letter|bill|page|component|statement|diagram|word|DNA|angle|fire|carbon|formula|graph|iron|lead|jury|light|list)(s|es)?_NN\S?\S?"
QUANTITY_N = r"(cycle|rate|date|second|frequency|section|future|semester|half|temperature|height|today|amount|week|age|day|century|part|energy|lot|heat|term|hour|time|month|mile|period|moment|morning|volume|per|weekend|percentage|weight|portion|minute|quantity|percent|quarter|length|ratio|measure|summer|meter|volt|voltage)(s|es)?_NN\S?\S?"
PLACE_N = r"(apartment|interior|bathroom|moon|bay|museum|bench|neighborhood|bookstore|opposite|border|orbit|cave|orbital|continent|outside|delta|parallel|desert|passage|estuary|pool|factory|prison|farm|restaurant|forest|sector|habitat|shaft|hell|shop|hemisphere|southwest|hill|station|hole|territory|horizon|road|bottom|store|boundary|stream|building|top|campus|valley|canyon|village|coast|city|county|country|court|earth|front|environment|district|field|floor|market|lake|office|land|organization|lecture|place|room|library|area|location|class|middle|classroom|mountain|ground|north|hall|ocean|park|planet|property|region|residence|river)(s|es)?_NN\S?\S?"
GROUP_N = r"(airline|institute|colony|bank|flight|church|hotel|firm|hospital|household|college|institution|house|lab|laboratory|community|company|government|university|school|home|congress|committee)(s|es)?_NN\S?\S?"
ABSTRACT_N = r"(action|activity|application|argument|development|education|effect|function|method|research|result|process|accounting|achievement|addition|administration|approach|arrangement|assignment|competition|construction|consumption|contribution|counseling|criticism|definition|discrimination|description|discussion|distribution|division|eruption|evolution|exchange|exercise|experiment|explanation|expression|formation|generation|graduation|management|marketing|marriage|mechanism|meeting|operation|orientation|performance|practice|presentation|procedure|production|progress|reaction|registration|regulation|revolution|selection|session|strategy|teaching|technique|tradition|training|transition|treatment|trial|act|agreement|attempt|attendance|birth|break|claim|comment|comparison|conflict|deal|death|debate|demand|answer|control|flow|service|work|test|use|war|change|question|study|talk|task|trade|transfer|admission|design|detail|dimension|direction|disorder|diversity|economy|emergency|emphasis|employment|equilibrium|equity|error|expense|facility|failure|fallacy|feature|format|freedom|fun|gender|goal|grammar|health|heat|help|identity|image|impact|importance|influence|input|labor|leadership|link|manner|math|matrix|meaning|music|network|objective|opportunity|option|origin|output|past|pattern|phase|philosophy|plan|potential|prerequisite|presence|principle|success|profile|profit|proposal|psychology|quality|quiz|race|reality|religion|resource|respect|rest|return|risk|substance|scene|security|series|set|setting|sex|shape|share|show|sign|signal|sort|sound|spring|stage|standard|start|stimulus|strength|stress|style|support|survey|symbol|topic|track|trait|trouble|truth|variation|variety|velocity|version|whole|action|account|condition|culture|end|factor|grade|interest|issue|job|kind|language|law|level|life|model|name|nature|order|policy|position|power|pressure|relationship|requirement|role|rule|science|side|situation|skill|source|structure|subject|type|information|right|state|system|value|way|address|absence|advantage|aid|alternative|aspect|authority|axis|background|balance|base|beginning|benefit|bias|bond|capital|care|career|cause|characteristic|charge|check|choice|circuit|circumstance|climate|code|color|column|combination|complex|connection|constant|constraint|contact|content|contract|context|contrast|crime|criteria|cross|current|curriculum|curve|debt|density)(s|es)?_NN\S?\S?"

# verb subcategories
BE_MAIN_VERB = rf"({BE}| 's_V\S+) ({NOT}|{ADV})?\s?({NOT}|{ADV})?\s?({NMOD}|\S+_IN)|({BE}| 's_V\S+) {ADV} {ADV}?\s?\S+_PRP"
PRO_VERB_DO = rf" ((doing|done)_\S+| (?:(?!{WHO}|{WHP})\S)+ {ADV}?\s?{DO} (?:(?!{NOT}|{VERB}|{SUBPRP}|{ADV} {VERB})\S)+)"
ACTIVITY_V = r"(buy|bought|make|made|get|got|gotten|go|went|give|gave|take|took|taken|come|came|use|leave|left|show|try|tried|work|move|follow|put|pay|bring|brought|meet|met|play|run|hold|held|turn|send|sent|sit|sat|wait|walk|carry|carried|lose|lost|eat|ate|watch|reach|add|produce|provide|pick|wear|wore|open|win|won|catch|pass|shake|smile|stare|sell|sold|spend|spent|apply|applied|form|obtain|arrange|beat|check|cover|divide|earn|extend|fix|hang|hung|join|lie|lay|obtain|pull|repeat|receive|save|share|smile|throw|threw|visit|accompany|accompanied|acquire|advance|behave|borrow|burn|clean|climb|combine|controll?|defend|deliver|dig|dug|encounter|engage|exercise|expand|explore|reduce)(s|d|ed|ing)?_VB\S?"
COMMUNICATION_V = r"(say|said|tell|told|call|ask|write|wrote|written|talk|speak|spoke|thank|describe|claim|offer|admit|announce|answer|argue|deny|denied|discuss|encourage|explain|express|insist|mention|offer|propose|quote|reply|replied|shout|sign|sing|sang|state|teach|warn|accuse|acknowledge|address|advise|appeal|assure|challenge|complain|consult|convince|declare|demand|emphasize|excuse|inform|invite|persuade|phone|pray|promise|question|recommend|remark|respond|specify|specified|swear|threaten|urge|welcome|whisper|suggest)(s|d|ed|ing)?_VB\S?"
MENTAL_V = r"(see|saw|seen|know|knew|known|think|thought|find|found|want|mean|meant|need|feel|felt|like|hear|remember|believe|read|consider|suppose|listen|love|wonder|understand|expect|hope|assume|determine|agree|bear|care|choose|compare|decide|discover|doubt|enjoy|examine|face|forget|hate|identify|imagine|intend|learn|mind|miss|notice|plan|prefer|prove|realize|recall|recognize|regard|suffer|wish|worry|accept|afford|appreciate|approve|assess|blame|bother|calculate|conclude|celebrate|confirm|count|dare|deserve|detect|dismiss|distinguish|experience|fear|forgive|guess|ignore|impress|interpret|judge|justify|observe|perceive|predict|pretend|reckon|remind|satisfy|solve|study|suspect|trust|figure)(s|d|ed|ing)?_VB\S?"
CAUSATIVE_V = r"(help|let|allow|affect|cause|enable|ensure|force|prevent|assist|guarantee|influence|permitt?|require)(s|d|ed|ing)?_VB\S?"
OCCURRENCE_V = r"(become|became|happen|change|die|grow|develop|arise|emerge|fall|fell|increase|last|rise|rose|risen|disappear|flow|flew|shine|sink|sank|slipp?|occur)(s|d|ed|ing)?_VB\S?"
EXISTENCE_V = r"(seem|look|stand|stood|stay|live|appear|include|involve|contain|exist|indicate|concern|constitute|define|derive|illustrate|imply|implied|lack|owe|own|possess|suit|vary|varied|deserve|fitt?|matter|reflect|relate|remain|reveal|sound|tend|represent)(s|d|ed|ing)?_VB\S?"
ASPECTUAL_V = r"(start|keep|kept|stop|begin|began|begun|complete|end|finish|cease|continue)(s|d|ed|ing)?_VB\S?"

# adjective subcategories
ATTRIBUTIVE_ADJ = rf"({ADJ}(?= ({CC}?\s?{ADJ} {NOUN}|{NOUN}|ones?_\S+))|(the_\S+|{QUANPRP}) {ADJ})"
PREDICATIVE_ADJ = rf"{LINKING_V} ({NOT}|{ADV})?\s?({NOT}|{ADV})?\s?{ADJ} (?:(?!{ADJ}|{NOUN}|ones?_\S+)\S)+|{BE} {NOT}?\s?{SUBPRP}\s?({NOT}|{ADV})?\s?{ADJ} (?:(?!{ADJ}|{NOUN})\S)+| (?:(?!{QUANPRP}|the_\S+)\S)+ {ADJ} \S+_(IN|CC|WRB|WP\S?|WDT)"

# adverb subcategories
PLACE_ADV = r"\b(aboard|above|abroad|across|ahead|alongside|around|ashore|astern|away|behind|below|beneath|beside|downhill|downstairs|downstream|east|far|hereabouts|indoors|inland|inshore|inside|locally|near|nearby|north|nowhere|outdoors|outside|overboard|overland|overseas|south|underfoot|underground|underneath|uphill|upstairs|upstream|west)_(?:(?!NNP)\S)+"
TIME_ADV = r'\b(afterwards|again|earlier|early|eventually|formerly|immediately|initially|instantly|late|lately|later|momentarily|now|nowadays|once|originally|presently|previously|recently|shortly|simultaneously|subsequently|today|to-day|tomorrow|to-morrow|tonight|to-night|yesterday|soon_\S+ as)_\S+'
NONFACTIVE_ADV = r"((accordingly|confidentially|figuratively|speaking|frankly|generally|honestly|mainly|strictly|technically|speaking|truthfully|typically|reportedly)_|according_\S+ to_)"
ATTITUDINAL_ADV = r"((amazingly|astonishingly|conveniently|curiously|disturbingly|hopefully|fortunately|importantly|ironically|regrettably|rightly|sadly|sensibly|surprisingly|unbelievably|unfortunately|wisely)_\S+|even_\S+ worse_\S+)"
FACTIVE_ADV = r"((actually|always|certainly|definitely|indeed|inevitably|in_IN fact_NN|never|obviously|really|undoubtedly)_\S+|without_\S+ doubt_\S+|no_\S+ doubt_\S+|of_\S+ course_\S+)"
LIKELIHOOD_ADV = rf"((apparently|evidently|perhaps|possibly|predictably|probably|roughly)_\S+|sort_\S+ of_\S+ ({ADJ}|{VERB})|most_\S+ (cases?|instances?)_\S+)"

# Conjunction
CAUSATIVE_CONJ = r"(because)_\S+"
CONDITIONAL_CONJ = r"(if|unless)_\S+"
CONTRASTIVE_CONJ = r"(although|tho|though|even_\S+ if|but|however|no_\S+ matter_\S+ how|whereas|despite|nevertheless|in_\S+ spite_\S+ of|regardless_\S+ of|as_\S+ opposed_\S+ to|in_\S+ contrast|instead_\S+ of_\S+|notwithstanding)_\S+"
OTHER_CONJ = rf"\b(since|while|whilst|whereupon|whereas|whereby)_\S+|(so|such)_\S+ that_\S+(?= (?:(?!{NOUN}|{ADJ})\S)+)|(inasmuch|forasmuch|insofar|insomuch)_\S+ as_\S+|as_\S+ (long|soon)_\S+ as_\S+"

# modal subcategories
POSSIBILITY_MD = r"(can?|may|might|could)_\S+"
NECESSITY_MD = r"(ought|should|must)_\S+"
PREDICTIVE_MD = r"(will| 'll|would|shall| 'd|wo|sha)_MD"

# Stance-related expressions
CONJUNCT = r"((alternatively|(altogether|else|rather)|consequently|conversely|eg|furthermore|hence|however|ie|instead|likewise|moreover|namely|nevertheless|nonetheless|notwithstanding|otherwise|similarly|therefore|thus|viz|via)_\S+|in_\S+ (comparison|contrast|particular|addition|conclusion|consequence|sum|summary|any_\S+ event|any_\S+ case|other_\S+ words)_\S+|for_\S+ (example|instance)_\S+|instead_\S+ of_\S+|by_\S+ (contrast|comparison)_|as_\S+ a_\S+ (result|consequence)_\S+|on_\S+ the_\S+ (contrary|other_\S+ hand)_\S+)"
DOWNTONER = r"(almost|barely|hardly|merely|mildly|nearly|only|partially|partly|practically|scarcely|slightly|somewhat)_\S+"
AMPLIFIER = rf"(absolutely|altogether|completely|enormously|entirely|extremely|fully|greatly|highly|intensely|perfectly|strongly|thoroughly|totally|utterly|very|terribly|awfully|vastly)_\S+|so_\S+ {ADJ}"
HEDGE = rf"(maybe|at_\S+ about|something_\S+ like|more_\S+ or_\S+ less)_\S+| (?:(?!{NMOD}|{WHO})\S)+ (sort|kind)_\S+ of_\S+|a_\S+ (little_\S+)?\s?bit_\S+"
EMPHATICS = rf"((just|really|most|more|anyway|especially|full|much|totally)_\S+|(real|so|all)_\S+ {ADJ}|({DO}|even|always) {VERB}|for_\S+ sure_\S+|a_\S+ lot_\S+|such_\S+ an?_\S+)"
POLITE_EXP = r"thanks?_\S+\s?(you)?|please_\S+|excuse_\S+ me_\S+"
EVIDENTIAL_EXP = r"((amazing|bad|beautiful|best|better|crazy|fun|funny|glad|good|great|happy|hate|love|mad|nice|okay|problem|rather|serious|sorry|stupid|trouble|weird|wrong)_\S+|like_V\S+)"
STANCE_RELATED = [CONJUNCT, DOWNTONER, AMPLIFIER, HEDGE, EMPHATICS, POLITE_EXP, EVIDENTIAL_EXP]

# ============================================================================================== #

FEATURE_DICT = {
    # ---------------------------- Structural feature ---------------------------- #
    "Six letter words and longer": SIX_LETTER_WORD_N_LONGER,

    # ---------------------------- Conversational feature ---------------------------- #
    "Contraction": CONTRACTION,

    # ---------------------------- Sentential feature ---------------------------- #
    # passive voice
    "Agentless passive": AGENTLESS_PASSIVE,
    "By passive": BY_PASSIVE,

    # Tense
    "Past tense": PAST_TENSE,
    "Perfect aspect": PERFECT_ASPECT,
    "Non-past tense": NON_PAST_TENSE,
    "Progressive tense": PROGESSIVE_TENSE,

    # Split structure
    "Split auxiliaries": SPLIT_AUX,

    # Coordination
    "Phrasal Coord": PHRASAL_COORD,
    "Independent clause coord": IND_CLAUSE_COORD,

    # WH structure
    "WH question": WH_QUESTION,
    "WH clause": WH_CLAUSE,

    # Nominal postmodifying clause
    "That relative": THAT_RELATIVE,
    "WH relative on subject position": WH_RELATIVE_SUB,
    "WH relative on object position": WH_RELATIVE_OBJ,
    "WH relative with fronted prep": PREP_WH_RELATIVE,
    "Past participial clause": PAST_PARTI_POST_NOMINAL_CLAUSE,

    # "To" clause preceded by
    "Speech act verb + to": SPEECH_ACT_V_PLUS_TO,
    "Cognition verb + to": COGNITION_V_PLUS_TO,
    "Desire verb + to": DESIRE_V_PLUS_TO,
    "Modality verb + to": MODALITY_V_PLUS_TO,
    "Probability verb + to": PROBABILITY_V_PLUS_TO,
    "Certainty adj + to": CERTAINTY_ADJ_PLUS_TO,
    "Ability adj + to": ABILITY_ADJ_PLUS_TO,
    "Personal affect adj + to": AFFECT_ADJ_PLUS_TO,
    "Ease_difficulty adj + to": EASE_HARD_ADJ_PLUS_TO,
    "Evaluative adj + to": EVALUATIVE_ADJ_PLUS_TO,
    "Control noun + to": CONTROL_NOUN_PLUS_TO,

    # "That" clause preceded by
    "Nonfactive noun + that": NONFACTIVE_N_PLUS_THAT,
    "Attitudinal noun + that": ATTITUDINAL_N_PLUS_THAT,
    "Factive noun + that": FACTIVE_N_PLUS_THAT,
    "Likelihood noun + that": LIKELIHOOD_N_PLUS_THAT,
    "Nonfactive verb + that": NONFACTIVE_V_PLUS_THAT,
    "Attitudinal verb + that": ATTITUDINAL_V_PLUS_THAT,
    "Factive verb + that": FACTIVE_V_PLUS_THAT,
    "Likelihood verb + that": LIKELIHOOD_V_PLUS_THAT,
    "Likelihood adj + that": LIKELIHOOD_ADJ_PLUS_THAT,
    "Attitudinal adj + that": ATTITUDINAL_ADJ_PLUS_THAT,

    # ---------------------------- Sentential feature ---------------------------- #
    # Part of speech
    "Noun": NOUN,
    "VERB": VERB,
    "Noun modifier": NMOD,
    "Article": ART,
    "Modal": MODAL,
    "Negator": NOT,
    "Preposition": PREP,

    # Pronoun
    "First person pronoun singular": FIRST_PRP_SING,
    "First person pronoun plural": FIRST_PRP_PLURAL,
    "Second person pronoun": SECOND_PRP,
    "Third person pronoun": THIRD_PRP,
    "Pronoun it": IT_PRP,
    "Demonstrative pronoun": DEMONSTRATIVE_PRP,
    "Indefinite pronoun": INDEFINITE_PRP,

    # Noun subcategories
    "Nominalization": NOMINALIZATION,
    "Animate noun": ANIMATE_N,
    "Cognitive noun": COGNITIVE_N,
    "Concrete noun": CONCRETE_N,
    "Technical noun": TECHNICAL_N,
    "Quantity noun": QUANTITY_N,
    "Place noun": PLACE_N,
    "Group noun": GROUP_N,
    "Abstract noun": ABSTRACT_N,

    # Verb subcategories
    "Be as main verb": BE_MAIN_VERB,
    "Pro-verb do": PRO_VERB_DO,
    "Activity verb": ACTIVITY_V,
    "Communication verb": COMMUNICATION_V,
    "Mental verb": MENTAL_V,
    "Causative verb": CAUSATIVE_V,
    "Ocurrence verb": OCCURRENCE_V,
    "Existence verb": EXISTENCE_V,
    "Aspectual verb": ASPECTUAL_V,

    # Adjective subcategories
    "Attributive adj": ATTRIBUTIVE_ADJ,
    "Predictive adjective": PREDICATIVE_ADJ,

    # Adverb subcategories
    "Place adverb": PLACE_ADV,
    "Time adverb": TIME_ADV,
    "Nonfactive adverb": NONFACTIVE_ADV,
    "Attitudinal adverb": ATTITUDINAL_ADV,
    "Factive adverb": FACTIVE_ADV,
    "Likelihood adverb": LIKELIHOOD_ADV,

    # Conjunction
    "Causative subordinator": CAUSATIVE_CONJ,
    "Conditional subordinator": CONDITIONAL_CONJ,
    "Contrastive subordinator": CONTRASTIVE_CONJ,
    "Other subordinator": OTHER_CONJ,

    # Modal subcategories
    "Possibility modal": POSSIBILITY_MD,
    "Necessity modal": NECESSITY_MD,
    "Predictive modal": PREDICTIVE_MD,

    # Stance-related expression
    "Conjunct": CONJUNCT,
    "Downtoner": DOWNTONER,
    "Amplifier": AMPLIFIER,
    "Hedge": HEDGE,
    "Emphatics": EMPHATICS,
    "polite expression": POLITE_EXP,
    "Evidential expression": EVIDENTIAL_EXP
    }


FEATURE_LIST = ['Six letter words and longer', 'Contraction', 'Agentless passive', 'By passive', 'Past tense', 'Perfect aspect', 'Non-past tense', 'Progressive tense', 'Split auxiliaries', 'Phrasal Coord', 'Independent clause coord', 'WH question', 'WH clause', 'That relative', 'WH relative on subject position', 'WH relative on object position', 'WH relative with fronted prep', 'Past participial clause', 'Speech act verb + to', 'Cognition verb + to', 'Desire verb + to', 'Modality verb + to', 'Probability verb + to', 'Certainty adj + to', 'Ability adj + to', 'Personal affect adj + to', 'Ease/difficulty adj + to', 'Evaluative adj + to', 'Control noun + to', 'Nonfactive noun + that', 'Attitudinal noun + that', 'Factive noun + that', 'Likelihood noun + that', 'Nonfactive verb + that', 'Attitudinal verb + that', 'Factive verb + that', 'Likelihood verb + that', 'Likelihood adj + that', 'Attitudinal adj + that', 'Noun', 'VERB', 'Noun modifier', 'Article', 'Modal', 'Negator', 'Preposition', 'First person pronoun', 'I reference', 'Second person pronoun', 'Third person pronoun', 'Pronoun it', 'Demonstrative pronoun', 'Indefinite pronoun', 'Nominalization', 'Animate noun', 'Cognitive noun', 'Concrete noun', 'Technical noun', 'Quantity noun', 'Place noun', 'Group noun', 'Abstract noun', 'Be as main verb', 'Pro-verb do', 'Activity verb', 'Communication verb', 'Mental verb', 'Causative verb', 'Ocurrence verb', 'Existence verb', 'Aspectual verb', 'Attributive adj', 'Predictive adjective', 'Place adverb', 'Time adverb', 'Nonfactive adverb', 'Attitudinal adverb', 'Factive adverb', 'Likelihood adverb', 'Causative subordinator', 'Conditional subordinator', 'Contrastive subordinator', 'Other subordinator', 'Possibility modal', 'Necessity modal', 'Predictive modal', 'Conjunct', 'Downtoner', 'Amplifier', 'Hedge', 'Emphatics', 'polite expression', 'Evidential expression']
SEN_FEATURE_LIST = ['Agentless passive', 'By passive', 'Past tense', 'Perfect aspect', 'Non-past tense', 'Progressive tense', 'Split auxiliaries', 'Phrasal Coord', 'Independent clause coord', 'WH question', 'WH clause', 'That relative', 'WH relative on subject position', 'WH relative on object position', 'WH relative with fronted prep', 'Past participial clause', 'Speech act verb + to', 'Cognition verb + to', 'Desire verb + to', 'Modality verb + to', 'Probability verb + to', 'Certainty adj + to', 'Ability adj + to', 'Personal affect adj + to', 'Ease/difficulty adj + to', 'Evaluative adj + to', 'Control noun + to', 'Nonfactive noun + that', 'Attitudinal noun + that', 'Factive noun + that', 'Likelihood noun + that', 'Nonfactive verb + that', 'Attitudinal verb + that', 'Factive verb + that', 'Likelihood verb + that', 'Likelihood adj + that', 'Attitudinal adj + that']
LEX_FEATURE_LIST = ['Noun', 'VERB', 'Noun modifier', 'Article', 'Modal', 'Negator', 'Preposition', 'First person pronoun', 'I reference', 'Second person pronoun', 'Third person pronoun', 'Pronoun it', 'Demonstrative pronoun', 'Indefinite pronoun', 'Nominalization', 'Animate noun', 'Cognitive noun', 'Concrete noun', 'Technical noun', 'Quantity noun', 'Place noun', 'Group noun', 'Abstract noun', 'Be as main verb', 'Pro-verb do', 'Activity verb', 'Communication verb', 'Mental verb', 'Causative verb', 'Ocurrence verb', 'Existence verb', 'Aspectual verb', 'Attributive adj', 'Predictive adjective', 'Place adverb', 'Time adverb', 'Nonfactive adverb', 'Attitudinal adverb', 'Factive adverb', 'Likelihood adverb', 'Causative subordinator', 'Conditional subordinator', 'Contrastive subordinator', 'Other subordinator', 'Possibility modal', 'Necessity modal', 'Predictive modal', 'Conjunct', 'Downtoner', 'Amplifier', 'Hedge', 'Emphatics', 'polite expression', 'Evidential expression']


def num_utterances(raw_text):
    return len(re.findall('<u', raw_text))


def num_overlaps(raw_text):
    return len(re.findall(r'(trans="overlap")|<overlap', raw_text))


def word_count(tagged_text):
    tagged_text = re.sub(r"(\S+_\W\S*|\S+_POS)", "", tagged_text)
    return len(re.findall(rf"{TOKEN}", tagged_text))


def total_char(tagged_text):
    tagged_text = re.sub(r'_\S+', '', tagged_text)
    tagged_text = re.sub(r'(\W|_)', '', tagged_text)
    return len(re.findall(r'\w', tagged_text))


def feature_finder(regex, pos_tagged_text):
    results = re.findall(rf"(\b\s?{regex})", pos_tagged_text, flags=re.IGNORECASE)
    return results


def get_feature_frequency(regex, pos_tagged_text):
    return len(feature_finder(regex, pos_tagged_text))


def concordance_generator(results, pos_tagged_text, left=0, right=0):
    if left == 0 and right == 0:
        extracted_texts = []
        for res in results:
            extracted_texts.append(res[0])
    else:
        results = set([res[0] for res in results])
        pattern = '|'.join(results)
        tokens = re.findall(rf'({pattern}|\S+)', pos_tagged_text)
        idx_all = [idx for idx, elem in enumerate(tokens) if elem in results]
        extracted_texts = []
        for idx in idx_all:
            left_context = tokens[idx - left if idx - left > 0 else 0: idx]
            left_context = ' '.join(left_context)
            right_context = tokens[idx+1: idx + right + 1]
            right_context = ' '.join(right_context)
            concordance_text = f'{left_context}\t【{tokens[idx]} 】\t{right_context}'
            extracted_texts.append(concordance_text)
    return extracted_texts


def display_extracted_res_by_regex(regex, pos_tagged_text, left=0, right=0, feature_name=None):
    results = feature_finder(regex, pos_tagged_text)
    num_cases = len(results)
    msg = f'\n{"#"*10} {num_cases} cases found: {feature_name} {"#"*10}\n\n'
    extracted_texts = concordance_generator(results, pos_tagged_text, left, right)
    return msg + '\n'.join(extracted_texts)


def display_extracted_res(results, pos_tagged_text=None, left=0, right=0, feature_name=None):
    num_cases = len(results)
    msg = f'\n{"#"*10} {num_cases} cases found: {feature_name} {"#"*10}\n\n'
    extracted_texts = concordance_generator(results, pos_tagged_text, left, right)
    return msg + '\n'.join(extracted_texts)

