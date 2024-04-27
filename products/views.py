from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import HttpResponse, get_object_or_404

from .models import Products, ProductsCategory, ProductImages, TagsKeywords, ProductReviewsRatings, ProductInteraction


# Create your views here.
# Util functions

def getSingleProdct(request,id):
    product = get_object_or_404(Products,id=id)
    try:
        prodCat = get_object_or_404(ProductsCategory,product=product)
    except:
        prodCat = {
            "subcategory1":"",
            "subcategory2":"",
            "category":"",
        }
        prodCat = ProductsCategory()
    try:
        tags = get_object_or_404(TagsKeywords,product=product)
    except:
        tags={
            "tags":""
        }
        tags = TagsKeywords()
    try:
        rating = get_object_or_404(ProductReviewsRatings,product=product)
    except:
        rating={

            "rating":"",
            "review": ""
        }
        rating = ProductReviewsRatings()
    try:
        # images = get_object_or_404(ProductImages, product=product)
        # img_list = [i.image for i in images]
        images = list(ProductImages.objects.filter(product=product))
        img_list = [i.image.url for i in images]
    except:
        images = []
        img_list = []

    data = {
        "id":product.id,
        "product_name":product.product_name,
        "product_description":product.product_description,
        "brand":product.brand,
        "price":product.price,
        "stock_quantity":product.stock_quantity,
        "sku":product.sku,
        "category":prodCat.category,
        "subcategory1":prodCat.subcategory1,
        "subcategory2":prodCat.subcategory2,
        "review":rating.review,
        "rating":rating.rating,
        "tags":tags.keyword,
        "images":img_list
    }
    return JsonResponse(data)

def gatherData(products):
    allProducts = []
    for product in products:
        try:
            try:
                prodCat = get_object_or_404(ProductsCategory,product=product)
            except:
                prodCat = {
                        "subcategory1":"",
                        "subcategory2":"",
                        "category":"",
                        }
                prodCat = ProductsCategory()
            try:
                tags = get_object_or_404(TagsKeywords,product=product)
            except:
                tags={
                        "tags":""
                }
                tags = TagsKeywords()
            try:
                rating = get_object_or_404(ProductReviewsRatings,product=product)
            except:
                rating={

                    "rating":"",
                    "review": ""
                 }
                rating = ProductReviewsRatings()

            images = list(ProductImages.objects.filter(product=product))


            img_list = [i.image.url for i in images]
            data = {
                "id": product.id,
                "product_name": product.product_name,
                "product_description": product.product_description,
                "brand": product.brand,
                "price": product.price,
                "stock_quantity": product.stock_quantity,
                "sku": product.sku,
                "category": prodCat.category,
                "subcategory1": prodCat.subcategory1,
                "subcategory2": prodCat.subcategory2,
                "review": rating.review,
                "rating": rating.rating,
                "tags": tags.keyword,
                "images":img_list
            }
            allProducts.append(data)
        except:
            continue


    return allProducts

def getAll(request):
    a = Products.objects.all()
    return JsonResponse( {"data":gatherData(a)})

def getCategoryProducts(request,cat):
    prodCat = ProductsCategory.objects.filter(category=cat)
    allProds = []
    for i in prodCat:
        product = i.product

        # tags = get_object_or_404(TagsKeywords, product=product)
        # rating = get_object_or_404(ProductReviewsRatings, product=product)
        try:
            images = ProductImages.oject.filter(product=product)
        except:
            images = []
        img_list = [i.image for i in images]
        data = {
            "id": product.id,
            "product_name": product.product_name,
            "product_description": product.product_description,
            "brand": product.brand,
            "price": product.price,
            "stock_quantity": product.stock_quantity,
            "sku": product.sku,
            "category": i.category,
            "subcategory1": i.subcategory1,
            "subcategory2": i.subcategory2,
            "review": [],
            "rating": [],
            "tags": [],
            "images":img_list
        }
        allProds.append(data)
    return HttpResponse(str({"data":allProds}))

def getIncrement(request,pid,uid):
    if request.method == "GET":
         prod = get_object_or_404(User,pk=uid)
         uid = get_object_or_404(Products,id=pid)
         incremented_product = ProductInteraction()
         incremented_product.product = uid
         incremented_product.user = prod
         incremented_product.save()
         return JsonResponse({"result":"incremented"})
    return JsonResponse({"result":"Invalid Request"})



def search(request,keyword):
    products = TagsKeywords.objects.filter(keyword=keyword)
    searchResults = []
    for i in products:
        product = i.product
        prodCat = get_object_or_404(ProductsCategory, product=product)
        rating = get_object_or_404(ProductReviewsRatings, product=product)
        try:
            images = get_object_or_404(ProductImages, product=product)
        except:
            images = []
        img_list = [i.image for i in images]
        data = {
            "id": product.id,
            "product_name": product.product_name,
            "product_description": product.product_description,
            "brand": product.brand,
            "price": product.price,
            "stock_quantity": product.stock_quantity,
            "sku": product.sku,
            "category": prodCat.category,
            "subcategory1": prodCat.subcategory1,
            "subcategory2": prodCat.subcategory2,
            "review": rating.review,
            "rating": rating.rating,
            "tags": i.keyword,
            "images":img_list
        }
        searchResults.append(data)
    return HttpResponse(str({"data":searchResults}))







