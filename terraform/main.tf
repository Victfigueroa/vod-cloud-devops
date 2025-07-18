resource "aws_s3_bucket" "devops_bucket" {
  bucket        = var.bucket_name
  force_destroy = true
}
