Lambda funkcija koja biva *trigerovana* kada se neka datoteka ubaci u S3 Bucket (koji potom salje poruku na SQS, a ta poruka trigeruje fju) i ubacuje ime datoteke, timestamp i status u DynamoDB :))


**`File -> Bucket -> SQS("New file") -> λ() -> DynamoDB`**