#!/usr/bin/env python
"""
Tests data either gained from an old DB implementation, AxiSEM, or to guard
against regressions.
"""
import numpy as np

BWD_TEST_DATA = {
    "Z": np.array([
        -3.81669935e-39, -3.35652626e-37,  3.57062429e-35,  5.06588589e-34,
        1.94696809e-32,  1.89072798e-31,  2.41251539e-28, -5.05942607e-27,
        -2.86760440e-25, -5.18421933e-24,  1.38887860e-22, -1.05029638e-21,
        9.59017864e-21, -5.51049004e-20,  3.27795998e-19,  3.66801598e-19,
        -3.62193631e-16, -4.75828883e-13, -9.34584127e-11, -3.92586924e-09,
        -3.48405306e-08, -7.17413831e-08, -4.98682132e-08, -3.48290709e-08,
        -3.06076206e-08, -5.12560088e-08, -4.93613106e-08,  9.23245204e-09,
        6.96333155e-08,  1.14468643e-07,  1.32974215e-07,  1.31444119e-07,
        1.30096351e-07,  1.25612507e-07,  1.28841749e-07,  1.62760082e-07,
        5.61877362e-08, -2.75919368e-07, -1.68349522e-07,  6.77548378e-08,
        6.12303545e-08,  5.23862687e-09, -5.59636764e-08, -6.57385329e-08,
        -1.05490967e-07, -8.09880336e-08, -4.07608006e-08, -5.50961014e-08,
        -1.82779995e-09,  3.98513859e-08,  3.83581746e-07, -3.77968643e-07,
        8.65527067e-08,  1.60996515e-06,  6.42389620e-07, -9.54976389e-07,
        -1.34522764e-06, -7.05372983e-07, -1.93699307e-08,  3.72837700e-07,
        4.26616234e-07,  3.06510952e-07,  1.16393236e-07, -1.65212277e-08,
        -9.96772346e-08, -1.14188573e-07]),
    "N": np.array([
        -5.96958190e-39, -5.89781130e-37, 2.83102215e-35, 2.56623118e-33,
        -5.10888221e-33, -4.16161621e-30, 1.67933008e-29, 2.04600795e-26,
        -6.59883324e-25, 5.28510811e-24, -5.83013590e-23, 7.83984748e-22,
        1.16609069e-20, -1.72158484e-19, 8.39366383e-19, -6.51025720e-19,
        -2.50960666e-17, 3.46178406e-13, 7.27449661e-11, 3.09476063e-09,
        2.82341121e-08, 6.57350773e-08, 7.00736863e-08, 8.74377643e-08,
        1.15063434e-07, 1.74533015e-07, 2.13544672e-07, 1.68080983e-07,
        1.06248829e-07, 4.50717945e-08, 3.60849044e-09, 1.44347709e-08,
        6.75163602e-08, 1.42474601e-07, 1.96200936e-07, 8.96202061e-08,
        -1.75033495e-07, -2.08592057e-07, 1.76976252e-07, 1.99391816e-07,
        1.33150566e-07, 1.00995467e-07, 1.02955473e-07, 9.80975901e-08,
        8.32742618e-08, 5.52240391e-08, -6.04359949e-08, -1.33982954e-07,
        -2.34621555e-08, -1.09880012e-07, 1.17431183e-07, 1.47581535e-07,
        -5.97205640e-07, -4.74928195e-08, 1.03865310e-06, 7.82422099e-07,
        5.02526701e-08, -4.30853146e-07, -4.10889299e-07, -2.40001809e-07,
        -8.01653007e-09, 1.05567943e-07, 1.61960044e-07, 1.40885921e-07,
        9.17636544e-08, 4.84211284e-08]),
    "E": np.array([
        1.15974698e-41, 1.05877338e-39, -5.31725007e-38, -4.36036084e-36,
        2.84916680e-35, 7.52473224e-33, -4.62279208e-32, -3.77515990e-29,
        1.38842091e-27, -1.49159509e-26, 8.99877513e-26, -4.05121461e-25,
        -3.00692098e-23, 3.76955317e-22, -1.74838407e-21, 6.65926876e-22,
        -3.38783935e-18, -2.03079411e-15, -2.80238719e-13, -8.47140012e-12,
        -4.30027468e-11, 3.71617561e-11, 2.97648621e-10, 5.34631634e-10,
        8.21952612e-10, 1.14353949e-09, 1.66616870e-09, 2.36990685e-09,
        2.96538284e-09, 3.41398317e-09, 3.70200166e-09, 3.84298249e-09,
        3.96385800e-09, 4.16369765e-09, 4.60881372e-09, 5.54941252e-09,
        6.24290656e-09, -4.35558007e-09, -1.82028654e-08, -1.33653999e-08,
        -1.07268491e-08, -1.04735277e-08, -1.18887443e-08, -1.36243647e-08,
        -2.25339355e-08, -5.58518081e-08, -3.16411314e-08, 8.10034292e-08,
        8.76700281e-08, 1.22798799e-08, -1.15736258e-08, -1.42783066e-08,
        -9.21718159e-09, -8.39552781e-09, -6.76709284e-09, -3.93653495e-09,
        9.29348648e-10, 6.55616912e-10, 1.66073119e-09, -7.88372632e-10,
        7.31150846e-10, -1.23458217e-09, 1.25831683e-11, -9.86027370e-10,
        2.33252099e-10, -7.74174495e-10]),
    "R": np.array([
        5.96959313e-39, 5.89782060e-37, -2.83102710e-35, -2.56623472e-33,
        5.10893003e-33, 4.16162289e-30, -1.67933604e-29, -2.04601139e-26,
        6.59884784e-25, -5.28512762e-24, 5.83014207e-23, -7.83983921e-22,
        -1.16609441e-20, 1.72158896e-19, -8.39368203e-19, 6.51025711e-19,
        2.50890400e-17, -3.46181853e-13, -7.27453888e-11, -3.09477151e-09,
        -2.82341408e-08, -6.57348616e-08, -7.00729252e-08, -8.74364786e-08,
        -1.15061498e-07, -1.74530292e-07, -2.13540790e-07, -1.68075749e-07,
        -1.06242500e-07, -4.50646718e-08, -3.60086273e-09, -1.44268301e-08,
        -6.75080581e-08, -1.42465729e-07, -1.96191034e-07, -8.96085935e-08,
        1.75045974e-07, 2.08582650e-07, -1.77013345e-07, -1.99418904e-07,
        -1.33172364e-07, -1.01016811e-07, -1.02979726e-07, -9.81254262e-08,
        -8.33204684e-08, -5.53388854e-08, 6.03707380e-08, 1.34149404e-07,
        2.36425626e-08, 1.09905055e-07, -1.17454757e-07, -1.47610612e-07,
        5.97185402e-07, 4.74754379e-08, -1.03866482e-06, -7.82428544e-07,
        -5.02506508e-08, 4.30853583e-07, 4.10891847e-07, 2.39999677e-07,
        8.01801806e-09, -1.05570260e-07, -1.61959675e-07, -1.40887653e-07,
        -9.17629799e-08, -4.84226194e-08]),
    "T": np.array([
        6.90125029e-43, 1.55212888e-40, -5.10034208e-39, -9.21885320e-37,
        -1.79756703e-35, 1.04140314e-33, 1.16611034e-32, -4.36276452e-30,
        -3.01381328e-29, 4.03724505e-27, 3.00178360e-26, -1.20860509e-24,
        6.06675951e-24, -2.25897561e-23, 2.06591338e-23, 6.74122196e-22,
        3.43948900e-18, 1.31822876e-15, 1.30502533e-13, 2.10123947e-12,
        -1.51134137e-11, -1.72468370e-10, -4.41885117e-10, -7.14609215e-10,
        -1.05879326e-09, -1.50278948e-09, -2.10571776e-09, -2.71587361e-09,
        -3.18407528e-09, -3.50675008e-09, -3.70942140e-09, -3.87268635e-09,
        -4.10282282e-09, -4.45695337e-09, -5.01265682e-09, -5.73387174e-09,
        -5.88261075e-09, 4.78492915e-09, 1.78385454e-08, 1.29549507e-08,
        1.04527541e-08, 1.02656201e-08, 1.16767993e-08, 1.34224153e-08,
        2.23624790e-08, 5.57380186e-08, 3.17654637e-08, -8.07274720e-08,
        -8.76215487e-08, -1.20536809e-08, 1.13318852e-08, 1.39744999e-08,
        1.04464284e-08, 8.49326752e-09, 4.62915275e-09, 2.32601743e-09,
        -1.03278495e-09, 2.31236920e-10, -8.14968084e-10, 1.28238196e-09,
        -7.14648363e-10, 1.01728234e-09, -3.45955805e-10, 6.96030825e-10,
        -4.22134573e-10, 6.74504566e-10])}


BWD_STRAIN_ONLY_TEST_DATA = {
    "Z": np.array([
        1.15148599e-39, -9.73396278e-38, -4.32233643e-35, -3.31650386e-34,
        -1.10425420e-32, -4.92696937e-31, -1.21338847e-28, 9.75744179e-27,
        1.78290957e-25, 3.38974431e-24, -1.07570187e-22, 6.46661243e-22,
        -3.22594737e-21, 2.13097712e-20, -9.56983839e-20, 1.58632582e-17,
        1.13931630e-14, 2.18844314e-12, 1.16630497e-10, 4.59735493e-10,
        -1.83854975e-08, -7.42772481e-08, -6.69552899e-08, -3.97902924e-08,
        -2.92515533e-08, -4.64077868e-08, -5.33769117e-08, 1.12327903e-09,
        6.44969754e-08, 1.16946288e-07, 1.40323862e-07, 1.36878094e-07,
        1.32968858e-07, 1.30552776e-07, 1.36442313e-07, 1.71210788e-07,
        4.64449667e-08, -3.56321355e-07, -1.99127593e-07, 9.69339603e-08,
        9.22437613e-08, 2.86680236e-08, -5.59789097e-08, -6.28544908e-08,
        -1.45356593e-07, -4.09542045e-08, 6.86171059e-08, -1.11319859e-07,
        -5.49049950e-08, 1.93735229e-07, 5.95885148e-08, -4.11725363e-08,
        4.59572880e-07, 7.12339802e-07, 1.92830435e-07, -5.47224377e-07,
        -7.87211987e-07, -4.95570253e-07, -8.14900106e-08, 2.04968267e-07,
        2.71109789e-07, 2.22878967e-07, 9.61779459e-08, 1.10655024e-08,
        -6.34180113e-08, -7.20811632e-08]),
    "N": np.array([
        2.85113519e-39, 2.22527040e-38, -5.99817577e-35, -1.39595164e-33,
        7.34262973e-34, 2.72297759e-30, -2.29168395e-28, -7.56457097e-27,
        3.36085442e-25, 5.88160718e-25, -5.93035388e-23, 1.18734652e-22,
        -7.89139768e-21, 8.31196253e-20, -2.88387614e-19, -4.00758833e-18,
        -7.47394261e-15, -1.57433980e-12, -8.31667862e-11, -2.11262254e-10,
        1.53307367e-08, 6.41977607e-08, 7.78266149e-08, 8.75615233e-08,
        1.15804263e-07, 1.69600723e-07, 2.21226119e-07, 1.83639277e-07,
        1.17799272e-07, 5.16264357e-08, 5.74668111e-09, 1.51687197e-08,
        6.90912207e-08, 1.40727921e-07, 1.99160760e-07, 8.76679475e-08,
        -2.37461252e-07, -2.26160404e-07, 2.43152563e-07, 2.12564136e-07,
        1.22817726e-07, 8.60873816e-08, 9.71418237e-08, 9.08938002e-08,
        7.38797132e-08, 5.09006787e-08, -6.25929029e-08, -9.46710398e-08,
        -6.46407012e-08, -1.12366519e-08, 9.37691177e-08, -9.17607787e-08,
        -1.74474742e-07, 2.19538016e-07, 5.39077121e-07, 4.60136079e-07,
        5.69320229e-08, -2.06513112e-07, -2.66915681e-07, -1.55674445e-07,
        -3.12279597e-08, 7.06317854e-08, 1.11756989e-07, 1.07466732e-07,
        8.21352392e-08, 4.97004025e-08]),
    "E": np.array([
        -5.86868541e-42, -9.42022429e-41, 1.31910356e-37, 3.26513266e-36,
        -7.50877737e-36, -6.20236168e-33, 4.95295123e-31, 1.85287720e-29,
        -8.19020452e-28, -5.88106697e-29, 1.23793536e-25, -3.47184583e-26,
        1.53610885e-23, -1.87706980e-22, 7.82037565e-22, 1.27529315e-20,
        4.30330643e-18, -1.78083097e-15, -3.86358209e-13, -1.49641746e-11,
        -1.23998305e-10, -1.87500658e-10, 9.37482836e-11, 3.35771478e-10,
        6.04097937e-10, 9.12802890e-10, 1.38492303e-09, 2.13746942e-09,
        2.79343678e-09, 3.27571106e-09, 3.57613533e-09, 3.70325246e-09,
        3.79176083e-09, 3.90997425e-09, 4.32783675e-09, 5.96775156e-09,
        1.30820579e-08, 7.90213524e-09, -2.36830124e-08, -1.76341422e-08,
        -1.23835082e-08, -1.08761104e-08, -1.18590173e-08, -9.94441878e-09,
        -8.09448284e-09, -6.36423411e-08, -6.38385768e-08, 8.48618177e-08,
        9.18620201e-08, 1.56452438e-08, -8.08617894e-09, -1.25985039e-08,
        -9.10338757e-09, -7.78292746e-09, -5.05872189e-09, -3.89181156e-09,
        1.22244725e-09, 2.41067558e-10, 8.44087580e-10, -9.07696567e-10,
        5.80574465e-10, -8.87446092e-10, 2.97617673e-10, -9.44557537e-10,
        7.60783652e-11, -8.06538768e-10]),
    "R": np.array([
        -2.85114123e-39, -2.22528507e-38, 5.99819022e-35, 1.39595540e-33,
        -7.34276873e-34, -2.72298459e-30, 2.29168929e-28, 7.56459309e-27,
        -3.36086416e-25, -5.88159593e-25, 5.93036679e-23, -1.18734472e-22,
        7.89141258e-21, -8.31198356e-20, 2.88388613e-19, 4.00760609e-18,
        7.47393564e-15, 1.57433280e-12, 8.31658147e-11, 2.11231004e-10,
        -1.53309595e-08, -6.41980106e-08, -7.78262570e-08, -8.75606467e-08,
        -1.15802775e-07, -1.69598485e-07, -2.21222800e-07, -1.83634488e-07,
        -1.17793272e-07, -5.16195838e-08, -5.73930795e-09, -1.51610649e-08,
        -6.90832695e-08, -1.40719575e-07, -1.99151430e-07, -8.76554780e-08,
        2.37487676e-07, 2.26176190e-07, -2.43200796e-07, -2.12599983e-07,
        -1.22842955e-07, -8.61095862e-08, -9.71660281e-08, -9.09140768e-08,
        -7.38962181e-08, -5.10315699e-08, 6.24613673e-08, 9.48455157e-08,
        6.48296498e-08, 1.12688317e-08, -9.37855634e-08, 9.17346520e-08,
        1.74455634e-07, -2.19553571e-07, -5.39086391e-07, -4.60143115e-07,
        -5.69293861e-08, 2.06513171e-07, 2.66916853e-07, 1.55672247e-07,
        3.12290886e-08, -7.06334624e-08, -1.11756140e-07, -1.07468449e-07,
        -8.21349086e-08, -4.97019574e-08]),
    "T": np.array([
        0.00000000e+00, 4.83978869e-41, -8.44580809e-39, -3.91749672e-37,
        5.99738127e-36, 5.97470510e-34, -2.35821855e-32, -2.95809498e-30,
        1.27232667e-28, -1.15183808e-27, -1.72502652e-27, -2.09680704e-25,
        8.82309946e-25, 1.66161694e-23, -1.88429334e-22, -4.50383041e-21,
        1.10807943e-17, 5.02139098e-15, 5.57544878e-13, 1.53989974e-11,
        9.24418118e-11, 5.53579254e-11, -2.53943558e-10, -5.16004221e-10,
        -8.42463941e-10, -1.26190092e-09, -1.84028390e-09, -2.51546130e-09,
        -3.03590460e-09, -3.38197009e-09, -3.58795652e-09, -3.73446735e-09,
        -3.93396765e-09, -4.19963520e-09, -4.73777284e-09, -6.14819143e-09,
        -1.25932486e-08, -7.43659815e-09, 2.31824658e-08, 1.71965705e-08,
        1.21306784e-08, 1.06988882e-08, 1.16590390e-08, 9.75730522e-09,
        7.94239438e-09, 6.35374341e-08, 6.39672805e-08, -8.46667705e-08,
        -9.17287715e-08, -1.56220815e-08, 7.89315087e-09, 1.27873542e-08,
        9.46250074e-09, 7.33102190e-09, 3.94909444e-09, 2.94467594e-09,
        -1.33963147e-09, 1.84012031e-10, -2.94676263e-10, 1.22812926e-09,
        -5.16294739e-10, 7.42058314e-10, -5.27653564e-10, 7.23349923e-10,
        -2.45142393e-10, 7.04235558e-10])}


BWD_FORCE_TEST_DATA = {
    "Z": np.array([
        -1.144605054e-41, -9.836268325e-41, -1.519660781e-39, -1.067675005e-37,
        -3.637070544e-36, 1.311769831e-33, 1.956326339e-32, 8.946207998e-31,
        -5.793197816e-30, -1.137351089e-28, 1.121149244e-27, -3.534360022e-27,
        1.567873141e-26, -5.056932450e-25, -1.608971517e-22, 2.004922964e-19,
        4.727288918e-17, 2.269189751e-15, 2.927798962e-14, 1.258700943e-13,
        2.237640098e-13, 2.032053699e-13, 1.207975565e-13, 4.658621193e-14,
        1.581158839e-14, -4.444359279e-14, -2.714347694e-13, -4.668963341e-13,
        -4.569083257e-13, -3.396605582e-13, -1.829811928e-13, -1.881242895e-14,
        1.200285251e-13, 1.784461380e-14, -3.009112714e-13, 3.355704728e-13,
        2.039407896e-12, 1.868549268e-12, -4.731161708e-13, -1.459901974e-12,
        -7.767960555e-13, -2.257835352e-13, -4.404042228e-14, 1.418872139e-13,
        6.277930960e-14, -5.756475365e-13, -6.521922282e-13, 2.148263527e-13,
        -1.639808882e-13, -2.777338148e-13, 1.072704179e-12, -2.178376676e-12,
        -3.476885285e-12, 5.412226060e-12, 9.503295414e-12, 1.539985520e-12,
        -5.905089041e-12, -6.162901089e-12, -2.735451444e-12, 3.566633600e-13,
        1.826679817e-12, 1.862621062e-12, 1.190316369e-12, 4.196567328e-13,
        5.852753937e-14, 5.209238190e-14]),
    "N": np.array([
        -2.103754595e-41, -1.015433738e-40, -5.732157792e-39, 2.511017243e-37,
        -4.825472547e-35, 5.064666085e-34, -3.262800163e-32, 1.933401234e-30,
        -2.160938475e-29, 2.585629223e-29, -1.931564679e-28, -1.004812067e-26,
        1.025724289e-25, 3.068381753e-25, 2.593488756e-22, -1.445236404e-19,
        -3.714277539e-17, -1.828059838e-15, -2.435133459e-14, -1.116527243e-13,
        -2.295763998e-13, -2.889753856e-13, -3.211732554e-13, -3.774794580e-13,
        -4.643131392e-13, -4.184574144e-13, -6.776457703e-14, 3.026607498e-13,
        4.487027540e-13, 4.140049244e-13, 1.494226770e-13, -2.711979919e-13,
        -5.965503838e-13, -5.046739110e-13, 4.492022856e-13, 2.058172637e-12,
        2.028990543e-12, -6.373426660e-13, -2.144013499e-12, -8.671471231e-13,
        2.512403551e-13, 1.958724563e-13, -1.013513749e-13, -2.849931323e-13,
        -2.005280073e-14, 8.147094415e-13, 1.004360089e-12, 2.525583309e-13,
        -3.460097041e-13, -8.634942390e-13, 2.739077637e-13, 1.239445900e-12,
        -2.795060707e-12, -4.382162903e-12, 1.639647628e-12, 5.574328463e-12,
        3.137144179e-12, -6.359243310e-13, -2.270006120e-12, -1.966345620e-12,
        -9.793045759e-13, -1.571313263e-13, 3.164180781e-13, 5.241750724e-13,
        3.656482036e-13, 1.959959944e-13]),
    "E": np.array([
        3.491949650e-44, 2.090091204e-43, 4.411996467e-42, -3.540640644e-40,
        7.840032432e-38, -6.498957055e-37, 4.233357200e-35, -3.054859947e-33,
        2.971617438e-32, 4.529963801e-31, -6.021693531e-30, 3.328879140e-29,
        -1.906879821e-29, -2.144202577e-26, -1.113613138e-23, 7.845187073e-21,
        2.327663618e-18, 1.402762723e-16, 2.404397256e-15, 1.457080390e-14,
        4.000220635e-14, 6.225045656e-14, 7.055200032e-14, 7.763675261e-14,
        9.305522982e-14, 1.111276746e-13, 1.145602120e-13, 9.459132048e-14,
        6.530428896e-14, 4.197413583e-14, 3.201656034e-14, 4.050846554e-14,
        6.881729412e-14, 1.009573838e-13, -5.109412363e-15, -8.739020597e-13,
        -2.511360925e-12, -2.448789866e-12, -1.412435681e-13, 1.086014048e-12,
        5.585021785e-13, -7.026890015e-14, -9.102727437e-13, -2.966515169e-12,
        -3.372263781e-12, 4.404603377e-12, 1.395803582e-11, 8.783998133e-12,
        -5.567695749e-12, -9.529876770e-12, -4.049516103e-12, -2.822773937e-13,
        4.770333059e-13, 5.966545649e-13, 6.661652548e-13, 5.019591532e-13,
        1.669841989e-13, -4.952005198e-14, -5.601889199e-14, -1.285319317e-14,
        -2.494078214e-14, -5.266668463e-15, -7.113536223e-15, 6.037726534e-15,
        6.179420397e-14, 9.187955135e-14]),
    "R": np.array([
        -2.103757326e-41, -1.015435889e-40, -5.732154730e-39, 2.511019212e-37,
        -4.825478462e-35, 5.064668733e-34, -3.262801965e-32, 1.933403426e-30,
        -2.160940014e-29, 2.585530503e-29, -1.931436638e-28, -1.004816791e-26,
        1.025722509e-25, 3.068816608e-25, 2.593712484e-22, -1.445394824e-19,
        -3.714748788e-17, -1.828344705e-15, -2.435623213e-14, -1.116824798e-13,
        -2.296582525e-13, -2.891029075e-13, -3.213177967e-13, -3.776384630e-13,
        -4.645036971e-13, -4.186852691e-13, -6.800024005e-14, 3.024654053e-13,
        4.485673835e-13, 4.139176493e-13, 1.493564587e-13, -2.712807986e-13,
        -5.966907711e-13, -5.048806489e-13, 4.492118511e-13, 2.059967085e-12,
        2.034155538e-12, -6.323008159e-13, -2.143718226e-12, -8.693806979e-13,
        2.500902223e-13, 1.960166803e-13, -9.947748791e-14, -2.788863616e-13,
        -1.311141314e-14, 8.056414402e-13, 9.756272482e-13, 2.344771336e-13,
        -3.345486287e-13, -8.438764580e-13, 2.822425601e-13, 1.240024304e-12,
        -2.796036694e-12, -4.383381752e-12, 1.638272944e-12, 5.573283440e-12,
        3.136793819e-12, -6.358210536e-13, -2.269886004e-12, -1.966314998e-12,
        -9.792511641e-13, -1.571201528e-13, 3.164320501e-13, 5.241615342e-13,
        3.655202340e-13, 1.958064577e-13]),
    "T": np.array([
        8.383496840e-45, 4.509538590e-48, 7.386877980e-42, -1.627953417e-40,
        2.092561349e-38, -3.925981163e-37, 2.482680944e-35, -9.247892997e-34,
        1.476386014e-32, -5.062170719e-31, 6.419267023e-30, -1.260603477e-29,
        -1.920625990e-28, 2.081039581e-26, 1.060227350e-23, -7.547688249e-21,
        -2.251205350e-18, -1.365131633e-16, -2.354268261e-15, -1.434095112e-14,
        -3.952956990e-14, -6.165550827e-14, -6.989075951e-14, -7.685959816e-14,
        -9.209930741e-14, -1.102661017e-13, -1.144204852e-13, -9.521410597e-14,
        -6.622774404e-14, -4.282621959e-14, -3.232405872e-14, -3.995015565e-14,
        -6.758923073e-14, -9.991836755e-14, 4.184779893e-15, 8.696637407e-13,
        2.507179204e-12, 2.450096561e-12, 1.456564283e-13, -1.084226843e-12,
        -5.590181394e-13, 6.986557455e-14, 9.104794333e-13, 2.967095504e-12,
        3.372297913e-12, -4.406271014e-12, -1.396007359e-11, -8.784499382e-12,
        5.568396168e-12, 9.531633967e-12, 4.048943723e-12, 2.797255653e-13,
        -4.712790440e-13, -5.876332162e-13, -6.695388346e-13, -5.134320848e-13,
        -1.734412286e-13, 5.082891059e-14, 6.069127135e-14, 1.690062024e-14,
        2.695649423e-14, 5.590090713e-15, 6.462217690e-15, -7.116656646e-15,
        -6.254671003e-14, -9.228278774e-14])}


FWD_TEST_DATA = {
    "Z": np.array([
        -4.05130050e-39, 1.18143139e-36, 2.74070476e-34, -2.17753206e-33,
        2.24870888e-32, -2.97897814e-30, 4.35393435e-28, -2.91575774e-26,
        1.16624902e-25, -5.43645090e-24, 4.64538470e-22, -7.41396886e-21,
        4.88933049e-20, -7.73084100e-20, -8.99641408e-19, -1.80542628e-17,
        -1.60475237e-14, -2.68348506e-12, -2.14458150e-10, -6.38909514e-09,
        -4.36153968e-08, -6.84710839e-08, -4.22740921e-08, -3.29152593e-08,
        -3.16327608e-08, -5.38883520e-08, -4.59771788e-08, 1.33398909e-08,
        7.23766588e-08, 1.13321925e-07, 1.29550253e-07, 1.29147418e-07,
        1.28760201e-07, 1.23260252e-07, 1.26735241e-07, 1.58788596e-07,
        5.13654241e-08, -2.34847102e-07, -1.49230626e-07, 5.29356978e-08,
        4.73639076e-08, -7.85615130e-09, -5.48621956e-08, -7.01396310e-08,
        -8.58697608e-08, -9.93042468e-08, -8.30175896e-08, -5.91832289e-08,
        8.17326009e-08, -1.03750882e-07, 5.86545423e-07, -5.07725133e-07,
        -2.06001601e-07, 2.12479505e-06, 8.79514605e-07, -1.18594410e-06,
        -1.64692353e-06, -7.98518592e-07, 3.91671142e-08, 4.48087546e-07,
        5.21543798e-07, 3.26319762e-07, 1.36250506e-07, -4.74254088e-08,
        -1.06125346e-07, -1.45335127e-07]),
    "N": np.array([
        -1.67557648e-39, 1.16346948e-36, 2.59132386e-34, -1.79557933e-33,
        2.56362583e-32, -2.82327248e-30, 3.99233123e-28, -2.71409199e-26,
        9.52113831e-26, -5.30627242e-24, 4.15604506e-22, -6.16527674e-21,
        4.30705503e-20, -1.49800801e-19, -2.10158076e-19, 1.20087297e-17,
        1.07156708e-14, 1.94138476e-12, 1.62873196e-10, 4.96696603e-09,
        3.52024483e-08, 6.52452724e-08, 6.69432349e-08, 8.78961262e-08,
        1.15236024e-07, 1.77972368e-07, 2.08325189e-07, 1.60708553e-07,
        1.00559938e-07, 4.16285374e-08, 2.95686813e-09, 1.48251236e-08,
        6.76853143e-08, 1.44531653e-07, 1.93253851e-07, 8.56857529e-08,
        -1.48725230e-07, -1.87876782e-07, 1.42435462e-07, 1.93464272e-07,
        1.37049322e-07, 1.07985513e-07, 1.05652761e-07, 1.01419409e-07,
        8.63033331e-08, 5.41702843e-08, -5.88945006e-08, -1.51695375e-07,
        -6.24887101e-09, -1.35808475e-07, 7.31740134e-08, 3.48703949e-07,
        -8.54940276e-07, -1.97130939e-07, 1.31894338e-06, 9.45809560e-07,
        3.78350168e-08, -5.62235612e-07, -4.71921664e-07, -2.93208995e-07,
        3.36482461e-08, 9.53978933e-08, 2.24948694e-07, 1.11234077e-07,
        1.37668094e-07, 1.70508011e-08]),
    "E": np.array([
        3.19160217e-42, -2.57005909e-39, -5.80297431e-37, 3.69023105e-36,
        -2.47643012e-35, 7.81070549e-33, -8.26147631e-31, 5.87408574e-29,
        -1.57485921e-28, 4.25443069e-27, -9.53367431e-25, 1.49786868e-23,
        -1.07418989e-22, 4.22563640e-22, 2.15076418e-22, -2.98695005e-20,
        -1.79852531e-17, -2.86746669e-15, -2.41055964e-13, -5.42837962e-12,
        -1.82342835e-14, 1.49403915e-10, 3.80522180e-10, 6.27474550e-10,
        9.23978421e-10, 1.25193283e-09, 1.80268910e-09, 2.47343709e-09,
        3.04292432e-09, 3.47804223e-09, 3.75884256e-09, 3.90556658e-09,
        4.04025352e-09, 4.28017196e-09, 4.70628902e-09, 5.46133129e-09,
        3.39339712e-09, -1.12286137e-08, -1.46665643e-08, -1.17285588e-08,
        -9.90297341e-09, -1.03839581e-08, -1.19133999e-08, -1.47093864e-08,
        -3.10049456e-08, -5.23373500e-08, -1.26686233e-08, 7.74259771e-08,
        8.56009515e-08, 9.96378574e-09, -1.36933244e-08, -1.45441539e-08,
        -9.56649417e-09, -8.09822738e-09, -8.12379521e-09, -3.46165126e-09,
        5.12904785e-10, 1.01061526e-09, 1.83647695e-09, 1.17065733e-10,
        -6.40068677e-10, 9.27899296e-11, -1.44814992e-09, 1.41196163e-10,
        -6.60389092e-10, -1.94308571e-10]),
    "R": np.array([
        1.67557950e-39, -1.16347230e-36, -2.59133032e-34, 1.79558312e-33,
        -2.56362549e-32, 2.82328258e-30, -3.99233977e-28, 2.71409833e-26,
        -9.52115055e-26, 5.30626994e-24, -4.15605588e-22, 6.16529451e-21,
        -4.30706801e-20, 1.49801354e-19, 2.10158074e-19, -1.20087657e-17,
        -1.07156851e-14, -1.94138655e-12, -1.62873348e-10, -4.96696668e-09,
        -3.52023737e-08, -6.52448267e-08, -6.69423099e-08, -8.78946484e-08,
        -1.15233878e-07, -1.77969414e-07, -2.08321037e-07, -1.60703121e-07,
        -1.00553461e-07, -4.16212901e-08, -2.94912480e-09, -1.48170531e-08,
        -6.76768546e-08, -1.44522537e-07, -1.93243754e-07, -8.56743299e-08,
        1.48731900e-07, 1.87853271e-07, -1.42465349e-07, -1.93488004e-07,
        -1.37069416e-07, -1.08006658e-07, -1.05677059e-07, -1.01449472e-07,
        -8.63669697e-08, -5.42778989e-08, 5.88682992e-08, 1.51854424e-07,
        6.42505565e-09, 1.35828696e-07, -7.32020442e-08, -3.48733148e-07,
        8.54918773e-07, 1.97113852e-07, -1.31895730e-06, -9.45814682e-07,
        -3.78338809e-08, 5.62236501e-07, 4.71924444e-07, 2.93208615e-07,
        -3.36494923e-08, -9.53975002e-08, -2.24951199e-07, -1.11233551e-07,
        -1.37669162e-07, -1.70511650e-08]),
    "T": np.array([
        2.57350260e-43, 1.75210397e-40, 4.69075234e-38, 5.73194241e-39,
        -2.80044928e-35, -1.99936756e-33, 4.37894319e-33, -2.87485066e-30,
        -3.84940599e-29, 6.66781647e-27, 9.79002141e-26, -2.28827371e-24,
        1.87639078e-23, -1.14218224e-22, 2.17505777e-22, 5.15110485e-21,
        -4.07153208e-18, -1.12861516e-15, -9.41968100e-14, -4.79545410e-12,
        -7.24412048e-11, -2.83702094e-10, -5.18314894e-10, -8.08395409e-10,
        -1.16117410e-09, -1.61826202e-09, -2.23149428e-09, -2.80422849e-09,
        -3.24990679e-09, -3.56372153e-09, -3.76492091e-09, -3.93607381e-09,
        -4.17956595e-09, -4.57766159e-09, -5.10406575e-09, -5.63769215e-09,
        -3.08725933e-09, 1.16153087e-08, 1.43733492e-08, 1.13303141e-08,
        9.62085510e-09, 1.01616627e-08, 1.16959029e-08, 1.45005972e-08,
        3.08272363e-08, 5.22257369e-08, 1.27898227e-08, -7.71135688e-08,
        -8.55879077e-08, -9.68422141e-09, 1.35426766e-08, 1.38263636e-08,
        1.13262519e-08, 8.50397738e-09, 5.40891293e-09, 1.51482393e-09,
        -5.90781921e-10, 1.46672210e-10, -8.65086673e-10, 4.86465246e-10,
        5.70806995e-10, -2.89153287e-10, 9.85120645e-10, -3.70156042e-10,
        3.77016695e-10, 1.59211410e-10])}
