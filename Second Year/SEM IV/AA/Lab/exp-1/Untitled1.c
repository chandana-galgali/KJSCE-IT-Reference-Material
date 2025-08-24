#include<stdio.h>
#include<stdlib.h>
int insertion_sort(int arr[], int n){
    int i, j, key;
    for(i=1; i<n; i++){
        key=arr[i];
        j=i-1;
        while(j>=0&&arr[j]>key){
            arr[j+1]=arr[j];
            j--;
        }
        arr[j+1]=key;
    }
    return arr[n];
}
int main(){
    int n, i;
    printf("Enter the size of the array: ");
    scanf("%d", &n);
    int arr[n];
    printf("\nEnter the elements of the array:\n");
    for(i=0; i<n; i++){
        scanf("%d", &arr[i]);
    }
    arr[n]=insertion_sort(arr, n);
    printf("\nThe sorted array is:\n");
    for(i=0; i<n; i++){
        printf("%d\t", arr[i]);
    }
    return 0;
}
