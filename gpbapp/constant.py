#! /usr/bin/env python
# coding: utf-8

STOP_WORD = ["a","abord","absolument","adresse","afin","ah","ai","aie","ailleurs","ainsi","aime","ait","allaient","allo","allons","allô","alors","anterieur","anterieure","anterieures","ami","amie","apres","après","as","assez","attendu","au","aucun","aucune","aujourd","aujourd'hui","aupres","auquel","aura","auraient","aurait","auront","aussi","autre","autrefois","autrement","autres","autrui","aux","auxquelles","auxquels","avaient","avais","avait","avant","avec","avoir","avons","ayant","b","bah","bas","basee","bat","beau","beaucoup","bien","bigre","bonjour","boum","bravo","brrr","c","car","ce","ceci","cela","celle","celle-ci","celle-là","celles","celles-ci","celles-là","celui","celui-ci","celui-là","cent","cependant","certain","certaine","certaines","certains","certes","ces","cet","cette","ceux","ceux-ci","ceux-là","chacun","chacune","chaque","cher","chers","chez","chiche","chut","chère","chères","ci","cinq","cinquantaine","cinquante","cinquantième","cinquième","clac","clic","combien","comme","comment","comparable","comparables","compris","concernant","contre","connait","connaitre","connais","couic","crac","d","da","dans","de","debout","dedans","dehors","deja","delà","depuis","dernier","derniere","derriere","derrière","des","desormais","desquelles","desquels","dessous","dessus","deux","deuxième","deuxièmement","devant","devers","devra","different","differentes","differents","différent","différente","différentes","différents","dire","directe","directement","dit","dite","dits","divers","diverse","diverses","dix","dix-huit","dix-neuf","dix-sept","dixième","doit","doivent","donc","dont","donne","donner","douze","douzième","dring","du","duquel","durant","dès","désormais","e","effet","egale","egalement","egales","eh","elle","elle-même","elles","elles-mêmes","en","encore","enfin","entre","envers","environ","es","est","et","etant","etc","etre","eu","euh","eux","eux-mêmes","exactement","excepté","extenso","exterieur","f","fais","faisaient","faisant","fait","façon","feront","fi","flac","floc","font","g","garage","gens","grandpy","grandpybot","gros","grosse","h","ha","hein","hem","hep","hi","ho","holà","hop","hormis","hors","hou","houp","hue","hui","huit","huitième","hum","hurrah","hé","hélas","i","il","ils","importe","j","je","jusqu","jusque","juste","k","l","la","laisser","laquelle","las","le","lequel","les","lesquelles","lesquels","leur","leurs","longtemps","lors","lorsque","lui","lui-meme","lui-même","là","lès","m","ma","maint","maintenant","mais","malgre","malgré","maximale","me","meme","memes","merci","mes","mien","mienne","miennes","miens","mille","mince","minimale","moi","moi-meme","moi-même","moindres","moins","mon","moyennant","multiple","multiples","même","mêmes","n","na","naturel","naturelle","naturelles","ne","neanmoins","necessaire","necessairement","neuf","neuvième","ni","nombreuses","nombreux","non","nos","notamment","notre","nous","nous-mêmes","nouveau","nul","néanmoins","nôtre","nôtres","o","obtenir","obtiens","obtiens","oh","ohé","ollé","olé","on","ont","onze","onzième","ore","ou","ouf","ouias","oust","ouste","outre","ouvert","ouverte","ouverts","ô","où","p","paf","pan","par","parce","parfois","parle","parlent","parler","parmi","parseme","partant","particulier","particulière","particulièrement","pas","passé","pendant","pense","permet","personne","peu","peut","peuvent","peux","pff","pfft","pfut","pif","pire","plait","plein","plouf","plus","plusieurs","plutôt","possessif","possessifs","possible","possibles","pote","poto","pouah","pour","pourquoi","pourrais","pourrait","pouvait","prealable","precisement","premier","première","premièrement","pres","probable","probante","procedant","proche","près","psitt","pu","puis","puisque","pur","pure","q","qu","quand","quant","quant-à-soi","quanta","quarante","quatorze","quatre","quatre-vingt","quatrième","quatrièmement","que","quel","quelconque","quelle","quelles","quelqu'un","quelque","quelques","quels","qui","quiconque","quinze","quoi","quoique","r","rare","rarement","rares","relative","relativement","remarquable","rend","rendre","restant","reste","restent","restrictif","retour","revoici","revoilà","rien","s","sa","sacrebleu","sait","salut","sans","sapristi","sauf","se","sein","seize","selon","semblable","semblaient","semble","semblent","sent","sept","septième","sera","seraient","serait","seront","ses","seul","seule","seulement","si","sien","sienne","siennes","siens","sinon","six","sixième","soi","soi-même","soit","soixante","son","sont","sous","souvent","specifique","specifiques","speculatif","stop","strictement","subtiles","suffisant","suffisante","suffit","suis","suit","suivant","suivante","suivantes","suivants","suivre","superpose","sur","surtout","t","ta","tac","tant","tardive","te","tel","telle","tellement","telles","tels","tenant","tend","tenir","tente","tes","tic","tien","tienne","tiennes","tiens","toc","toi","toi-même","ton","touchant","toujours","tous","tout","toute","toutefois","toutes","treize","trente","tres","trois","troisième","troisièmement","trop","trouver","très","tsoin","tsouin","tu","té","u","un","une","unes","uniformement","unique","uniques","uns","v","va","vais","vas","vers","veut","via","vif","vifs","vingt","vivat","vive","vives","vlan","voici","voilà","vont","vos","votre","voudrais","vous","vous-mêmes","vu","vé","vôtre","vôtres","w","x","y","z","zut","à","â","ça","ès","étaient","étais","était","étant","été","être","ô"]

API_KEY = "AIzaSyAe9CeEUswtLQ21TiWLtkt4kXZQFSSYuQQ"

STORY = ["Mais faut que je te raconte mon histoire, c'est ici que j'ai rencontré grandMy, par un soir de pleine lune. Elle était assise sur le capot de sa Peugeot 205 GTI et moi, j'étais au volant de ma citroen saxo VTS, autant te dire que pour l'époque, c'étaient deux voitures taillées pour la course. Je me suis placé à sa hauteur et je lui ai proposé une balade plutôt sportive pour voir si la voiture pouvait faire la différence ou si se serais le conducteur.", "Mon petit canard, ce lieu aura eu l'honneur de voir grandPy faire du monocycle en chaussette, hé oui !!!", "Tiens, ça me fait penser qu'avec mon oncle Boty, on était présent sur les lieus quand soudain, le tigre du cirque qui était de passage et qui s'était évader, c'est retrouver nez à nez avec nous. Oncle Boty avait abusé du jus de pomme de grandMy. En voyant la bête, il a tellement eu peur qu'il c'est totalement laissé aller... Je ne t'explique pas l'état du pantalon.", "Attention, cet endroit n'est pas sûr gamin, c'est ici que deux voyous m'ont laissé piéton après avoir réussi à me prendre ma mobylette toute neuve. Donc fais attention à toi et à ta monture.", "Ahah, écoute bien mon poussin, c'est précisément ici que l'oncle Boty m'avais mit au défi de faire un kilomètre sur un seul pied et en claquette chaussette par-dessus le marché. Heureusement pour moi dans ma jeunesse, j'étais sportif et oncle Boty a été obligé d'avouer ma victoire."]