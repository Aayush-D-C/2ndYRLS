#include <iostream>
using namespace std;

class Binary_Search
{
    int size;
    int *arr;
    int target;
    int count_steps = 0;

public:
    void array_input()
    {
        cout << "Enter the size of array (greater than 0): ";
        cin >> size;
        arr = new int[size];

        // Array input
        for (int i = 0; i < size; i++) // Fix: i < size
        {
            arr[i] = i + 1; // Filling the array with 1 to size
        }

        cout << "Enter the target number: ";
        cin >> target;

        binary_search(arr, size, target);

    }

    void binary_search(int *arr, int size, int target);

    
    ~Binary_Search(){
        // Clean up memory
        delete[] arr;
    }
    
};

void Binary_Search::binary_search(int *arr, int size, int target)
{
    int low = 0;
    int high = size - 1;

    while (low <= high)
    {
        count_steps++; // Increment step count

        int mid = low + (high - low) / 2; // Calculate middle index

        if (arr[mid] == target) // Compare with element, not index
        {
            cout << "Found the number " << target << " in " << count_steps << " steps." << endl;
            return;
        }
        else if (target < arr[mid]) // Search in left half
        {
            high = mid - 1;
        }
        else // Search in right half
        {
            low = mid + 1;
        }
    }

    // If not found
    cout << "Number " << target << " not found after " << count_steps << " steps." << endl;
}

int main()
{
    Binary_Search b;
    b.array_input();
    return 0;
}
