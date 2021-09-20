import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)
sns.set_theme()

x_axis_labels = ['M2_Matrona',
'M1_MVargas-Martinete',
'M1_ElIndioGitano',
'M1_Pedrosanz',
'M2_PSanz',
'M2_TiaAnicalaPiriniaca',
'M1_JoseMendez',
'M1_AMairena-Martinete',
'M2_ElTorta',
'M1_CurroMairena',
'M2_EMorente',
'M1_JuanTalega',
'M1_ManueldeAngustias',
'M2_EnriqueSotoSordera',
'M1_PansequitoTriana',
'M2_Chocolate',
'M1_Chaqueta',
'M1_PdeLucia',
'M1_NinioGloria',
'M1_DiegoRubichi',
'M2_DAgujetas',
'M2_MariaSolea',
'M1_PacoelLobo',
'M1_TioMollino',
'M2_SDonday',
'M2_Rancapinos',
'M1_ElChocolate',
'M2_AMairena',
'M1_TPabon',
'M2_MAgujetas',
'M1_Mijitahijo',
'M2_ElZambo',
'M1_JHeredia-Martinete',
'M1_AntonioMairena',
'M1_Naranjito',
'M1_AntonioAgujetas',
'M1_MiguelVargas',
'M1_EnriqueMorente',
'M2_ElChaqueta',
'M1_ChanoLobato-Martinete',
'M1_JuanTalega',
'M1_JuanTalega',
'M1_Turronero',
'M1_JuanTalega',
'M1_ElNegrodelPuerto',
'M2_MMairena',
'M2_NiniodeBarbate',
'M1_DiegoClavel',
'M2_MPoveda',
'M1_AMairena',
'M2_Barullo',
'M1_Talegon',
'M1_MSimon-Martinete',
'M1_Chocolate-Martinete',
'M2_ManolilloelHerrao']

y_axis_labels = ['M2_Matrona',
'M1_MVargas-Martinete',
'M1_ElIndioGitano',
'M1_Pedrosanz',
'M2_PSanz',
'M2_TiaAnicalaPiriniaca',
'M1_JoseMendez',
'M1_AMairena-Martinete',
'M2_ElTorta',
'M1_CurroMairena',
'M2_EMorente',
'M1_JuanTalega',
'M1_ManueldeAngustias',
'M2_EnriqueSotoSordera',
'M1_PansequitoTriana',
'M2_Chocolate',
'M1_Chaqueta',
'M1_PdeLucia',
'M1_NinioGloria',
'M1_DiegoRubichi',
'M2_DAgujetas',
'M2_MariaSolea',
'M1_PacoelLobo',
'M1_TioMollino',
'M2_SDonday',
'M2_Rancapinos',
'M1_ElChocolate',
'M2_AMairena',
'M1_TPabon',
'M2_MAgujetas',
'M1_Mijitahijo',
'M2_ElZambo',
'M1_JHeredia-Martinete',
'M1_AntonioMairena',
'M1_Naranjito',
'M1_AntonioAgujetas',
'M1_MiguelVargas',
'M1_EnriqueMorente',
'M2_ElChaqueta',
'M1_ChanoLobato-Martinete',
'M1_JuanTalega',
'M1_JuanTalega',
'M1_Turronero',
'M1_JuanTalega',
'M1_ElNegrodelPuerto',
'M2_MMairena',
'M2_NiniodeBarbate',
'M1_DiegoClavel',
'M2_MPoveda',
'M1_AMairena',
'M2_Barullo',
'M1_Talegon',
'M1_MSimon-Martinete',
'M1_Chocolate-Martinete',
'M2_ManolilloelHerrao']


distance_matrix = np.array([(0.0,224.150684,362.645732,264.678252,349.570619,162.969231,299.312132,196.962833,127.061671,213.304866,280.070953,256.50665,305.427917,174.493581,268.333434,200.044552,380.859785,283.134805,345.006268,491.011643,244.778384,250.341727,233.157296,214.977725,349.535342,224.023146,199.347607,239.503234,208.825622,477.696258,196.610184,138.643532,330.763186,246.809237,366.65889,310.389612,260.044547,263.828228,263.05916,272.819703,299.566375,226.254088,271.97661,298.560294,323.354779,228.779429,220.995538,397.835376,343.335033,279.219124,166.227558,366.081291,372.005075,287.319234,162.400309),
(224.150684,0.0,302.160302,278.526382,293.355318,306.211578,249.149723,150.688536,259.990805,198.834265,227.114464,157.31197,228.19241,273.158691,186.237054,198.624039,271.919085,323.499533,381.949735,389.159696,318.523934,266.954498,257.577007,201.133984,269.058678,267.947208,184.839536,256.094015,128.798405,411.221457,176.276218,207.031122,277.010245,287.515836,390.561392,269.619325,82.130023,329.436395,246.845727,241.653892,167.960854,123.182603,166.669094,179.933055,360.080933,265.357768,268.033537,361.429693,322.495371,311.408784,217.133598,335.48329,329.504083,184.633715,245.177472),
(362.645732,302.160302,0.0,309.542954,326.953704,381.792943,195.558753,256.651986,413.339925,221.474564,321.542465,279.854899,305.990098,353.733667,225.023193,299.886753,330.93686,244.707107,418.614278,306.087908,391.338865,324.741324,357.083175,238.0598,336.648022,317.181442,281.202535,327.764273,276.911446,232.41591,270.340192,325.78378,254.099711,333.768439,431.355594,269.754232,328.121195,288.736194,438.080342,369.587503,316.03304,334.425954,277.70475,263.582596,298.750642,379.982485,365.621327,243.14273,254.459292,276.358407,276.062466,184.932582,353.610839,400.136899,331.031362),
(264.678252,278.526382,309.542954,0.0,357.245236,259.589388,224.230758,190.031684,259.239323,260.486895,357.403556,270.106195,304.119605,258.109558,257.75685,228.43017,289.643811,182.475705,350.887109,366.045541,255.163541,302.743157,277.342025,180.950188,374.764916,259.412873,175.464726,257.705682,220.56437,380.892768,161.782432,244.49075,267.150851,271.792679,347.216033,210.897869,267.520823,240.953594,359.549062,324.673661,277.655508,244.26281,210.899692,293.951182,244.544654,260.087516,228.461707,315.320369,272.500861,259.082111,215.645028,300.690161,331.969814,324.255319,218.659548),
(349.570619,293.355318,326.953704,357.245236,0.0,367.724922,287.771474,227.388175,353.016137,220.355318,340.862695,317.344843,310.0683,328.688594,345.252156,256.509756,393.246934,342.519369,333.710911,426.663604,264.654642,219.325881,409.44479,258.38442,381.8583,339.424896,252.662926,279.555451,279.2964,396.380957,237.056198,346.795755,330.004664,378.24015,379.741802,435.122752,335.033959,369.792824,442.23521,410.410093,337.902495,341.534751,309.06662,347.986893,406.329897,289.045702,262.870439,399.717308,186.671356,373.856047,276.663205,345.210006,367.929666,426.187775,303.731022),
(162.969231,306.211578,381.792943,259.589388,367.724922,0.0,286.735102,245.319384,99.714477,264.380715,324.852107,335.248018,357.575758,175.242956,316.152517,231.780198,394.545377,245.33511,364.511602,536.829488,230.855501,261.249155,200.223159,263.490389,391.203174,199.679286,210.8232,232.249055,263.51238,486.489211,217.334981,170.628943,351.162458,290.014925,369.965645,327.045935,325.205826,318.694533,310.024683,341.771987,341.43333,272.434045,327.283108,354.499441,344.444077,181.771793,227.513589,417.119181,323.604356,333.372657,181.002693,379.468702,358.220179,343.340604,182.441218),
(299.312132,249.149723,195.558753,224.230758,287.771474,286.735102,0.0,214.908765,324.659571,234.484106,236.834803,209.7542,248.096718,319.092035,152.675245,236.931642,294.534872,224.5524,446.567455,371.147327,333.46247,235.888776,324.42221,244.739239,288.370373,271.386871,191.317499,250.485254,199.157057,285.725287,180.054574,242.612004,220.189857,346.995372,359.697527,261.640595,270.905869,314.923019,385.610344,331.780957,263.012612,264.128255,226.368147,214.780268,357.208953,281.295217,290.275368,271.023486,201.971703,336.273397,206.324432,212.872854,318.146738,340.095164,271.943257),
(196.962833,150.688536,256.651986,190.031684,227.388175,245.319384,214.908765,0.0,214.012695,148.380774,204.309242,176.131516,216.331501,176.131739,196.313754,141.884547,346.595571,266.459465,292.843866,400.013171,262.390044,185.474679,238.044452,145.867874,275.770373,191.216561,137.718159,178.96348,134.69,423.740119,115.863878,176.295598,314.523177,233.520268,304.291617,325.22598,186.885032,249.781486,280.325382,238.736024,241.373186,150.964121,176.691149,232.197717,281.146142,206.173873,174.687782,364.388627,272.231018,228.420589,140.504026,256.325302,282.763285,237.959892,170.194552),
(127.061671,259.990805,413.339925,259.239323,353.016137,99.714477,324.659571,214.012695,0.0,249.750177,239.358573,303.687725,346.327261,136.418314,323.499532,208.766313,407.613604,264.443988,324.095505,551.545667,193.315836,234.815015,207.365362,259.995714,383.737755,175.333705,196.641974,216.023553,237.058539,519.195958,213.952451,123.145932,364.729263,236.348189,332.41321,335.672451,293.957984,260.462547,256.810522,304.645845,328.404327,249.950145,321.875885,364.761745,317.979346,199.295764,166.102538,417.597,346.466718,274.474887,138.411163,401.767378,366.740033,319.904705,107.956719),
(213.304866,198.834265,221.474564,260.486895,220.355318,264.380715,234.484106,148.380774,249.750177,0.0,247.509433,197.452545,257.000091,240.039858,235.45943,168.932799,375.412217,264.672133,330.935718,395.417894,269.174072,194.193437,250.375493,164.129406,297.993587,219.0271,176.249945,191.341782,164.888929,366.130298,120.37752,217.362404,359.140954,255.235262,352.950084,327.710953,228.571006,260.891227,323.372172,278.723568,274.4208,202.530992,258.886544,255.45942,314.317756,219.713525,194.571477,340.346706,279.922086,261.21638,164.581943,270.216929,333.638194,283.909147,207.217984),
(280.070953,227.114464,321.542465,357.403556,340.862695,324.852107,236.834803,204.309242,239.358573,247.509433,0.0,169.201531,200.775184,320.951212,128.004571,217.652488,317.352941,330.407498,425.987463,431.696748,356.420214,231.074495,270.618758,248.813784,233.140276,252.221809,199.845533,248.210503,182.100451,432.462028,188.464966,205.640871,320.339847,354.30623,430.042325,327.987079,216.261914,386.816253,334.483325,278.030449,215.146851,206.147184,200.746385,182.377102,418.951469,300.114752,274.802936,374.004078,276.900805,366.601199,201.828921,262.349611,390.495353,273.095293,271.218542),
(256.50665,157.31197,279.854899,270.106195,317.344843,335.248018,209.7542,176.131516,303.687725,197.452545,169.201531,0.0,165.90862,268.505371,121.310583,160.778378,285.400451,334.463133,365.307187,434.611756,290.503251,187.389942,230.575702,195.276717,230.970791,209.695994,182.25886,203.60621,128.994908,421.701969,134.249282,167.984454,313.416792,294.463232,407.25942,318.700887,173.823474,337.557992,270.301235,201.637423,213.988662,143.973366,205.520588,187.18637,399.798391,290.328567,244.970219,406.397343,306.540507,322.852197,188.64098,298.830956,368.204574,220.413013,257.426627),
(305.427917,228.19241,305.990098,304.119605,310.0683,357.575758,248.096718,216.331501,346.327261,257.000091,200.775184,165.90862,0.0,296.2015,172.741517,182.571618,293.867694,351.712963,350.468094,405.182213,263.168684,208.470423,217.050481,242.061473,218.90933,259.011326,207.803188,251.324231,180.422071,434.224168,197.239793,225.427636,328.652861,323.002925,393.138456,359.882113,232.36982,347.445628,330.108656,254.254638,267.953938,239.773673,209.058668,234.837718,394.742158,315.308149,268.469623,404.638787,290.581206,322.437165,231.987712,320.477531,376.140863,299.778788,274.37251),
(174.493581,273.158691,353.733667,258.109558,328.688594,175.242956,319.092035,176.131739,136.418314,240.039858,320.951212,268.505371,296.2015,0.0,287.326263,177.901209,332.983005,264.742365,252.601577,481.686614,162.990287,221.096287,166.237545,196.556645,372.415371,142.490907,196.886377,206.572875,233.851037,495.315406,204.322414,110.177076,359.557232,200.553841,289.031219,310.330177,253.465491,212.518145,238.84777,269.594145,310.955076,218.308195,307.664339,343.980027,282.442822,211.508101,181.445257,387.167431,355.185545,222.145808,151.311709,346.740223,368.061859,298.090695,129.320405),
(268.333434,186.237054,225.023193,257.75685,345.252156,316.152517,152.675245,196.313754,323.499532,235.45943,128.004571,121.310583,172.741517,287.326263,0.0,187.06783,238.985052,236.147456,406.008374,432.056134,332.344125,214.64753,222.396387,221.249538,219.024431,209.997612,171.69053,221.34813,147.007327,378.443438,166.195408,186.774067,260.501997,343.64998,411.525641,283.166722,190.910413,381.668492,281.672908,242.192833,187.908556,170.845021,163.412177,151.526943,431.309393,289.283739,257.406229,373.491299,280.431385,358.732841,184.959503,255.982324,348.015163,250.096966,257.735465),
(200.044552,198.624039,299.886753,228.43017,256.509756,231.780198,236.931642,141.884547,208.766313,168.932799,217.652488,160.778378,182.571618,177.901209,187.06783,0.0,313.50089,224.499521,288.533474,491.761046,264.427962,226.293986,148.446524,246.626888,228.578329,134.503047,193.990343,199.859915,225.874184,487.881866,216.792809,125.214762,300.702512,237.142955,331.094755,285.315644,251.584384,255.599168,253.88866,237.112504,299.088366,213.363695,284.222765,311.950535,302.489275,203.727183,145.48438,377.476618,369.756382,238.744001,113.780079,348.479205,371.452875,275.803473,160.907601),
(380.859785,271.919085,330.93686,289.643811,393.246934,394.545377,294.534872,346.595571,407.613604,375.412217,317.352941,285.400451,293.867694,332.983005,238.985052,313.50089,0.0,216.112051,406.800254,333.736749,357.11861,376.401114,305.532993,249.443575,367.791492,358.69107,269.868624,378.688162,219.827186,393.744035,268.515657,289.020089,264.929375,388.127953,459.515101,266.512078,264.436325,449.413471,246.342116,369.551557,214.325002,244.111053,226.360701,241.827047,442.751008,448.242899,420.764858,393.067369,389.773817,440.41172,337.075885,366.566987,444.210221,202.457562,432.995231),
(283.134805,323.499533,244.707107,182.475705,342.519369,245.33511,224.5524,266.459465,264.443988,264.672133,330.407498,334.463133,351.712963,264.742365,236.147456,224.499521,216.112051,0.0,227.836086,370.314034,278.156969,287.340134,270.802525,210.560611,389.601326,273.202898,166.495281,238.565292,199.751479,327.027139,147.457256,253.34285,245.308928,268.203004,272.050648,214.17106,277.761075,232.310567,368.8367,330.969326,282.702598,236.560287,244.19737,266.799595,247.821156,238.534392,225.88418,264.798837,221.999204,245.063375,191.350449,244.181743,297.844125,338.213559,231.273397),
(345.006268,381.949735,418.614278,350.887109,333.710911,364.511602,446.567455,292.843866,324.095505,330.935718,425.987463,365.307187,350.468094,252.601577,406.008374,288.533474,406.800254,227.836086,0.0,398.193336,227.921365,295.649573,335.037904,259.341443,426.24305,270.92001,237.884666,280.446539,340.757786,510.877253,232.17063,297.590276,460.878594,256.712921,267.298527,339.642798,385.24976,244.80916,407.251932,355.073319,401.93421,330.774329,380.503241,390.583668,236.683312,287.734594,286.592724,367.599636,274.26663,209.976332,293.173525,323.723434,481.856255,430.022073,289.738981),
(491.011643,389.159696,306.087908,366.045541,426.663604,536.829488,371.147327,400.013171,551.545667,395.417894,431.696748,434.611756,405.182213,481.686614,432.056134,491.761046,333.736749,370.314034,398.193336,0.0,466.214862,519.557506,463.138942,341.649382,428.641165,480.701527,401.417615,487.457586,379.147087,347.732063,389.128182,422.631114,346.874933,433.005528,464.912535,329.126774,391.531294,428.44912,464.975308,400.242399,391.951284,437.051514,337.158367,317.875917,348.603715,496.884499,448.957825,312.554815,384.041744,384.64584,399.735939,267.403676,401.737418,476.155093,443.92126),
(244.778384,318.523934,391.338865,255.163541,264.654642,230.855501,333.46247,262.390044,193.315836,269.174072,356.420214,290.503251,263.168684,162.990287,332.344125,264.427962,357.11861,278.156969,227.921365,466.214862,0.0,200.422064,261.406214,220.109207,364.788577,211.310813,231.059202,185.983988,280.348236,491.461472,236.318583,181.92805,413.119446,265.867326,292.643962,395.260011,326.2863,261.461239,331.466043,334.201469,389.049815,299.855835,351.309073,410.673424,337.287817,198.627942,208.576919,450.84349,296.975211,283.725005,228.844901,390.070974,385.548823,374.449852,184.331607),
(250.341727,266.954498,324.741324,302.743157,219.325881,261.249155,235.888776,185.474679,234.815015,194.193437,231.074495,187.389942,208.470423,221.096287,214.64753,226.293986,376.401114,287.340134,295.649573,519.557506,200.422064,0.0,249.0614,234.727155,294.25504,183.744408,192.560811,103.394761,192.729746,403.68252,135.046863,207.966684,373.592903,286.224345,336.866173,400.33918,280.135507,295.02704,353.584409,287.641312,344.600795,252.873738,319.689721,316.783333,379.726473,147.740158,174.899788,453.783124,216.153519,320.478509,160.349082,294.367219,372.871776,336.010973,184.547138),
(233.157296,257.577007,357.083175,277.342025,409.44479,200.223159,324.42221,238.044452,207.365362,250.375493,270.618758,230.575702,217.050481,166.237545,222.396387,148.446524,305.532993,270.802525,335.037904,463.138942,261.406214,249.0614,0.0,266.410976,255.677499,152.159915,232.406465,283.604721,215.894621,505.923575,234.572842,148.65302,324.282089,269.679448,381.307562,262.14252,238.039458,327.791794,208.910104,265.119169,244.72622,186.363292,249.144408,277.0358,374.187789,288.896765,237.054269,408.677301,410.902866,298.882953,188.124631,405.352927,393.924748,237.282307,215.273788),
(214.977725,201.133984,238.0598,180.950188,258.38442,263.490389,244.739239,145.867874,259.995714,164.129406,248.813784,195.276717,242.061473,196.556645,221.249538,246.626888,249.443575,210.560611,259.341443,341.649382,220.109207,234.727155,266.410976,0.0,307.72271,208.575267,129.738811,226.857524,155.713806,393.105753,147.646171,208.855186,279.116857,190.074601,308.258718,312.81271,183.976254,224.00841,302.577934,254.835984,222.212534,183.283988,212.986622,239.479974,279.912004,238.984964,196.767272,305.976162,286.416667,215.481505,186.762359,234.331629,296.778314,262.581196,216.312293),
(349.535342,269.058678,336.648022,374.764916,381.8583,391.203174,288.370373,275.770373,383.737755,297.993587,233.140276,230.970791,218.90933,372.415371,219.024431,228.578329,367.791492,389.601326,426.24305,428.641165,364.788577,294.25504,255.677499,307.72271,0.0,240.823381,280.686654,310.5369,253.106601,485.29193,249.135744,258.347003,367.463426,353.524227,440.695999,404.904009,306.838989,372.16141,349.300967,316.997804,346.88918,304.750306,300.198812,300.116576,413.249367,338.775,319.52336,397.132751,378.956339,369.168601,261.580989,352.437106,441.804723,366.932865,311.375862),
(224.023146,267.947208,317.181442,259.412873,339.424896,199.679286,271.386871,191.216561,175.333705,219.0271,252.221809,209.695994,259.011326,142.490907,209.997612,134.503047,358.69107,273.202898,270.92001,480.701527,211.310813,183.744408,152.159915,208.575267,240.823381,0.0,191.673719,190.631679,240.588017,435.916212,218.51544,138.525033,361.367242,208.542735,298.605178,325.501042,274.111779,251.048377,258.48354,274.78252,324.365091,212.17079,303.533277,346.615589,310.313588,193.238095,156.123387,408.303809,359.396226,254.768512,103.541573,382.379692,353.729082,311.914873,135.350803),
(199.347607,184.839536,281.202535,175.464726,252.662926,210.8232,191.317499,137.718159,196.641974,176.249945,199.845533,182.25886,207.803188,196.886377,171.69053,193.990343,269.868624,166.495281,237.884666,401.417615,231.059202,192.560811,232.406465,129.738811,280.686654,191.673719,0.0,179.66528,120.755409,388.751538,95.856727,172.882934,235.264591,223.308291,326.918978,307.794727,170.674094,263.425673,304.607157,268.204013,223.855546,156.159704,205.781431,230.65806,317.269286,161.146925,163.106471,313.270211,231.791025,265.689841,141.986925,273.240569,260.490132,251.264986,134.132912),
(239.503234,256.094015,327.764273,257.705682,279.555451,232.249055,250.485254,178.96348,216.023553,191.341782,248.210503,203.60621,251.324231,206.572875,221.34813,199.859915,378.688162,238.565292,280.446539,487.457586,185.983988,103.394761,283.604721,226.857524,310.5369,190.631679,179.66528,0.0,203.336392,396.010702,155.50918,176.123235,360.921154,251.709178,336.049494,371.917274,292.104186,280.077007,338.98088,249.042317,354.60703,272.878647,335.321718,316.596724,341.857285,127.74853,137.715492,411.605475,255.963555,301.835816,143.828394,295.577424,363.966527,338.738293,158.604673),
(208.825622,128.798405,276.911446,220.56437,279.2964,263.51238,199.157057,134.69,237.058539,164.888929,182.100451,128.994908,180.422071,233.851037,147.007327,225.874184,219.827186,199.751479,340.757786,379.147087,280.348236,192.729746,215.894621,155.713806,253.106601,240.588017,120.755409,203.336392,0.0,383.099126,104.34505,172.590253,254.018129,275.702675,374.88467,281.315492,148.674989,318.2584,257.091103,237.678238,181.196704,132.246385,160.376158,153.885948,357.945665,238.499674,234.627135,378.315606,271.344446,295.128094,171.135951,295.960058,297.24652,207.640119,215.993382),
(477.696258,411.221457,232.41591,380.892768,396.380957,486.489211,285.725287,423.740119,519.195958,366.130298,432.462028,421.701969,434.224168,495.315406,378.443438,487.881866,393.744035,327.027139,510.877253,347.732063,491.461472,403.68252,505.923575,393.105753,485.29193,435.916212,388.751538,396.010702,383.099126,0.0,380.048753,449.915956,349.013563,462.901321,544.806677,383.817101,439.942397,429.429465,526.665984,475.52384,432.002695,471.498058,398.154596,384.801255,470.140302,432.01124,392.988365,328.714485,297.155805,453.404366,400.818001,314.096775,435.206596,532.862928,440.925807),
(196.610184,176.276218,270.340192,161.782432,237.056198,217.334981,180.054574,115.863878,213.952451,120.37752,188.464966,134.249282,197.239793,204.322414,166.195408,216.792809,268.515657,147.457256,232.17063,389.128182,236.318583,135.046863,234.572842,147.646171,249.135744,218.51544,95.856727,155.50918,104.34505,380.048753,0.0,164.945608,222.508063,256.1447,256.475435,344.448392,199.11967,287.855188,304.438663,256.621227,245.377126,166.464943,237.91679,222.794767,344.975544,179.219323,163.334651,378.3922,235.061661,292.863027,103.283961,264.48435,274.87612,252.998826,150.485696),
(138.643532,207.031122,325.78378,244.49075,346.795755,170.628943,242.612004,176.295598,123.145932,217.362404,205.640871,167.984454,225.427636,110.177076,186.774067,125.214762,289.020089,253.34285,297.590276,422.631114,181.92805,207.966684,148.65302,208.855186,258.347003,138.525033,172.882934,176.123235,172.590253,449.915956,164.945608,0.0,278.393114,198.836524,309.276743,257.898543,192.407644,254.649304,169.752198,229.566465,236.773589,161.910343,234.727452,273.818828,305.197712,206.420435,184.665657,401.099111,357.114381,230.593848,134.41249,401.497089,344.102531,219.844202,121.843599),
(330.763186,277.010245,254.099711,267.150851,330.004664,351.162458,220.189857,314.523177,364.729263,359.140954,320.339847,313.416792,328.652861,359.557232,260.501997,300.702512,264.929375,245.308928,460.878594,346.874933,413.119446,373.592903,324.282089,279.116857,367.463426,361.367242,235.264591,360.921154,254.018129,349.013563,222.508063,278.393114,0.0,356.781422,412.892217,242.862557,259.980813,337.390444,366.272338,322.131196,242.797684,240.605162,231.8283,215.757556,354.798989,369.435177,342.319339,257.818916,309.021873,338.007526,289.524666,331.249913,326.821473,311.944927,323.474348),
(246.809237,287.515836,333.768439,271.792679,378.24015,290.014925,346.995372,233.520268,236.348189,255.235262,354.30623,294.463232,323.002925,200.553841,343.64998,237.142955,388.127953,268.203004,256.712921,433.005528,265.867326,286.224345,269.679448,190.074601,353.524227,208.542735,223.308291,251.709178,275.702675,462.901321,256.1447,198.836524,356.781422,0.0,299.49181,236.548441,267.725792,191.667946,303.322116,240.369281,314.091007,202.224817,284.53784,298.535072,246.429648,263.551552,218.080598,292.542123,347.279518,200.663226,210.423896,349.210991,402.415156,305.785244,204.148138),
(366.65889,390.561392,431.355594,347.216033,379.741802,369.965645,359.697527,304.291617,332.41321,352.950084,430.042325,407.25942,393.138456,289.031219,411.525641,331.094755,459.515101,272.050648,267.298527,464.912535,292.643962,336.866173,381.307562,308.258718,440.695999,298.605178,326.918978,336.049494,374.88467,544.806677,256.475435,309.276743,412.892217,299.49181,0.0,367.044398,373.427489,277.560144,386.431675,378.765399,388.172649,323.262517,372.728785,411.214672,238.274922,316.104211,322.794219,427.741695,395.197414,266.809939,306.327952,386.782616,468.695854,395.930141,286.867487),
(310.389612,269.619325,269.754232,210.897869,435.122752,327.045935,261.640595,325.22598,335.672451,327.710953,327.987079,318.700887,359.882113,310.330177,283.166722,285.315644,266.512078,214.17106,339.642798,329.126774,395.260011,400.33918,262.14252,312.81271,404.904009,325.501042,307.794727,371.917274,281.315492,383.817101,344.448392,257.898543,242.862557,236.548441,367.044398,0.0,249.331156,266.329916,256.606932,312.300103,171.716016,170.966845,160.822024,208.840576,232.471137,307.217687,285.856172,298.03317,289.865975,293.729353,236.691186,305.436865,333.353263,232.272687,313.590524),
(260.044547,82.130023,328.121195,267.520823,335.033959,325.205826,270.905869,186.885032,293.957984,228.571006,216.261914,173.823474,232.36982,253.465491,190.910413,251.584384,264.436325,277.761075,385.24976,391.531294,326.2863,280.135507,238.039458,183.976254,306.838989,274.111779,170.674094,292.104186,148.674989,439.942397,199.11967,192.407644,259.980813,267.725792,373.427489,249.331156,0.0,271.658181,188.298012,231.667168,141.209126,80.776322,146.953171,174.616378,305.010929,225.49139,207.44866,312.232414,291.354286,278.408757,192.081328,317.479365,325.372006,162.191701,248.56909),
(263.828228,329.436395,288.736194,240.953594,369.792824,318.694533,314.923019,249.781486,260.462547,260.891227,386.816253,337.557992,347.445628,212.518145,381.668492,255.599168,449.413471,232.310567,244.80916,428.44912,261.461239,295.02704,327.791794,224.00841,372.16141,251.048377,263.425673,280.077007,318.2584,429.429465,287.855188,254.649304,337.390444,191.667946,277.560144,266.329916,271.658181,0.0,281.753643,273.047128,283.345875,190.901108,244.055405,329.592546,203.124693,236.022627,221.74009,322.340558,312.883649,166.937433,225.826667,286.357362,371.585303,327.8876,238.977225),
(263.05916,246.845727,438.080342,359.549062,442.23521,310.024683,385.610344,280.325382,256.810522,323.372172,334.483325,270.301235,330.108656,238.84777,281.672908,253.88866,246.342116,368.8367,407.251932,464.975308,331.466043,353.584409,208.910104,302.577934,349.300967,258.48354,304.607157,338.98088,257.091103,526.665984,304.438663,169.752198,366.272338,303.322116,386.431675,256.606932,188.298012,281.753643,0.0,225.098725,215.925625,151.82473,240.051704,253.448965,327.280683,256.33738,238.730126,422.681921,406.897962,287.69618,219.328643,422.339607,438.649123,121.958655,262.292612),
(272.819703,241.653892,369.587503,324.673661,410.410093,341.771987,331.780957,238.736024,304.645845,278.723568,278.030449,201.637423,254.254638,269.594145,242.192833,237.112504,369.551557,330.969326,355.073319,400.242399,334.201469,287.641312,265.119169,254.835984,316.997804,274.78252,268.204013,249.042317,237.678238,475.52384,256.621227,229.566465,322.131196,240.369281,378.765399,312.300103,231.667168,273.047128,225.098725,0.0,268.007472,207.861158,264.333589,293.084071,277.710742,252.965876,195.175776,348.828633,355.881592,275.685305,203.227671,349.696345,381.333928,266.887924,256.373122),
(299.566375,167.960854,316.03304,277.655508,337.902495,341.43333,263.012612,241.373186,328.404327,274.4208,215.146851,213.988662,267.953938,310.955076,187.908556,299.088366,214.325002,282.702598,401.93421,391.951284,389.049815,344.600795,244.72622,222.212534,346.88918,324.365091,223.855546,354.60703,181.196704,432.002695,245.377126,236.773589,242.797684,314.091007,388.172649,171.716016,141.209126,283.345875,215.925625,268.007472,0.0,112.479709,125.685447,146.487299,273.396235,264.603209,263.207947,307.771952,281.628234,332.957867,240.385037,316.831541,329.472626,164.989345,298.372847),
(226.254088,123.182603,334.425954,244.26281,341.534751,272.434045,264.128255,150.964121,249.950145,202.530992,206.147184,143.973366,239.773673,218.308195,170.845021,213.363695,244.111053,236.560287,330.774329,437.051514,299.855835,252.873738,186.363292,183.283988,304.750306,212.17079,156.159704,272.878647,132.246385,471.498058,166.464943,161.910343,240.605162,202.224817,323.262517,170.966845,80.776322,190.901108,151.82473,207.861158,112.479709,0.0,136.032802,158.227153,233.76099,193.579066,195.23785,326.817847,288.800923,262.259458,159.601114,327.130949,314.681636,114.472403,215.208362),
(271.97661,166.669094,277.70475,210.899692,309.06662,327.283108,226.368147,176.691149,321.875885,258.886544,200.746385,205.520588,209.058668,307.664339,163.412177,284.222765,226.360701,244.19737,380.503241,337.158367,351.309073,319.689721,249.144408,212.986622,300.198812,303.533277,205.781431,335.321718,160.376158,398.154596,237.91679,234.727452,231.8283,284.53784,372.728785,160.822024,146.953171,244.055405,240.051704,264.333589,125.685447,136.032802,0.0,156.098996,248.316806,268.968563,247.548764,296.354893,243.298279,308.846092,184.671815,266.715416,330.186266,222.282931,286.49287),
(298.560294,179.933055,263.582596,293.951182,347.986893,354.499441,214.780268,232.197717,364.761745,255.45942,182.377102,187.18637,234.837718,343.980027,151.526943,311.950535,241.827047,266.799595,390.583668,317.875917,410.673424,316.783333,277.0358,239.479974,300.116576,346.615589,230.65806,316.596724,153.885948,384.801255,222.794767,273.818828,215.757556,298.535072,411.214672,208.840576,174.616378,329.592546,253.448965,293.084071,146.487299,158.227153,156.098996,0.0,278.434281,286.538112,263.24229,286.869982,270.510219,337.796707,202.520605,260.240305,329.19946,228.408484,305.918889),
(323.354779,360.080933,298.750642,244.544654,406.329897,344.444077,357.208953,281.146142,317.979346,314.317756,418.951469,399.798391,394.742158,282.442822,431.309393,302.489275,442.751008,247.821156,236.683312,348.603715,337.287817,379.726473,374.187789,279.912004,413.249367,310.313588,317.269286,341.857285,357.945665,470.140302,344.975544,305.197712,354.798989,246.429648,238.274922,232.471137,305.010929,203.124693,327.280683,277.710742,273.396235,233.76099,248.316806,278.434281,0.0,304.610114,274.570442,317.08189,304.421239,137.054506,274.528466,255.989625,412.388166,353.066697,290.456558),
(228.779429,265.357768,379.982485,260.087516,289.045702,181.771793,281.295217,206.173873,199.295764,219.713525,300.114752,290.328567,315.308149,211.508101,289.283739,203.727183,448.242899,238.534392,287.734594,496.884499,198.627942,147.740158,288.896765,238.984964,338.775,193.238095,161.146925,127.74853,238.499674,432.01124,179.219323,206.420435,369.435177,263.551552,316.104211,307.217687,225.49139,236.022627,256.33738,252.965876,264.603209,193.579066,268.968563,286.538112,304.610114,0.0,144.020266,368.8511,260.432368,261.866058,125.730291,345.8817,352.550553,330.299043,148.864644),
(220.995538,268.033537,365.621327,228.461707,262.870439,227.513589,290.275368,174.687782,166.102538,194.571477,274.802936,244.970219,268.469623,181.445257,257.406229,145.48438,420.764858,225.88418,286.592724,448.957825,208.576919,174.899788,237.054269,196.767272,319.52336,156.123387,163.106471,137.715492,234.627135,392.988365,163.334651,184.665657,342.319339,218.080598,322.794219,285.856172,207.44866,221.74009,238.730126,195.175776,263.207947,195.23785,247.548764,263.24229,274.570442,144.020266,0.0,336.98382,297.807314,227.564018,107.77836,342.870758,323.380143,306.812847,115.024278),
(397.835376,361.429693,243.14273,315.320369,399.717308,417.119181,271.023486,364.388627,417.597,340.346706,374.004078,406.397343,404.638787,387.167431,373.491299,377.476618,393.067369,264.798837,367.599636,312.554815,450.84349,453.783124,408.677301,305.976162,397.132751,408.303809,313.270211,411.605475,378.315606,328.714485,378.3922,401.099111,257.818916,292.542123,427.741695,298.03317,312.232414,322.340558,422.681921,348.828633,307.771952,326.817847,296.354893,286.869982,317.08189,368.8511,336.98382,0.0,252.63349,312.121764,300.518262,250.434759,353.959468,407.780735,376.222281),
(343.335033,322.495371,254.459292,272.500861,186.671356,323.604356,201.971703,272.231018,346.466718,279.922086,276.900805,306.540507,290.581206,355.185545,280.431385,369.756382,389.773817,221.999204,274.26663,384.041744,296.975211,216.153519,410.902866,286.416667,378.956339,359.396226,231.791025,255.963555,271.344446,297.155805,235.061661,357.114381,309.021873,347.279518,395.197414,289.865975,291.354286,312.883649,406.897962,355.881592,281.628234,288.800923,243.298279,270.510219,304.421239,260.432368,297.807314,252.63349,0.0,383.537705,213.581995,286.759645,355.609756,405.533721,293.135087),
(279.219124,311.408784,276.358407,259.082111,373.856047,333.372657,336.273397,228.420589,274.474887,261.21638,366.601199,322.852197,322.437165,222.145808,358.732841,238.744001,440.41172,245.063375,209.976332,384.64584,283.725005,320.478509,298.882953,215.481505,369.168601,254.768512,265.689841,301.835816,295.128094,453.404366,292.863027,230.593848,338.007526,200.663226,266.809939,293.729353,278.408757,166.937433,287.69618,275.685305,332.957867,262.259458,308.846092,337.796707,137.054506,261.866058,227.564018,312.121764,383.537705,0.0,228.839164,269.594926,385.689504,289.760535,230.804902),
(166.227558,217.133598,276.062466,215.645028,276.663205,181.002693,206.324432,140.504026,138.411163,164.581943,201.828921,188.64098,231.987712,151.311709,184.959503,113.780079,337.075885,191.350449,293.173525,399.735939,228.844901,160.349082,188.124631,186.762359,261.580989,103.541573,141.986925,143.828394,171.135951,400.818001,103.283961,134.41249,289.524666,210.423896,306.327952,236.691186,192.081328,225.826667,219.328643,203.227671,240.385037,159.601114,184.671815,202.520605,274.528466,125.730291,107.77836,300.518262,213.581995,228.839164,0.0,252.31636,304.971218,275.10842,104.003473),
(366.081291,335.48329,184.932582,300.690161,345.210006,379.468702,212.872854,256.325302,401.767378,270.216929,262.349611,298.830956,320.477531,346.740223,255.982324,348.479205,366.566987,244.181743,323.723434,267.403676,390.070974,294.367219,405.352927,234.331629,352.437106,382.379692,273.240569,295.577424,295.960058,314.096775,264.48435,401.497089,331.249913,349.210991,386.782616,305.436865,317.479365,286.357362,422.339607,349.696345,316.831541,327.130949,266.715416,260.240305,255.989625,345.8817,342.870758,250.434759,286.759645,269.594926,252.31636,0.0,413.053004,419.778306,302.160561),
(372.005075,329.504083,353.610839,331.969814,367.929666,358.220179,318.146738,282.763285,366.740033,333.638194,390.495353,368.204574,376.140863,368.061859,348.015163,371.452875,444.210221,297.844125,481.856255,401.737418,385.548823,372.871776,393.924748,296.778314,441.804723,353.729082,260.490132,363.966527,297.24652,435.206596,274.87612,344.102531,326.821473,402.415156,468.695854,333.353263,325.372006,371.585303,438.649123,381.333928,329.472626,314.681636,330.186266,329.19946,412.388166,352.550553,323.380143,353.959468,355.609756,385.689504,304.971218,413.053004,0.0,373.25508,316.642449),
(287.319234,184.633715,400.136899,324.255319,426.187775,343.340604,340.095164,237.959892,319.904705,283.909147,273.095293,220.413013,299.778788,298.090695,250.096966,275.803473,202.457562,338.213559,430.022073,476.155093,374.449852,336.010973,237.282307,262.581196,366.932865,311.914873,251.264986,338.738293,207.640119,532.862928,252.998826,219.844202,311.944927,305.785244,395.930141,232.272687,162.191701,327.8876,121.958655,266.887924,164.989345,114.472403,222.282931,228.408484,353.066697,330.299043,306.812847,407.780735,405.533721,289.760535,275.10842,419.778306,373.25508,0.0,148.529773),
(162.400309,245.177472,331.031362,218.659548,303.731022,182.441218,271.943257,170.194552,107.956719,207.217984,271.218542,257.426627,274.37251,129.320405,257.735465,160.907601,432.995231,231.273397,289.738981,443.92126,184.331607,184.547138,215.273788,216.312293,311.375862,135.350803,134.132912,158.604673,215.993382,440.925807,150.485696,121.843599,323.474348,204.148138,286.867487,313.590524,248.56909,238.977225,262.292612,256.373122,298.372847,215.208362,286.49287,305.918889,290.456558,148.864644,115.024278,376.222281,293.135087,230.804902,104.003473,302.160561,316.642449,148.529773,0.0)])

mask = np.zeros_like(distance_matrix)
mask[np.triu_indices_from(mask)] = True

# uniform_data = np.random.rand(10, 12)
ax = sns.heatmap(distance_matrix, xticklabels=x_axis_labels,
                 yticklabels=y_axis_labels, mask=mask)

plt.show()