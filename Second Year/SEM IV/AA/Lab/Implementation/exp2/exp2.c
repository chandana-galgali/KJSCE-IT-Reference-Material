#include<stdio.h>
void swap(int *x, int *y){
    int temp = *x;
    *x = *y;
    *y = temp;
}
int partition(int arr[], int start, int end){
    int pivot_v = arr[end];
    int i = start;
    for(int j = start; j < end; j++){
        if(arr[j] <= pivot_v){
            swap(&arr[i], &arr[j]);
            i++;
        }
    }
    swap(&arr[i], &arr[end]);
    return i;
}
void quicksort_recursion(int arr[], int start, int end){
    if (start < end){
        int pivot_i = partition(arr, start, end);
        quicksort_recursion(arr, start, pivot_i-1);
        quicksort_recursion(arr, pivot_i+1, end);
    }
}
void quicksort(int arr[], int n){
    quicksort_recursion(arr, 0, n-1);
}
void print_arr(int arr[], int n){
    int i;
    for(i = 0; i < n; i++){
        printf("%d ", arr[i]);
    }
}
int main(){
    int n, i;
    printf("Enter the size of the array: ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter the elements of the array: ");
    for(i = 0; i < n; i++){
        scanf("%d", &arr[i]);
    }
    quicksort(arr, n);
    printf("The array after sorting: ");
    print_arr(arr, n);
}
