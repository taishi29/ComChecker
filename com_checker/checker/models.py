from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# 企業情報データベース
class Company(models.Model):
    # 基本情報
    name = models.CharField(max_length=255)  # 企業名
    industry = models.CharField(max_length=100)  # 業種
    location = models.CharField(max_length=255)  # 所在地
    # パラメータ
    work_life_balance_rating = models.DecimalField(
        max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)]
    )  # ワークライフバランス
    compensation_rating = models.DecimalField(
        max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)]
    )  # 待遇・福利厚生
    career_advancement_rating = models.DecimalField(
        max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)]
    )  # 定着率・昇進
    management_relationship_rating = models.DecimalField(
        max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)]
    )  # 上司との関係
    work_environment_rating = models.DecimalField(
        max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)]
    )  # 職場環境
    overall_rating = models.DecimalField(
        max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)]
    )  # 総合評価

    def __str__(self):
        return self.name

# 企業の画像情報
class CompanyImage(models.Model):
    company = models.ForeignKey(Company, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='company_images/')
    
    def __str__(self):
        return f"Image for {self.company.name}"
