'''
Re-ID
=====

There's some unrest in the minion ranks: minions with ID numbers like "1", "42", and
other "good" numbers have been lording it over the poor minions who are stuck with
more boring IDs. To quell the unrest, Commander Lambda has tasked you with reassigning
everyone new, random IDs based on her Completely Foolproof Scheme. 

She's concatenated the prime numbers in a single long string: "2357111317192329...".
Now every minion must draw a number from a hat. That number is the starting index in
that string of primes, and the minion's new ID number will be the next five digits in
the string. So if a minion draws "3", their ID number will be "71113". 

Help the Commander assign these IDs by writing a function answer(n) which takes in the
starting index n of Lambda's string of all primes, and returns the next five digits in
the string. Commander Lambda has a lot of minions, so the value of n will always be
between 0 and 10000.


Test cases
==========

Inputs:
    (int) n = 0
Output:
    (string) "23571"

Inputs:
    (int) n = 3
Output:
    (string) "71113"
'''

temp_concant_prime_mega = (
    '2357111317192329313741434753596167717379838997101103107109113127131137139149'
    '1511571631671731791811911931971992112232272292332392412512572632692712772812'
    '8329330731131331733133734734935335936737337938338939740140941942143143343944'
    '3449457461463467479487491499503509521523541547557563569571577587593599601607'
    '6136176196316416436476536596616736776836917017097197277337397437517577617697'
    '7378779780981182182382782983985385785986387788188388790791191992993794194795'
    '3967971977983991997100910131019102110311033103910491051106110631069108710911'
    '0931097110311091117112311291151115311631171118111871193120112131217122312291'
    '2311237124912591277127912831289129112971301130313071319132113271361136713731'
    '3811399140914231427142914331439144714511453145914711481148314871489149314991'
    '5111523153115431549155315591567157115791583159716011607160916131619162116271'
    '6371657166316671669169316971699170917211723173317411747175317591777178317871'
    '7891801181118231831184718611867187118731877187918891901190719131931193319491'
    '9511973197919871993199719992003201120172027202920392053206320692081208320872'
    '0892099211121132129213121372141214321532161217922032207221322212237223922432'
    '2512267226922732281228722932297230923112333233923412347235123572371237723812'
    '3832389239323992411241724232437244124472459246724732477250325212531253925432'
    '5492551255725792591259326092617262126332647265726592663267126772683268726892'
    '6932699270727112713271927292731274127492753276727772789279127972801280328192'
    '8332837284328512857286128792887289729032909291729272939295329572963296929712'
    '9993001301130193023303730413049306130673079308330893109311931213137316331673'
    '1693181318731913203320932173221322932513253325732593271329933013307331333193'
    '3233329333133433347335933613371337333893391340734133433344934573461346334673'
    '4693491349935113517352735293533353935413547355735593571358135833593360736133'
    '6173623363136373643365936713673367736913697370137093719372737333739376137673'
    '7693779379337973803382138233833384738513853386338773881388939073911391739193'
    '9233929393139433947396739894001400340074013401940214027404940514057407340794'
    '0914093409941114127412941334139415341574159417742014211421742194229423142414'
    '2434253425942614271427342834289429743274337433943494357436343734391439744094'
    '4214423444144474451445744634481448344934507451345174519452345474549456145674'
    '5834591459746034621463746394643464946514657466346734679469147034721472347294'
    '7334751475947834787478947934799480148134817483148614871487748894903490949194'
    '9314933493749434951495749674969497349874993499950035009501150215023503950515'
    '0595077508150875099510151075113511951475153516751715179518951975209522752315'
    '2335237526152735279528152975303530953235333534753515381538753935399540754135'
    '4175419543154375441544354495471547754795483550155035507551955215527553155575'
    '5635569557355815591562356395641564756515653565756595669568356895693570157115'
    '7175737574157435749577957835791580158075813582158275839584358495851585758615'
    '8675869587958815897590359235927593959535981598760076011602960376043604760536'
    '0676073607960896091610161136121613161336143615161636173619761996203621162176'
    '2216229624762576263626962716277628762996301631163176323632963376343635363596'
    '3616367637363796389639764216427644964516469647364816491652165296547655165536'
    '5636569657165776581659966076619663766536659666166736679668966916701670367096'
    '7196733673767616763677967816791679368036823682768296833684168576863686968716'
    '8836899690769116917694769496959696169676971697769836991699770017013701970277'
    '0397043705770697079710371097121712771297151715971777187719372077211721372197'
    '2297237724372477253728372977307730973217331733373497351736973937411741774337'
    '4517457745974777481748774897499750775177523752975377541754775497559756175737'
    '5777583758975917603760776217639764376497669767376817687769176997703771777237'
    '7277741775377577759778977937817782378297841785378677873787778797883790179077'
    '9197927793379377949795179637993800980118017803980538059806980818087808980938'
    '1018111811781238147816181678171817981918209821982218231823382378243826382698'
    '2738287829182938297831183178329835383638369837783878389841984238429843184438'
    '4478461846785018513852185278537853985438563857385818597859986098623862786298'
    '6418647866386698677868186898693869987078713871987318737874187478753876187798'
    '7838803880788198821883188378839884988618863886788878893892389298933894189518'
    '9638969897189999001900790119013902990419043904990599067909191039109912791339'
    '1379151915791619173918191879199920392099221922792399241925792779281928392939'
    '3119319932393379341934393499371937793919397940394139419942194319433943794399'
    '4619463946794739479949194979511952195339539954795519587960196139619962396299'
    '6319643964996619677967996899697971997219733973997439749976797699781978797919'
    '8039811981798299833983998519857985998719883988799019907992399299931994199499'
    '9679973100071000910037100391006110067100691007910091100931009910103101111013'
    '3101391014110151101591016310169101771018110193102111022310243102471025310259'
    '1026710271102731028910301103031031310321103311033310337103431035710369103911'
    '0399104271042910433104531045710459104631047710487104991050110513105291053110'
    '5591056710589105971060110607106131062710631106391065110657106631066710687106'
    '9110709107111072310729107331073910753107711078110789107991083110837108471085'
    '3108591086110867108831088910891109031090910937109391094910957109731097910987'
    '1099311003110271104711057110591106911071110831108711093111131111711119111311'
    '1149111591116111171111731117711197112131123911243112511125711261112731127911'
    '2871129911311113171132111329113511135311369113831139311399114111142311437114'
    '4311447114671147111483114891149111497115031151911527115491155111579115871159'
    '3115971161711621116331165711677116811168911699117011171711719117311174311777'
    '1177911783117891180111807118131182111827118311183311839118631186711887118971'
    '1903119091192311927119331193911941119531195911969119711198111987120071201112'
    '0371204112043120491207112073120971210112107121091211312119121431214912157121'
    '6112163121971220312211122271223912241122511225312263122691227712281122891230'
    '1123231232912343123471237312377123791239112401124091241312421124331243712451'
    '1245712473124791248712491124971250312511125171252712539125411254712553125691'
    '2577125831258912601126111261312619126371264112647126531265912671126891269712'
    '7031271312721127391274312757127631278112791127991280912821128231282912841128'
    '5312889128931289912907129111291712919129231294112953129591296712973129791298'
    '3130011300313007130091303313037130431304913063130931309913103131091312113127'
    '1314713151131591316313171131771318313187132171321913229132411324913259132671'
    '3291132971330913313133271333113337133391336713381133971339913411134171342113'
    '4411345113457134631346913477134871349913513135231353713553135671357713591135'
    '9713613136191362713633136491366913679136811368713691136931369713709137111372'
    '1137231372913751137571375913763137811378913799138071382913831138411385913873'
    '1387713879138831390113903139071391313921139311393313963139671399713999140091'
    '4011140291403314051140571407114081140831408714107141431414914153141591417314'
    '1771419714207142211424314249142511428114293143031432114323143271434114347143'
    '6914387143891440114407144111441914423144311443714447144491446114479144891450'
    '3145191453314537145431454914551145571456114563145911459314621146271462914633'
    '1463914653146571466914683146991471314717147231473114737147411474714753147591'
    '4767147711477914783147971481314821148271483114843148511486714869148791488714'
    '8911489714923149291493914947149511495714969149831501315017150311505315061150'
    '7315077150831509115101151071512115131151371513915149151611517315187151931519'
    '9152171522715233152411525915263152691527115277152871528915299153071531315319'
    '1532915331153491535915361153731537715383153911540115413154271543915443154511'
    '5461154671547315493154971551115527155411555115559155691558115583156011560715'
    '6191562915641156431564715649156611566715671156791568315727157311573315737157'
    '3915749157611576715773157871579115797158031580915817158231585915877158811588'
    '7158891590115907159131591915923159371595915971159731599116001160071603316057'
    '1606116063160671606916073160871609116097161031611116127161391614116183161871'
    '6189161931621716223162291623116249162531626716273163011631916333163391634916'
    '3611636316369163811641116417164211642716433164471645116453164771648116487164'
    '9316519165291654716553165611656716573166031660716619166311663316649166511665'
    '7166611667316691166931669916703167291674116747167591676316787168111682316829'
    '1683116843168711687916883168891690116903169211692716931169371694316963169791'
    '6981169871699317011170211702717029170331704117047170531707717093170991710717'
    '1171712317137171591716717183171891719117203172071720917231172391725717291172'
    '9317299173171732117327173331734117351173591737717383173871738917393174011741'
    '7174191743117443174491746717471174771748317489174911749717509175191753917551'
    '1756917573175791758117597175991760917623176271765717659176691768117683177071'
    '7713177291773717747177491776117783177891779117807178271783717839178511786317'
    '8811789117903179091791117921179231792917939179571795917971179771798117987179'
    '8918013180411804318047180491805918061180771808918097181191812118127181311813'
    '3181431814918169181811819118199182111821718223182291823318251182531825718269'
    '1828718289183011830718311183131832918341183531836718371183791839718401184131'
    '8427184331843918443184511845718461184811849318503185171852118523185391854118'
    '5531858318587185931861718637186611867118679186911870118713187191873118743187'
    '4918757187731878718793187971880318839188591886918899189111891318917189191894'
    '7189591897318979190011900919013190311903719051190691907319079190811908719121'
    '1913919141191571916319181191831920719211192131921919231192371924919259192671'
    '9273192891930119309193191933319373193791938119387193911940319417194211942319'
    '4271942919433194411944719457194631946919471194771948319489195011950719531195'
    '4119543195531955919571195771958319597196031960919661196811968719697196991970'
    '9197171972719739197511975319759197631977719793198011981319819198411984319853'
    '1986119867198891989119913199191992719937199491996119963199731997919991199931'
    '9997200112002120023200292004720051200632007120089201012010720113201172012320'
    '12920143201472014920161201732017720183202012021920231'
)

def answer1(n):
    return temp_concant_prime_mega[n:n+5]

def GenerateMegaPrime(max_len):
    new_num = ''
    num = 2;
    # for num in range(2, max_len + 1):
    while len(new_num) != max_len:
        for i in range(2, num):
            if (num % i) == 0:
                break
            else:
                new_num += str(num)
        num += 1
    return new_num

def answer2(n):
    concant_prime_mega = GenerateMegaPrime(n + 5)
    return concant_prime_mega[n:n+5]
    # concant_prime_mega = GenerateMegaPrime(10005)
    # return temp_concant_prime_mega[n:n+5]


# print(answer1(0)) #23571
print(answer2(0))

# print(answer1(3)) #71113
print(answer2(3))
