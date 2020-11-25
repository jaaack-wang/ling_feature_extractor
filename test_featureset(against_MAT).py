TOKEN = r"(\S+)"
NOT = r"(\b(not|n't)_\S+)"
BE = r"(\b(am|is|are|was|were|be|being|been| 'm| 're)_\S+)"
LINKING_V = rf"({BE}|\b(become|became|becoming|seem|grow|grew|grown|look|prove|proving|remain|smell|sound|taste|tasting|turn|get|got|gotten|getting|appear|feel|felt)(s|end|ing)?_\S+)"
HAVE = r"(\b(have|has|had|having| 've| 'd|hath)_\S+)"
DO = r"(\b(do|does|did)_\S+)"
MODAL = r"(\S+_MD)"
AUX = rf"({BE}|{HAVE}|{DO}|{MODAL}| 's_VB\S?)"
ADV = r"(\S+_RB)"
ADJ = r"(\S+JJ\S?)"
VERB = r"(\S+VB\S?)"
NOUN = r"(\S+NN\S?\S?)"
DEM = r"(\b(this|those|these)_\S+|that_DT)"
ART = r"\b(an?_\S+|the_\S+)"
NMOD = rf"(\S+_P?DT|\S+PRP\$|\S+JJ\S?|\S+CD|{ART})"
QUANPRP = r"(\b(everybody|somebody|anybody|everyone|someone|anyone|everything|something|anything)_\S+)"
SUBPRP = rf"(\b(i|we|he|she|they|you|it)_\S+|{DEM})"
OBJPRP = rf"(\b(me|us|him|her|them|you|it)_\S+|{DEM})"
SUBJ = rf"({ART}?\s?{NMOD}?\s?{NOUN}|{SUBPRP})"
OBJ = rf"({ART}?\s?{NMOD}?\s?{NOUN}|{OBJPRP})"
CC = r"(\b(and|or)_\S+)"
WHP = rf"(\b(who|whom|which|whose_\S+ {NMOD}?\s?{NOUN})_\S+)"
WHO = r"(\b(what|where|when|how|whether|why|whoever|whomever|whichever|wherever|whenever|whatever|however)_\S+)"
PREP = r"(\b(against|amid|amidst|among|amongst|at|besides|between|by|despite|during|except|for|from|in|into|minus|notwithstanding|of|off|on|onto|opposite|out|per| re|plus|pro|than|through|throughout|thru|toward|towards|upon|versus|via|with|within|without)_\S+|to_IN)"

# -------------------------------------- Other features --------------------------------------- #

CONTRACTION = r"(n't| '\S\S?)_[^P]\S+"

# passive voice
BY_PASSIVE = rf"({BE}| 's_V\S+) ({NOT}|{ADV})?\s?{SUBJ}?\s?({ADV}|{NOT})?\s?(\S+VBN) by_\S+"
AGENTLESS_PASSIVE = rf"{BE} ({NOT}|{ADV})?\s?{SUBJ}?\s?({ADV}|{NOT})?\s?(\S+VBN)(?= \b(?:(?!by_)\S)+)"

# Tense
PAST_TENSE = r"(\S+_VBD)"
PERFECT_ASPECT = rf"{HAVE} ({NOT}|{ADV})?\s?{SUBJ}?\s?({NOT}|{ADV})?\s?\S+_VB[ND]"

# Split structure
SPLIT_AUX = rf"{AUX} {NOT}?\s?{ADV} {ADV}?\s?{VERB}"

# Coordination
PHRASAL_COORD = rf"{ADJ}(=? {CC} {ADJ})|{NOUN}(?= {CC} {NOUN})|{VERB}(?= {CC} {VERB})|{ADV}(?= {CC} {ADV})"
IND_CLAUSE_COORD = fr"{CC} ({ADV}|\S+_IN)?\s?({SUBPRP}|\S+_EX|{WHO}|{WHP}) ({ADV})?\s?({AUX}\s?{NOT}?|{ADV})?\s?({AUX}|{VERB})"

# WH structure
WH_QUESTION = rf"{WHO} {AUX} ({NOT}|{ADV})?\s?({NOT}|{ADV})?\s?{SUBJ}"
WH_CLAUSE = rf"{WHO} (?:(?!{AUX})\S)+|what_\S+ ({AUX}\s?{NOT}?|{ADV})?\s?{ADV}?\s?{VERB} {NOT}?\s?\b(?:(?!{SUBJ})\S)+"

# Nominal postmodifying clause
WH_RELATIVE_SUB = rf" (?:(?!((ask|tell|told)(s|ed|ing)?_\S+|told_\S+))\S)+ \S+ ({NOUN}|\S+_PRP) {WHP} ({AUX}\s?{NOT}?|{ADV})?\s?({AUX}|{VERB})"
WH_RELATIVE_OBJ = rf" (?:(?!((ask|tell)(s|ed|ing)?_\S+|told_\S+))\S)+ \S+ ({NOUN}|\S+_PRP) {WHP} (?:(?!{AUX}|{VERB}|{ADV}|{NOT})\S)+"
PREP_WH_RELATIVE = rf"{PREP} (who|whom|which|whose)_\S+"
PAST_PARTI_POST_NOMINAL_CLAUSE = rf"({NOUN}|{QUANPRP}) \S+VBN ({PREP}|{BE}|{ADV})"

# pronoun subcategories
FIRST_PRP = r"(i|me|us|let_\S+ 's|my|we|our|myself|ourselves)_\S+"
SECOND_PRP = r"(you|your|yourself|yourselves|thy|thee|thyself|thou)_\S+"
THIRD_PRP = r"(s?he|they|her|him|them|his|their|himself|herself|themselves)_\S+"
IT_PRP = r"(it|its|itself)_\S+"
DEMONSTRATIVE_PRP = rf"{DEM} ({AUX}|\S+VB[PZD]?\b|{WHP}|\S+_CC|\S+_IN)"
INDEFINITE_PRP = r"((anybody|anyone|anything|everybody|everyone|everything|nobody|none|nothing|nowhere|somebody|someone|something)_\S+)"

# noun and adjective subcategories
NOMINALIZATION = r"\S+(tions?|ments?|ness|nesses|ity|ities)_NN"

# verb subcategories
BE_MAIN_VERB = rf"({BE}| 's_V\S+) ({NOT}|{ADV})?\s?({NOT}|{ADV})?\s?({NMOD}|\S+_IN)|({BE}| 's_V\S+) {ADV} {ADV}?\s?\S+_PRP"
PRO_VERB_DO = rf" ((doing|done)_\S+| (?:(?!{WHO}|{WHP})\S)+ {ADV}?\s?{DO} (?:(?!{NOT}|{VERB}|{SUBPRP}|{ADV} {VERB})\S)+)"

# adjective subcategories
ATTRIBUTIVE_ADJ = rf"({ADJ}(?= ({CC}?\s?{ADJ} {NOUN}|{NOUN}|ones?_\S+))|(the_\S+|{QUANPRP}) {ADJ})"
PREDICATIVE_ADJ = rf"{LINKING_V} ({NOT}|{ADV})?\s?({NOT}|{ADV})?\s?{ADJ} (?:(?!{ADJ}|{NOUN}|ones?_\S+)\S)+|{BE} {NOT}?\s?{SUBPRP}\s?({NOT}|{ADV})?\s?{ADJ} (?:(?!{ADJ}|{NOUN})\S)+| (?:(?!{QUANPRP}|the_\S+)\S)+ {ADJ} \S+_(IN|CC|WRB|WP\S?|WDT)"

# adverb subcategories
PLACE_ADV = r"\b(aboard|above|abroad|across|ahead|alongside|around|ashore|astern|away|behind|below|beneath|beside|downhill|downstairs|downstream|east|far|hereabouts|indoors|inland|inshore|inside|locally|near|nearby|north|nowhere|outdoors|outside|overboard|overland|overseas|south|underfoot|underground|underneath|uphill|upstairs|upstream|west)_(?:(?!NNP)\S)+"
TIME_ADV = r'\b(afterwards|again|earlier|early|eventually|formerly|immediately|initially|instantly|late|lately|later|momentarily|now|nowadays|once|originally|presently|previously|recently|shortly|simultaneously|subsequently|today|to-day|tomorrow|to-morrow|tonight|to-night|yesterday|soon_\S+ as)_\S+'

# Conjunction
CAUSATIVE_CONJ = r"(because)_\S+"
CONDITIONAL_CONJ = r"(if|unless)_\S+"
OTHER_CONJ = rf"\b(since|while|whilst|whereupon|whereas|whereby)_\S+|(so|such)_\S+ that_\S+(?= (?:(?!{NOUN}|{ADJ})\S)+)|(inasmuch|forasmuch|insofar|insomuch)_\S+ as_\S+|as_\S+ (long|soon)_\S+ as_\S+"

# modal subcategories
POSSIBILITY_MD = r"\b(can?|may|might|could)_\S+"
NECESSITY_MD = r"\b(ought|should|must)_\S+"
PREDICTIVE_MD = r"\b(will| 'll|would|shall| 'd|wo|sha)_MD"

# Stance-related expressions
CONJUNCT = r"((alternatively|consequently|conversely|eg|furthermore|hence|however|ie|instead|likewise|moreover|namely|nevertheless|nonetheless|notwithstanding|otherwise|similarly|therefore|thus|viz)_\S+|in_\S+ (comparison|contrast|particular|addition|conclusion|consequence|sum|summary|any_\S+ event|any_\S+ case|other_\S+ words)_\S+|for_\S+ (example|instance)_\S+|instead_\S+ of_\S+|by_\S+ (contrast|comparison)_|as_\S+ a_\S+ (result|consequence)_\S+|on_\S+ the_\S+ (contrary|other_\S+ hand)_\S+)"
DOWNTONER = r"(almost|barely|hardly|merely|mildly|nearly|only|partially|partly|practically|scarcely|slightly|somewhat)_\S+"
AMPLIFIER = rf"(absolutely|altogether|completely|enormously|entirely|extremely|fully|greatly|highly|intensely|perfectly|strongly|thoroughly|totally|utterly|very)_\S+"
HEDGE = rf"(maybe|at_\S+ about|something_\S+ like|more_\S+ or_\S+ less)_\S+| \b(?:(?!{NMOD}|{WHO})\S)+ (sort|kind)_\S+ of_\S+"
EMPHATICS = rf"((just|really|most|more)_\S+|(real|so)_\S+ {ADJ}|{DO} {VERB}|for_\S+ sure_\S+|a_\S+ lot_\S+|such_\S+ an?_\S+)"
