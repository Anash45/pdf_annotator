# annotator/admin.py
from django.contrib import admin
from .models import PDFDocument, Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'x_position', 'y_position')

admin.site.register(Comment, CommentAdmin)

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class PDFDocumentAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    list_display = ('id', 'file')

admin.site.register(PDFDocument, PDFDocumentAdmin)
