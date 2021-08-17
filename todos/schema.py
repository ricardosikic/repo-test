import graphene
from graphene_django import DjangoObjectType
from .models import Todo

class TodoType(DjangoObjectType):
    class Meta: 
        model = Todo
        fields = ('id','title')



class Query(graphene.ObjectType):
    todos = graphene.List(TodoType)

    def resolve_todos(root, info, **kwargs):
        # Querying a list
        return Todo.objects.all()


class CreateTodo(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)

    todo = graphene.Field(TodoType)

    @classmethod
    def mutate(cls, root, info, title):
        todo = Todo()
        
        todo.title = title
        todo.save()

        return CreateTodo(todo=todo)


class Mutation(graphene.ObjectType):
    create_todo = CreateTodo.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)