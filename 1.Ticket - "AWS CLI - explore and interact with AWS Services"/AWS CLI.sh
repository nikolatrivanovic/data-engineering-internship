AWS CLI
pravljenje s3 bucketa: aws mb s3://NAZIV_BUCKETA NAZIV_BUCKETA mora biti jedinstven u svetu...sta god --region
aws ls 
aws cp sta_kopiram s3://NAZIV_BUCKETA
aws cp s3://NAZIV_BUCKETA/fajl.ext gde_kopiram

aws dynamodb:
aws dynamodb create-table \
    --table-name first-table-nt \
    --attribute-definitions \
        AttributeName=UserID,AttributeType=N \
        AttributeName=OrderID,AttributeType=N \
    --key-schema \
        AttributeName=UserID,KeyType=HASH \
        AttributeName=OrderID,KeyType=RANGE \
    --billing-mode PAY_PER_REQUEST \

point in time:
    aws dynamodb update-table \
    --table-name first-table-nt \
    --point-in-time-recovery-specification PointInTimeRecoveryEnabled=true \


point-in-time
aws dynamodb update-continuous-backups \
    --table-name first-table-nt \
    --point-in-time-recovery-specification PointInTimeRecoveryEnabled=true  

aws dynamodb update-time-to-live \
    --table-name first-table-nt \
    --time-to-live-specification "Enabled=true, AttributeName=ExpirationTime" \


ttl_timestamp=$(date -v +5M +%s)

aws dynamodb update-item \
    --table-name first-table-nt \
    --key '{"OrderID": {"N": "103"}, "UserID": {"N": "2"}}' \
    --update-expression "SET ExpirationTime = :ttl" \
    --expression-attribute-values "{\":ttl\": {\"N\": \"$ttl_timestamp\"}}" \
    --region eu-central-1


aws dynamodb put-item \
    --table-name first-table-nt \
    --item '{
        "UserID": {"N": "2"},
        "OrderID": {"N": "103"},
        "ItemName": {"S": "Tablet"},
        "Quantity": {"N": "3"},
        "Price": {"N": "1500"} }' ... (vise puta)

aws dynamodb scan \
    --table-name first-table-nt \
    --filter-expression "ItemName = :itemName" \
    --expression-attribute-values '{":itemName": {"S": "Tablet"}}' \
    --region eu-central-1


aws s3api put-bucket-versioning --bucket bucket-14-11-nt-v2 --versioning-configuration Status=Enabled

aws s3api get-bucket-versioning --bucket bucket-14-11-nt-v2