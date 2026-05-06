void
merge(int *arr, int start, int middle, int end)
{
    int arrL[middle - start];
    int arrR[end - middle + 1];
    int i, idxL, idxR, lSize, rSize;
    
    lSize = middle - start;
    rSize = end - middle + 1;
    
    for (i = 0; i < lSize; i++) {
        arrL[i] = arr[start + i];
    }
    
    for (i = 0; i < rSize; i++) {
        arrR[i] = arr[start + lSize + i];
    }
    
    idxL = 0; idxR = 0;
    for ( i = start; i < end; i++) {
    
        if ( (idxL < lSize) && (arrL[idxL] < arrR[idxR])) {
            arr[i] = arrL[idxL++];
        }
        
        if ( (idxR < rSize) && (arrR[idxR] <= arrL[idxL])) {
            arr[i] = arrR[idxR++];
        }
        
        if ( (idxL == lSize) || (idxR == rSize)) {
            break;
        }
    }
    
    if (idxR != rSize) {
        for (; i < end; i ++) {
            arr[i] = arrR[idxR++];
        }
    } else if (idxL != lSize) {
            for (; i < end; i ++) {
               arr[i] = arrL[idxL++];
            }
        }
    }
    
    return;
}

void
merge_sort(int *arr, int start, int end)
{
 int middle;
 
 if (start < end) {
     middle = (start + end)/2;
     merge_sort(arr, start, middle);
     merge_sort(arr, middle+1, end);
     merge(arr, start, middle, end);
 }
 
 return;
}

typdef enum _return_code {

} return_code;

return_code
sort(int *arr, int len)
{
    if (!arr || !len) {
        return;
    }
    
    merge_sort(arr,  0, len);
    return;
}


