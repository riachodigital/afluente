# from django.db import models

# Create your models here.
from collections import namedtuple

Cliente = namedtuple('Cliente', 'nome status servico')
