resource "aws_dynamodb_table" "this" {
  name         = "nobel"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "rank"

  attribute {
    name = "rank"
    type = "S"
  }
}
