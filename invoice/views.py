from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView

from .models import Item
from .filters import ItemFilter
from .forms import ItemForm


# Create your views here.
# 検索一覧画面
class ItemFilterView(LoginRequiredMixin, FilterView):
	model = Item
	filterset_class = ItemFilter
	# デフォルトの並び順を新しい順とする
	queryset = Item.objects.all().order_by('-created_at')

	# クエリ未指定の時に全件検索を行うために以下のオプションを指定（django-filter2.0以降）
	strict = False

	# 1ページあたりの表示件数
	paginate_by = 10

	# 検索条件をセッションに保存する or 呼び出す
	def get(self, request, **kwargs):
		if request.GET:
			request.session['query'] = request.GET
		else:
			request.GET = request.GET.copy()
			if 'query' in request.session.keys():
				for key in request.session['query'].keys():
					request.GET[key] = request.session['query'][key]

		return super().get(request, **kwargs)


# 詳細画面
class ItemDetailView(LoginRequiredMixin, DetailView):
	model = Item


# 登録画面
class ItemCreateView(LoginRequiredMixin, CreateView):
	model = Item
	form_class = ItemForm
	success_url = reverse_lazy('index')


# 更新画面
class ItemUpdateView(LoginRequiredMixin, UpdateView):
	model = Item
	form_class = ItemForm
	success_url = reverse_lazy('index')


# 削除画面
class ItemDeleteView(LoginRequiredMixin, DeleteView):
	model = Item
	success_url = reverse_lazy('index')

class FormsetMixin(object):
	object = None

	def get(self, request, *args, **kwargs):
		if getattr(self, 'is_update_view', False):
			self.object = self.get_object()
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		formset_class = self.get_formset_class()
		formset = self.get_formset(formset_class)
		return self.render_to_response(self.get_context_data(form=form, formset=formset))

	def post(self, request, *args, **kwargs):
		if getattr(self, 'is_update_view', False):
			self.object = self.get_object()
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		formset_class = self.get_formset_class()
		formset = self.get_formset(formset_class)
		if form.is_valid() and formset.is_valid():
			return self.form_valid(form, formset)
		else:
			return self.form_invalid(form, formset)

	def get_formset_class(self):
		return self.formset_class

	def get_formset(self, formset_class):
		return formset_class(**self.get_formset_kwargs())

	def get_formset_kwargs(self):
		kwargs = {
			'instance': self.object
		}
		if self.request.method in ('POST', 'PUT'):
			kwargs.update({
				'data': self.request.POST,
				'files': self.request.FILES,
			})
		return kwargs

	def form_valid(self, form, formset):
		self.object = form.save()
		formset.instance = self.object
		formset.save()
		return redirect(self.object.get_absolute_url())

	def form_invalid(self, form, formset):
		return self.render_to_response(self.get_context_data(form=form, formset=formset))

class InvoiceMixin(object):
	def form_valid(self, form, formset):

		# formset.saveでインスタンスを取得できるように、既存データに変更が無くても更新対象となるようにする
		for detail_form in formset.forms:
			if detail_form.cleaned_data:
				detail_form.has_changed = lambda: True

		# インスタンスの取得
		invoice = form.save(commit=False)
		formset.instance = invoice
		details = formset.save(commit=False)

		sub_total = 0

		# 明細に単価と合計を設定
		for detail in details:
			detail.unit_price = detail.item.unit_price
			detail.amount = detail.unit_price * detail.quantity
			sub_total += detail.amount

		# 見出しに小計、消費税、合計、担当者を設定
		tax = round(sub_total * 0.08)
		total_amount = sub_total + tax

		invoice.sub_total = sub_total
		invoice.tax = tax
		invoice.total_amount = total_amount
		invoice.created_by = self.request.user

		# DB更新
		with transaction.atomic():
			invoice.save()
			formset.instance = invoice
			formset.save()

		# 処理後は詳細ページを表示
		return redirect(invoice.get_absolute_url())


class InvoiceCreateView(LoginRequiredMixin, InvoiceMixin, FormsetMixin, CreateView):
	template_name = 'invoice/invoice_form.html'
	model = Invoice
	form_class = InvoiceForm
	formset_class = InvoiceDetailFormSet


class InvoiceUpdateView(LoginRequiredMixin, InvoiceMixin, FormsetMixin, UpdateView):
	is_update_view = True
	template_name = 'invoice/invoice_form.html'
	model = Invoice
	form_class = InvoiceForm
	formset_class = InvoiceDetailFormSet
