from django.shortcuts import get_object_or_404,redirect,render
from .models import ToDo


#dispplay all the task in the home page
def home(request):
    # Fetch all tasks from the database
    tasks = ToDo.objects.all()
    # Pass tasks to the template
    return render(request, 'list.html', {'tasks': tasks})



def add_task(request):
    # Check if the request method is POST (indicating that the task creation form has been submitted)
    if request.method == 'POST':
        # Create a new task object and save it to the database
        ToDo.objects.create(
            # Set the task title from the POST data
            title=request.POST['title'],
            # Set the task description from the POST data, defaulting to an empty string if not provided
            description=request.POST.get('description', ''),
            # Set the task status from the POST data
            status=request.POST['status']
        )
        
        # Redirect to the home page with a success message in the query parameters
        return redirect('/?success=true')
    
    # If the request method is not POST (i.e., the form was not submitted), redirect to the home page
    return redirect('home')






def edit_task(request, task_id):
    # Retrieve the task object with the given task_id, or return a 404 error if not found
    task = get_object_or_404(ToDo, id=task_id)
    
    # Check if the request method is POST (indicating that the form has been submitted with new data)
    if request.method == 'POST':
        # Update the task's title with the new value from the POST request
        task.title = request.POST.get('title')
        
        # Update the task's description with the new value, or set it to an empty string if not provided
        task.description = request.POST.get('description', '')
        
        # Update the task's status with the new value from the POST request
        task.status = request.POST.get('status')
        
        # Save the updated task object in the database
        task.save()
        
        # Redirect the user to the 'home' page after the task has been successfully updated
        return redirect('home')




def delete_task(request, task_id):
    # Get the task object or return a 404 error if the task with the given ID doesn't exist
    task = get_object_or_404(ToDo, id=task_id)
    
    # Check if the request method is POST (indicating that the delete action is being confirmed)
    if request.method == 'POST':
        # Delete the task from the database
        task.delete()
    
    # Redirect the user to the 'home' page after the deletion
    return redirect('home')
