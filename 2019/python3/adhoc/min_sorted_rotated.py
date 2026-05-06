#!/usr/bin/env python3


def find_minimum(arr):

    n = arr.size()

    if(n==1):
        return arr.get(0)

            if(n==2) {
                    return Math.min(arr.get(0), arr.get(1));
                    }

            if(n==3) {
                    return Math.min(arr.get(0), Math.min(arr.get(1), arr.get(2)));
                    }

            *
            * All numbers of array are unique as given in question so don't consider the cases when 
         * numbers are equal and get confuse.
         */

        /*
         * consider example [4, 7, 8, 10, 15].
         * for this given array was [4, 7, 8, 10, 15] which was sorted in ascending order
         * and rotated right by 0
         */
        if(arr.get(0)-arr.get(n-1)<0 && arr.get(0)-arr.get(1)<0 && arr.get(n-2)-arr.get(n-1)<0) {
            return arr.get(0);
        }

        /*
         * consider example [15, 10, 8, 7, 4].
         * for this given array was [15, 10, 8, 7, 4] which was sorted in descending order
         * and rotated right by 0
         */
        if(arr.get(0)-arr.get(n-1)>0 && arr.get(0)-arr.get(1)>0 && arr.get(n-2)-arr.get(n-1)>0) {
            return arr.get(n-1);
        }

        if(arr.get(0)-arr.get(n-1) > 0) {
            /*
             * consider example [10, 13, 15, 4, 6, 8].
             * for this given array was [4, 6, 8, 10, 13, 15] which was sorted in ascending order
             * and rotated right by 3
             */
            return find_minimum_in_increasing(arr);
        }
        else {
            /*
             * consider example [8, 6, 4, 15, 13, 10].
             * for this given array was [15, 13, 10, 8, 6, 4] which was sorted in descending order
             * and rotated right by 3
             */
            return find_minimum_in_decreasing(arr);

        }
    }

    public static int find_minimum_in_increasing(List<Integer> arr) {

        int low = 0;
        int high = arr.size()-1;

        while(low<=high) {

            if(arr.get(low)-arr.get(high)<=0) {
                return arr.get(low);
            }

            int mid = (low+high)/2;

            if(arr.get(mid)-arr.get(low)>=0) {

                //Minimum is in right subarray
                low = mid + 1;

            }else {

                //Minimum is in left subarray 
                high = mid;
            }
        }

        return -1;
    }

    public static int find_minimum_in_decreasing(List<Integer> arr) {
        int low = 0;

        int high = arr.size()-1;

        while(low<=high) {

            if(arr.get(low)-arr.get(high)>=0) {

                return arr.get(high);
            }

            int mid = (low + high)/2;

            if(arr.get(mid)-arr.get(low)<0) {

                //Minimum is in right subarray
                low = mid;

            }else {

                //Minimum is in left subarray
                high = mid;
            }
        }

        return -1;
    }

    // ============================= End ==============================
}

