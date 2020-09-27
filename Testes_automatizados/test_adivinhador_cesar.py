import Utilitarios.adivinhador_cesar as adivinhador_cesar

# Apenas letras - Português.
def test_adivinhador_cesar_apenas_letras_port_mensagem_invalida():
    assert adivinhador_cesar.adivinhar_cesar_apenas_letras('', idioma_teste='Portugues') == False

def test_adivinhador_cesar_apenas_letras_port_adivinhando_mensagem_1():
    assert adivinhador_cesar.adivinhar_cesar_apenas_letras(
    'Pqb, fbj, uvep cfn ? Qsjnfjsp uftuf ep bejwjoibeps vujmjaboep b dibwf 1 !', idioma_teste='Portugues'
    ) == ['Opa, eai, tudo bem ? Primeiro teste do adivinhador utilizando a chave 1 !', 1]

def test_adivinhador_cesar_apenas_letras_port_adivinhando_mensagem_2():
    assert adivinhador_cesar.adivinhar_cesar_apenas_letras(
    'Abm, qmu, fgpa nqy ? Bduyquda fqefq pa mpuhuztmpad gfuxulmzpa m otmhq 12 !', idioma_teste='Portugues'
    ) == ['Opa, eai, tudo bem ? Primeiro teste do adivinhador utilizando a chave 12 !', 12]

def test_adivinhador_cesar_apenas_letras_port_adivinhando_mensagem_3():
    assert adivinhador_cesar.adivinhar_cesar_apenas_letras(
    'Kqybk fkwyc docdkb ew dohdy woxyb', idioma_teste='Portugues'
    ) == ['Agora vamos testar um texto menor', 10]

def test_adivinhador_cesar_apenas_letras_port_adivinhando_mensagem_4():
    assert adivinhador_cesar.adivinhar_cesar_apenas_letras(
    'Pexmsyxye myw y woxyb ?? Kqybk fkwyc fob myw ew dohdy low wksyb. Fkwyc oxbyvkb occo dohdy zkbk ovo psmkb qbkxnky, zkbk fob co ovo zyno cob knsfsxrkny zovk knsfsxrknyb !', idioma_teste='Portugues'
    ) == ['Funcionou com o menor ?? Agora vamos ver com um texto bem maior. Vamos enrolar esse texto para ele ficar grandao, para ver se ele pode ser adivinhado pela adivinhador !', 10]

def test_adivinhador_cesar_apenas_letras_port_adivinhando_mensagem_5():
    assert adivinhador_cesar.adivinhar_cesar_apenas_letras(
    'Xknw paopwn iweo qi patpk ! Wcknw yki qiw ydwra iwekn !', idioma_teste='Portugues'
    ) == ['Bora testar mais um texto ! Agora com uma chave maior !', 22]

# Apenas letras - Inglês.
def test_adivinhador_cesar_apenas_letras_eng_mensagem_invalida():
    assert adivinhador_cesar.adivinhar_cesar_apenas_letras('', idioma_teste='English') == False

def test_adivinhador_cesar_apenas_letras_eng_adivinhando_mensagem_1():
    assert adivinhador_cesar.adivinhar_cesar_apenas_letras(
    'Mfut uftu uif dftbs Hvftt xjui uif lfz 1 !', idioma_teste='English'
    ) == ['Lets test the cesar Guess with the key 1 !', 1]

def test_adivinhador_cesar_apenas_letras_eng_adivinhando_mensagem_2():
    assert adivinhador_cesar.adivinhar_cesar_apenas_letras(
    'Xqfe fqef ftq oqemd Sgqee iuft ftq wqk 12 !', idioma_teste='English'
    ) == ['Lets test the cesar Guess with the key 12 !', 12]

def test_adivinhador_cesar_apenas_letras_eng_adivinhando_mensagem_3():
    assert adivinhador_cesar.adivinhar_cesar_apenas_letras(
    'Docdsxq k cwkvv dohd', idioma_teste='English'
    ) == ['Testing a small text', 10]

def test_adivinhador_cesar_apenas_letras_eng_adivinhando_mensagem_4():
    assert adivinhador_cesar.adivinhar_cesar_apenas_letras(
    'Xyg, vodc docd gsdr k lsq dohd. Wi oxqvscr sc fobi fobi lkn, sw cybbi ! Led s rkfo dy gbsdo k lsq dohd kxn s nyxd uxyg grkd dy gbsdo, cy sw gbsxdq k xyx coxco dohd...', idioma_teste='English'
    ) == ['Now, lets test with a big text. My english is very very bad, im sorry ! But i have to write a big text and i dont know what to write, so im wrintg a non sense text...', 10]

def test_adivinhador_cesar_apenas_letras_eng_adivinhando_mensagem_5():
    assert adivinhador_cesar.adivinhar_cesar_apenas_letras(
    'Jks, hapo paop sepd w xeccan gau !', idioma_teste='English'
    ) == ['Now, lets test with a bigger key !', 22]

# Vários caracteres - Português
def test_adivinhador_cesar_varios_caracteres_port_mensagem_invalida():
    assert adivinhador_cesar.adivinhar_cesar_varios_caracteres('', idioma_teste='Portugues') == False

def test_adivinhador_cesar_varios_caracteres_port_adivinhando_mensagem_1():
    assert adivinhador_cesar.adivinhar_cesar_varios_caracteres(
    'Ly|k*~o}~k|*myw*y*¢ë|sy}*mk|km~o|o}*kqy|k*+', idioma_teste='Portugues'
    ) == ['Bora testar com o vários caracteres agora !', 10]

def test_adivinhador_cesar_varios_caracteres_port_adivinhando_mensagem_2():
    assert adivinhador_cesar.adivinhar_cesar_varios_caracteres(
    'Éöùè¦ûìúûèù¦êöô¦ö¦ýŅùðöú¦êèùèêûìùìú¦èîöùè³¦êïèýì¦üô¦÷öüêö¦ôèðöù¦§', idioma_teste='Portugues'
    ) == ['Bora testar com o vários caracteres agora, chave um pouco maior !', 100]

def test_adivinhador_cesar_varios_caracteres_port_adivinhando_mensagem_3():
    assert adivinhador_cesar.adivinhar_cesar_varios_caracteres(
    'ã¾āčċ¾ĒăĖĒč¾ĎăďēăČč¾Ý', idioma_teste='Portugues'
    ) == ['E com texto pequeno ?', 123]

def test_adivinhador_cesar_varios_caracteres_port_adivinhando_mensagem_4():
    assert adivinhador_cesar.adivinhar_cesar_varios_caracteres(
    'áćďĒāÀĖāčďēÀĔąēĔāĒÀăďčÀĕčÀĔąĘĔďÀčāĉďĒÎÎÎÀöďĕÀąĎĒďČāĒÀĕčÀĔāĎĔďÀāđĕĉÀĎąēēāÀčąĎēāćąčÌÀĐāĒāÀąČāÀĆĉăāĒÀčāĉďĒÌÀēąĉÀČŞÀĎŦÎÎÎÀîŠďÀēąĉÀďÀđĕąÀąēăĒąĖąĒÌÀēŰÀĖďĕÀąĎĒďČāĒÀčąēčďÌÀĎŠďÀĔąčÀčĕĉĔďÀďÀđĕąÀĆāĚąĒÀÁ', idioma_teste='Portugues'
    ) == ['Agora vamos testar com um texto maior... Vou enrolar um tanto aqui nessa mensagem, para ela ficar maior, sei lá né... Não sei o que escrever, só vou enrolar mesmo, não tem muito o que fazer !', 125]

def test_adivinhador_cesar_varios_caracteres_port_adivinhando_mensagem_5():
    assert adivinhador_cesar.adivinhar_cesar_varios_caracteres(
    'ɱʗʟʢʑɐʦʑʝʟʣɐʤʕʣʤʑʢɐʓʟʝɐʥʝʑɐʓʘʑʦʕɐʝʑʙʟʢɐɑ', idioma_teste='Portugues'
    ) == ['Agora vamos testar com uma chave maior !', 525]

# Vários caracteres - Inglês
def test_adivinhador_cesar_varios_caracteres_Eng_mensagem_invalida():
    assert adivinhador_cesar.adivinhar_cesar_varios_caracteres('', idioma_teste='English') == False

def test_adivinhador_cesar_varios_caracteres_Eng_adivinhando_mensagem_1():
    assert adivinhador_cesar.adivinhar_cesar_varios_caracteres(
    'Xy£6*vo~}*~o}~*£s~r*~ro*yz~syxD*]o¢o|kv*mrk|km~o|}', idioma_teste='English'
    ) == ['Now, lets test with the option: Several characters', 10]

def test_adivinhador_cesar_varios_caracteres_Eng_adivinhando_mensagem_2():
    assert adivinhador_cesar.adivinhar_cesar_varios_caracteres(
    'Õöþ³¦óìûú¦ûìúû¦þðûï¦ûïì¦ö÷ûðöõÁ¦Úìýìùèó¦êïèùèêûìùú¦ă¦òìĀÁ¦¸··¦§', idioma_teste='English'
    ) == ['Now, lets test with the option: Several characters | key: 100 !', 100]

def test_adivinhador_cesar_varios_caracteres_Eng_adivinhando_mensagem_3():
    assert adivinhador_cesar.adivinhar_cesar_varios_caracteres(
    'ßČĂ¾ĕćĒĆ¾ÿ¾đċÿĊĊ¾ĒăĖĒ¾Ý', idioma_teste='English'
    ) == ['And with a small text ?', 123]

def test_adivinhador_cesar_varios_caracteres_Eng_adivinhando_mensagem_4():
    assert adivinhador_cesar.adivinhar_cesar_varios_caracteres(
    'îďėÌÀČąĔēÀĔąēĔÀėĉĔĈÀāÀĂĉććąĒÀĂĉććąĒÀĔąĘĔÎÎÎÀéÀĄďĎĔÀċĎďėÀėĈāĔÀĔďÀėĒĉĔąÌÀēďÀĉčÀėĒĉĔĉĎćÀāĎęĔĈĉĎćÎÎÎÀêĕēĔÀėĒĉĎĔćÌÀĊĕēĔÀėĒĉĔĉĎćÎÎÎÀóďĒĒęÌÀčęÀąĎćČĉēĈÀĉēÀĈďĒĒĉĂČąÀÚÈ', idioma_teste='English'
    ) == ['Now, lets test with a bigger bigger text... I dont know what to write, so im writing anything... Just wrintg, just writing... Sorry, my english is horrible :(', 125]

def test_adivinhador_cesar_varios_caracteres_Eng_adivinhando_mensagem_5():
    assert adivinhador_cesar.adivinhar_cesar_varios_caracteres(
    'ʄʕʣʤʙʞʗɐʧʙʤʘɐʑɐʦʕʢʩɐʒʙʗɐʛʕʩɞɞɞ', idioma_teste='English'
    ) == ['Testing with a very big key...', 525]