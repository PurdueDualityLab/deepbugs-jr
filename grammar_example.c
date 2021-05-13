// This program is used to assist building up the basic grammar of C
/* comment */

// simple structures
//int some_int;
//float some_float;

// structures can be called like this
struct struct_name
{
    int int_e;
    float float_e;
};

//union union_name { int u_int; float u_float; };

// scope of structures
//struct bigger_struct { struct struct_name s_obj; };

//struct even_bigger_struct { struct bigger_struct bs_obj; int struct_leaf; };

//typedef struct even_bigger_struct ebs;

int main ()
{
    struct struct_name obj1;

    (obj1 . int_e) = (1 + 2);

    2.2;

    " struct struct_name obj1;";

    return 0;
} 
