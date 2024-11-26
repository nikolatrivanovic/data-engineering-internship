select * from weather limit 10;

returned values:
#	name	time_nano	location_latitude	location_longitude	location_name	weather_temperature	weather_feelslike	weather_pressure	weather_humidity	weather_dewpoint	weather_clouds	weather_windspeed	weather_winddeg	weather_windgust	no_of_people_visited
1	1297 - Dorćol 2, Beograd, Serbia	1648960200000000000	44.82619213661757	20.456258794127013	Dorćol 2, Beograd, Serbia	0.76	-3.43	1007	88	-0.88	32	4.12	250		5184
2	1297 - Dorćol 2, Beograd, Serbia	1649158200000000000	44.82619213661757	20.456258794127013	Dorćol 2, Beograd, Serbia	15.6	14.13	1008	35	0.21	0	3.09	220		5131
3	1297 - Dorćol 2, Beograd, Serbia	1649079000000000000	44.82619213661757	20.456258794127013	Dorćol 2, Beograd, Serbia	10.1	8.24	1015	41	-2.25	0	2.06	140		5121
4	1297 - Dorćol 2, Beograd, Serbia	1648733400000000000	44.82619213661757	20.456258794127013	Dorćol 2, Beograd, Serbia	16.56	16.15	993	72	11.5	0	6.17	120		6635
5	1297 - Dorćol 2, Beograd, Serbia	1649061000000000000	44.82619213661757	20.456258794127013	Dorćol 2, Beograd, Serbia	6.74	5.88	1019	51	-2.37	0	1.54	170		5121
6	1297 - Dorćol 2, Beograd, Serbia	1648747800000000000	44.82619213661757	20.456258794127013	Dorćol 2, Beograd, Serbia	13.14	12.76	991	86	10.85	40	5.66	110		6635
7	1297 - Dorćol 2, Beograd, Serbia	1649183400000000000	44.82619213661757	20.456258794127013	Dorćol 2, Beograd, Serbia	11.26	9.72	1008	49	0.95	0	0	0		5131
8	1297 - Dorćol 2, Beograd, Serbia	1649064600000000000	44.82619213661757	20.456258794127013	Dorćol 2, Beograd, Serbia	7.81	7.11	1019	41	-4.09	0	1.54	160		5121
9	1297 - Dorćol 2, Beograd, Serbia	1648834200000000000	44.82619213661757	20.456258794127013	Dorćol 2, Beograd, Serbia	13.28	12.47	992	69	7.72	20	4.63	10		5207
10	1297 - Dorćol 2, Beograd, Serbia	1648798200000000000	44.82619213661757	20.456258794127013	Dorćol 2, Beograd, Serbia	16.97	16.32	990	61	9.41	20	6.17	150		5207

select * from pollution limit 10;

returned values:
#	name	time_nano	location_latitude	location_longitude	location_name	measurement_pm10atmo	measurement_pm25atmo	measurement_pm100atmo	no_of_people_visited
1	1297 - Dorćol 2, Beograd, Serbia	1649032200000000000	44.82619213661757	20.456258794127013	Dorćol 2, Beograd, Serbia		43	50.5	5121
2	1297 - Dorćol 2, Beograd, Serbia	1648719000000000000	44.82619213661757	20.456258794127013	Dorćol 2, Beograd, Serbia		13	15	6635
3	1297 - Dorćol 2, Beograd, Serbia	1648708200000000000	44.82619213661757	20.456258794127013	Dorćol 2, Beograd, Serbia		11	13	6635
4	1297 - Dorćol 2, Beograd, Serbia	1649017800000000000	44.82619213661757	20.456258794127013	Dorćol 2, Beograd, Serbia		31.5	35	5184
5	1297 - Dorćol 2, Beograd, Serbia	1649093400000000000	44.82619213661757	20.456258794127013	Dorćol 2, Beograd, Serbia		37.5	41.5	5121
6	1297 - Dorćol 2, Beograd, Serbia	1648783800000000000	44.82619213661757	20.456258794127013	Dorćol 2, Beograd, Serbia		5.5	15.5	5207
7	1297 - Dorćol 2, Beograd, Serbia	1648791000000000000	44.82619213661757	20.456258794127013	Dorćol 2, Beograd, Serbia		8	9	5207
8	1297 - Dorćol 2, Beograd, Serbia	1648888200000000000	44.82619213661757	20.456258794127013	Dorćol 2, Beograd, Serbia		63	75	5236
9	1297 - Dorćol 2, Beograd, Serbia	1648812600000000000	44.82619213661757	20.456258794127013	Dorćol 2, Beograd, Serbia		2	2.5	5207
10	1297 - Dorćol 2, Beograd, Serbia	1648924200000000000	44.82619213661757	20.456258794127013	Dorćol 2, Beograd, Serbia		29	31.5	5236

select * from sensor limit 10;

returned values:
#	location_latitude	location_longitude	location_name	name	pms7003measurement_pm10atmo	pms7003measurement_pm25atmo	pms7003measurement_pm100atmo	bmp280measurement_temperature	bmp280measurement_pressure	dht11measurement_humidity	no_of_people_visited
1	44.8226240494248	20.46802286442072	Zorza Klemansoa, Belgrade, Serbia	Levi9 NineAir Belgrade	6	9	9	27.0078125	1007.9279833232316	18	6447
2	44.8226240494248	20.46802286442072	Zorza Klemansoa, Belgrade, Serbia	Levi9 NineAir Belgrade	6	8	8	26.972265625	1007.2888667672848	19	6447
3	44.8226240494248	20.46802286442072	Zorza Klemansoa, Belgrade, Serbia	Levi9 NineAir Belgrade	7	9	9	29.3060546875	1011.1694997887638	12	6463
4	44.8226240494248	20.46802286442072	Zorza Klemansoa, Belgrade, Serbia	Levi9 NineAir Belgrade	31	47	47	30.7658203125	1000.5502421665074	15	6447
5	44.8226240494248	20.46802286442072	Zorza Klemansoa, Belgrade, Serbia	Levi9 NineAir Belgrade	4	5	5	29.6779296875	1006.1905149188184	17	6447
6	44.8226240494248	20.46802286442072	Zorza Klemansoa, Belgrade, Serbia	Levi9 NineAir Belgrade	5	8	9	31.3982421875	1016.4253739838084	9	6463
7	44.8226240494248	20.46802286442072	Zorza Klemansoa, Belgrade, Serbia	Levi9 NineAir Belgrade	7	9	9	27.129296875	1007.7396268087072	19	6447
8	44.8226240494248	20.46802286442072	Zorza Klemansoa, Belgrade, Serbia	Levi9 NineAir Belgrade	7	11	11	27.339453125	1009.010173967031	17	6463
9	44.8226240494248	20.46802286442072	Zorza Klemansoa, Belgrade, Serbia	Levi9 NineAir Belgrade	6	8	8	34.7634765625	1013.51507468932	9	6463
10	44.8226240494248	20.46802286442072	Zorza Klemansoa, Belgrade, Serbia	Levi9 NineAir Belgrade	6	7	7	29.9234375	1006.0518250594804	16	6447
