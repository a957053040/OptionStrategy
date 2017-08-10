import matplotlib.pyplot as plt
import numpy as np
import datetime
import plot_util as pu

def Date(d,m,y):
    dt = datetime.date(y,m,d)
    return dt
sse_bs2 =  {Date(2,12,2016): 0.021773731624818448, Date(5,12,2016): 0.014379582314893929, Date(6,12,2016): 0.011850249309545062, Date(7,12,2016): 0.02032940691628889, Date(8,12,2016): 0.0283121416943723, Date(9,12,2016): 0.033715543779210294, Date(12,12,2016): 0.017197102579944272, Date(13,12,2016): 0.014608576063454545, Date(14,12,2016): 0.014369704610904482, Date(15,12,2016): 0.010664965134832444, Date(16,12,2016): 0.012697103051791584, Date(19,12,2016): 0.02390580838417724, Date(20,12,2016): 0.05289131053864914, Date(21,12,2016): 0.023989784826995274, Date(22,12,2016): 0.02101433778496755, Date(23,12,2016): 0.031357919885004665, Date(26,12,2016): 0.033073210265287645, Date(27,12,2016): 0.026173641676931467, Date(28,12,2016): 0.024995259691856096, Date(29,12,2016): 0.01178887226344672, Date(30,12,2016): 0.01245470685069835, Date(3,1,2017): 0.008670694993334647, Date(4,1,2017): 0.01706195484157167, Date(5,1,2017): 0.01684219386991765, Date(6,1,2017): 0.013704802508770654, Date(9,1,2017): 0.011277607201499479, Date(10,1,2017): 0.007118440447376363, Date(11,1,2017): 0.010443056602689687, Date(12,1,2017): 0.012258808153089478, Date(13,1,2017): 0.015741281516670952, Date(16,1,2017): 0.0408661172298387, Date(17,1,2017): 0.01450771074925527, Date(18,1,2017): 0.013369319882787407, Date(19,1,2017): 0.007503896136294112, Date(20,1,2017): 0.006926416731539816, Date(23,1,2017): 0.00336690009836523, Date(24,1,2017): 0.005010566772272855, Date(25,1,2017): 0.0057190333878799696, Date(26,1,2017): 0.0048518574993679725, Date(3,2,2017): 0.0038125988159429425, Date(6,2,2017): 0.0038060658555530845, Date(7,2,2017): 0.004208602323527047, Date(8,2,2017): 0.005501428198384265, Date(9,2,2017): 0.003928156360300062, Date(10,2,2017): 0.005540706161983302, Date(13,2,2017): 0.009150599876107609, Date(14,2,2017): 0.006587747190880724, Date(15,2,2017): 0.004477298854792587, Date(16,2,2017): 0.0049710277760413365, Date(17,2,2017): 0.004675047856864376, Date(20,2,2017): 0.008126158163218898, Date(21,2,2017): 0.005502519644683561, Date(22,2,2017): 0.006747173261708599, Date(23,2,2017): 0.006573132506061778, Date(24,2,2017): 0.004267554587939731, Date(27,2,2017): 0.0032093226563237112, Date(28,2,2017): 0.004092050623558416, Date(1,3,2017): 0.003784232888356775, Date(2,3,2017): 0.003558162819346998, Date(3,3,2017): 0.003987415150568739, Date(6,3,2017): 0.006620924677299948, Date(7,3,2017): 0.008265080955441921, Date(8,3,2017): 0.008996863756652672, Date(9,3,2017): 0.01457626298604996, Date(10,3,2017): 0.011150145591022937, Date(13,3,2017): 0.012660915645225937, Date(14,3,2017): 0.011546560100419774, Date(15,3,2017): 0.01479023771278795, Date(16,3,2017): 0.011095762767941348, Date(17,3,2017): 0.008958372448096472, Date(20,3,2017): 0.008820259390407544, Date(21,3,2017): 0.01076655841176158, Date(22,3,2017): 0.010353085529540812, Date(23,3,2017): 0.012805609589626999, Date(24,3,2017): 0.008745505717166252, Date(27,3,2017): 0.007826533918238258, Date(28,3,2017): 0.007057570222142303, Date(29,3,2017): 0.006853734855214788, Date(30,3,2017): 0.004067733978730203, Date(31,3,2017): 0.005955478994496848, Date(5,4,2017): 0.005943579774449891, Date(6,4,2017): 0.0074861954187276205, Date(7,4,2017): 0.008799845965319837, Date(10,4,2017): 0.0055112329363160425, Date(11,4,2017): 0.006465579699356073, Date(12,4,2017): 0.01112005887937461, Date(13,4,2017): 0.004555165423071635, Date(14,4,2017): 0.0032513417483165633, Date(17,4,2017): 0.004790452842960772, Date(18,4,2017): 0.0036404123001800006, Date(19,4,2017): 0.004620972600796142, Date(20,4,2017): 0.007257689591069675, Date(21,4,2017): 0.009513713525104049, Date(24,4,2017): 0.00946863309758829, Date(25,4,2017): 0.00942258485063292, Date(26,4,2017): 0.005839023703350105, Date(27,4,2017): 0.013212977902741072, Date(28,4,2017): 0.011581899781884989, Date(2,5,2017): 0.008209375748691142, Date(3,5,2017): 0.008727582850217132, Date(4,5,2017): 0.009401699916544349, Date(5,5,2017): 0.013514411378896517, Date(8,5,2017): 0.012950029771438424, Date(9,5,2017): 0.00894846993517653, Date(10,5,2017): 0.010286392139795127, Date(11,5,2017): 0.012790339359903174, Date(12,5,2017): 0.022020278852775414, Date(15,5,2017): 0.017349113775090415, Date(16,5,2017): 0.01819211018853899, Date(17,5,2017): 0.010947304117783501, Date(18,5,2017): 0.01058275859463851, Date(19,5,2017): 0.012154837061727874, Date(22,5,2017): 0.019743313200076884, Date(23,5,2017): 0.02772449773580871, Date(24,5,2017): 0.02118573033236668, Date(25,5,2017): 0.01947877475611705, Date(26,5,2017): 0.017666836657741845, Date(31,5,2017): 0.012934431034689215, Date(1,6,2017): 0.01449590523122907, Date(2,6,2017): 0.008903968980709031, Date(5,6,2017): 0.007285145222005873, Date(6,6,2017): 0.009882739184153735, Date(7,6,2017): 0.011632816862171306, Date(8,6,2017): 0.005887882999644069, Date(9,6,2017): 0.009185053725314498, Date(12,6,2017): 0.014167824971498374, Date(13,6,2017): 0.009810226225857734, Date(14,6,2017): 0.00502270067072603, Date(15,6,2017): 0.005160484670630142, Date(16,6,2017): 0.008047761634497712, Date(19,6,2017): 0.0076013621675189505, Date(20,6,2017): 0.005424776186742709, Date(21,6,2017): 0.009583809725072268, Date(22,6,2017): 0.007009428440732161, Date(23,6,2017): 0.007789604157770617, Date(26,6,2017): 0.006076360698362123, Date(27,6,2017): 0.0074479097449322105, Date(28,6,2017): 0.006142173133054542, Date(29,6,2017): 0.008212333727197407, Date(30,6,2017): 0.00620011463055479, Date(3,7,2017): 0.006927268195773195, Date(4,7,2017): 0.006898398824911087, Date(5,7,2017): 0.008441834387463704, Date(6,7,2017): 0.007527018805684854, Date(7,7,2017): 0.007558960936715748, Date(10,7,2017): 0.011688521873144241, Date(11,7,2017): 0.008606401899264406, Date(12,7,2017): 0.00931016554402342, Date(13,7,2017): 0.012310286330681848, Date(14,7,2017): 0.011299479298929757, Date(17,7,2017): 0.0027466487939234235, Date(18,7,2017): 0.005358195399871529, Date(19,7,2017): 0.0056386007298748365, Date(20,7,2017): 0.004867088045152872}
sse_svi =  {Date(2,12,2016): 0.007281354428249263, Date(5,12,2016): 0.001255098151194368, Date(6,12,2016): 0.002107071323859257, Date(7,12,2016): 0.0057386417539824494, Date(8,12,2016): 0.012230333992169155, Date(9,12,2016): 0.016918059764510267, Date(12,12,2016): 0.0028082156037314682, Date(13,12,2016): 0.0005918347292810003, Date(14,12,2016): 0.0005952909123899134, Date(15,12,2016): 0.0008749758602790515, Date(16,12,2016): 0.0031378165881493624, Date(19,12,2016): 0.007127933834007291, Date(20,12,2016): 0.07060966330212647, Date(21,12,2016): 0.006607848513085409, Date(22,12,2016): 0.004839864391244699, Date(23,12,2016): 0.03396496130984608, Date(26,12,2016): 0.038557092758732356, Date(27,12,2016): 0.018796216002596296, Date(28,12,2016): 0.013553304774910627, Date(3,1,2017): 0.0010872591019071439, Date(4,1,2017): 0.00506798806879255, Date(5,1,2017): 0.0038818761456364545, Date(6,1,2017): 0.003103967273781797, Date(9,1,2017): 0.0005452807612816687, Date(10,1,2017): 0.0008902755151071163, Date(11,1,2017): 0.000593060476458495, Date(12,1,2017): 0.001143003277234582, Date(13,1,2017): 0.017412323877837484, Date(16,1,2017): 0.09229025970190025, Date(17,1,2017): 0.011138711483188712, Date(18,1,2017): 0.00536297071026169, Date(19,1,2017): 0.000576380026150618, Date(20,1,2017): 0.0007340825271280537, Date(23,1,2017): 0.001535358864500424, Date(24,1,2017): 0.00028051454268469844, Date(25,1,2017): 0.0009153917323617747, Date(3,2,2017): 0.0037235625246902133, Date(6,2,2017): 0.0035733529615338305, Date(7,2,2017): 0.0028930151817865455, Date(8,2,2017): 0.0018279519164203333, Date(9,2,2017): 0.0032208975755482296, Date(10,2,2017): 0.0015345599275932702, Date(13,2,2017): 0.0003566399634300554, Date(14,2,2017): 0.0010289772063297774, Date(15,2,2017): 0.0021387928783639047, Date(16,2,2017): 0.0015740568644045426, Date(17,2,2017): 0.0020377186414008664, Date(20,2,2017): 0.00017186091338902113, Date(21,2,2017): 0.0009172686935838874, Date(22,2,2017): 0.0011633690432262713, Date(1,3,2017): 0.0026883500599305644, Date(2,3,2017): 0.0030766646767453527, Date(3,3,2017): 0.002599656651999433, Date(6,3,2017): 0.001427372021308628, Date(7,3,2017): 0.0008559027488118489, Date(8,3,2017): 0.000679471129733297, Date(9,3,2017): 'NAN', Date(10,3,2017): 0.0012007111630688864, Date(13,3,2017): 0.004184983666587765, Date(14,3,2017): 0.002499526179521333, Date(15,3,2017): 0.01289464229880658, Date(16,3,2017): 0.0019871470990239217, Date(17,3,2017): 0.00027546357581856925, Date(20,3,2017): 4.839730044251323e-05, Date(21,3,2017): 0.001034393638946397, Date(22,3,2017): 0.002570317678090863, Date(5,4,2017): 0.000462603195994986, Date(6,4,2017): 0.0003878348017385704, Date(7,4,2017): 0.0004296185818825368, Date(10,4,2017): 0.00031347341282335817, Date(11,4,2017): 0.00016247965923619906, Date(12,4,2017): 0.002584448740275049, Date(13,4,2017): 0.000269680084868562, Date(14,4,2017): 0.0006149306744359503, Date(17,4,2017): 0.00019346604027293922, Date(18,4,2017): 0.0005726178463884807, Date(19,4,2017): 'NAN', Date(20,4,2017): 5.8898267470021775e-05, Date(21,4,2017): 0.0022431864099481612, Date(24,4,2017): 0.0018885702714881612, Date(25,4,2017): 0.0016181828580277707, Date(26,4,2017): 0.00017877951483291648, Date(2,5,2017): 0.0005123707817592839, Date(3,5,2017): 0.0004042149979081409, Date(4,5,2017): 0.0001956583999589932, Date(5,5,2017): 0.00015263417175746227, Date(8,5,2017): 0.00014933235349151225, Date(9,5,2017): 0.0006393225504746966, Date(10,5,2017): 0.0005662988963005308, Date(11,5,2017): 0.0002004850771565892, Date(12,5,2017): 0.009754338289198698, Date(15,5,2017): 0.004140142027551714, Date(16,5,2017): 0.003737567896729384, Date(17,5,2017): 0.0003942907934829293, Date(18,5,2017): 0.00042662807048252685, Date(19,5,2017): 9.968454896464793e-05, Date(22,5,2017): 0.006326528533617393, Date(23,5,2017): 0.014915004166746468, Date(24,5,2017): 0.006199478728010772, Date(1,6,2017): 0.0005445804828787815, Date(2,6,2017): 0.0013897097295377879, Date(5,6,2017): 0.0020075065399830557, Date(6,6,2017): 0.0009516304874966755, Date(7,6,2017): 0.0004513683157727075, Date(8,6,2017): 0.002827421626182244, Date(9,6,2017): 0.0008863944578582368, Date(12,6,2017): 0.001104583124502801, Date(13,6,2017): 0.0008907788953929415, Date(14,6,2017): 0.004092740618474986, Date(15,6,2017): 0.004236789375067349, Date(16,6,2017): 0.0016650608905758907, Date(19,6,2017): 0.0019004356612221985, Date(20,6,2017): 0.0034773045749640855, Date(21,6,2017): 0.0014153081917469615, Date(22,6,2017): 0.0017936205712940092, Date(23,6,2017): 0.0020833302247411606, Date(26,6,2017): 0.0026390670454316794, Date(27,6,2017): 0.0015237239241067215, Date(28,6,2017): 0.001752722985945572, Date(3,7,2017): 0.001155487129988529, Date(4,7,2017): 0.0010248295673537177, Date(5,7,2017): 0.0006171361546632658, Date(6,7,2017): 0.0008901831428774472, Date(7,7,2017): 0.00066691669902742, Date(10,7,2017): 0.0003162676449420163, Date(11,7,2017): 0.0004002183973258158, Date(12,7,2017): 0.0004065615853894415, Date(13,7,2017): 0.08674942231070434, Date(14,7,2017): 0.0006766654833722321, Date(17,7,2017): 0.0038434868161747473, Date(18,7,2017): 0.0013763825160737382, Date(19,7,2017): 0.0009084996351854986, Date(20,7,2017): 0.0021571229246838035}
#sse_svi2 =  {Date(2,12,2016): 0.09475596309634078, Date(5,12,2016): 0.0014785086500241791, Date(6,12,2016): 0.002196495952193252, Date(7,12,2016): 0.005861393383829583, Date(8,12,2016): 0.012176308756709452, Date(9,12,2016): 0.08136414474180799, Date(12,12,2016): 0.0030180987905378633, Date(13,12,2016): 0.0011339158673648135, Date(14,12,2016): 0.0006858291218972531, Date(15,12,2016): 0.0009147219713688035, Date(16,12,2016): 0.0012517730800400183, Date(19,12,2016): 0.07901568983249813, Date(20,12,2016): 0.07031297792028696, Date(21,12,2016): 0.19152461491036996, Date(22,12,2016): 0.004784118935182471, Date(23,12,2016): 0.10610435037731705, Date(26,12,2016): 0.03798458261176886, Date(27,12,2016): 0.018765331657053963, Date(28,12,2016): 0.23760918647604615, Date(3,1,2017): 0.001443460939306823, Date(4,1,2017): 0.004948871290065393, Date(5,1,2017): 0.004061953020148156, Date(6,1,2017): 0.003366739806284645, Date(9,1,2017): 0.000591140601409827, Date(10,1,2017): 0.0011671871365971551, Date(11,1,2017): 0.0007150312879252994, Date(12,1,2017): 0.001028501114688315, Date(13,1,2017): 0.04142656584155181, Date(16,1,2017): 0.31843395580525163, Date(17,1,2017): 0.011284459167541736, Date(18,1,2017): 0.005403827265758552, Date(19,1,2017): 0.0006361457261499257, Date(20,1,2017): 0.0006534923055423571, Date(23,1,2017): 0.0014906816849152775, Date(24,1,2017): 0.0003094129010571147, Date(25,1,2017): 0.001056928725062438, Date(3,2,2017): 0.003845395244890419, Date(6,2,2017): 0.0037903535888146427, Date(7,2,2017): 0.003031865960808163, Date(8,2,2017): 0.0019112046872112444, Date(9,2,2017): 0.003448718329731001, Date(10,2,2017): 'NAN', Date(13,2,2017): 0.0008573656356403106, Date(14,2,2017): 0.0012874615954334076, Date(15,2,2017): 0.004885335697143626, Date(16,2,2017): 'NAN', Date(17,2,2017): 0.005329034203702965, Date(20,2,2017): 0.0006765540903401568, Date(21,2,2017): 0.004206943680165643, Date(22,2,2017): 0.005225090443310954, Date(1,3,2017): 0.002790950413244347, Date(2,3,2017): 0.0029817863981821927, Date(3,3,2017): 0.0024554557601028752, Date(6,3,2017): 0.0014266660423743569, Date(7,3,2017): 0.0009377513532881633, Date(8,3,2017): 0.0006667254181726241, Date(9,3,2017): 0.005076021859877815, Date(10,3,2017): 0.0015045490056479543, Date(13,3,2017): 0.003500098302632165, Date(14,3,2017): 0.002683493284789632, Date(15,3,2017): 0.012061815051279194, Date(16,3,2017): 0.002001504994567154, Date(17,3,2017): 0.0004389320127432651, Date(20,3,2017): 0.00022093581151451475, Date(21,3,2017): 0.0009087843106318735, Date(22,3,2017): 0.019011784863581748, Date(5,4,2017): 0.00041650412328888436, Date(6,4,2017): 0.0002718121064561641, Date(7,4,2017): 0.0005634684422232394, Date(10,4,2017): 0.0002791784908298951, Date(11,4,2017): 0.00020333006920239343, Date(12,4,2017): 0.0025374341384276694, Date(13,4,2017): 0.00026767845868616303, Date(14,4,2017): 0.0005097024817525476, Date(17,4,2017): 0.0002647552069537073, Date(18,4,2017): 0.0020851967535482677, Date(19,4,2017): 0.00043075675665209625, Date(20,4,2017): 0.00016158256297140123, Date(21,4,2017): 0.010688344795686516, Date(24,4,2017): 'NAN', Date(25,4,2017): 0.0016957596067671578, Date(26,4,2017): 0.00021517252919860786, Date(2,5,2017): 0.0007152928981244975, Date(3,5,2017): 0.0006570495103325188, Date(4,5,2017): 0.00031419875206735155, Date(5,5,2017): 0.0005578215258775624, Date(8,5,2017): 0.0006056155178385313, Date(9,5,2017): 0.0009642312251825849, Date(10,5,2017): 0.0017795965998304254, Date(11,5,2017): 0.0005758253184421645, Date(12,5,2017): 0.01740309443203925, Date(15,5,2017): 0.004063802106723956, Date(16,5,2017): 0.0035706323231199885, Date(17,5,2017): 0.0007220907953228044, Date(18,5,2017): 0.0007875987679464929, Date(19,5,2017): 0.006006226592641296, Date(22,5,2017): 0.005297947480482606, Date(23,5,2017): 0.01766631877615758, Date(24,5,2017): 0.009147392252495752, Date(1,6,2017): 0.0004708806143933263, Date(2,6,2017): 0.0013223426528948421, Date(5,6,2017): 0.0020037598409149153, Date(6,6,2017): 0.0009263516498550362, Date(7,6,2017): 0.00048568268040773805, Date(8,6,2017): 0.0022331498729004553, Date(9,6,2017): 0.0009277654906849652, Date(12,6,2017): 0.0011401972123570435, Date(13,6,2017): 0.0009383449295111919, Date(14,6,2017): 0.003533949326345977, Date(15,6,2017): 0.003052063148082514, Date(16,6,2017): 0.0015444511143032906, Date(19,6,2017): 0.001468111947618487, Date(20,6,2017): 0.01741234351232627, Date(21,6,2017): 0.0011952618665754975, Date(22,6,2017): 0.0016987427593179638, Date(23,6,2017): 0.0021165277548460355, Date(26,6,2017): 0.0020250021412005943, Date(27,6,2017): 0.023080338974421653, Date(28,6,2017): 0.0017636557987589004, Date(3,7,2017): 0.0011753414310318872, Date(4,7,2017): 0.002908069474312455, Date(5,7,2017): 0.0006899512624337932, Date(6,7,2017): 0.0009523286620608448, Date(7,7,2017): 0.0009169060506419245, Date(10,7,2017): 0.0006259502217649097, Date(11,7,2017): 0.00027681564876076573, Date(12,7,2017): 0.05633827658475852, Date(13,7,2017): 0.019403928841137032, Date(14,7,2017): 0.0015233965619247637, Date(17,7,2017): 0.003874254096812609, Date(18,7,2017): 0.0018166152488687413, Date(19,7,2017): 0.001204677815419483, Date(20,7,2017): 0.0449960752949125}
#sse_svi3 =  {Date(2,12,2016): 0.007228266745447604, Date(5,12,2016): 0.0012113415331844921, Date(6,12,2016): 0.002098142211016923, Date(7,12,2016): 0.0059972342513573, Date(8,12,2016): 0.07303795585285743, Date(9,12,2016): 0.016848234864553245, Date(12,12,2016): 0.14105091382397275, Date(13,12,2016): 0.0012934261154944413, Date(14,12,2016): 0.0010553137885044772, Date(15,12,2016): 0.0009730080830257243, Date(16,12,2016): 0.0014334332526802452, Date(19,12,2016): 0.007033716414929648, Date(20,12,2016): 0.2880643504761589, Date(21,12,2016): 0.006717669069253254, Date(22,12,2016): 0.004953663421838843, Date(23,12,2016): 0.033156982709985294, Date(26,12,2016): 'NAN', Date(27,12,2016): 0.019277940162074843, Date(28,12,2016): 0.013062786669942225, Date(3,1,2017): 0.001330183391311787, Date(4,1,2017): 0.004939517679438367, Date(5,1,2017): 0.03956501104720564, Date(6,1,2017): 0.0033442678685593453, Date(9,1,2017): 0.0005484749420502465, Date(10,1,2017): 0.0010470829505763444, Date(11,1,2017): 0.0006874831185404727, Date(12,1,2017): 0.0010942104525836955, Date(13,1,2017): 'NAN', Date(16,1,2017): 0.3185239739809695, Date(17,1,2017): 0.030262184050783514, Date(18,1,2017): 0.027608550119088887, Date(19,1,2017): 0.0005964875984945122, Date(20,1,2017): 0.0007296295239076105, Date(23,1,2017): 0.0015100044586711316, Date(24,1,2017): 0.0003476184917381901, Date(25,1,2017): 0.0009902847036605022, Date(3,2,2017): 0.0035017287326768753, Date(6,2,2017): 0.0038226800124677904, Date(7,2,2017): 0.0029714412447055067, Date(8,2,2017): 0.0018710985596811112, Date(9,2,2017): 0.003444978679598814, Date(10,2,2017): 0.0018175664396613562, Date(13,2,2017): 0.00036353360014664655, Date(14,2,2017): 0.0010311441148029604, Date(15,2,2017): 0.0027697922981303785, Date(16,2,2017): 0.004201184347567686, Date(17,2,2017): 0.002535940736587985, Date(20,2,2017): 0.000740236672867357, Date(21,2,2017): 0.0041316993844457105, Date(22,2,2017): 0.0013224188792309594, Date(1,3,2017): 0.002789859649269224, Date(2,3,2017): 0.003042160517296403, Date(3,3,2017): 0.002562605636375799, Date(6,3,2017): 0.0013755222438256792, Date(7,3,2017): 0.0009640488288050998, Date(8,3,2017): 0.0006601848317798136, Date(9,3,2017): 0.004605887824076021, Date(10,3,2017): 0.0014767854378606447, Date(13,3,2017): 'NAN', Date(14,3,2017): 0.005209332130068039, Date(15,3,2017): 0.012744874690093822, Date(16,3,2017): 0.001974818294954814, Date(17,3,2017): 0.00030424496389382365, Date(20,3,2017): 0.00015252491534205955, Date(21,3,2017): 0.001070170494598605, Date(22,3,2017): 0.0025754983841556702, Date(5,4,2017): 0.00042762845606867425, Date(6,4,2017): 0.0002643505289233875, Date(7,4,2017): 0.0005768450521570891, Date(10,4,2017): 0.000293337767230933, Date(11,4,2017): 0.0002987725898213147, Date(12,4,2017): 0.0025383694700907566, Date(13,4,2017): 0.00028536369268451436, Date(14,4,2017): 0.0005837331759390277, Date(17,4,2017): 0.0002331339145448618, Date(18,4,2017): 0.000665876562948207, Date(19,4,2017): 'NAN', Date(20,4,2017): 0.0003317565258785902, Date(21,4,2017): 0.002326384767504066, Date(24,4,2017): 0.007329973555785097, Date(25,4,2017): 0.0018040093349586009, Date(26,4,2017): 0.0003843224536247797, Date(2,5,2017): 0.0006744943778692899, Date(3,5,2017): 0.0004225282594865639, Date(4,5,2017): 0.0004967574098596291, Date(5,5,2017): 0.0006356695841172057, Date(8,5,2017): 0.0006414454202447523, Date(9,5,2017): 0.001011765564453884, Date(10,5,2017): 0.000757912619786173, Date(11,5,2017): 0.0005849067085224636, Date(12,5,2017): 0.00965727227490584, Date(15,5,2017): 0.006056289080490676, Date(16,5,2017): 0.003404471111643262, Date(17,5,2017): 0.0008203879336161102, Date(18,5,2017): 0.0008373277709673216, Date(19,5,2017): 0.000521862430300666, Date(22,5,2017): 0.005660091280300561, Date(23,5,2017): 0.01754878867548754, Date(24,5,2017): 0.009042186701958544, Date(1,6,2017): 0.0004705380718782044, Date(2,6,2017): 0.0012226960684421516, Date(5,6,2017): 0.0019155661519274047, Date(6,6,2017): 0.0009505224194898041, Date(7,6,2017): 0.00038507223932262994, Date(8,6,2017): 0.06845652989284341, Date(9,6,2017): 0.0006614833027349821, Date(12,6,2017): 0.0011452751393954425, Date(13,6,2017): 0.0007327638808578424, Date(14,6,2017): 0.003710845090889128, Date(15,6,2017): 0.0030852612538117712, Date(16,6,2017): 0.0011999308237067678, Date(19,6,2017): 0.001959647803833089, Date(20,6,2017): 0.002723719842620648, Date(21,6,2017): 0.001473791100618291, Date(22,6,2017): 0.001280281624681126, Date(23,6,2017): 0.0019080013248444015, Date(26,6,2017): 0.007841189491484043, Date(27,6,2017): 0.0015423240772754867, Date(28,6,2017): 0.0014132501827671612, Date(3,7,2017): 0.0010240525795054344, Date(4,7,2017): 0.0008442226869140763, Date(5,7,2017): 0.00057886553655647, Date(6,7,2017): 0.0009886025962133765, Date(7,7,2017): 0.000721845485439817, Date(10,7,2017): 0.0005316565647832254, Date(11,7,2017): 0.00033605128846938973, Date(12,7,2017): 0.0005098708700304514, Date(13,7,2017): 0.01938354274710904, Date(14,7,2017): 0.0016609364960134996, Date(17,7,2017): 0.09052072772740109, Date(18,7,2017): 0.0014795007625504257, Date(19,7,2017): 0.0013111875560384426, Date(20,7,2017): 0.0017705073329359743}
sse_bs =  {Date(2,12,2016): 0.021773731624818448, Date(5,12,2016): 0.014379582314893929, Date(6,12,2016): 0.011850249309545062, Date(7,12,2016): 0.02032940691628889, Date(8,12,2016): 0.0283121416943723, Date(9,12,2016): 0.033715543779210294, Date(12,12,2016): 0.017197102579944272, Date(13,12,2016): 0.014608576063454545, Date(14,12,2016): 0.014369704610904482, Date(15,12,2016): 0.010664965134832444, Date(16,12,2016): 0.012697103051791584, Date(19,12,2016): 0.02390580838417724, Date(20,12,2016): 0.05289131053864914, Date(21,12,2016): 0.023989784826995274, Date(22,12,2016): 0.02101433778496755, Date(23,12,2016): 0.031357919885004665, Date(26,12,2016): 0.033073210265287645, Date(27,12,2016): 0.026173641676931467, Date(28,12,2016): 0.6982046196918565, Date(29,12,2016): 0.01178887226344672, Date(30,12,2016): 0.01245470685069835, Date(3,1,2017): 0.008670694993334647, Date(4,1,2017): 0.01706195484157167, Date(5,1,2017): 0.01684219386991765, Date(6,1,2017): 0.013704802508770654, Date(9,1,2017): 0.011277607201499479, Date(10,1,2017): 0.007118440447376363, Date(11,1,2017): 0.010443056602689687, Date(12,1,2017): 0.012258808153089478, Date(13,1,2017): 0.015741281516670952, Date(16,1,2017): 0.0408661172298387, Date(17,1,2017): 0.01450771074925527, Date(18,1,2017): 0.013369319882787407, Date(19,1,2017): 0.007503896136294112, Date(20,1,2017): 0.006926416731539816, Date(23,1,2017): 0.00336690009836523, Date(24,1,2017): 0.005010566772272855, Date(25,1,2017): 0.15415250338787995, Date(26,1,2017): 0.0048518574993679725, Date(3,2,2017): 0.0038125988159429425, Date(6,2,2017): 0.0038060658555530845, Date(7,2,2017): 0.004208602323527047, Date(8,2,2017): 0.005501428198384265, Date(9,2,2017): 0.003928156360300062, Date(10,2,2017): 0.005540706161983302, Date(13,2,2017): 0.009150599876107609, Date(14,2,2017): 0.006587747190880724, Date(15,2,2017): 0.004477298854792587, Date(16,2,2017): 0.0049710277760413365, Date(17,2,2017): 0.004675047856864376, Date(20,2,2017): 0.008126158163218898, Date(21,2,2017): 0.005502519644683561, Date(22,2,2017): 0.08932959326170858, Date(23,2,2017): 0.006573132506061778, Date(24,2,2017): 0.004267554587939731, Date(27,2,2017): 0.0032093226563237112, Date(28,2,2017): 0.004092050623558416, Date(1,3,2017): 0.003784232888356775, Date(2,3,2017): 0.003558162819346998, Date(3,3,2017): 0.003987415150568739, Date(6,3,2017): 0.006620924677299948, Date(7,3,2017): 0.008265080955441921, Date(8,3,2017): 0.008996863756652672, Date(9,3,2017): 0.01457626298604996, Date(10,3,2017): 0.011150145591022937, Date(13,3,2017): 0.012660915645225937, Date(14,3,2017): 0.011546560100419774, Date(15,3,2017): 0.01479023771278795, Date(16,3,2017): 0.011095762767941348, Date(17,3,2017): 0.008958372448096472, Date(20,3,2017): 0.008820259390407544, Date(21,3,2017): 0.01076655841176158, Date(22,3,2017): 0.3501032655295408, Date(23,3,2017): 0.012805609589626999, Date(24,3,2017): 0.008745505717166252, Date(27,3,2017): 0.007826533918238258, Date(28,3,2017): 0.007057570222142303, Date(29,3,2017): 0.006853734855214788, Date(30,3,2017): 0.004067733978730203, Date(31,3,2017): 0.005955478994496848, Date(5,4,2017): 0.005943579774449891, Date(6,4,2017): 0.0074861954187276205, Date(7,4,2017): 0.008799845965319837, Date(10,4,2017): 0.0055112329363160425, Date(11,4,2017): 0.006465579699356073, Date(12,4,2017): 0.01112005887937461, Date(13,4,2017): 0.004555165423071635, Date(14,4,2017): 0.0032513417483165633, Date(17,4,2017): 0.004790452842960772, Date(18,4,2017): 0.0036404123001800006, Date(19,4,2017): 0.004620972600796142, Date(20,4,2017): 0.007257689591069675, Date(21,4,2017): 0.009513713525104049, Date(24,4,2017): 0.00946863309758829, Date(25,4,2017): 0.00942258485063292, Date(26,4,2017): 0.0737209137033501, Date(27,4,2017): 0.013212977902741072, Date(28,4,2017): 0.011581899781884989, Date(2,5,2017): 0.008209375748691142, Date(3,5,2017): 0.008727582850217132, Date(4,5,2017): 0.009401699916544349, Date(5,5,2017): 0.013514411378896517, Date(8,5,2017): 0.012950029771438424, Date(9,5,2017): 0.00894846993517653, Date(10,5,2017): 0.010286392139795127, Date(11,5,2017): 0.012790339359903174, Date(12,5,2017): 0.022020278852775414, Date(15,5,2017): 0.017349113775090415, Date(16,5,2017): 0.01819211018853899, Date(17,5,2017): 0.010947304117783501, Date(18,5,2017): 0.01058275859463851, Date(19,5,2017): 0.012154837061727874, Date(22,5,2017): 0.019743313200076884, Date(23,5,2017): 0.02772449773580871, Date(24,5,2017): 0.10996851033236668, Date(25,5,2017): 0.01947877475611705, Date(26,5,2017): 0.017666836657741845, Date(31,5,2017): 0.012934431034689215, Date(1,6,2017): 0.01449590523122907, Date(2,6,2017): 0.008903968980709031, Date(5,6,2017): 0.007285145222005873, Date(6,6,2017): 0.009882739184153735, Date(7,6,2017): 0.011632816862171306, Date(8,6,2017): 0.005887882999644069, Date(9,6,2017): 0.009185053725314498, Date(12,6,2017): 0.014167824971498374, Date(13,6,2017): 0.009810226225857734, Date(14,6,2017): 0.00502270067072603, Date(15,6,2017): 0.005160484670630142, Date(16,6,2017): 0.008047761634497712, Date(19,6,2017): 0.0076013621675189505, Date(20,6,2017): 0.005424776186742709, Date(21,6,2017): 0.009583809725072268, Date(22,6,2017): 0.007009428440732161, Date(23,6,2017): 0.007789604157770617, Date(26,6,2017): 0.006076360698362123, Date(27,6,2017): 0.0074479097449322105, Date(28,6,2017): 0.8610931031330552, Date(29,6,2017): 0.008212333727197407, Date(30,6,2017): 0.00620011463055479, Date(3,7,2017): 0.006927268195773195, Date(4,7,2017): 0.006898398824911087, Date(5,7,2017): 0.008441834387463704, Date(6,7,2017): 0.007527018805684854, Date(7,7,2017): 0.007558960936715748, Date(10,7,2017): 0.011688521873144241, Date(11,7,2017): 0.008606401899264406, Date(12,7,2017): 0.00931016554402342, Date(13,7,2017): 0.012310286330681848, Date(14,7,2017): 0.011299479298929757, Date(17,7,2017): 0.0027466487939234235, Date(18,7,2017): 0.005358195399871529, Date(19,7,2017): 0.0056386007298748365, Date(20,7,2017): 0.004867088045152872}
sse_svi_others =  {Date(2,12,2016): 0.007320004922734151, Date(7,12,2016): 0.005533432401774129, Date(8,12,2016): 0.01225892393879061, Date(9,12,2016): 0.016930274192885276, Date(19,12,2016): 0.006897047752172257, Date(20,12,2016): 0.06969240331803553, Date(21,12,2016): 0.006552009752018908, Date(23,12,2016): 0.03308252639314112, Date(27,12,2016): 0.018851433033726748, Date(28,12,2016): 0.013462452746679078, Date(16,1,2017): 0.09237854897116285, Date(17,1,2017): 0.011123939154359426, Date(18,1,2017): 0.00532795722253802, Date(15,3,2017): 0.014595388238081314, Date(12,5,2017): 0.00979151896821356, Date(22,5,2017): 0.04390835285237134, Date(23,5,2017): 0.014937357610399781, Date(24,5,2017): 0.006402438263365139, Date(13,7,2017): 0.0006973462417516303}
sse_svi_others2 =  {Date(2,12,2016): 0.007307408036742361, Date(7,12,2016): 0.005709988936771913, Date(8,12,2016): 0.012294187230499184, Date(9,12,2016): 0.017091065391489493, Date(19,12,2016): 0.006883220405178919, Date(20,12,2016): 0.070892951041363, Date(21,12,2016): 0.006496458401198163, Date(23,12,2016): 0.03290189247324176, Date(26,12,2016): 0.03929631116547378, Date(27,12,2016): 0.018783601844874966, Date(28,12,2016): 0.013297094906819112, Date(4,1,2017): 0.004993101113635812, Date(13,1,2017): 0.0171542422470419, Date(16,1,2017): 0.0923133118469171, Date(17,1,2017): 0.011118815401415436, Date(18,1,2017): 0.005337710460770951, Date(15,3,2017): 0.012853479737687523, Date(12,5,2017): 0.009815344936240136, Date(22,5,2017): 0.006233724550403362, Date(23,5,2017): 0.014869736526766751, Date(24,5,2017): 0.006237160877136648}
print(len(sse_svi))
dates = []
sse_svi_list1 = []
sse_bs_list1 = []
date_exceptions = []
for date in sse_svi.keys():
    e_svi1 = sse_svi.get(date)
    #e_svi2 = sse_svi2.get(date)
    #e_svi3 = sse_svi3.get(date)
    #if e_svi1 == 'NAN' or e_svi2 == 'NAN'or e_svi3 == 'NAN': continue
    #e_svi = min(e_svi1,e_svi2,e_svi3)
    if e_svi1 == 'NAN' : continue
    e_svi = e_svi1
    e_bs = sse_bs2.get(date)
    if date in sse_svi_others.keys():
        e_svi = min(e_svi1,sse_svi_others.get(date))
    if date in sse_svi_others2.keys():
        e_svi = min(e_svi,sse_svi_others2.get(date))
    if e_svi >0.009 :
        #print(date)
        date_exceptions.append(date)
        continue
    dates.append(date)
    sse_svi_list1.append(e_svi)
    sse_bs_list1.append(e_bs)
print(date_exceptions)
    #print(" %15s %25s " % (date, round(e_svi, 6)))
#print("-" * 80)

#print('Mean SSE svi : ',sum(sse_svi_list1)/len(sse_svi_list1))
#print('Mean SSE bs : ',sum(sse_bs_list1)/len(sse_bs_list1))

avg_svi = sum(sse_svi_list1)/len(sse_svi_list1)
avg_bs = sum(sse_bs_list1)/len(sse_bs_list1)
print('avg_svi',avg_svi)
print('avg_bs',avg_bs)
plt.rcParams['font.sans-serif'] = ['STKaiti']
plt.rcParams.update({'font.size': 13})
f,axarr = plt.subplots()
axarr.plot(dates, sse_svi_list1,color = pu.c1,linestyle = pu.l1,linewidth = 2,label="SVI-SSE")
axarr.plot(dates, [avg_svi]*len(dates), color=pu.c3, linestyle=pu.l3, linewidth=1,label="SVI-平均SSE")
axarr.plot(dates, sse_bs_list1,color = pu.c2,linestyle = pu.l2,linewidth = 2,label="BS-SSE")
l, = axarr.plot(dates, [avg_bs]*len(dates), color=pu.c4, linestyle=pu.l4, linewidth=1,label="BS-平均SSE")
l.set_dashes(pu.dash)
axarr.set_ylabel('SSE')
axarr.legend(bbox_to_anchor=(0., 1, 1.1, .102), loc=3,
           ncol=4, borderaxespad=0.,columnspacing=0.5,frameon=False)
# Hide the right and top spines
axarr.spines['right'].set_visible(False)
axarr.spines['top'].set_visible(False)
# Only show ticks on the left and bottom spines
axarr.yaxis.set_ticks_position('left')
axarr.xaxis.set_ticks_position('bottom')
for label in axarr.get_xmajorticklabels():
    label.set_rotation(30)
    label.set_horizontalalignment("right")
f.savefig('model_performance.png', dpi=300, format='png')
plt.show()
