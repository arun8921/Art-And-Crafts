"""webstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from artcraftapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('index/',views.index),
    path('login_action/', views.sign_in_process),
    path('customer_action/', views.customer_action),
    path('artist_action/', views.artist_action),


    path('login/', views.login_page),
    path('customer_registration/', views.customer_registration),
    path('artist_registration/', views.artist_registration),




    path('Customer/', views.Customer),
    path('admin_home/', views.admin_home),
    path('artist/', views.artist),
    path('admin_logout/', views.admin_logout),


    #admin

    path('check_username/', views.check_username, name='check_username'),
    # path('display_district/', views.display_district, name='display_district'),
    # path('display_shop/', views.display_shop, name='display_shop'),
    # ..................

    path('approve_artist/', views.approve_artist),
    path('approve/<int:id>', views.approve),
    path('reject/<int:id>', views.reject),
    path('artist_list/', views.artist_list),


    path('user_list/', views.user_list),

    path('add_category/', views.add_category),
    path('save_category/', views.save_category),
    path('edit_category/<int:id>', views.edit_category),
    path('update_category/<int:id>', views.update_category),
    path('delete_category/<int:id>', views.delete_category),
    #Product
    path('add_product/', views.add_product),
    path('save_product/', views.save_product),
    path('edit_product/<int:id>', views.edit_product),
    path('update_product/<int:id>', views.update_product),
    path('delete_product/<int:id>', views.delete_product),
    path('product_list/', views.product_list),
    path('checkout/', views.checkout),

    path('add_qty/', views.add_qty, name='add_qty'),
    path('sub_qty/', views.add_qty, name='sub_qty'),
    path('remove_order/', views.add_qty, name='remove_order'),

    path('user_logout/', views.user_logout),
    #Notification
    path('add_notification/', views.add_notification),
    path('save_notification/', views.save_notification),
    path('edit_notification/<int:id>', views.edit_notification),
    path('update_notification/<int:id>', views.update_notification),
    path('delete_notification/<int:id>', views.delete_notification),
    path('manage_notification/', views.notification_list),

    path('add_raw_materials/', views.add_raw_materials),
    path('save_raw_materials/', views.save_raw_materials),
    path('edit_raw_materials/<int:id>', views.edit_raw_materials),
    path('update_raw_materials/<int:id>', views.update_raw_materials),
    path('delete_raw_materials/<int:id>', views.delete_raw_materials),
    path('manage_raw_materials/', views.raw_materials_list),




    path('upload_work/', views.upload_work),
    path('save_upload_work/', views.save_upload_work),
    path('edit_upload_work/<int:id>', views.edit_upload_work),
    path('update_upload_work/<int:id>', views.update_upload_work),
    path('delete_upload_work/<int:id>', views.delete_upload_work),
    path('manage_upload_work/', views.uploaded_work_list),
    path('artist_work_list/', views.artist_work_list),
    path('raw_materials_list_user/', views.raw_materials_list_user),

    path('view_raw_materials/', views.view_raw_materials),
    path('Buy_raw_materials/<int:id>', views.Buy_raw_materials),
    path('payment_raw_matierial/<int:id>', views.payment_raw_matierial),
    path('payment_action_raw_matierial/', views.payment_action_raw_matierial),
    path('raw_materials_order_list/', views.raw_materials_order_list),
    path('adm_order_raw_materials/', views.adm_order_raw_materials),
    path('adm_delivered_raw_materials/', views.adm_delivered_raw_materials),
    path('deliver_raw_materials/<int:id>', views.deliver_raw_materials),



    path('buy_artist_work/<int:id>', views.buy_artist_work),
    path('payment_artist_work/<int:id>', views.payment_artist_work),
    path('payment_action_artist_work/', views.payment_action_artist_work),
    path('artist_work_order_list/', views.artist_work_order_list),
    path('work_order/', views.work_order),
    path('work_order_delivered_list/', views.delivered_work_order),
    path('deliver_work_order/<int:id>', views.deliver_work_order),

    path('artist_work_comment/<int:id>', views.artist_work_comment),
    path('save_comments/<int:id>', views.save_comments),
    path('comment_list/<int:id>', views.comment_list),


    #Complaints
    path('view_complaints/', views.view_complaints),
    path('replied_list/', views.replied_list),
    path('adm_reply_complaint/<int:id>', views.adm_reply_complaint),
    path('add_reply/<int:id>', views.add_reply),

    #  Customer
    path('Complaint/', views.Complaint_frm),
    path('save_complaint/', views.save_complaint),
    path('Complaint_list/', views.Complaint_list),
    path('delete_complaint/<int:id>', views.delete_complaint),

    # SHOP
    # path('shop_category_list/', views.shop_category_list),
    path('display_product/', views.display_product, name='display_product'),
    path('cust_events/', views.cust_events),

    path('payment/<int:id>', views.payment),
    path('pay_action/', views.pay_action),
    path('myorder/', views.myorder),
    path('order_list/', views.order_list),
    path('deliver/<int:id>', views.deliver),
    path('deliverd_list/', views.deliverd_list),
    path('clear_cart/', views.clear_cart),

    path('cust_product/', views.cust_product),

    path('Feedback/', views.Feedback),
    path('save_feedback/', views.save_feedback),
    path('Feedback_list/', views.Feedback_list),
    path('view_feedback/', views.view_feedback),
    path('view_replied_feedback/', views.view_replied_feedback),
    path('adm_reply_feedback/<int:id>', views.adm_reply_feedback),
    path('add_feedback_reply/<int:id>', views.add_feedback_reply),


    path('single/<int:id>', views.single),


    path('cust_product_art/', views.cust_product_art),
    path('cust_product_artist/', views.cust_product_artist),
    path('cust_product_category/', views.cust_product_category),



    ]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

